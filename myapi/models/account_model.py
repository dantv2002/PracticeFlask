class AccountModel:
    """
    Account model.
    """

    def __init__(self, id, email, password, roles, trangThai, createdDate, lastModifiedDate, userID, accountName):
        """
        Create a new account model.

        Args:
            id: The ID.
            email: The email address.
            password: The password.
            roles: The roles.
            trangThai: The trang thai.
            createdDate: The created date.
            lastModifiedDate: The last modified date.
            userID: The user ID.
            accountName: The account name.
        """

        self.id = id
        self.email = email
        self.password = password
        self.roles = roles
        self.trangThai = trangThai
        self.createdDate = createdDate
        self.lastModifiedDate = lastModifiedDate
        self.userID = userID
        self.accountName = accountName

