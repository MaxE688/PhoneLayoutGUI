from Model.constants import phoneModels

class NewConfiguration:
    
    def getString(self, model):
        cfg = ""

        if model == "Astra 6737i":
            #return 6 topsoftkeys, and 3 softkeys
            str = ""
            for i in range(6):
                pass
                
        elif phoneModels[model]["brand"] == "Astra":
            str = ""
            for i in range(phoneModels[model]['tilesPerPage']):
                str += ("softkey" + str(i+1) + " type = NA\n" +
                       "softkey" + str(i+1) + " label = " + str(i+1) + "\n" +
                       "softkey" + str(i+1) + " value = " + str(i+1) + "\n\n")
            cfg = str
        elif phoneModels[model]["brand"] == "Yealink":
            str = ""
            for i in range(phoneModels[model]['tilesPerPage']):
                str += ("linekey." + str(i+1) + ".type = 0\n" +
                       "linekey." + str(i+1) + ".line = 1\n" +
                       "linekey." + str(i+1) + ".label = " + str(i+1) + "\n\n")
            cfg = str

        return cfg
