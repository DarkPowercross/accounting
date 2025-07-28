from .base_cli import BaseCLI

class TransactionCLI(BaseCLI):
    prompt = 'Transacting ' + BaseCLI.prompt

    def do_print(self, line):
        print(line)