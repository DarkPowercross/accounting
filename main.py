import os
from dotenv import load_dotenv
from database.database import Database

def main():
    load_dotenv()

    with Database() as db:
        results = db.execute("PRAGMA table_info(users)")
        for row in results:
            print(row)


if __name__ == "__main__":
    main()
