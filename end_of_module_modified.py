"""Modified Grade 3 Module 2 End-of-Module Assessment (12 questions).

Students take the test on the computer, so this keeps everything that the
computer's answer key depends on:
  * same questions, same order, same numbers
  * same answer choices in the same order with the same letters
Supports: plain wording, number sentences set up, strip diagrams / number
lines, partly worked steps. Question 1: most fact answers are filled in;
students fill in only the x1, /1, x10, and /10 facts.

Run: python3 end_of_module_modified.py  ->  writes G3_M2_EndOfModule_Modified.pdf
"""
from reportlab.lib.colors import HexColor, black

from build_module2 import MARGIN, W, blank, footer, header, main, rich_line
from lessons_15_19_simple import hline, stacked
from lessons_20_24 import bars, top_brace
from reteach_mid_module import sentence
from topic_e_simple import column

GREY = HexColor("#666666")
FOOT = ("Module 2:", "Place Value and Problem Solving with Units of Measure")
TITLE = "End-of-Module Assessment"


def start(c, tip=None):
    y = header(c, TITLE)
    if tip:
        rich_line(c, MARGIN, y - 6, [("Tip: ", True), (tip, False)], 12)
        return y - 44
    return y - 20


def q(c, y, num, lines, size=14):
    for k, parts in enumerate(lines):
        rich_line(c, MARGIN + (0 if k == 0 else 26), y, ([(f"{num}.  ", True)] if k == 0 else []) + parts, size)
        y -= 22
    return y


def choices(c, x, y, items, gap=28, size=14):
    for letter, text in items:
        rich_line(c, x, y, [(f"{letter}     ", True), (text, False)], size)
        y -= gap
    return y


# ---------------------------------------------------------------- Question 1: facts

FACTS = [
    # (left, right, answer, give_answer)   "_" marks the blank
    ("3 × 1 = _", 3, False), ("2 ÷ 1 = _", 2, False), ("_ = 20 ÷ 10", 2, False), ("2 × 2 = _", 4, True), ("5 × _ = 10", 2, True),
    ("_ × 2 = 4", 2, True), ("10 ÷ 5 = _", 2, True), ("10 × _ = 30", 3, False), ("_ = 2 × 3", 6, True), ("_ = 12 ÷ 4", 3, True),
    ("4 × 3 = _", 12, True), ("15 ÷ 5 = _", 3, True), ("_ × 4 = 16", 4, True), ("_ = 40 ÷ 10", 4, False), ("2 × 4 = _", 8, True),
    ("3 × 4 = _", 12, True), ("4 × _ = 12", 3, True), ("20 ÷ 4 = _", 5, True), ("_ = 10 × 5", 50, False), ("_ × 5 = 25", 5, True),
    ("4 × _ = 20", 5, True), ("_ = 10 ÷ 2", 5, True), ("_ × 3 = 18", 6, True), ("10 × 6 = _", 60, False), ("30 ÷ 5 = _", 6, True),
    ("3 × 6 = _", 18, True), ("_ = 24 ÷ 4", 6, True), ("5 × _ = 35", 7, True), ("_ = 10 × 7", 70, False), ("14 ÷ 2 = _", 7, True),
    ("2 × 7 = _", 14, True), ("_ × 4 = 28", 7, True), ("_ = 40 ÷ 5", 8, True), ("10 × _ = 80", 8, False), ("_ = 3 × 8", 24, True),
    ("24 ÷ 3 = _", 8, True), ("80 ÷ 10 = _", 8, False), ("36 ÷ 4 = _", 9, True), ("5 × 9 = _", 45, True), ("2 × _ = 18", 9, True),
]


def fact(c, x, y, text, ans, given, size=11.5, bw=26):
    left, right = text.split("_")
    x = rich_line(c, x, y, [(left, False)], size)
    if given:
        c.setFont("Sans-Bold", size)
        c.drawCentredString(x + bw / 2 + 1, y, str(ans))
        c.setLineWidth(0.6)
        c.line(x + 1, y - 3, x + bw + 1, y - 3)
        c.setLineWidth(1)
    else:
        c.setLineWidth(1.2)
        c.rect(x + 1, y - 6, bw, 20)
        c.setLineWidth(1)
    rich_line(c, x + bw + 3, y, [(right, False)], size)


