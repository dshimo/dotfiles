#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

"""
Main Collatz program
Contains all logic and functions
CACHE is simply a dictionary
"""

import sys
CACHE = {}
META_CACHE = {
    0: 179,
    1: 182,
    2: 217,
    3: 238,
    4: 215,
    5: 236,
    6: 262,
    7: 252,
    8: 247,
    9: 260,
    10: 268,
    11: 250,
    12: 263,
    13: 276,
    14: 271,
    15: 271,
    16: 266,
    17: 279,
    18: 261,
    19: 274,
    20: 256,
    21: 269,
    22: 269,
    23: 282,
    24: 264,
    25: 264,
    26: 308,
    27: 259,
    28: 259,
    29: 272,
    30: 272,
    31: 285,
    32: 267,
    33: 267,
    34: 311,
    35: 324,
    36: 249,
    37: 306,
    38: 244,
    39: 306,
    40: 288,
    41: 257,
    42: 288,
    43: 270,
    44: 270,
    45: 314,
    46: 283,
    47: 314,
    48: 296,
    49: 296,
    50: 278,
    51: 309,
    52: 340,
    53: 322,
    54: 260,
    55: 260,
    56: 322,
    57: 304,
    58: 273,
    59: 304,
    60: 335,
    61: 317,
    62: 286,
    63: 330,
    64: 299,
    65: 268,
    66: 268,
    67: 312,
    68: 312,
    69: 299,
    70: 312,
    71: 325,
    72: 263,
    73: 294,
    74: 325,
    75: 307,
    76: 307,
    77: 351,
    78: 338,
    79: 307,
    80: 320,
    81: 320,
    82: 320,
    83: 289,
    84: 320,
    85: 302,
    86: 302,
    87: 333,
    88: 333,
    89: 315,
    90: 315,
    91: 333,
    92: 315,
    93: 284,
    94: 315,
    95: 328,
    96: 297,
    97: 297,
    98: 284,
    99: 328,
    100: 341,
    101: 310,
    102: 310,
    103: 248,
    104: 310,
    105: 341,
    106: 354,
    107: 292,
    108: 279,
    109: 310,
    110: 292,
    111: 323,
    112: 323,
    113: 292,
    114: 305,
    115: 349,
    116: 305,
    117: 305,
    118: 336,
    119: 305,
    120: 318,
    121: 336,
    122: 318,
    123: 331,
    124: 287,
    125: 318,
    126: 331,
    127: 287,
    128: 331,
    129: 344,
    130: 331,
    131: 300,
    132: 331,
    133: 313,
    134: 300,
    135: 344,
    136: 313,
    137: 331,
    138: 313,
    139: 313,
    140: 344,
    141: 326,
    142: 375,
    143: 282,
    144: 326,
    145: 295,
    146: 357,
    147: 295,
    148: 326,
    149: 326,
    150: 370,
    151: 295,
    152: 308,
    153: 308,
    154: 352,
    155: 308,
    156: 383,
    157: 339,
    158: 321,
    159: 352,
    160: 370,
    161: 290,
    162: 339,
    163: 321,
    164: 334,
    165: 321,
    166: 352,
    167: 321,
    168: 321,
    169: 334,
    170: 290,
    171: 334,
    172: 303,
    173: 347,
    174: 334,
    175: 272,
    176: 334,
    177: 334,
    178: 347,
    179: 303,
    180: 365,
    181: 316,
    182: 334,
    183: 254,
    184: 316,
    185: 329,
    186: 347,
    187: 329,
    188: 316,
    189: 360,
    190: 329,
    191: 329,
    192: 347,
    193: 329,
    194: 342,
    195: 360,
    196: 298,
    197: 285,
    198: 329,
    199: 329,
    200: 342,
    201: 311,
    202: 342,
    203: 311,
    204: 311,
    205: 355,
    206: 373,
    207: 311,
    208: 311,
    209: 311,
    210: 342,
    211: 355,
    212: 355,
    213: 373,
    214: 293,
    215: 280,
    216: 386,
    217: 324,
    218: 324,
    219: 355,
    220: 324,
    221: 355,
    222: 324,
    223: 324,
    224: 324,
    225: 368,
    226: 368,
    227: 306,
    228: 355,
    229: 306,
    230: 443,
    231: 350,
    232: 337,
    233: 368,
    234: 381,
    235: 306,
    236: 337,
    237: 350,
    238: 306,
    239: 350,
    240: 368,
    241: 275,
    242: 319,
    243: 337,
    244: 275,
    245: 319,
    246: 332,
    247: 350,
    248: 288,
    249: 350,
    250: 332,
    251: 319,
    252: 319,
    253: 332,
    254: 363,
    255: 288,
    256: 332,
    257: 345,
    258: 301,
    259: 345,
    260: 332,
    261: 332,
    262: 301,
    263: 407,
    264: 332,
    265: 332,
    266: 314,
    267: 345,
    268: 270,
    269: 345,
    270: 407,
    271: 283,
    272: 314,
    273: 358,
    274: 332,
    275: 345,
    276: 314,
    277: 389,
    278: 345,
    279: 314,
    280: 345,
    281: 358,
    282: 314,
    283: 358,
    284: 358,
    285: 376,
    286: 314,
    287: 327,
    288: 389,
    289: 345,
    290: 327,
    291: 327,
    292: 340,
    293: 358,
    294: 296,
    295: 358,
    296: 327,
    297: 327,
    298: 371,
    299: 327,
    300: 371,
    301: 296,
    302: 340,
    303: 340,
    304: 340,
    305: 265,
    306: 309,
    307: 309,
    308: 371,
    309: 340,
    310: 371,
    311: 309,
    312: 384,
    313: 340,
    314: 278,
    315: 340,
    316: 353,
    317: 309,
    318: 353,
    319: 322,
    320: 371,
    321: 353,
    322: 309,
    323: 322,
    324: 384,
    325: 340,
    326: 247,
    327: 322,
    328: 291,
    329: 353,
    330: 322,
    331: 291,
    332: 353,
    333: 335,
    334: 322,
    335: 322,
    336: 366,
    337: 366,
    338: 335,
    339: 366,
    340: 304,
    341: 335,
    342: 353,
    343: 335,
    344: 304,
    345: 441,
    346: 348,
    347: 322,
    348: 335,
    349: 366,
    350: 304,
    351: 379,
    352: 335,
    353: 304,
    354: 348,
    355: 379,
    356: 348,
    357: 304,
    358: 379,
    359: 348,
    360: 410,
    361: 348,
    362: 361,
    363: 317,
    364: 317,
    365: 361,
    366: 348,
    367: 286,
    368: 317,
    369: 361,
    370: 392,
    371: 348,
    372: 317,
    373: 348,
    374: 330,
    375: 361,
    376: 423,
    377: 361,
    378: 330,
    379: 361,
    380: 379,
    381: 374,
    382: 361,
    383: 330,
    384: 330,
    385: 348,
    386: 330,
    387: 299,
    388: 330,
    389: 436,
    390: 361,
    391: 330,
    392: 299,
    393: 361,
    394: 405,
    395: 312,
    396: 330,
    397: 330,
    398: 374,
    399: 299,
    400: 374,
    401: 387,
    402: 268,
    403: 343,
    404: 343,
    405: 405,
    406: 361,
    407: 268,
    408: 312,
    409: 312,
    410: 449,
    411: 330,
    412: 343,
    413: 374,
    414: 374,
    415: 312,
    416: 387,
    417: 343,
    418: 343,
    419: 281,
    420: 343,
    421: 325,
    422: 356,
    423: 418,
    424: 356,
    425: 356,
    426: 356,
    427: 374,
    428: 294,
    429: 281,
    430: 312,
    431: 343,
    432: 387,
    433: 343,
    434: 356,
    435: 281,
    436: 325,
    437: 387,
    438: 400,
    439: 356,
    440: 325,
    441: 294,
    442: 356,
    443: 338,
    444: 325,
    445: 338,
    446: 325,
    447: 325,
    448: 369,
    449: 369,
    450: 387,
    451: 307,
    452: 294,
    453: 369,
    454: 338,
    455: 338,
    456: 356,
    457: 338,
    458: 307,
    459: 307,
    460: 307,
    461: 444,
    462: 369,
    463: 325,
    464: 338,
    465: 369,
    466: 369,
    467: 413,
    468: 382,
    469: 338,
    470: 307,
    471: 276,
    472: 338,
    473: 307,
    474: 382,
    475: 320,
    476: 307,
    477: 382,
    478: 351,
    479: 351,
    480: 413,
    481: 382,
    482: 351,
    483: 307,
    484: 320,
    485: 338,
    486: 382,
    487: 382,
    488: 382,
    489: 351,
    490: 320,
    491: 320,
    492: 426,
    493: 395,
    494: 351,
    495: 320,
    496: 320,
    497: 289,
    498: 351,
    499: 395,
    500: 364,
    501: 320,
    502: 426,
    503: 320,
    504: 364,
    505: 364,
    506: 382,
    507: 364,
    508: 377,
    509: 364,
    510: 333,
    511: 470,
    512: 333,
    513: 351,
    514: 364,
    515: 395,
    516: 302,
    517: 333,
    518: 439,
    519: 364,
    520: 333,
    521: 364,
    522: 333,
    523: 302,
    524: 364,
    525: 408,
    526: 408,
    527: 377,
    528: 377,
    529: 333,
    530: 346,
    531: 346,
    532: 377,
    533: 377,
    534: 346,
    535: 302,
    536: 333,
    537: 377,
    538: 346,
    539: 346,
    540: 408,
    541: 364,
    542: 346,
    543: 359,
    544: 315,
    545: 346,
    546: 452,
    547: 377,
    548: 333,
    549: 315,
    550: 346,
    551: 377,
    552: 315,
    553: 346,
    554: 421,
    555: 390,
    556: 346,
    557: 315,
    558: 315,
    559: 284,
    560: 359,
    561: 328,
    562: 359,
    563: 328,
    564: 421,
    565: 328,
    566: 359,
    567: 359,
    568: 359,
    569: 359,
    570: 377,
    571: 359,
    572: 372,
    573: 359,
    574: 328,
    575: 346,
    576: 390,
    577: 390,
    578: 346,
    579: 359,
    580: 266,
    581: 328,
    582: 328,
    583: 434,
    584: 372,
    585: 359,
    586: 359,
    587: 328,
    588: 315,
    589: 297,
    590: 359,
    591: 403,
    592: 328,
    593: 328,
    594: 328,
    595: 328,
    596: 372,
    597: 372,
    598: 341,
    599: 372,
    600: 372,
    601: 403,
    602: 297,
    603: 297,
    604: 372,
    605: 341,
    606: 328,
    607: 341,
    608: 403,
    609: 359,
    610: 341,
    611: 354,
    612: 310,
    613: 310,
    614: 310,
    615: 447,
    616: 372,
    617: 372,
    618: 310,
    619: 341,
    620: 372,
    621: 372,
    622: 310,
    623: 354,
    624: 385,
    625: 354,
    626: 509,
    627: 341,
    628: 279,
    629: 279,
    630: 341,
    631: 310,
    632: 385,
    633: 354,
    634: 310,
    635: 416,
    636: 310,
    637: 354,
    638: 354,
    639: 354,
    640: 416,
    641: 372,
    642: 416,
    643: 279,
    644: 279,
    645: 310,
    646: 323,
    647: 341,
    648: 323,
    649: 385,
    650: 341,
    651: 336,
    652: 354,
    653: 385,
    654: 323,
    655: 385,
    656: 429,
    657: 354,
    658: 398,
    659: 354,
    660: 323,
    661: 323,
    662: 292,
    663: 292,
    664: 367,
    665: 442,
    666: 323,
    667: 367,
    668: 323,
    669: 336,
    670: 323,
    671: 323,
    672: 367,
    673: 336,
    674: 367,
    675: 385,
    676: 336,
    677: 336,
    678: 380,
    679: 367,
    680: 336,
    681: 336,
    682: 305,
    683: 380,
    684: 336,
    685: 354,
    686: 398,
    687: 380,
    688: 292,
    689: 336,
    690: 336,
    691: 442,
    692: 323,
    693: 367,
    694: 367,
    695: 336,
    696: 336,
    697: 318,
    698: 367,
    699: 367,
    700: 367,
    701: 411,
    702: 380,
    703: 349,
    704: 504,
    705: 380,
    706: 305,
    707: 349,
    708: 349,
    709: 336,
    710: 380,
    711: 380,
    712: 411,
    713: 380,
    714: 305,
    715: 305,
    716: 380,
    717: 349,
    718: 336,
    719: 349,
    720: 411,
    721: 367,
    722: 411,
    723: 349,
    724: 362,
    725: 305,
    726: 349,
    727: 318,
    728: 362,
    729: 318,
    730: 380,
    731: 336,
    732: 380,
    733: 349,
    734: 349,
    735: 424,
    736: 318,
    737: 380,
    738: 424,
    739: 424,
    740: 393,
    741: 318,
    742: 349,
    743: 318,
    744: 318,
    745: 349,
    746: 287,
    747: 362,
    748: 318,
    749: 393,
    750: 362,
    751: 331,
    752: 318,
    753: 424,
    754: 318,
    755: 362,
    756: 362,
    757: 331,
    758: 362,
    759: 362,
    760: 380,
    761: 362,
    762: 331,
    763: 375,
    764: 362,
    765: 331,
    766: 331,
    767: 468,
    768: 331,
    769: 393,
    770: 349,
    771: 344,
    772: 393,
    773: 362,
    774: 331,
    775: 437,
    776: 331,
    777: 393,
    778: 437,
    779: 362,
    780: 344,
    781: 362,
    782: 331,
    783: 331,
    784: 313,
    785: 375,
    786: 300,
    787: 362,
    788: 406,
    789: 406,
    790: 375,
    791: 344,
    792: 437,
    793: 375,
    794: 331,
    795: 331,
    796: 468,
    797: 344,
    798: 300,
    799: 375,
    800: 375,
    801: 406,
    802: 388,
    803: 300,
    804: 331,
    805: 375,
    806: 344,
    807: 406,
    808: 331,
    809: 344,
    810: 406,
    811: 287,
    812: 362,
    813: 375,
    814: 313,
    815: 357,
    816: 344,
    817: 344,
    818: 450,
    819: 357,
    820: 450,
    821: 375,
    822: 344,
    823: 375,
    824: 326,
    825: 344,
    826: 313,
    827: 419,
    828: 313,
    829: 375,
    830: 344,
    831: 419,
    832: 388,
    833: 357,
    834: 344,
    835: 313,
    836: 344,
    837: 525,
    838: 344,
    839: 388,
    840: 357,
    841: 313,
    842: 388,
    843: 331,
    844: 357,
    845: 401,
    846: 313,
    847: 419,
    848: 313,
    849: 357,
    850: 357,
    851: 357,
    852: 326,
    853: 357,
    854: 419,
    855: 388,
    856: 375,
    857: 357,
    858: 370,
    859: 313,
    860: 357,
    861: 326,
    862: 326,
    863: 344,
    864: 326,
    865: 388,
    866: 326,
    867: 344,
    868: 357,
    869: 388,
    870: 326,
    871: 432,
    872: 326,
    873: 326,
    874: 388,
    875: 432,
    876: 370,
    877: 401,
    878: 326,
    879: 357,
    880: 326,
    881: 326,
    882: 313,
    883: 370,
    884: 295,
    885: 370,
    886: 445,
    887: 401,
    888: 295,
    889: 370,
    890: 339,
    891: 326,
    892: 295,
    893: 326,
    894: 370,
    895: 326,
    896: 370,
    897: 339,
    898: 370,
    899: 295,
    900: 401,
    901: 401,
    902: 383,
    903: 295,
    904: 383,
    905: 295,
    906: 445,
    907: 326,
    908: 370,
    909: 326,
    910: 476,
    911: 383,
    912: 401,
    913: 357,
    914: 370,
    915: 339,
    916: 339,
    917: 383,
    918: 339,
    919: 432,
    920: 339,
    921: 339,
    922: 445,
    923: 308,
    924: 370,
    925: 339,
    926: 370,
    927: 476,
    928: 383,
    929: 339,
    930: 370,
    931: 308,
    932: 370,
    933: 370,
    934: 414,
    935: 414,
    936: 383,
    937: 352,
    938: 445,
    939: 507,
    940: 383,
    941: 339,
    942: 339,
    943: 352,
    944: 383,
    945: 352,
    946: 383,
    947: 383,
    948: 383,
    949: 352,
    950: 414,
    951: 383,
    952: 414,
    953: 414,
    954: 383,
    955: 339,
    956: 352,
    957: 352,
    958: 321,
    959: 352,
    960: 414,
    961: 352,
    962: 383,
    963: 414,
    964: 352,
    965: 321,
    966: 365,
    967: 308,
    968: 321,
    969: 352,
    970: 458,
    971: 352,
    972: 321,
    973: 383,
    974: 383,
    975: 339,
    976: 383,
    977: 334,
    978: 383,
    979: 334,
    980: 427,
    981: 321,
    982: 383,
    983: 383,
    984: 352,
    985: 427,
    986: 352,
    987: 396,
    988: 321,
    989: 352,
    990: 321,
    991: 321,
    992: 352,
    993: 290,
    994: 365,
    995: 365,
    996: 365,
    997: 440,
    998: 396,
    999: 396
}

