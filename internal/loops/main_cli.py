from .base_cli import BaseCLI
from .transaction_cli import TransactionCLI
import art

class MainCLI(BaseCLI):
    prompt = "Main " + BaseCLI.prompt

    def preloop(self):
        super().preloop()
        art.tprint("Accounting")

    def do_transaction(self, line):
        "start new transaction"
        self.clearstio()
        TransactionCLI().cmdloop()

