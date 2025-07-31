import os
from dotenv import load_dotenv
from internal.loops.main_cli import MainCLI
from internal.database.database import Database
from internal.usercontrol.userclass import User

def main():
    load_dotenv()
    with Database() as db:
        db.load_schema()

    MainCLI().cmdloop()

if __name__ == "__main__":
    main()
