from internal.database.database import Database
from getpass import getpass
from werkzeug.security import check_password_hash

class User:
    def __init__(self):
        self.username = None
        self.password_authenticated = False
        self.role = None
        self._val_user()

    def _val_user(self):
        while True:
            try:
                username = input("Username: ")
                password = getpass("Password: ")

                if not username or not password:
                    raise ValueError("Username and password are required.")

                with Database() as db:
                    result = db.execute(
                        "SELECT password_hash FROM users WHERE username = ?", 
                        (username,)
                    )

                if result is None:
                    raise ValueError("Invalid username/password")

                password_hash = result[0][0]

                if not check_password_hash(password_hash, password):
                    raise ValueError("Invalid username/password")

                self.username = username
                self.password_authenticated = True
                print("Login successful.\n")
                break

            except Exception as e:
                print(f"Error: {e}")
                
    def __repr__(self):
        return f"{self.username}"