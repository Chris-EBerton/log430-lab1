"""
User DAO (Data Access Object)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
from dotenv import load_dotenv
import mysql.connector
from models.user import User
from pymongo import MongoClient

class UserDAOMongo:
    def init(self):
            try:
                env_path = ".env"
                print(os.path.abspath(env_path))

                load_dotenv(dotenv_path=env_path)

                mongo_host = os.getenv("MONGODB_HOST")
                mongo_port = os.getenv("MONGODB_PORT")
                mongo_db = os.getenv("MONGODB_NAME")

                mongo_user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
                mongo_pass = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

                mongo_uri = (
                    f"mongodb://{mongo_user}:{mongo_pass}"
                    f"@{mongo_host}:{mongo_port}/"
                    f"?authSource=admin"
                )

                self.client = MongoClient(mongo_uri)

                self.db = self.client[mongo_db]

                self.collection = self.db["users"]

            except FileNotFoundError:
                print("Attention : Veuillez créer un fichier .env")

            except Exception as e:
                print("Erreur : " + str(e))


    def select_all(self):
        """ Select all users from MongoDB """
        rows = self.collection.find({}, {"_id": 0, "id": 1, "name": 1, "email": 1})
        return [User(row["id"], row["name"], row["email"]) for row in rows]


    def insert(self, user):
        """ Insert given user into MongoDB """
        result = self.collection.insert_one({
            "name": user.name,
            "email": user.email
        })
        return str(result.inserted_id)
    

    def update(self, user):
        """ Update given user in MongoDB """
        self.collection.update_one
        (
            {"id": user.id},
            {
                "$set": {
                    "name": user.name,
                    "email": user.email
                }
            }
        )

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        self.collection.delete_one(
            {"id": user_id}
        )

    def delete_all(self): # extra
        """ Empty users table in MySQL """
        pass
        

    def close(self):
        self.cursor.close()
        self.conn.close()
