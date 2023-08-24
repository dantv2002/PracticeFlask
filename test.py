import pymongo
import os # importing operating system module
f = open("myinfor.txt", "r")
userName = f.readline()
password = f.readline()
dbName = f.readline()
f.close()

MONGODB_URI = 'mongodb+srv://'+userName.strip()+':'+password.strip()+'@'+ dbName.strip()+'.jwxjj9n.mongodb.net/?retryWrites=true&w=majority'
print(MONGODB_URI)
client = pymongo.MongoClient(MONGODB_URI)
## Creating database
db = client.thirty_days_of_python
#print(client.list_database_names())

## Creating students collection and inserting a document
# db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
# students = [
#         {'name':'David','country':'UK','city':'London','age':34},
#         {'name':'John','country':'Sweden','city':'Stockholm','age':28},
#         {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
#     ]
# for student in students:
#     db.students.insert_one(student)

##find
# student = db.students.find_one({'name':'David'})
# print(student)

#find with query, limiting documents, sort
# query = {
#     "country":"Finland"
# }
# students = db.students.find(query).limit(2).sort('name',-1)

# for student in students:
#     print(student)

db = client['my_database']
collection = db['my_collection']

# Find all documents in the collection
documents = collection.find()

# Paginate the results to return only the first 10 results
documents = documents.limit(10)
    
# Sort the results in ascending order by the `email` field
documents = documents.sort('email', pymongo.ASCENDING)
    
# Filter the results to only return documents where the `email` field contains the string "johndoe" and the `age` field is greater than 18
documents = documents.filter('$and', [
    ('email', 'johndoe'),
    ('age', {'$gt': 18})
])

# Calculate the average age of all documents in the collection
results = collection.aggregate([
    {"$group": {"_id": None, "average_age": {"$avg": "$age"}}}
])

for result in results:
    print(result)
    
# Perform an upsert operation
collection.update_one({'_id': 12345}, {'$set': {'name': 'John Doe'}}, upsert=True)

# Perform a findAndModify() operation
document = collection.findAndModify({'_id': 12345}, {'$set': {'name': 'John Doe'}}, fields={'_id': 1, 'name': 1})

# Perform a MapReduce operation
results = collection.map_reduce(
    map_function=lambda document: {'_id': document['_id']},
    reduce_function=lambda documents: {'count': len(documents)}
)

for result in results:
    print(result)
    

# Perform a bulk insert operation
documents = [
    {'name': 'John Doe'},
    {'name': 'Jane Doe'},
    {'name': 'Peter Smith'}
]

# Skip the first two results
cursor = cursor.skip(2)

for document in cursor:
    print(document)
    
