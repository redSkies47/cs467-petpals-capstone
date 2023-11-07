"""
Contains all functions that perform CRUD operations on the Animals entity group.
"""

def add_animal(id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created, db):
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
        :param Database db: database to be queried
        :return: None
        """
        addAnimal_cmd = "INSERT INTO Animals (id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        addAnimal_params = (id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created)
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

def find_animal_by_id(id_animal, db):
        """
        Returns an animal matching the id_animal from the Animals. Returns an empty list if no such Animal exists.

        :param int id_animal: ID of the target Animal
        :param Database db: database to be queried
        :return: [(id_animal, id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created)]
        """
        selectIDAnimal_cmd = "SELECT * FROM Animals WHERE id_animal = %s"
        selectIDAnimal_params = (id_animal,)
        selectIDAnimal_result = db.query(selectIDAnimal_cmd, selectIDAnimal_params)
        return selectIDAnimal_result

def get_all_animals(db):
        """
        Returns a list containing the all the Animal entries. Returns an empty list if no entries exist.

        :param Database db: database to be queried
        :return: [(id_animal, id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created)]
        """
        selectAllAnimals_cmd = "SELECT * FROM Animals"
        selectAllAnimals_params = ()
        selectAllAnimals_result = db.query(selectAllAnimals_cmd, selectAllAnimals_params)
        return selectAllAnimals_result

def get_animal_disposition_by_id(id_animal, db):
        """
        Returns a list containing Animal Dispositions matching the id_animal. Returns an empty list if none exist.

        :param int id_animal: ID of the target Animal
        :param Database db: database to be queried
        :return: [(id_animal_disposition, description)]
        """
        selectAnimalDispositionID_cmd = "SELECT AD.id_animal_disposition, D.description FROM  Animal_Dispositions AS AD JOIN Dispositons AS D ON AD.id_disposition = D.id_disposition WHERE id_animal = %s"
        selectAnimalDispositionID_params = (id_animal,)
        selectAnimalDispositionID_result = db.query(selectAnimalDispositionID_cmd, selectAnimalDispositionID_params)
        return selectAnimalDispositionID_result

def get_availability(db):
        """
        Returns a list containing all Availabilities. Returns an empty list if none exist.

        :param Database db: database to be queried
        :return: [(id_availability, description)]
        """
        selectAvailability_cmd = "SELECT * FROM Availabilities"
        selectAvailability_params = ()
        selectAvailability_result = db.query(selectAvailability_cmd, selectAvailability_params)
        return selectAvailability_result

def get_breed_by_species(id_species, db):
        """
        Returns a list containing Breeds matching the id_species. Returns an empty list if none exist.

        :param int id_species: ID of the target Species
        :param Database db: database to be queried
        :return: [(id_breed, description)]
        """
        selectSpeciesBreed_cmd = "SELECT id_breed, description FROM Breeds WHERE id_species = %s"
        selectSpeciesBreed_params = (id_species,)
        selectSpeciesBreed_result = db.query(selectSpeciesBreed_cmd, selectSpeciesBreed_params)
        return selectSpeciesBreed_result

def get_cat_breeds(db):
        """
        Returns a list containing Cat Breeds. Returns an empty list if none exist. Assumes id_species for cats is 3.

        :param Database db: database to be queried
        :return: [(id_breed, description)]
        """
        selectCatBreed_cmd = "SELECT id_breed, description FROM Breeds WHERE id_species = 3"
        selectCatBreed_params = ()
        selectCatBreed_result = db.query(selectCatBreed_cmd, selectCatBreed_params)
        return selectCatBreed_result

def get_dog_breeds(db):
        """
        Returns a list containing Dog Breeds. Returns an empty list if none exist. Assumes id_species for dogs is 2.

        :param Database db: database to be queried
        :return: [(id_breed, description)]
        """
        selectDogBreed_cmd = "SELECT id_breed, description FROM Breeds WHERE id_species = 2"
        selectDogBreed_params = ()
        selectDogBreed_result = db.query(selectDogBreed_cmd, selectDogBreed_params)
        return selectDogBreed_result

def get_other_breeds(db):
        """
        Returns a list containing Other Breeds. Returns an empty list if none exist. Assumes id_species for non dogs/cats is 1.

        :param Database db: database to be queried
        :return: [(id_breed, description)]
        """
        selectOtherBreed_cmd = "SELECT id_breed, description FROM Breeds WHERE id_species = 1"
        selectOtherBreed_params = ()
        selectOtherBreed_result = db.query(selectOtherBreed_cmd, selectOtherBreed_params)
        return selectOtherBreed_result

def get_dispositions(db):
        """
        Returns a list containing all Dispositions. Returns an empty list if none exist.

        :param Database db: database to be queried
        :return: [(id_disposition, description)]
        """
        selectDispositions_cmd = "SELECT * FROM Dispositions"
        selectDispositions_params = ()
        selectDispositions_result = db.query(selectDispositions_cmd, selectDispositions_params)
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
        updateIDAnimal_params = (id_availability, id_species, id_breed, name, birth_date, id_gender, size, summary, date_created, id_animal)
        updateIDAnimal_result = db.query(updateIDAnimal_cmd, updateIDAnimal_params)
        return updateIDAnimal_result
