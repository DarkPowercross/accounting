import cmd
import sys
import os

class BaseCLI(cmd.Cmd):
    prompt = '>> '

    def preloop(self):
        """Enable blinking cursor when the application starts."""
        sys.stdout.write("\033[?12h")
        sys.stdout.flush()

    def default(self, line):
        """Convert all inputs to lowercase before processing"""
        return super().default(line.lower().strip()) 

    def do_exit(self, line):
        "Exit back to main"
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
