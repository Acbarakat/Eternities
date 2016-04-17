import sys

RATIO = 20.0
#if sys.platform != "win32":
#    RATIO = 7.5

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
        #"fn_italic": "data/fonts/RobotoCondensed-LightItalic.ttf",
        #"fn_bolditalic": "data/fonts/RobotoCondensed-Italic.ttf"
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
        #"fn_bolditalic": "data/fonts/RobotoCondensed-Italic.ttf"
    },
]