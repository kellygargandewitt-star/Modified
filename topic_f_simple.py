"""Simplified Topic F (Lessons 25-28, book pages 171-195) for Grade 3 Module 2.

Readiness TEKS only: 3.4A (add/subtract within 1,000) and 3.5A (strip diagrams
and equations for one- and two-step problems). Estimation (3.4B) becomes exact
answers; "is it reasonable?" becomes "check by adding back." Measuring
activities give the measurements. 1-3 problems per page, plain layout,
book page numbers kept, at most one regrouping per problem.

Run: python3 topic_f_simple.py  ->  writes G3_M2_TopicF_Simplified.pdf
"""
from build_module2 import MARGIN, W, footer, main, rich_line
from reteach_mid_module import sentence
from topic_e_simple import block, column, start, strip, strip_total, sum_grid, text, two_step

L25 = (25, "Decompose once to subtract measurements including three-digit minuends with zeros.")
L26 = (26, "Decompose twice to subtract measurements including three-digit minuends with zeros.")
L27 = (27, "Estimate differences by rounding and apply to solve measurement word problems.")
L28 = (28, "Estimate sums and differences of measurements by rounding, then solve word problems.")

TIP_SUB = "Subtract the ones first. If the top is smaller, trade 1 ten for 10 ones."
TIP_SUB0 = "Top digit is 0? Trade 1 hundred for 10 tens first."
TIP_PART = "Know the total and one part? Subtract to find the other part."


def one(c, y, num, lines, model, sent, col, op="−"):
    return block(c, y, num, lines, model, [sent], col, col_op=op)


# ---------------------------------------------------------------- Lesson 25

def page_171(c):
    y = start(c, "Lesson 25 Application Problem", "TEKS 3.4A, 3.5A", "\"How many in all\" means add.")
    one(c, y, "", [[("Tara has 2 water bottles: ", False), ("471 mL", True), (" and ", False), ("254 mL", True), (".", False)],
                   [("How many milliliters in all?", False)]],
        strip([("", [("471", 471, False), ("254", 254, False)])], 725, brace=("?", 0, 725)),
        "471 + 254 = |______|  mL", [471, 254], "+")
    footer(c, *L25, 171)


def page_173(c):
    y = start(c, "Lesson 25 Problem Set", "TEKS 3.4A", TIP_SUB)
    y = text(c, y, "1.", [[("Subtract.", False)]])
    sum_grid(c, y - 10, [("a", 60, 24, "−"), ("b", 360, 24, "−"), ("c", 518, 21, "−"), ("d", 307, 130, "−")])
    footer(c, *L25, 173)


def page_174(c):
    y = start(c, "Lesson 25 Problem Set", "TEKS 3.4A, 3.5A", TIP_PART)
    y = one(c, y, "2.", [[("Flour, sugar, and salt weigh ", False), ("405 ounces", True), (" in all.", False)],
                         [("Sugar and salt weigh ", False), ("230 ounces", True), (". How much does the flour weigh?", False)]],
            strip_total("405", [("230", 230, False), ("?", 175, False)], 405),
            "405 − 230 = |______|  ounces", [405, 230])
    y -= 40
    one(c, y, "3.", [[("The Lost Ship", True), (" is ", False), ("117 minutes", True), (" long.", False)],
                     [("Champions", True), (" is ", False), ("22 minutes shorter", True), (". How long is Champions?", False)]],
        strip([("Lost Ship", [("117", 117, False)]), ("Champions", [("?", 95, False)])], 117),
        "117 − 22 = |______|  minutes", [117, 22])
    footer(c, *L25, 174)


def page_175(c):
    y = start(c, "Lesson 25 Exit Ticket", "TEKS 3.4A, 3.5A", TIP_SUB)
    y = text(c, y, "1.", [[("Subtract.", False)]])
    sum_grid(c, y - 10, [("a", 381, 146, "−"), ("b", 730, 420, "−")], bottom=y - 200)
    y -= 230
    one(c, y, "2.", [[("A banner is ", False), ("408 cm", True), (" long. Carly paints ", False), ("180 cm", True), (".", False)],
                     [("How much is left to paint?", False)]],
        strip_total("408", [("180", 180, False), ("?", 228, False)], 408),
        "408 − 180 = |______|  cm", [408, 180])
    footer(c, *L25, 175)


