from .base_cli import BaseCLI
from internal.functions.users import generate_password
from internal.database.database import Database
from werkzeug.security import generate_password_hash


class UsersCLI(BaseCLI):
    prompt = 'User management ' + BaseCLI.prompt

    def __init__(self, user, completekey = "tab", stdin = None, stdout = None):
        super().__init__(completekey, stdin, stdout)
        self.user = user

    def do_createuser(self, line):
        """Create New user"""
        
        name = input("Name; ")
        surname = input("Surname: ")
        username = input("Username: ")

        password = generate_password()
        
        with Database() as db:
            db.execute_commit("INSERT INTO users (name, surname, username, password_hash) VALUES (?, ?, ?, ?)", 
                      (name, surname, username, generate_password_hash(password)))
            
        print("User Created Successfully")
        print(f"\n\n Password:{password}")

    def do_printuser(self, line):
        print(self.user)