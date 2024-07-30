
class Tile:
    """
    tile class contains all of the information that belongs to a single button on phone models

    Attributes
    ----------
    id : str
        number of tile based on it's location in list
    type : str
        type of the button
    line : str
        line of the button
    label : str
        label of the button
    value : str
        value of the button

    Methods
    -------
    toString()
        returns tile object represented by a string

    """
   
    def __init__(self, id, type, line, value, label):
        """
        Parameters
        ----------
        id : str
        type : str
        line : str
        value : str
        label : str
        """

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
