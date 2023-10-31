"""
Contains all functions that perform CRUD operations on the News entity.
"""

def add_news_entry(date, title, body, db):
        """
        Adds a News entry to the database with the given values for its attributes.

        :param str date: formatted as YYYY-MM-DD
        :param str title: title of the news entry
        :param str body: the text of the body
        :param Database db: database to be queried
        :return: None
        """
        addNews_cmd = "INSERT INTO News (date, title, body) VALUES (%s, %s, %s)"
        addNews_params = (date, title, body)
        db.query(addNews_cmd, addNews_params)

def get_all_news(db):
        """
        Returns a list containing the all the News entries. Returns an empty list if no entries exist.

        :param Database db: database to be queried
        :return: [(id_news, date, title, body)]
        """
        selectAllNews_cmd = "SELECT * FROM News"
        selectAllNews_params = tuple()
        selectAllNews_result = db.query(selectAllNews_cmd, selectAllNews_params)
        return selectAllNews_result

def get_one_news(entry, db):
        """
        Returns an entry matching the id_news for the News. Returns an empty list if no such News entry exists.

        :param str entry: target entry
        :param Database db: database to be queried
        :return: [(id_news, date, title, body)]
        """
        selectIDNews_cmd = "SELECT * FROM News WHERE id_news = %s"
        selectIDNews_params = (entry,)
        selectIDNews_result = db.query(selectIDNews_cmd, selectIDNews_params)
        return selectIDNews_result

def update_one_news(entry, date, title, body, db):
        """
        Updates an entry matching the id_news for the News. Must receive date, title, body arguments. Returns an empty list if no such News entry exists.

        :param str entry: target entry
        :param str date: formatted as YYYY-MM-DD
        :param str title: title of the news entry
        :param str body: the text of the body
        :param Database db: database to be queried
        :return: [(id_news, date, title, body)]
        """
        updateIDNews_cmd = "UPDATE News SET date = %s, title = %s, body = %s WHERE id_news = %s"
        updateIDNews_params = (date, title, body, entry)
        updateIDNews_result = db.query(updateIDNews_cmd, updateIDNews_params)
        return updateIDNews_result

def delete_one_news(entry, db):
        """
        Removes an entry matching the id_news for the News.

        :param str entry: target entry
        :param Database db: database to be queried
        :return: None
        """
        deleteOneNews_cmd = "DELETE FROM News WHERE id_news = %s"
        deleteOneNews_params = (entry,)
        db.query(deleteOneNews_cmd, deleteOneNews_params)
