from flask import Blueprint, request
from bson import json_util

from services import AccountsService

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/account', methods=['GET'])
def get_accounts_by_email():
    """
    Get all accounts.
    """
    try:
        email = request.args['email']
        accounts = AccountsService.get_accounts_by_email(email)
    except:
        accounts = {'message': 'Error when finding'}
    return json_util.dumps(accounts)

@accounts_bp.route('/accounts', methods=['GET'])
def get_all_accounts():
    """
    Get all accounts.
    """

    accounts = AccountsService.get_all_accounts()

    return json_util.dumps(accounts)


@accounts_bp.route('/accounts/create', methods=['POST'])
def create_account():
    """
    Create a new account.
    """

    account_data = request.get_json()

    account = AccountsService.create_account(account_data)

    return json_util.dumps(account)


@accounts_bp.route('/accounts/update/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    """
    Update an account.
    """

    account_data = request.get_json()

    account = AccountsService.update_account(account_id, account_data)

    return json_util.dumps(account)


@accounts_bp.route('/accounts/delete/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    """
    Delete an account.
    """

    account = AccountsService.delete_account(account_id)

    return json_util.dumps({'message': 'Account deleted successfully'})

