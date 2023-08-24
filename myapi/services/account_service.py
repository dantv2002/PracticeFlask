class AccountsService:
    """
    Accounts service.
    """

    def __init__(self, db):
        """
        Create a new accounts service.

        Args:
            db: The database connection.
        """
        self.db = db
    def get_accounts_by_email(self, email):
        """
        Get account by email.

        Returns:
            A list of accounts.
        """
        return self.db['accounts'].find({"email":{'$regex': email}})
    
    def get_all_accounts(self):
        """
        Get all accounts.

        Returns:
            A list of accounts.
        """
        return self.db['accounts'].find()

    def create_account(self, account_data):
        """
        Create a new account.

        Args:
            account_data: The account data.

        Returns:
            The created account.
        """

        account_data['id'] = self.db['accounts'].insert_one(account_data).inserted_id

        return account_data

    def update_account(self, account_id, account_data):
        """
        Update an account.

        Args:
            account_id: The account ID.
            account_data: The account data.

        Returns:
            The updated account.
        """

        account = self.db['accounts'].find_one({'id': account_id})

        if account is None:
            raise ValueError('Account not found')

        for key, value in account_data.items():
            account[key] = value

        self.db['accounts'].update_one({'id': account_id}, {'$set': account})

        return account

    def delete_account(self, account_id):
        """
        Delete an account.

        Args:
            account_id: The account ID.

        Returns:
            The deleted account.
        """

        account = self.db['accounts'].find_one({'id': account_id})

        if account is None:
            raise ValueError('Account not found')

        self.db['accounts'].delete_one({'id': account_id})

        return account

