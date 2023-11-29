"""
Contains all functions that perform CRUD operations on the Animals entity group.
"""


def add_animal(id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created, id_shelter, db):
    """
    Adds a Animal entry to the database with the given values for its attributes.

    :param int id_availability: availability of the Animal
    :param int id_species: species of the new Animal
    :param int id_breed: breed of the Animal
    :param str name: the name of the Animal
    :param str birth_date: formatted as YYYY-MM-DD
    :param int id_gender: gender of the new Animal
    :param int size: size of the new Animal
    :param str summary: summary of the new Animal
    :param str date_created: formatted as YYYY-MM-DD
    :param int id_shelter: shelter of the new Animal
    :param Database db: database to be queried
    :return: None
    """
    addAnimal_cmd = "INSERT INTO Animals (id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created, id_shelter) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    addAnimal_params = (id_availability, id_species, id_breed,
                        name, birth_date, id_gender, size, summary, date_created, id_shelter)
    db.query(addAnimal_cmd, addAnimal_params)


def add_animal_disposition(id_animal, id_disposition, db):
    """
    Adds a Animal Disposition entry to the database with the given values for its attributes.

    :param int id_animal: ID of the target Animal
    :param int id_disposition: ID of the target Disposition
    :param Database db: database to be queried
    :return: None
    """
    addAnimalDispositions_cmd = "INSERT INTO Animal_Dispositions (id_animal, id_disposition) VALUES (%s, %s)"
    addAnimalDispositions_params = (id_animal, id_disposition)
    db.query(addAnimalDispositions_cmd, addAnimalDispositions_params)


def add_image(id_animal, db):
    """
    Adds an Image to the database with the given values for its attributes.

    :param int id_animal: ID of the target Animal
    :param Database db: database to be queried
    :return: None
    """
    addImage_cmd = "INSERT INTO Images (id_animal) VALUES (%s)"
    addImage_params = (id_animal,)
    print("***** addImage_params: ", addImage_params)
    db.query(addImage_cmd, addImage_params)


def delete_animal(id_animal, db):
    """
    Removes an Animal matching the id_animal from the Animals.

    :param int id_animal: ID of the target Animal
    :param Database db: database to be queried
    :return: None
    """
    deleteAnimal_cmd = "DELETE FROM News WHERE id_news = %s"
    deleteAnimal_params = (id_animal,)
    db.query(deleteAnimal_cmd, deleteAnimal_params)


def delete_image(id_image, db):
    """
    Removes an entry matching the id_image from the Images.

    :param int id_image: ID of the target Image
    :param Database db: database to be queried
    :return: None
    """
    deleteImage_cmd = "DELETE FROM Images WHERE id_image = %s"
    deleteImage_params = (id_image,)
    db.query(deleteImage_cmd, deleteImage_params)


def find_animal_by_id(id_animal, db):
    """
    Returns an animal matching the id_animal from the Animals. Returns an empty list if no such Animal exists. Converts foreign keys to their corresponding values.

    :param int id_animal: ID of the target Animal
    :param Database db: database to be queried
    :return: [(id_animal, availability, species, breed, name, birth_date, gender, size, summary, date_created, shelter)]
    """
    selectIDAnimal_cmd = "SELECT Animals.id_animal, Availabilities.description AS availability, Species.description AS species, Breeds.description AS breed, Animals.name, Animals.birth_date, Genders.description AS gender, Animals.size, Animals.summary, Animals.date_created, Shelters.name AS shelter \
        FROM Animals \
            INNER JOIN Availabilities ON Availabilities.id_availability = Animals.id_availability \
            INNER JOIN Species ON Species.id_species = Animals.id_species \
            INNER JOIN Breeds ON Breeds.id_breed = Animals.id_breed \
            INNER JOIN Genders ON Genders.id_gender = Animals.id_gender \
            INNER JOIN Shelters ON Shelters.id_shelter = Animals.id_shelter \
        WHERE id_animal = %s"
    selectIDAnimal_params = (id_animal,)
    selectIDAnimal_result = db.query(selectIDAnimal_cmd, selectIDAnimal_params)
    return selectIDAnimal_result