# ---------------------------------------------------------------- Lesson 26

def page_177(c):
    y = start(c, "Lesson 26 Application Problem", "TEKS 3.4A, 3.5A", TIP_PART)
    one(c, y, "", [[("A washer and dryer weigh ", False), ("417 pounds", True), (" together.", False)],
                   [("The washer weighs ", False), ("223 pounds", True), (". How much does the dryer weigh?", False)]],
        strip_total("417", [("223", 223, False), ("?", 194, False)], 417),
        "417 − 223 = |______|  pounds", [417, 223])
    footer(c, *L26, 177)


def page_179(c):
    y = start(c, "Lesson 26 Problem Set", "TEKS 3.4A", TIP_SUB0)
    y = text(c, y, "1.", [[("Subtract.", False)]])
    sum_grid(c, y - 10, [("a", 340, 60, "−"), ("b", 340, 260, "−"), ("c", 513, 140, "−"), ("d", 700, 50, "−")])
    footer(c, *L26, 179)


def page_180(c):
    y = start(c, "Lesson 26 Problem Set", "TEKS 3.4A, 3.5A", TIP_PART)
    y = one(c, y, "2.", [[("The trip is ", False), ("672 km", True), (". David still has ", False), ("480 km", True), (" left.", False)],
                         [("How far has he driven so far?", False)]],
            strip_total("672", [("?", 192, False), ("480", 480, False)], 672),
            "672 − 480 = |______|  km", [672, 480])
    y -= 40
    one(c, y, "4.", [[("Tank B holds ", False), ("400 liters", True), (". Tank A holds ", False), ("150 fewer", True), (" liters.", False)],
                     [("How much does Tank A hold?", False)]],
        strip([("Tank B", [("400", 400, False)]), ("Tank A", [("?", 250, False)])], 400),
        "400 − 150 = |______|  liters", [400, 150])
    footer(c, *L26, 180)


def page_181(c):
    y = start(c, "Lesson 26 Exit Ticket", "TEKS 3.4A, 3.5A", TIP_SUB)
    y = text(c, y, "1.", [[("Subtract.", False)]])
    sum_grid(c, y - 10, [("a", 346, 180, "−"), ("b", 700, 590, "−")], bottom=y - 200)
    y -= 230
    one(c, y, "2.", [[("The horse weighs ", False), ("725 pounds", True), (". The pig weighs ", False),
                      ("600 pounds less", True), (".", False)],
                     [("How much does the pig weigh?", False)]],
        strip([("Horse", [("725", 725, False)]), ("Pig", [("?", 125, False)])], 725),
        "725 − 600 = |______|  pounds", [725, 600])
    footer(c, *L26, 181)


# ---------------------------------------------------------------- Lesson 27 (estimates become exact answers)

def page_183(c):
    y = start(c, "Lesson 27 Application Problem", "TEKS 3.4A, 3.5A", "\"Empties out\" means subtract.")
    one(c, y, "", [[("Millie's fish tank holds ", False), ("403 liters", True), (". She empties out ", False),
                    ("180 liters", True), (".", False)],
                   [("How many liters are left?", False)]],
        strip_total("403", [("180", 180, False), ("?", 223, False)], 403),
        "403 − 180 = |______|  liters", [403, 180])
    footer(c, *L27, 183)


def page_184(c):
    y = start(c, "Lesson 27 Application Problem", "TEKS 3.4A", "Check subtraction by adding back.")
    y = text(c, y, "", [[("Check your answer from page 183. Add the part you took out back on.", False)]])
    sentence(c, MARGIN + 24, y - 40, "______|  +  180  =  |______", size=18, wide_w=80)
    column(c, W - MARGIN - 130, y - 10, [None, 180], "+", places=3)
    rich_line(c, MARGIN + 24, y - 110, [("Did you get ", False), ("403", True), ("?   ", False), ("yes  /  no", True)], 16)
    footer(c, *L27, 184)


