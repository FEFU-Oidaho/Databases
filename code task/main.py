"""
Main code file
"""
from data import DataBase

PHRASE = "Hello world!"
db = DataBase()

if __name__ == "main":
    print(db)
    print(PHRASE)
    