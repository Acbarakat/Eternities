import sys

ABILITY_HEIGHT = 90.0
if sys.platform != "win32":
    ABILITY_HEIGHT = 90.0

LOYALTY = {
            "0": "./assets/loyaltynaught.png",
            "+": "./assets/loyaltyup.png",
            "-": "./assets/loyaltydown.png"
          }

FONTS = [  
    {
        "name": "Beleren",
        "fn_regular": "./assets/font/beleren-bold_P1.01.ttf",
        "fn_bold": "./assets/font/beleren-bold_P1.01.ttf",
    },
    {
        "name": "Matrix",
        "fn_regular": "./assets/font/MatrixRegular.ttf",
        "fn_bold": "./assets/font/MatrixBold.ttf",
    },
    {
        "name": "MatrixSmallCaps",
        "fn_regular": "./assets/font/MatrixSmallCaps_Regular.ttf",
        "fn_bold": "./assets/font/MatrixSmallCaps_Bold.ttf",
    },
    {
        "name": "MPlanti",
        "fn_regular": "./assets/font/mplantin.ttf",
        "fn_bold": "./assets/font/mplanti1.ttf",
        "fn_italic": "./assets/font/mplantinit.ttf",
    },
]