def page_185(c):
    y = start(c, "Lesson 27 Problem Set", "TEKS 3.4A", TIP_SUB)
    y = text(c, y, "1.", [[("Find the exact differences.", False)]])
    sum_grid(c, y - 10, [("A", 448, 153, "−"), ("B", 747, 261, "−"), ("C", 451, 141, "−"), ("D", 756, 248, "−")])
    footer(c, *L27, 185)


def page_186(c):
    y = start(c, "Lesson 27 Problem Set", "TEKS 3.4A, 3.5A", TIP_PART)
    y = one(c, y, "2.", [[("Camden uses ", False), ("372 liters", True), (" of gas in 2 months. Month 1: ", False),
                          ("180 liters", True), (".", False)],
                         [("How many liters in month 2?", False)]],
            strip_total("372", [("180", 180, False), ("?", 192, False)], 372),
            "372 − 180 = |______|  liters", [372, 180])
    y -= 40
    one(c, y, "3.", [[("A cat, dog, and rabbit weigh ", False), ("800 ounces", True), (".", False)],
                     [("The cat and rabbit weigh ", False), ("350 oz", True), (". How much does the dog weigh?", False)]],
        strip_total("800", [("350", 350, False), ("?", 450, False)], 800),
        "800 − 350 = |______|  ounces", [800, 350])
    footer(c, *L27, 186)


def page_187(c):
    y = start(c, "Lesson 27 Exit Ticket", "TEKS 3.4A, 3.5A", TIP_PART)
    y = one(c, y, "", [[("A chef buys ", False), ("416 fluid ounces", True), (" of oil in 2 containers.", False)],
                       [("The large one has ", False), ("320 fluid ounces", True), (". How much is in the small one?", False)]],
            strip_total("416", [("320", 320, False), ("?", 96, False)], 416),
            "416 − 320 = |______|  fl oz", [416, 320])
    y -= 30
    rich_line(c, MARGIN, y, [("Check: ", True), ("add back.", False)], 14)
    sentence(c, MARGIN + 24, y - 40, "______|  +  320  =  |______", size=16, wide_w=80)
    footer(c, *L27, 187)


# ---------------------------------------------------------------- Lesson 28

def page_189(c):
    y = start(c, "Lesson 28 Application Problem", "TEKS 3.4A, 3.5A", "Two balloons with the same amount: add it twice.")
    one(c, y, "", [[("Each water balloon has ", False), ("238 mL", True), (" of water.", False)],
                   [("How many milliliters are in ", False), ("2", True), (" balloons?", False)]],
        strip([("", [("238", 238, False), ("238", 238, False)])], 476, brace=("?", 0, 476)),
        "238 + 238 = |______|  mL", [238, 238], "+")
    footer(c, *L28, 189)


def page_191(c):
    y = start(c, "Lesson 28 Problem Set", "TEKS 3.4A", "\"Total\" means add.  \"Difference\" means subtract.")
    y = text(c, y, "1.", [[("The beans weigh ", False), ("52 oz", True), (". The rice weighs ", False), ("35 oz", True), (".", False)]])
    rich_line(c, MARGIN + 24, y - 10, [("a.  Find the ", False), ("total", True), (".", False)], 14)
    sentence(c, MARGIN + 60, y - 50, "52 + 35 = |______|  oz", size=18, wide_w=80)
    column(c, W - MARGIN - 130, y - 20, [52, 35])
    y -= 190
    rich_line(c, MARGIN + 24, y, [("b.  Find the ", False), ("difference", True), (".", False)], 14)
    sentence(c, MARGIN + 60, y - 40, "52 − 35 = |______|  oz", size=18, wide_w=80)
    column(c, W - MARGIN - 130, y - 10, [52, 35], "−")
    footer(c, *L28, 191)


