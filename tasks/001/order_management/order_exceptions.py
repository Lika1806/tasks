class MissigOrderError(Exception):
    def __init__(self, message="Order is missing"):
        self.message = message
        super().__init__(self.message)

class ClosedOrderError(Exception):
    def __init__(self, message="You are not able to adit order"):
        self.message = message
        super().__init__(self.message)
