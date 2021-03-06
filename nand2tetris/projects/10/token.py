#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 10
# FILENAME:.......... token.py
# PYTHON VERSION:.... 3.3.0
#============================================================
class JackToken:
    FLAVOURS = ["integerConstant", "keyword", "stringConstant", "identifier", "symbol"]

    def __init__(self, flavour, value):
        if value == '<':
            self.value = '&lt;'
        elif value == '>':
            self.value = '&gt;'
        elif value == '"':
            self.value = '&quot;'
        elif value == '&':
            self.value = '&amp;'
        else:
            self.value = value
        if flavour in self.FLAVOURS:
            self.flavour = flavour
        else:
            print("Token type not found.")

    def __str__(self):
        return "<{0}> {1} </{0}>".format(self.flavour, self.value)

    def __eq__(self, other):
        return ((self.flavour == other.flavour) & (self.value == other.value))

    def getValue(self):
        return str(self.value)

    def getFlavour(self):
        return self.flavour
