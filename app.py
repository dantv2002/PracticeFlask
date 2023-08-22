# let's import the flask
from flask import Flask, render_template
import pymongo
import os # importing operating system module
MONGODB_URI = 'mongodb+srv://pythonwebpractice:iN3wvDprkrvPFG2@practice.jwxjj9n.mongodb.net/?retryWrites=true&w=majority'
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
query = {
    "country":"Finland"
}
students = db.students.find(query).limit(2).sort('name',-1)

for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)