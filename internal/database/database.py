import sqlite3
import os

class Database:
    def __init__(self):
        self.db_name = os.getenv("DB_NAME")
        self.db_folder = os.getenv("DB_PATH")
        
        if not self.db_name or not self.db_folder:
            raise ValueError("Missing DB_NAME or DB_PATH in environment variables")
        
        self.db_path = os.path.join(self.db_folder, self.db_name)
        if not os.path.isfile(self.db_path):
            self.load_schema()
        
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.connection.commit()
        else:
            print(f"An error occurred: {exc_value}")
        self.connection.close()

    def execute(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def execute_commit(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.connection.commit()


    def import_schema(self):
        schema_dir = "internal/database/schema/"
        files = sorted(os.listdir(schema_dir))
        schema = ""

        for file in files:
            full_path = os.path.join(schema_dir, file)
            if not os.path.isfile(full_path):
                print("Skipped:", full_path)
                continue
            with open(full_path, "r", encoding="utf-8") as f:
                schema_content = f.read()
                schema += schema_content + "\n\n"
        return schema

    def load_schema(self):
        if os.path.exists(self.db_path):
            print("⚠️ Database already exists. Skipping schema load.")
            return
    
        os.makedirs(self.db_folder, exist_ok=True)
        schema_sql = self.import_schema()

        with sqlite3.connect(self.db_path) as conn:
            conn.executescript(schema_sql)
            print("✅ Schema loaded successfully.")


