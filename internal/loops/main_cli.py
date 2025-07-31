from .base_cli import BaseCLI
from .users_cli import UsersCLI
from .transaction_cli import TransactionCLI
from internal.usercontrol.userclass import User
import art

class MainCLI(BaseCLI):
    prompt = "Main " + BaseCLI.prompt

    def preloop(self):
        super().preloop()
        art.tprint("Accounting")
        self.user = User()

    def do_transaction(self, line):
        "start new transaction"
        TransactionCLI().cmdloop()

    def do_users(self, line):
        """manage application users"""
        UsersCLI(self.user).cmdloop()
    
    def do_currentuser(self, line):
        print(self.user)