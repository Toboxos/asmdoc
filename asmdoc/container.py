class Function:

    def __init__(self, fileName, name, description):
        self.name = name
        self.description = description
        self.params = []
        self.returns = "-"
        self.fileName = fileName

    def addParameter(self, name, description):
        self.params.append( (name, description) )

    def setReturns(self, description):
        self.returns = description
