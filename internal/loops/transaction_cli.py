from .base_cli import BaseCLI
from internal.database.database import Database

class TransactionCLI(BaseCLI):
    prompt = 'Transacting ' + BaseCLI.prompt

    def do_print(self, line):
        """Prints added information"""
        with Database() as db:
            if line:
                results = db.execute("SELECT * FROM users WHERE username = ?", (line,))
            else:
                results = db.execute("SELECT * FROM users")
            for row in results:
                print(row)