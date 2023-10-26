# --- Imports --- #

# mySQL connector
import mysql.connector


# --- Database Interface --- #
class Database():
    """
    Represents the MySQL database connection. Provides an interface with which to query the database without having to manually open/close a new connection and cursor each time.
    """
    def __init__(self, host, user, password, name):
        self.connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = name
        )
        self.cursor = None

    def __connect(self):
        """
        Creates a connection to the database.
        """
        self.cursor = self.connection.cursor()

    def __close(self):
        """
        Closes the connection to the database.
        """
        self.cursor.close()

    def __commit(self):
        """
        Commits the transaction to the database.
        """
        self.connection.commit()

    def query(self, cmd, params):
        """
        Executes a query. Returns the results.

        :param str cmd: parameterized SQL statement
        :param tuple params: parameter values, in order
        :return: list of tuples, each representing a row of the query results
        """
        # Create cursor
        self.__connect()
        # Execute query
        self.cursor.execute(cmd, params)
        result = self.cursor.fetchall()
        # Commit changes
        self.__commit()
        # Close cursor
        self.__close()

        return result