def find_animal_id_by_name(name, db):
    """
    Returns an animal id matching the name from the Animals. Returns an empty list if no entries exist.

    :param str name: name of the target Animal
    :param Database db: database to be queried
    :return: [(id_animal)]
    """
    selectIDAnimalName_cmd = 'SELECT id_animal FROM Animals WHERE Name = %s'
    selectIDAnimalName_params = (name,)
    selectIDAnimalName_result = db.query(
        selectIDAnimalName_cmd, selectIDAnimalName_params)
    return selectIDAnimalName_result


def find_latest_image_id_by_animal(id_animal, db):
    """
    Returns an image id of the latest added entry from Images. Returns an empty list if no entries exist.

    :param int id_animal: ID of the target Animal
    :param Database db: database to be queried
    :return: [(id_image)]
    """
    selectIDAnimalLatest_cmd = 'SELECT id_image FROM Images WHERE id_animal = %s ORDER BY id_image DESC'
    selectIDAnimalLatest_params = (id_animal,)
    selectIDAnimalLatest_result = db.query(
        selectIDAnimalLatest_cmd, selectIDAnimalLatest_params)
    return selectIDAnimalLatest_result[0] if selectIDAnimalLatest_result else selectIDAnimalLatest_result


def get_all_animals(db):
    """
    Returns a list containing the all the Animal entries. Returns an empty list if no entries exist.

    :param Database db: database to be queried
    :return: [(id_animal, id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created)]
    """
    selectAllAnimals_cmd = "SELECT * FROM Animals"
    selectAllAnimals_params = ()
    selectAllAnimals_result = db.query(
        selectAllAnimals_cmd, selectAllAnimals_params)
    return selectAllAnimals_result


def get_animals_by_species_breed_gender_availability_dispositions(id_species, id_breed, id_gender, id_availability, list_id_dispositions, db):
    """
    Returns a list containing the all the Animal entries satisfying the given parameters. Returns an empty list if no entries exist.

    :param int id_species: ID of the target Animal(s)
    :param int id_breed: breed of the target Animal(s)
    :param int id_gender: gender of the target Animal(s)
    :param int id_availability: availability of the target Animal(s)
    :param List[int] list_id_dispositions: list of dispositions of the target Animal(s)
    :param Database db: database to be queried
    :return: [(id_animal, id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created, id_shelter, list(id_dispositions))]
    """

    selectAnimals_cmd = "select id_animal, id_availability, id_species, id_breed, name, birth_date, id_gender, summary, date_created, id_shelter, group_concat(c.id_disposition) as dispositions from \
                            (select a.*, b.id_disposition from Animals a left join Animal_Dispositions b on a.id_animal = b.id_animal) c "
    first_clause = 1
    selectAnimals_params = []

    if id_species:
        selectAnimals_cmd += ' where c.id_species = %s '
        selectAnimals_params.append(id_species)
        first_clause = 0
    if id_breed:
        if not first_clause:
            selectAnimals_cmd += ' and '
        else:
            selectAnimals_cmd += ' where '
        selectAnimals_cmd += ' c.id_breed = %s '
        selectAnimals_params.append(id_breed)
        first_clause = 0
    if id_gender:
        if not first_clause:
            selectAnimals_cmd += ' and '
        else:
            selectAnimals_cmd += ' where '
        selectAnimals_cmd += ' c.id_gender = %s '
        selectAnimals_params.append(id_gender)
        first_clause = 0
    if id_availability:
        if not first_clause:
            selectAnimals_cmd += ' and '
        else:
            selectAnimals_cmd += ' where '
        selectAnimals_cmd += ' c.id_availability = %s '
        selectAnimals_params.append(id_availability)
        first_clause = 0

    for i in range(len(list_id_dispositions)):
        if list_id_dispositions[i] != 0:
            if not first_clause:
                selectAnimals_cmd += ' and '
            else:
                selectAnimals_cmd += ' where '
            selectAnimals_cmd += ' (select count(*) from Animal_Dispositions where id_disposition = %s and id_animal = c.id_animal > 0) '
            selectAnimals_params.append(i)
            first_clause = 0
    selectAnimals_cmd += "group by c.id_animal"
    print(selectAnimals_cmd, selectAnimals_params)
    selectAnimals_result = db.query(selectAnimals_cmd, selectAnimals_params)
    return selectAnimals_result


def get_latest_animal(db):
    """
    Returns the most recently added animal. Returns an empty list if no entry exists.
    :param Database db: database to be queried
    :return: [(id_animal, id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created, id_shelter, list(id_dispositions))]
    """
    selectLatestAnimal_cmd = "select * from Animals order by id_animal desc limit 1;"
    selectLatestAnimal_params = ()
    selectLatestAnimal_result = db.query(
        selectLatestAnimal_cmd, selectLatestAnimal_params)
    return selectLatestAnimal_result


