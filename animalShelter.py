from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        if username and password:
            print("username and password are", username, password)
            self.client = MongoClient('mongodb://%s:%s@localhost:54314/AAC' %(username, password))
            self.database = self.client['AAC']
            print("connection was successful")
    def create(self,data):
        if data is not None:
            self.database.animals.insert(data)
            print("successful create")
        else:
            raise Exception("Nothing to submit")
            
    def read(self, search):
        if search:
            searchResult = self.database.animals.find(search,{"_id":False})
        else:
            searchResult = self.database.animals.find({}, {"_id":False})
        return searchResult
        
    def update(self, search, updateKeys):
        """ updates all documents associated with the search query """
        if search:
            if updateKeys:
                update = self.database.animals.update_many(search, updateKeys)
            else:
                raise Exception("No changes given")
        else:
            raise Exception("No search given")
        
    def delete(self, search):
        if search:
            self.database.animals.delete_one(search)
        else:
            raise Exeption("No search given")