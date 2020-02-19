class Function:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.params = []
        self.returns = "-"

    def addParameter(self, name, description):
        self.params.append( (name, description) )

    def setReturns(self, description):
        self.returns = description
