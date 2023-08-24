from flask import Flask, Blueprint
from bson import json_util

def create_app():
    """
    Create Flask application.
    """
    app = Flask(__name__)
    
    app.created_app_message = "APP CREATED!!!!!!!!!"
    # print(app.created_app_message)
    # Create a blueprint for the accounts controller
    accounts_bp = Blueprint('accounts', __name__)

    # Import the accounts controller
    from controllers import account_controller

    # Register the accounts controller with the blueprint
    accounts_bp.add_url_rule('/account', view_func=account_controller.get_accounts_by_email)
    accounts_bp.add_url_rule('/accounts', view_func=account_controller.get_all_accounts)
    accounts_bp.add_url_rule('/accounts/create', view_func=account_controller.create_account)
    accounts_bp.add_url_rule('/accounts/update/<int:account_id>', view_func=account_controller.update_account)
    accounts_bp.add_url_rule('/accounts/delete/<int:account_id>', view_func=account_controller.delete_account)

    app.register_blueprint(accounts_bp)

    return app

app = create_app()