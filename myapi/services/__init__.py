from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME
from services.account_service import AccountsService

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

# print(client.list_database_names())
AccountsService = AccountsService(db)