def get_all_dogs(db):
    """
    Returns a list containing all the dogs. Returns an empty list if no dogs exist.

    :param Database db: database to be queried
    :return:
    """
    selectAllDogs_cmd = "SELECT * FROM Animals WHERE id_species = 2"
    selectAllDogs_params = tuple()
    selectAllDogs_result = db.query(selectAllDogs_cmd, selectAllDogs_params)
    return selectAllDogs_result


def get_all_images_by_id_animal(id_animal, db):
    """
    Returns a list containing all the Images belong to the target ID Animal. Returns an empty list if no Images exist.

    :param int id_animal: ID of the target Animal
    :param Database db: database to be queried
    :return:
    """
    selectAllImagesByAnimal_cmd = "SELECT id_image FROM Images WHERE id_animal = %s ORDER BY id_image ASC"
    selectAllImagesByAnimal_params = (id_animal,)
    selectAllImagesByAnimal_result = db.query(
        selectAllImagesByAnimal_cmd, selectAllImagesByAnimal_params)
    return selectAllImagesByAnimal_result


def get_dogs(breed, dispositions, recency, db):
    """
    Returns a list containing the dogs that match the search filter options. Returns an empty list if no such dogs exist.

    :param string breed: specified breed, empty string if no preference
    :param list dispositions: specified dispositions, empty list if no preference
    :param boolean recency: True if sorted by most recent, False if sorted by least recent, None if no preference
    :param Database db: database to be queried
    :return: [(id_animal, name, date_created)]
    """
    # filter by breed
    if breed == "":
        breed_clause = ""
    else:
        breed_clause = f"AND Breeds.description = '{breed}'"
    # filter by disposition
    if dispositions == []:
        disposition_clause = ""
    else:
        disposition_clause = f"AND Dispositions.description IN ({str(dispositions)[1:-1]}) GROUP BY Animals.id_animal HAVING COUNT(DISTINCT Dispositions.id_disposition) = {len(dispositions)}"
    # sort by date
    if recency is None:
        recency_clause = ""
    elif recency:
        recency_clause = "ORDER BY date_created DESC"
    else:
        recency_clause = "ORDER BY date_created ASC"
    # format and execute query
    selectDogscmd = f"SELECT DISTINCT Animals.id_animal, Animals.name, Animals.date_created FROM Animals JOIN Breeds ON Breeds.id_breed = Animals.id_breed JOIN Animal_Dispositions ON Animal_Dispositions.id_animal = Animals.id_animal JOIN Dispositions ON Dispositions.id_disposition = Animal_Dispositions.id_disposition WHERE Animals.id_species = 2 {breed_clause} {disposition_clause} {recency_clause}"
    selectDogsparams = tuple()
    selectDogsresult = db.query(selectDogscmd, selectDogsparams)
    return selectDogsresult


def get_cats(breed, dispositions, recency, db):
    """
    Returns a list containing the cats that match the search filter options. Returns an empty list if no such cats exist.

    :param string breed: specified breed, empty string if no preference
    :param list dispositions: specified dispositions, empty list if no preference
    :param boolean recency: True if sorted by most recent, False if sorted by least recent, None if no preference
    :param Database db: database to be queried
    :return: [(id_animal, name, date_created)]
    """
    # filter by breed
    if breed == "":
        breed_clause = ""
    else:
        breed_clause = f"AND Breeds.description = '{breed}'"
    # filter by disposition
    if dispositions == []:
        disposition_clause = ""
    else:
        disposition_clause = f"AND Dispositions.description IN ({str(dispositions)[1:-1]}) GROUP BY Animals.id_animal HAVING COUNT(DISTINCT Dispositions.id_disposition) = {len(dispositions)}"
    # sort by date
    if recency is None:
        recency_clause = ""
    elif recency:
        recency_clause = "ORDER BY date_created DESC"
    else:
        recency_clause = "ORDER BY date_created ASC"
    # format and execute query
    selectCatscmd = f"SELECT DISTINCT Animals.id_animal, Animals.name, Animals.date_created FROM Animals JOIN Breeds ON Breeds.id_breed = Animals.id_breed JOIN Animal_Dispositions ON Animal_Dispositions.id_animal = Animals.id_animal JOIN Dispositions ON Dispositions.id_disposition = Animal_Dispositions.id_disposition WHERE Animals.id_species = 3 {breed_clause} {disposition_clause} {recency_clause}"
    selectCatsparams = tuple()
    selectCatsresult = db.query(selectCatscmd, selectCatsparams)
    return selectCatsresult


