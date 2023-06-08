from werkzeug.security import check_password_hash, generate_password_hash
from database import the_database


class UserRepository:
    def __init__(self, connection=the_database.connection):
        self.connection = connection

    def search_user(self, username):
        """Search user function, returns True if user is found"""

        cursor = self.connection.cursor()
        values = {"username": username}
        sql = """SELECT username FROM users
        WHERE username=:username"""
        return bool(cursor.execute(sql, values).fetchall())

    def get_user_id_by_username(self, username):
        """Search user_id function, returns user_id for given argument username"""

        cursor = self.connection.cursor()
        values = {"username": username}
        sql = """SELECT user_id FROM users
        WHERE username=:username"""

        result = cursor.execute(sql, values).fetchone()
        if result:
            return result[0]
        else:
            return None

    def create_user(self, username, password):
        """Create new user function. Password is saved as a hash value to
        improve security. """

        hash_value = generate_password_hash(password)

        cursor = self.connection.cursor()
        values = {"username": username, "password": hash_value}
        sql = """INSERT INTO users (username, password)
        VALUES (:username, :password)"""
        cursor.execute(sql, values)

        self.connection.commit()
        cursor.close()

    def sign_in(self, username, password):
        """Sign in function. User is searched, if there are no users
        with the username, returns False. If there is, check the password
        and if password is correct, return True. """
        cursor = self.connection.cursor()
        values = {"username": username}
        sql = """SELECT username, password
        FROM users WHERE username=:username"""

        user = cursor.execute(sql, values).fetchone()
        if not user:
            return False

        hash_value_password = user[1]
        return check_password_hash(hash_value_password, password)


the_user_repository = UserRepository()
