# from Model.A37 import A37
# from Model.A39 import A39
# from Model.T48 import T48
# from Model.T46 import T46
# from Model.T42 import T42
# from Model.EXP40 import EXP40



MAX_COL = 5
MAX_ROW = 6
TILE_HEIGHT = 80
TILE_WIDTH = 280
WINDOW_HEIGHT = TILE_HEIGHT*MAX_ROW
WINDOW_WIDTH = TILE_WIDTH*MAX_COL
SELECT_MODEL_FRAME_WIDTH = "500"
SELECT_MODEL_FRAME_HEIGHT = "200"

phoneModels = {
                "Astra 6737i":{
                                "brand":"Astra",
                                "tilesPerPage":12,
                                # "layout":A37()
                              },
                "Astra 6739i":{
                                "brand":"Astra",
                                "tilesPerPage":12,
                                # "layout":A39()
                              },
                "Yealink T48":{
                                "brand":"Yealink",
                                "tilesPerPage":30,
                                # "layout":T48()
                              },
                "Yealink T46":{
                                "brand":"Yealink",
                                "tilesPerPage":10,
                                # "layout":T46()
                              },
                "Yealink T42":{
                                "brand":"Yealink",
                                "tilesPerPage":6,
                                # "layout":T42()
                              },
                "Yealink T41":{
                                "brand":"Yealink",
                                "tilesPerPage":6,
                                # "layout":T42()
                              },
                "Yealink EXP40":{
                                "brand":"Yealink",
                                "tilesPerPage":20,
                                # "layout":EXP40()
                              },
              }