def get_others(breed, dispositions, recency, db):
    """
    Returns a list containing the other animals that match the search filter options. Returns an empty list if no such animals exist.

    :param string breed: specified breed, empty string if no preference
    :param list dispositions: specified dispositions, empty list if no preference
    :param boolean recency: True if sorted by most recent, False if sorted by least recent, None if no preference
    :param Database db: database to be queried
    :return: [(id_animal, name, date_created)]
    """
    # filter by breed
    if breed == "":
        breed_clause = ""
    else:
        breed_clause = f"AND Breeds.description = '{breed}'"
    # filter by disposition
    if dispositions == []:
        disposition_clause = ""
    else:
        disposition_clause = f"AND Dispositions.description IN ({str(dispositions)[1:-1]}) GROUP BY Animals.id_animal HAVING COUNT(DISTINCT Dispositions.id_disposition) = {len(dispositions)}"
    # sort by date
    if recency is None:
        recency_clause = ""
    elif recency:
        recency_clause = "ORDER BY date_created DESC"
    else:
        recency_clause = "ORDER BY date_created ASC"
    # format and execute query
    selectOtherscmd = f"SELECT DISTINCT Animals.id_animal, Animals.name, Animals.date_created FROM Animals JOIN Breeds ON Breeds.id_breed = Animals.id_breed JOIN Animal_Dispositions ON Animal_Dispositions.id_animal = Animals.id_animal JOIN Dispositions ON Dispositions.id_disposition = Animal_Dispositions.id_disposition WHERE Animals.id_species = 1 {breed_clause} {disposition_clause} {recency_clause}"
    selectOthersparams = tuple()
    selectOthersresult = db.query(selectOtherscmd, selectOthersparams)
    return selectOthersresult


def get_animal_disposition_by_id(id_animal, db):
    """
    Returns a list containing Animal Dispositions matching the id_animal. Returns an empty list if none exist.

    :param int id_animal: ID of the target Animal
    :param Database db: database to be queried
    :return: [(id_animal_disposition, description)]
    """
    selectAnimalDispositionID_cmd = "SELECT AD.id_animal_disposition, D.description FROM  Animal_Dispositions AS AD JOIN Dispositons AS D ON AD.id_disposition = D.id_disposition WHERE id_animal = %s"
    selectAnimalDispositionID_params = (id_animal,)
    selectAnimalDispositionID_result = db.query(
        selectAnimalDispositionID_cmd, selectAnimalDispositionID_params)
    return selectAnimalDispositionID_result


def get_availability(db):
    """
    Returns a list containing all Availabilities. Returns an empty list if none exist.

    :param Database db: database to be queried
    :return: [(id_availability, description)]
    """
    selectAvailability_cmd = "SELECT * FROM Availabilities"
    selectAvailability_params = ()
    selectAvailability_result = db.query(
        selectAvailability_cmd, selectAvailability_params)
    return selectAvailability_result


def get_shelters(db):
    """
    Returns a list containing all shelters. Returns an empty list if none exist.

    :param Database db: database to be queried
    :return: [(id_shelter, name, address, phone_number, opening_hour, closing_hour)]
    """
    selectShelter_cmd = "SELECT * FROM Shelters"
    selectShelter_params = ()
    selectShelter_result = db.query(
        selectShelter_cmd, selectShelter_params)
    return selectShelter_result


def get_breed_by_species(id_species, db):
    """
    Returns a list containing Breeds matching the id_species. Returns an empty list if none exist.

    :param int id_species: ID of the target Species
    :param Database db: database to be queried
    :return: [(id_breed, description)]
    """
    selectSpeciesBreed_cmd = "SELECT id_breed, description FROM Breeds WHERE id_species = %s"
    selectSpeciesBreed_params = (id_species,)
    selectSpeciesBreed_result = db.query(
        selectSpeciesBreed_cmd, selectSpeciesBreed_params)
    return selectSpeciesBreed_result


