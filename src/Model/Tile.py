
class Tile:
   
    def __init__(self, id, type, line, value, label):
        self.id = id
        self.type = type
        if line == None:
            self.line = None
        else:
            self.line = line
        self.label = label
        if value != None:
            self.value = value
        else:
            self.value = 0

    

    def toString(self):
        return "id: " + str(self.id) + "\ntype: " + str(self.type) + "\nline: " + str(self.line) + "\nlabel: " + str(self.label) + "\nvalue: " + str(self.value) + "\n"
