##################
# Error handling #
##################


from colorama import Fore, Style


class ProtoCSSError(Exception):
    def __init__(self, message, line_number=None):
        self.message = message
        self.line_number = line_number
        super().__init__(self.message)

    def __str__(self):
        return f" {Fore.LIGHTYELLOW_EX}{self.message}{Style.RESET_ALL}"