def get_cat_breeds(db):
    """
    Returns a list containing Cat Breeds. Returns an empty list if none exist. Assumes id_species for cats is 3.

    :param Database db: database to be queried
    :return: [(id_breed, description)]
    """
    selectCatBreed_cmd = "SELECT id_breed, description FROM Breeds WHERE id_species = 3 ORDER BY description"
    selectCatBreed_params = ()
    selectCatBreed_result = db.query(selectCatBreed_cmd, selectCatBreed_params)
    return selectCatBreed_result


def get_dog_breeds(db):
    """
    Returns a list containing Dog Breeds. Returns an empty list if none exist. Assumes id_species for dogs is 2.

    :param Database db: database to be queried
    :return: [(id_breed, description)]
    """
    selectDogBreed_cmd = "SELECT id_breed, description FROM Breeds WHERE id_species = 2 ORDER BY description"
    selectDogBreed_params = ()
    selectDogBreed_result = db.query(selectDogBreed_cmd, selectDogBreed_params)
    return selectDogBreed_result


def get_other_breeds(db):
    """
    Returns a list containing Other Breeds. Returns an empty list if none exist. Assumes id_species for non dogs/cats is 1.

    :param Database db: database to be queried
    :return: [(id_breed, description)]
    """
    selectOtherBreed_cmd = "SELECT id_breed, description FROM Breeds WHERE id_species = 1 ORDER BY description"
    selectOtherBreed_params = ()
    selectOtherBreed_result = db.query(
        selectOtherBreed_cmd, selectOtherBreed_params)
    return selectOtherBreed_result


def get_dispositions(db):
    """
    Returns a list containing all Dispositions. Returns an empty list if none exist.

    :param Database db: database to be queried
    :return: [(id_disposition, description)]
    """
    selectDispositions_cmd = "SELECT * FROM Dispositions"
    selectDispositions_params = ()
    selectDispositions_result = db.query(
        selectDispositions_cmd, selectDispositions_params)
    return selectDispositions_result


def get_genders(db):
    """
    Returns a list containing all Genders. Returns an empty list if none exist.

    :param Database db: database to be queried
    :return: [(id_gender, description)]
    """
    selectGender_cmd = "SELECT * FROM Genders"
    selectGender_params = ()
    selectGender_result = db.query(selectGender_cmd, selectGender_params)
    return selectGender_result


def get_species(db):
    """
    Returns a list containing all Species. Returns an empty list if none exist.

    :param Database db: database to be queried
    :return: [(id_species, description)]
    """
    selectSpecies_cmd = "SELECT * FROM Species"
    selectSpecies_params = ()
    selectSpecies_result = db.query(selectSpecies_cmd, selectSpecies_params)
    return selectSpecies_result


def update_animal(id_animal, id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created, db):
    """
    Updates an Animal matching the id_animal from the Animals. Must receive all arguments. Returns an empty list if no such Animal exists.

    :param int id_animal: ID of the target Animal
    :param int id_availability: availability of the Animal
    :param int id_species: species of the Animal
    :param int id_breed: breed of the Animal
    :param str name: the name of the Animal
    :param str birth_date: formatted as YYYY-MM-DD
    :param int id_gender: gender of the Animal
    :param int size: size of the Animal
    :param str summary: summary of the Animal
    :param str date_created: formatted as YYYY-MM-DD
    :param Database db: database to be queried
    :return: [(id_animal, id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created)]
    """
    updateIDAnimal_cmd = "UPDATE Animals SET id_availability = %s, id_species = %s, id_breed = %s, name = %s, birth_date = %s, id_gender = %s, size = %s, summary = %s, date_created = %s WHERE id_animal = %s"
    updateIDAnimal_params = (id_availability, id_species, id_breed, name,
                             birth_date, id_gender, size, summary, date_created, id_animal)
    updateIDAnimal_result = db.query(updateIDAnimal_cmd, updateIDAnimal_params)
    return updateIDAnimal_result


def update_image(id_image, id_animal, db):
    """
    Updates an Image entry in the database with the given values for its attributes.

    :param int id_image: ID of the target Image reference
    :param int id_animal: ID of the target Animal
    :param Database db: database to be queried
    :return: None
    """
    updateImage_cmd = "UPDATE Images SET id_animal = %s WHERE id_image = %s"
    UpdateImage_params = (id_animal, id_image)
    updateImage_result = db.query(updateImage_cmd, UpdateImage_params)
    return updateImage_result