def page_192(c):
    two_step(c, 192, L28, "Lesson 28 Problem Set", "2.",
             [[("Yarn A is ", False), ("24 cm", True), (". Yarn B is ", False), ("31 cm", True), (". Yarn C is ", False),
               ("15 cm", True), (".", False)],
              [("How much longer are A and C together than B?", False)]],
             strip([("A + C", [("24", 24, False), ("15", 15, False)]), ("B", [("31", 31, False)])], 39),
             "24 + 15 = |______|  (A + C)", "______| − 31 = |______|  cm", [24, 15], [None, 31], "−",
             tip="Step 1: add A and C. Step 2: subtract B.")


def page_193(c):
    y = start(c, "Lesson 28 Problem Set", "TEKS 3.4A", "\"Total\" means add.  \"Difference\" means subtract.")
    y = text(c, y, "3.", [[("Container D has ", False), ("46 mL", True), (". Container E has ", False), ("28 mL", True), (".", False)]])
    rich_line(c, MARGIN + 24, y - 10, [("a.  Find the ", False), ("total", True), (".", False)], 14)
    sentence(c, MARGIN + 60, y - 50, "46 + 28 = |______|  mL", size=18, wide_w=80)
    column(c, W - MARGIN - 130, y - 20, [46, 28])
    y -= 190
    rich_line(c, MARGIN + 24, y, [("b.  Find the ", False), ("difference", True), (".", False)], 14)
    sentence(c, MARGIN + 60, y - 40, "46 − 28 = |______|  mL", size=18, wide_w=80)
    column(c, W - MARGIN - 130, y - 10, [46, 28], "−")
    footer(c, *L28, 193)


def page_194(c):
    two_step(c, 194, L28, "Lesson 28 Problem Set", "4.",
             [[("A movie with previews is ", False), ("115 minutes", True), (".", False)],
              [("The previews are ", False), ("5, 4, 3, 5, and 4", True), (" minutes.", False)],
              [("How long is the movie without previews?", False)]],
             strip_total("115", [("previews", 40, False), ("? movie", 75, False)], 115),
             "5 + 4 + 3 + 5 + 4 = |______", "115 − |______| = |______|  minutes", None, [115, None], "−",
             tip="Step 1: add the previews. Step 2: subtract from 115.")


def page_195(c):
    y = start(c, "Lesson 28 Exit Ticket", "TEKS 3.4A, 3.5A", "\"Total\" means add.  \"How much more\" means subtract.")
    y = text(c, y, "", [[("Rogelio drinks ", False), ("230 mL", True), (" at breakfast, ", False), ("300 mL", True),
                         (" at lunch,", False)],
                        [("and ", False), ("170 mL", True), (" at dinner.", False)]])
    rich_line(c, MARGIN, y - 10, [("a.  ", True), ("How much water in all?", False)], 14)
    sentence(c, MARGIN + 40, y - 50, "230 + 300 = |______", size=16, wide_w=80)
    sentence(c, MARGIN + 40, y - 90, "______|  +  170  =  |______|  mL", size=16, wide_w=80)
    y -= 190
    rich_line(c, MARGIN, y, [("b.  ", True), ("How much ", False), ("more", True), (" at lunch than at dinner?", False)], 14)
    sentence(c, MARGIN + 40, y - 40, "300 − 170 = |______|  mL", size=16, wide_w=80)
    column(c, W - MARGIN - 130, y - 10, [300, 170], "−")
    footer(c, *L28, 195)


BOOK = {171: page_171, 173: page_173, 174: page_174, 175: page_175, 177: page_177, 179: page_179,
        180: page_180, 181: page_181, 183: page_183, 184: page_184, 185: page_185, 186: page_186,
        187: page_187, 189: page_189, 191: page_191, 192: page_192, 193: page_193, 194: page_194,
        195: page_195}

if __name__ == "__main__":
    main("G3_M2_TopicF_Simplified.pdf", [BOOK[k] for k in sorted(BOOK)],
         "Bluebonnet Learning Grade 3 Module 2 Topic F – Simplified")
