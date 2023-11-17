from github import Github # pip install PyGithub
import base64
import os
from dotenv import load_dotenv
from database import db_interface
from database import animals_dml
# run terminal with command: python -m database.images

# Assign environment variables
load_dotenv()

TOKEN = os.getenv('TOKEN')
REPO = "redSkies47/cs467-petpals-capstone"
REPO_PATH = "images//"
MESSAGE = "upload encoded image"
BRANCH = "main"

"""
Contains functions to save and retrieve images from github
"""
def upload_and_save_image(id_animal, filename, db):
    """
    Uploads and saves the image located at the provided filename for the target animal matchin the id_animal.

    :param int id_animal: ID of the target Animal
    :param str file_name: provide the intended file name of the image
    :param Database db: database to be queried
    :return: None
    """
    # add image reference entry to database
    github_path = ""
    animals_dml.add_image(github_path, db)
    id_image = animals_dml.find_latest_image_id(db)

    # add animal image relationship to database
    animals_dml.add_animal_image(id_animal, id_image[0], db)
    id_animal_image = animals_dml.find_latest_animal_image_id(id_animal, id_image[0], db)

    # encode image as base64 string
    g=Github(TOKEN)
    repo=g.get_repo(REPO)

    with open(filename, 'rb') as file:
        bytes = file.read()
        b64_data = base64.b64encode(bytes)

    # craft github path based on the unique id animal image number
    github_path = REPO_PATH + str(id_animal_image[0]) + '.jpg'

    # use github api to store image in repo
    repo.create_file(github_path, MESSAGE, b64_data, BRANCH)
    
    # update image reference with github url
    results = animals_dml.update_image(id_image[0], github_path, db)
    # print(results)

# Retrieve from github and locally store image
def get_animal_image_by_id(id_animal, db):
    """
    Retrieves an image using the provided encoded data using Base64. Returns the data as a binary object.

    :param str file_name: provide the intended file name of the image
    :param str data: encoded image data
    :return: None
    """
    pass

def place_sample_images():
    """
    Places sample images into the github repo.

    :return: None
    """
    # Get database credentials
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')

    DB = db_interface.Database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    
    # Set image relative paths
    # paths = [".\images\\01.jpg",
    #          ".\images\\02.jpg",
    #          ".\images\\03.jpg",
    #          ".\images\\04.jpg",
    #          ".\images\\05.jpg",
    #          ".\images\\06.jpg",
    #          ".\images\\07.jpg"]
    
    paths = [".\images\\02.jpg"]
    
    # pet_id = {
    #        paths[0]: "1",
    #        paths[1]: "2",
    #        paths[2]: "3",
    #        paths[3]: "4",
    #        paths[4]: "5",
    #        paths[5]: "6",
    #        paths[6]: "7"
    # }

    pet_id = {
            paths[0]: "2"
    }

    # Place sample image into github and update database
    # for path in paths:
    #     upload_and_save_image(pet_id[path], path, DB)
    upload_and_save_image(pet_id[paths[0]], paths[0], DB)

if __name__ == "__main__":
    
    place_sample_images()
