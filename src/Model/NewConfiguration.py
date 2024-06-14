from Model.constants import phoneModels

class NewConfiguration:

    def getString(model):
        cfg = ""
        tilesRange = phoneModels[model]['tilesPerPage'] + 1
                
        if phoneModels[model]["brand"] == "Astra":
            
            if model == "Astra 6737i":
                #return 6 topsoftkeys, and 3 softkeys
                tilesRange = 7
                for i in range(1, 7):
                    cfg += (
                        "topsoftkey" + str(i) + " type: NA\n"
                        "topsoftkey" + str(i) + " label: New\n"
                        "topsoftkey" + str(i) + " value: 0\n\n"
                    )
            
            for i in range(1, tilesRange):
                cfg += (
                    "softkey" + str(i) + " type: NA\n" +
                    "softkey" + str(i) + " label: " + str(i) + "\n" +
                    "softkey" + str(i) + " value: " + str(i) + "\n\n"
                )
            

        elif phoneModels[model]["brand"] == "Yealink":
            
            for i in range(tilesRange):
                cfg += (
                    "linekey." + str(i) + ".type = 0\n" +
                    "linekey." + str(i) + ".line = 1\n" +
                    "linekey." + str(i) + ".label = " + str(i) + "\n\n"
                )
        # print(cfg)
        return cfg
