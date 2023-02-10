#code shared by Jörgen to someone in class
import pymongo
connection = pymongo.MongoClient('localhost', 27017)
db = connection['mydb']
collection = db['mycollection']
def insert_document(documentToInsert):
    try:
        collection.insert_one(documentToInsert)
        return True
    except pymongo.errors.PyMongoError as e:
        print("An exception occurred: ", e)
        return False
def main():
    document = {
        "_id": 123,
        "doc_id": 1,
        "some_number": 9278806,
    }
    print(insert_document(document))
main()


#Another code shared by Jörgen:
def update_one_document(filter, newValues):
    try:
        result = collection.update_one(filter, newValues, upsert=True)
        print("UpdateResult( nMatched : ", result.matched_count, ", nModified : ", result.modified_count, ", nUpsertedId : ", result.upserted_id, " )")
        return True
    except pymongo.errors.PyMongoError as e:
        print("An exception occurred update_document failed: ", e)
        return False

 # He says: I call it with something like this:
filter = {'doc_id': 125}
newvalues = {"$set": {'some_number': 1234567}}
print("Update was run:", update_one_document(filter, newvalues))

