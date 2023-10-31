"""
Contains all functions that perform CRUD operations on the Animals entity.
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
