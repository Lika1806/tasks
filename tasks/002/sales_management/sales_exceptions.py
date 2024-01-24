class NotEnoghtFundsError(Exception):
    def __init__(self, message="Not enough funds!"):
        self.message = message
        super().__init__(self.message)