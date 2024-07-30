from Model.constants import Brand, Model, phoneModels

class NewConfiguration:
    """creates config string for when user wants to start without an existing config string
    
    Methods
    -------
    getString(model : str)
        returns a config string that is supported by the selected phone model

    """

    def getString(model):
        """returns newly generated config string
        
        Parameters
        ----------
        model : str
        """

        cfg = ""
        tilesRange = phoneModels[model]['tilesPerPage'] + 1
                
        if phoneModels[model]["brand"] == Brand.AASTRA.value:
            
            if model == Model.AASTRA_6737.value:
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
            

        elif phoneModels[model]["brand"] == Brand.YEALINK.value:
            
            for i in range(1, tilesRange):
                cfg += (
                    "linekey." + str(i) + ".type = 0\n" +
                    "linekey." + str(i) + ".line = 1\n" +
                    "linekey." + str(i) + ".label = " + str(i) + "\n\n"
                )
        # print(cfg)
        return cfg