# ------------
# collatz_read
# ------------


def collatz_read(line):
    """
    read in first two ints
    input is a string or StringIO()
    return a list of two ints of range [begin, end]
    """
    scope = line.split()
    return [int(scope[0]), int(scope[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(begin, end):
    """
    beginning of the range, inclusive
    end       of the range, inclusive
    return the max cycle length of the range [begin, end]
    """
    # <your code>
    if begin > end:
        begin, end = end, begin
    midpoint = (end // 2) + 1
    if midpoint > begin:
        begin = midpoint

    max_cycle = 1

    number = begin
    if end - begin >= 1000:
        while number < end:
            if number % 1000 != 0:
                next_number = ((number // 1000) + 1) * 1000
                max_cycle = max(max_cycle, collatz_fetch(number, next_number, max_cycle))
                number = next_number
            else:
                if number + 1000 < end:
                    max_cycle = max(max_cycle, META_CACHE[number // 1000])
                    number += 1000
                elif number + 1000 > end:
                    return max(max_cycle, collatz_fetch(number, end, max_cycle))
                elif number + 1000 == end:
                    return max(max_cycle, META_CACHE[number // 1000])
        return max_cycle
    else:
        return collatz_fetch(begin, end, max_cycle)

# -------------
# collatz_fetch
# -------------


def collatz_fetch(begin, end, max_cycle):
    for number in range(begin, end + 1):
        cycle = collatz_cache(number)
        max_cycle = max(max_cycle, cycle)
    return max_cycle


# -------------
# collatz_cache
# -------------


def collatz_cache(number):
    """
    Cache system using a dict
    Simple recursive approach
    """
    if number in CACHE:
        return CACHE[number]
    else:
        if number == 1:
            return 1
        elif number % 2 == 0:
            CACHE[number] = 1 + collatz_cache(number // 2)
        elif number % 2 == 1:
            CACHE[number] = 2 + collatz_cache(number + (number >> 1) + 1)
        return CACHE[number]

# -------------
# collatz_print
# -------------


def collatz_print(output, begin, end, value):
    """
    print three ints
    output, or a writer
    beginning of the range, inclusive
    end       of the range, inclusive
    value of the max cycle length
    """
    output.write(str(begin) + " " + str(end) + " " + str(value) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(inln, output):
    """
    inln, or a reader
    output, or a writer
    """
    for line in inln:
        line = line.strip()
        if not line:
            continue
        begin, end = collatz_read(line)
        value = collatz_eval(begin, end)
        collatz_print(output, begin, end, value)

if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)
