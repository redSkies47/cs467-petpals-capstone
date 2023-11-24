from github import Github
import os
from dotenv import load_dotenv
from database import db_interface
from database import animals_dml

# Assign environment variables
load_dotenv()

TOKEN = os.getenv('TOKEN')
REPO = "redSkies47/cs467-petpals-capstone"
REPO_PATH = "images/"
MESSAGE = "upload image"
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
    :return: str github_path: the github path for the uploaded and saved image
    """
    # Add image reference entry to database
    animals_dml.add_image(id_animal, db)
    id_image = animals_dml.find_latest_image_id_by_animal(id_animal, db)

    # Connect to github api
    g = Github(TOKEN)
    repo = g.get_repo(REPO)

    with open(filename, 'rb') as file:
        bytes = file.read()

    # Craft github path based on the unique id animal image number
    num = str(id_image[0])
    github_path = REPO_PATH + num + '.jpg'

    # Use github api to store image in repo
    repo.create_file(github_path, MESSAGE, bytes, BRANCH)

    return github_path


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
    paths = [".\images\\01.jpg",
             ".\images\\02.jpg",
             ".\images\\03.jpg",
             ".\images\\04.jpg",
             ".\images\\05.jpg",
             ".\images\\06.jpg",
             ".\images\\07.jpg"]

    pet_id = {
        paths[0]: 1,
        paths[1]: 2,
        paths[2]: 3,
        paths[3]: 4,
        paths[4]: 5,
        paths[5]: 6,
        paths[6]: 7
    }

    # Place sample image into github and update database
    for path in paths:
        relative_path = upload_and_save_image(pet_id[path], path, DB)
        print(relative_path)


if __name__ == "__main__":

    place_sample_images()
