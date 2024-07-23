from enum import Enum

class Brand(Enum):
  AASTRA = "Aastra"
  YEALINK = "Yealink"


class Model(Enum):
  AASTRA_6737 = "Aastra 6737i"
  AASTRA_6739 = "Aastra 6739i"
  YEALINK_T48 = "Yealink T48"
  YEALINK_T46 = "Yealink T46"
  YEALINK_T42 = "Yealink T42"
  YEALINK_T41 = "Yealink T41"
  YEALINK_EXP40 = "Yealink EXP40"
  

MAX_COL = 5
MAX_ROW = 6


TILE_HEIGHT = 80
TILE_WIDTH = 280


WINDOW_HEIGHT = TILE_HEIGHT*MAX_ROW
WINDOW_WIDTH = TILE_WIDTH*MAX_COL


SELECT_MODEL_FRAME_WIDTH = "500"
SELECT_MODEL_FRAME_HEIGHT = "200"


phoneModels = {
  "Aastra 6737i":{
                  "brand":Brand.AASTRA.value,
                  "tilesPerPage":6
                },
  "Aastra 6739i":{
                  "brand":Brand.AASTRA.value,
                  "tilesPerPage":12
                },
  "Yealink T48":{
                  "brand":Brand.YEALINK.value,
                  "tilesPerPage":30
                },
  "Yealink T46":{
                  "brand":Brand.YEALINK.value,
                  "tilesPerPage":10
                },
  "Yealink T42":{
                  "brand":Brand.YEALINK.value,
                  "tilesPerPage":6
                },
  "Yealink T41":{
                  "brand":Brand.YEALINK.value,
                  "tilesPerPage":6
                },
  "Yealink EXP40":{
                  "brand":Brand.YEALINK.value,
                  "tilesPerPage":20
                },
}


