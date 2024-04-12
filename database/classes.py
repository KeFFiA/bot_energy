import sqlite3
from bot.logging_settings import logger
class DB:
    def __init__(self):
        self.__connect = sqlite3.connect('./database/Energy.db')
        self.cursor = self.__connect.cursor()

    def insert(self, *, table=None, objects=None, value=None):
        """
        Implements data entry into a table, using SQLite3

        table: Name of table in DataBase \n
        objects: Name of the columns in which you need to enter data \n
        value: Values that need to be entered into the table (in order == column declarations earlier) \n
        Each value must be wrapped in quotes -> "SOME_VALUE"
        """
        try:
            self.cursor.execute(f"INSERT INTO {table} ({objects}) VALUES ({value})")
            self.__connect.commit()
        except (sqlite3.OperationalError, sqlite3.IntegrityError):
            logger.critical('Error in data insert function')

    def view(self, *, table: str = None, objects: str = None, where: str = None, value: str = None):
        """
        Implements data view from a table, using SQLite3
        table:      Name of table in DataBase
        objects:    The names of the columns in which you need to find data (can accept the '*' operator)
        where:      Name of the columns that need to be compared
        value:      Values to compare
        """
        try:
            if where is None:
                self.cursor.execute(f'SELECT {objects} FROM {table}')
                result = self.cursor.fetchall()
            else:
                if value is not None:
                    self.cursor.execute(f'SELECT {objects} FROM {table} WHERE {where}="{value}"')
                    result = self.cursor.fetchall()
                else:
                    self.cursor.execute(f'SELECT {objects} FROM {table} WHERE {where}={where}')
                    result = self.cursor.fetchall()
            return result
        except (sqlite3.OperationalError, sqlite3.IntegrityError):
            logger.critical('Error in data view function')

    def update(self, *, table: str = None, objects: str = None, where: str = None, value: str = None,
               whereobject: str = None):
        """
        Implements data update in a table, using SQLite3
        table:       Name of table in DataBase
        objects:     The names of the columns in which you need to update data
        where:       Name of the columns that need to be compared
        whereobject: Item to be replaced
        value:       Values to update
        """
        try:
            values = value.split(sep=', ')
            whereobject = whereobject.split(sep=', ')
            if where is not None:
                for i in range(len(values)):
                    self.cursor.execute(f"UPDATE {table} SET {objects}='{values[i]}' WHERE {where}='{whereobject[i]}'")
            else:
                for i in range(len(values)):
                    self.cursor.execute(
                        f"UPDATE {table} SET {objects}='{values[i]}' WHERE {objects}='{whereobject[i]}'")
            self.__connect.commit()
        except (IndexError, sqlite3.IntegrityError):
            logger.critical('Error in data update function')

    def delete(self, *, table: str = None, where: str = None, whereobject: str = None):
        """
        Implements data delete in a table, using SQLite3
        table:       Name of table in DataBase
        objects:     The names of the columns in which you need to delete data
        where:       Name of the columns that need to be compared
        whereobject: Item to be deleted
        """
        try:
            if whereobject is not None:
                whereobject = whereobject.split(sep=', ')
                for i in range(len(whereobject)):
                    self.cursor.execute(f'DELETE FROM {table} WHERE {where}="{whereobject[i]}"')
            else:
                self.cursor.execute(f'DELETE FROM {table} WHERE {where}={where}')
            self.__connect.commit()
        except (sqlite3.OperationalError, sqlite3.IntegrityError):
            logger.critical('Error in data delete function')

    def __del__(self):
        self.__connect.close()