def page_1(c):
    y = start(c)
    y = q(c, y, "1", [[("Multiplication and division facts.", False)],
                      [("Most answers are ", False), ("filled in", True), (". Copy them. Fill in the ", False),
                       ("empty boxes", True), (".", False)]])
    rich_line(c, MARGIN + 26, y - 2, [("× 1", True), (" or ", False), ("÷ 1", True), (": the number stays the same.    ", False),
                                     ("× 10", True), (": add a 0.    ", False), ("÷ 10", True), (": take off the 0.", False)], 12)
    y -= 46
    cw = (W - 2 * MARGIN) / 5
    for i, (text, ans, given) in enumerate(FACTS):
        fact(c, MARGIN + (i % 5) * cw, y - (i // 5) * 62, text, ans, given)
    footer(c, *FOOT, 1)


# ---------------------------------------------------------------- Questions 2-3

def page_2(c):
    y = start(c, "\"Difference\" means subtract.")
    y = q(c, y, "2", [[("Trail mix weighs ", False), ("56 ounces", True), (". Almonds weigh ", False), ("18 ounces", True), (".", False)],
                      [("What is the ", False), ("difference", True), ("?", False)]])
    bars(c, MARGIN + 90, y - 14, 260, [("Trail mix", [("56", 56, False)]),
                                        ("Almonds", [("18", 18, False), ("?", 38, False)])], 56, row_gap=34, h=26)
    column(c, W - MARGIN - 130, y - 6, [56, 18], "−")
    sentence(c, MARGIN + 26, y - 110, "56 − 18 = |______|  ounces", size=16, wide_w=80)

    y -= 200
    y = q(c, y, "3", [[("Round ", False), ("3,746", True), (" to the nearest ", False), ("hundred", True), (".", False)]])
    hline(c, MARGIN + 40, W - MARGIN - 40, y - 40, 3700, 3800, 10, 50)
    c.circle(MARGIN + 40 + (W - 2 * MARGIN - 80) * 46 / 100, y - 40, 4, stroke=0, fill=1)
    c.setFont("Sans-Bold", 11)
    c.drawCentredString(MARGIN + 40 + (W - 2 * MARGIN - 80) * 46 / 100, y - 26, "3,746")
    ty = y - 90
    for s in ("3,746 is between 3,700 and 3,800.", "The halfway number is 3,750.",
              "3,746 is LESS than 3,750, so round DOWN."):
        rich_line(c, MARGIN + 26, ty, [(s, False)], 13)
        ty -= 24
    sentence(c, MARGIN + 26, ty - 14, "3,746 rounds to  |______", size=16, wide_w=90)
    footer(c, *FOOT, 2)


# ---------------------------------------------------------------- Questions 4-5

def page_3(c):
    y = start(c, "Same weight 3 times: add it 3 times.")
    y = q(c, y, "4", [[("One bag weighs ", False), ("45 pounds", True), (". A worker lifts ", False), ("3 bags", True), (".", False)]])
    c.drawImage("images/eom_scale.png", W - MARGIN - 120, y - 92, width=120, height=110,
                preserveAspectRatio=True, mask="auto")
    rich_line(c, MARGIN + 26, y - 20, [("a.  ", True), ("Estimate:", True), ("  45 rounds to 50.", False)], 13)
    sentence(c, MARGIN + 60, y - 56, "50 + 50 + 50 = |______|  pounds", size=15, wide_w=80)
    rich_line(c, MARGIN + 26, y - 106, [("b.  ", True), ("Exact:", True)], 13)
    sentence(c, MARGIN + 60, y - 142, "45 + 45 = |______", size=15, wide_w=80)
    sentence(c, MARGIN + 60, y - 178, "______|  +  45  =  |______|  pounds", size=15, wide_w=80)

    y -= 250
    y = q(c, y, "5", [[("Passenger 1's bags weigh ", False), ("120 pounds", True), (".", False)],
                      [("Passenger 2's bags weigh ", False), ("97 pounds", True), (".", False)],
                      [("How much ", False), ("more", True), (" does passenger 1's luggage weigh?", False)]])
    bars(c, MARGIN + 100, y - 14, 250, [("Passenger 1", [("120", 120, False)]),
                                         ("Passenger 2", [("97", 97, False), ("?", 23, False)])], 120, row_gap=34, h=26)
    column(c, W - MARGIN - 130, y - 6, [120, 97], "−")
    sentence(c, MARGIN + 26, y - 110, "120 − 97 = |______|  pounds", size=16, wide_w=80)
    footer(c, *FOOT, 3)


# ---------------------------------------------------------------- Questions 6-7

def page_4(c):
    y = start(c, "Compare from the left. Look at the thousands first.")
    y = q(c, y, "6", [[("Put the airports in order from ", False), ("greatest", True), (" to ", False), ("least", True), (".", False)]])
    rows = [("Biggs Army Airfield", 26730), ("East Texas Regional", 22480), ("Jack Brooks Regional", 26518)]
    ty = y - 14
    for name, n in rows:
        rich_line(c, MARGIN + 26, ty, [(name, False)], 13)
        c.setFont("Sans", 18)
        c.drawRightString(MARGIN + 320, ty, f"{n:,}")
        ty -= 30
    ty -= 10
    for k, lbl in enumerate(["Greatest:", "Next:", "Least:"]):
        rich_line(c, MARGIN + 26, ty, [(lbl, True)], 13)
        blank(c, MARGIN + 120, ty, 220)
        ty -= 34
    grey_note(c, MARGIN + 26, ty, "Hint: 22,480 has the smallest thousands. Then compare 26,730 and 26,518 by the hundreds.")

    y = ty - 50
    y = q(c, y, "7", [[("Which list goes from ", False), ("least", True), (" to ", False), ("greatest", True), ("?", False)],
                      [("Pick the list where the numbers get ", False), ("bigger every time", True), (".", False)]])
    choices(c, MARGIN + 30, y - 10, [("A", "53,607;   53,670;   53,760;   56,370"),
                                     ("B", "53,670;   53,607;   53,760;   56,370"),
                                     ("C", "56,370;   53,760;   53,670;   53,607"),
                                     ("D", "53,607;   53,760;   53,670;   56,370")], gap=30)
    footer(c, *FOOT, 4)


def grey_note(c, x, y, text, size=11):
    c.setFont("Sans", size)
    c.setFillColor(GREY)
    c.drawString(x, y, text)
    c.setFillColor(black)


# ---------------------------------------------------------------- Questions 8-9

def page_5(c):
    y = start(c, "Add the two pumpkins in each choice. Find the one that makes 200.")
    y = q(c, y, "8", [[("Mr. Diaz buys 2 pumpkins. Together they weigh ", False), ("200 ounces", True), (".", False)],
                      [("Which two pumpkins?", False)]])
    ty = y - 6
    for name, w in (("A", 110), ("B", 108), ("C", 114), ("D", 94), ("E", 86)):
        rich_line(c, W - MARGIN - 130, ty, [(f"Pumpkin {name}:  ", False), (f"{w} oz", True)], 12)
        ty -= 20
    y -= 20
    for letter, a, b, wa, wb in (("F", "C", "E", 114, 86), ("G", "A", "B", 110, 108),
                                 ("H", "B", "D", 108, 94), ("J", "D", "E", 94, 86)):
        rich_line(c, MARGIN + 30, y, [(f"{letter}     ", True), (f"Pumpkins {a} and {b}", False)], 14)
        sentence(c, MARGIN + 60, y - 24, f"{wa} + {wb} = |______", size=13, wide_w=60)
        y -= 58

    y -= 10
    y = q(c, y, "9", [[("What number is the same as  ", False), ("80,000 + 100 + 50 + 6", True), ("?", False)]])
    places = ["Ten\nThousands", "Thousands", "Hundreds", "Tens", "Ones"]
    digits = ["8", "0", "1", "5", "6"]
    cw, x0 = 70, MARGIN + 30
    for k, (p, d) in enumerate(zip(places, digits)):
        for j, ln in enumerate(p.split("\n")):
            c.setFont("Sans", 9)
            c.drawCentredString(x0 + k * cw + cw / 2, y - 10 - 10 * j, ln)
        c.rect(x0 + k * cw + 6, y - 58, cw - 12, 30)
        c.setFont("Sans-Bold", 18)
        c.drawCentredString(x0 + k * cw + cw / 2, y - 50, d)
    choices(c, x0 + 5 * cw + 30, y - 8, [("A", "81,056"), ("B", "80,156"), ("C", "8,516"), ("D", "80,516")], gap=22, size=13)
    footer(c, *FOOT, 5)


# ---------------------------------------------------------------- Question 10

def page_6(c):
    y = start(c, "60 minutes = 1 hour.")
    y = q(c, y, "10", [[("Ana read ", False), ("24 minutes", True), (". Ben read ", False), ("35 minutes", True),
                        (". Carlos read ", False), ("23 minutes", True), (".", False)],
                       [("What is the ", False), ("total", True), (" time? Write it in hours and minutes.", False)]])
    bars(c, MARGIN + 60, y - 14, 360, [("", [("24", 24, False), ("35", 35, False), ("23", 23, False)])], 82,
         brace=("?", 0, 82), h=26)
    y -= 110
    rich_line(c, MARGIN, y, [("Step 1:", True)], 13)
    sentence(c, MARGIN + 70, y, "24 + 23 = |______", size=16, wide_w=80)
    y -= 50
    rich_line(c, MARGIN, y, [("Step 2:", True)], 13)
    sentence(c, MARGIN + 70, y, "______|  +  35  =  |______|  minutes", size=16, wide_w=80)
    y -= 110
    rich_line(c, MARGIN, y, [("Step 3:", True)], 13)
    sentence(c, MARGIN + 70, y, "______|  minutes  =  60 minutes  +  |___|  minutes", size=14, wide_w=70, blank_w=50)
    y -= 50
    sentence(c, MARGIN + 70, y, "=  1 hour  |___|  minutes", size=18, blank_w=60)
    footer(c, *FOOT, 6)


# ---------------------------------------------------------------- Questions 11-12

def page_7(c):
    y = start(c, "Weight words: ounces, pounds, tons.")
    y = q(c, y, "11", [[("Which units measure ", False), ("weight", True), ("? Pick ", False), ("TWO", True), (".", False)],
                       [("(A shipping container full of bricks is very, very heavy.)", False)]])
    choices(c, MARGIN + 30, y - 10, [("A", "Gallons"), ("B", "Pounds"), ("C", "Feet"), ("D", "Milliliters"),
                                     ("F", "Fluid Ounces"), ("G", "Tons")], gap=28)
    y -= 210
    y = q(c, y, "12", [[("About how much liquid is in the container? Nearest ", False), ("liter", True), (".", False)]])
    c.drawImage("images/eom_beaker.png", MARGIN + 40, y - 230, width=180, height=220,
                preserveAspectRatio=True, mask="auto")
    rich_line(c, MARGIN + 260, y - 80, [("Look at the top of the liquid.", False)], 13)
    rich_line(c, MARGIN + 260, y - 104, [("Which line is it closest to?", False)], 13)
    sentence(c, MARGIN + 260, y - 150, "About  |___|  liters", size=18, blank_w=60)
    footer(c, *FOOT, 7)


PAGES = [page_1, page_2, page_3, page_4, page_5, page_6, page_7]

if __name__ == "__main__":
    main("G3_M2_EndOfModule_Modified.pdf", PAGES, "Grade 3 Module 2 End-of-Module Assessment – Modified")
