class Account:
    """return the account"""

    def __init__(self, name):
        
        self.holder = name
        self.blance = 0
    
    def deposit(self, amount):

        self.blance += amount
        return self.blance

    def draw(self, amount):

        self.blance -= amount
        return self.blance
    def _check_blance_positive(self):
        assert self.blance >= 0, "please iv"
    

