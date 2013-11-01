class Token:
    FLAVOURS = ["integerConstant", "keyword", "stringConstant", "identifier", "symbol"]

    def __init__(self, flavour, value):
        self.value = value
        if flavour in self.FLAVOURS:
            self.flavour = flavour
        else:
            print("Token type not found.")

    def __str__(self):
        return "<{0}>{1}</{0}>".format(self.flavour, self.value)        
