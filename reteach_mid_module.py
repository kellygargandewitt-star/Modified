"""Reteach for the Grade 3 Module 2 Mid-Module Assessment Task (book pages 37-40).

Each page starts with a "Let's Learn" worked example, then mirrors the
assessment questions in the same order with friendlier numbers and the
number sentences set up.

Run: python3 reteach_mid_module.py  ->  writes G3_M2_MidModule_Reteach.pdf
"""
import math

from reportlab.lib.colors import HexColor, black

from build_module2 import (
    MARGIN, W, blank, footer, header, helper_box, main, pv_chart, rich_line, teks,
)

LEARN_BG = HexColor("#EEF8EE")
LEARN_LINE = HexColor("#3E8E4A")
GREY = HexColor("#666666")
TITLE = "Mid-Module Assessment Reteach"
MODULE = ("Module 2:", "Place Value and Problem Solving with Units of Measure")
PLACES = ["Thousands", "Hundreds", "Tens", "Ones"]


def learn_box(c, y, lines):
    return helper_box(c, MARGIN, y, W - 2 * MARGIN, "Let's Learn", lines, LEARN_BG, LEARN_LINE)


def start(c, teks_label):
    y = header(c, TITLE, suffix="")
    teks(c, y, teks_label)
    return y


def compare_circle(c, x, y, r=14):
    c.setLineWidth(1.5)
    c.circle(x + r, y + 5, r)
    c.setLineWidth(1)
    return x + 2 * r


def digit_chart(c, x, y, digits=None, cw=38):
    """One-row Thousands/Hundreds/Tens/Ones chart; digits may be None (blank)."""
    hh, rh = 14, 26
    c.rect(x, y - hh - rh, cw * 4, hh + rh)
    c.line(x, y - hh, x + cw * 4, y - hh)
    for k in range(1, 4):
        c.line(x + k * cw, y, x + k * cw, y - hh - rh)
    for k, p in enumerate(PLACES):
        c.setFont("Sans-Bold", 6.5)
        c.drawCentredString(x + (k + 0.5) * cw, y - 10, p)
        if digits:
            c.setFont("Sans-Bold", 15)
            c.drawCentredString(x + (k + 0.5) * cw, y - hh - 19, digits[k])
    return x + cw * 4


def sentence(c, x, y, text, size=12, blank_w=34, wide_w=70):
    """Draw text where ___ is a short blank and ______ a wide blank. Bold throughout."""
    for i, chunk in enumerate(text.split("|")):
        if chunk == "___":
            x = blank(c, x + 2, y, blank_w) + 2
        elif chunk == "______":
            x = blank(c, x + 2, y, wide_w) + 2
        elif chunk == "O":
            x = compare_circle(c, x + 4, y) + 4
        else:
            x = rich_line(c, x, y, [(chunk, True)], size)
    return x


# ---------------------------------------------------------------- pages

def page_37a(c):
    """Assessment Q1: expanded notation.
    Original: 32,400 / (5×1,000)+(4×10)+(2×1) / (2×10,000)+(6×100)+(2×10)+(9×1) / 19,001"""
    y = start(c, "TEKS 3.2A")
    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", [
        [("Expanded notation", True), (" shows the value of each digit.", False)],
        [("(3 × 1,000)", True), (" means 3 thousands = 3,000.     A ", False), ("0", True),
         (" digit is skipped.", False)],
    ])
    y -= 10
    top = y
    y = learn_box(c, y, [[("", False)]] * 3)
    digit_chart(c, MARGIN + 16, top - 30, "3425")
    rich_line(c, MARGIN + 200, top - 46, [("3,425 =", True)], 12)
    rich_line(c, MARGIN + 200, top - 66, [("(3 × 1,000) + (4 × 100) + (2 × 10) + (5 × 1)", True)], 12)

    y -= 26
    rich_line(c, MARGIN, y, [("1. ", True), ("Fill in the chart. Then finish the number sentence.", False)], 13)
    rows = [
        ("a", "2400", "2,400 = (|___| × 1,000) + (|___| × 100)"),
        ("b", None, "(5 × 1,000) + (4 × 10) + (2 × 1)\n= |______"),
        ("c", None, "(2 × 1,000) + (6 × 100) + (2 × 10) + (9 × 1)\n= |______"),
        ("d", "4021", "4,021 = (|___| × 1,000) + (|___| × 10) + (|___| × 1)"),
    ]
    y -= 16
    rh = 74
    for letter_, digits, text in rows:
        c.rect(MARGIN, y - rh, W - 2 * MARGIN, rh)
        c.setFont("Sans-Bold", 13)
        c.drawString(MARGIN + 8, y - 22, f"{letter_}.")
        digit_chart(c, MARGIN + 30, y - 12, digits)
        lines = text.split("\n")
        for k, ln in enumerate(lines):
            sentence(c, MARGIN + 188, y - (42 if len(lines) == 1 else 30) - 26 * k, ln, size=11.5, blank_w=24)
        if not digits:
            c.setFont("Sans", 9)
            c.setFillColor(GREY)
            c.drawString(MARGIN + 30, y - rh + 8, "Write a 0 where there is no value.")
            c.setFillColor(black)
        y -= rh

    footer(c, *MODULE, "37 (part 1)")


def page_37b(c):
    """Assessment Q2-5: compare with >, <, =.
    Original: 20,219 ? 20,129 / 2,000 + 8 ones + 3 tens ? 2,830 /
              52 thousands 6 hundreds ? 52,600 / 17,499 ? 17 thousands 5 tens"""
    y = start(c, "TEKS 3.2D, 3.2A")
    top = y
    y = learn_box(c, y, [[("", False)]] * 6)
    pv_chart(c, MARGIN + 16, top - 32, 170, PLACES, [3452, 3425], shade=2)
    ty = top - 44
    for parts in (
        [(">", True), (" greater than   ", False), ("<", True), (" less than   ", False), ("=", True), (" equal", False)],
        [("Compare from the ", False), ("left", True), (", one place at a time.", False)],
        [("Thousands: ", False), ("3 = 3", True), ("  same", False)],
        [("Hundreds: ", False), ("4 = 4", True), ("  same", False)],
        [("Tens: ", False), ("5 > 2", True), ("  ← different! Stop here.", False)],
        [("So  ", False), ("3,452 > 3,425", True)],
    ):
        rich_line(c, MARGIN + 210, ty, parts, 11.5)
        ty -= 19

    y -= 22
    rich_line(c, MARGIN, y, [("Write ", False), (">", True), (", ", False), ("<", True), (", or ", False),
                             ("=", True), (" in the circle.", False)], 13)

    # 2: chart provided
    y -= 12
    bh = 106
    c.rect(MARGIN, y - bh, W - 2 * MARGIN, bh)
    rich_line(c, MARGIN + 8, y - 20, [("2.", True)], 13)
    pv_chart(c, MARGIN + 30, y - 8, 170, PLACES, [2219, 2129], shade=None)
    sentence(c, MARGIN + 240, y - 50, "2,219  |O|  2,129", size=16)
    y -= bh

    items = [
        ("3.", ["3 tens = |___|      8 ones = |___", "2,000 + |___| + |___| = |______"],
         "______|  |O|  2,830"),
        ("4.", ["5 thousands = 5,000      6 hundreds = |___", "5,000 + |___| = |______"],
         "______|  |O|  5,600"),
        ("5.", ["1 thousand = |______|      5 tens = |___", "______| + |___| = |______"],
         "1,499  |O|  |______"),
    ]
    titles = ["2,000 + 8 ones + 3 tens   ◯   2,830",
              "5 thousands 6 hundreds   ◯   5,600",
              "1,499   ◯   1 thousand 5 tens"]
    bh = 98
    for (num, steps, final), t in zip(items, titles):
        c.rect(MARGIN, y - bh, W - 2 * MARGIN, bh)
        rich_line(c, MARGIN + 8, y - 20, [(num + "  ", True), (t, True)], 13)
        sy = y - 42
        for k, st in enumerate(steps):
            rich_line(c, MARGIN + 30, sy, [(f"Step {k + 1}:", False)], 10)
            sentence(c, MARGIN + 90, sy, st, size=12)
            sy -= 23
        rich_line(c, MARGIN + 30, sy, [("Step 3:", False)], 10)
        sentence(c, MARGIN + 90, sy, final, size=13)
        y -= bh

    footer(c, *MODULE, "37 (part 2)")


def page_38(c):
    """Assessment Q6-8 (units of weight) and Q9 (55 min - 20 min on a number line)."""
    y = start(c, "TEKS 3.7E, 3.7C, 3.4A")
    y -= 14
    rich_line(c, MARGIN, y, [("Let's Learn: ", True), ("Which unit of weight?", False)], 13)
    y -= 10
    cards = [
        ("OUNCE", "very light", ["Fits in your hand:", "a pencil, a grape,", "a key"]),
        ("POUND", "you can carry it", ["a book, a pineapple,", "a puppy"]),
        ("TON", "very, very heavy", ["a truck, an elephant,", "a school bus"]),
    ]
    gap = 10
    cw = (W - 2 * MARGIN - 2 * gap) / 3
    ch = 92
    for i, (name, feel, examples) in enumerate(cards):
        x = MARGIN + i * (cw + gap)
        c.setFillColor(LEARN_BG)
        c.setStrokeColor(LEARN_LINE)
        c.setLineWidth(1.5)
        c.roundRect(x, y - ch, cw, ch, 8, stroke=1, fill=1)
        c.setLineWidth(1)
        c.setStrokeColor(black)
        c.setFillColor(LEARN_LINE)
        c.setFont("Sans-Bold", 15)
        c.drawCentredString(x + cw / 2, y - 22, name)
        c.setFillColor(black)
        c.setFont("Sans-Bold", 11)
        c.drawCentredString(x + cw / 2, y - 40, feel)
        c.setFont("Sans", 10.5)
        for k, e in enumerate(examples):
            c.drawCentredString(x + cw / 2, y - 58 - 14 * k, e)
    y -= ch + 26

    rich_line(c, MARGIN, y, [("Circle the correct unit.", True),
                             ("  Ask: Can I hold it? Can I carry it? Is it as heavy as a truck?", False)], 12)
    y -= 30
    for num, thing, n, units in (
        ("6.", "A large car", "2", "ounces   /   pounds   /   tons"),
        ("7.", "A slice of bread", "1", "ounce   /   pound   /   ton"),
        ("8.", "A bag of potatoes", "5", "ounces   /   pounds   /   tons"),
    ):
        rich_line(c, MARGIN + 6, y, [(num + "  ", True), (thing, True), (f" weighs about {n}", False)], 13)
        c.setFont("Sans-Bold", 14)
        c.drawString(MARGIN + 300, y, units)
        y -= 32

    y -= 10
    c.line(MARGIN, y + 8, W - MARGIN, y + 8)
    y -= 16
    y = learn_box(c, y, [
        [("How much longer", True), (" → subtract  ( − )", False)],
        [("50 − 30", True), (":  start at 50.  Jump back 3 tens:  40, 30, ", False), ("20", True),
         (".   So 50 − 30 = 20.", False)],
    ])
    y -= 24
    rich_line(c, MARGIN, y, [("9. ", True), ("Ricardo is at the library for ", False), ("45 minutes", True),
                             (". He walks for ", False), ("20 minutes", True), (".", False)], 12)
    y -= 20
    rich_line(c, MARGIN + 22, y, [("How much longer", True), (" is the library than the walk?", False)], 12)

    # number line 0..60 by 5s
    y -= 52
    x0, x1 = MARGIN + 20, W - MARGIN - 20
    c.setLineWidth(1.5)
    c.line(x0 - 10, y, x1 + 10, y)
    c.setLineWidth(1)
    step = (x1 - x0) / 12
    for i in range(13):
        tx = x0 + i * step
        big = i % 2 == 0
        c.line(tx, y - (8 if big else 5), tx, y + (8 if big else 5))
        c.setFont("Sans-Bold" if i * 5 == 45 else "Sans", 11)
        c.drawCentredString(tx, y - 22, str(i * 5))
    c.circle(x0 + 9 * step, y - 18, 13)
    c.setFont("Sans", 9)
    c.setFillColor(GREY)
    c.drawString(x0 + 9 * step + 18, y + 14, "Start here. Jump back 2 tens.")
    c.setFillColor(black)

    y -= 56
    sentence(c, MARGIN + 22, y, "45 − 20 = |______|  minutes", size=16)

    footer(c, *MODULE, "38")


def clock(c, cx, cy, r):
    c.setLineWidth(2)
    c.circle(cx, cy, r)
    c.setLineWidth(1)
    for m in range(60):
        a = math.radians(90 - m * 6)
        inner = r - (9 if m % 5 == 0 else 4)
        c.line(cx + inner * math.cos(a), cy + inner * math.sin(a), cx + r * math.cos(a), cy + r * math.sin(a))
    for h in range(1, 13):
        a = math.radians(90 - h * 30)
        c.setFont("Sans-Bold", 11)
        c.drawCentredString(cx + (r - 20) * math.cos(a), cy + (r - 20) * math.sin(a) - 4, str(h))
        c.setFont("Sans", 8)
        c.setFillColor(LEARN_LINE)
        mins = (h * 5) % 60
        c.drawCentredString(cx + (r + 12) * math.cos(a), cy + (r + 12) * math.sin(a) - 3, str(mins))
        c.setFillColor(black)
    c.circle(cx, cy, 2.5, stroke=0, fill=1)


def page_39(c):
    """Assessment Q10: 23 + 30 + 12 minutes = 1 hour 5 minutes."""
    y = start(c, "TEKS 3.7C, 3.4A")
    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", [
        [("60 minutes = 1 hour", True)],
        [("total", True), (" or ", False), ("in all", True), (" → add  ( + )", False)],
    ])
    y -= 10
    y = learn_box(c, y, [
        [("70 minutes", True), ("  =  60 minutes + 10 minutes  =  ", False), ("1 hour 10 minutes", True)],
    ])

    y -= 28
    rich_line(c, MARGIN, y, [("10. ", True), ("Christa did 3 things one morning.", False)], 13)
    y -= 26
    for t in (("Listened to music:", "20 minutes"), ("Played the guitar:", "30 minutes"),
              ("Practiced singing:", "15 minutes")):
        rich_line(c, MARGIN + 30, y, [("•  " + t[0] + "  ", False), (t[1], True)], 13)
        y -= 22
    clock(c, W - MARGIN - 85, y + 22, 58)

    y -= 14
    rich_line(c, MARGIN, y, [("What is the ", False), ("total", True), (" time?", False)], 13)

    y -= 40
    rich_line(c, MARGIN + 10, y, [("Step 1:", False)], 11)
    sentence(c, MARGIN + 70, y, "20 + 30 + 15 = |______|  minutes", size=15)
    y -= 40
    rich_line(c, MARGIN + 10, y, [("Step 2:", False)], 11)
    sentence(c, MARGIN + 70, y, "______|  minutes  =  60 minutes + |___|  minutes", size=13)
    y -= 40
    rich_line(c, MARGIN + 10, y, [("Step 3:", False)], 11)
    sentence(c, MARGIN + 70, y, "= 1 hour  |___|  minutes", size=15)

    y -= 46
    rich_line(c, MARGIN, y, [("Step 4:  Circle the letter that matches.", True)], 13)
    y -= 30
    for k, choice in enumerate(["1 hour", "55 minutes", "1 hour 15 minutes", "1 hour 5 minutes"]):
        rich_line(c, MARGIN + 30, y, [("ABCD"[k] + "     ", True), (choice, False)], 14)
        y -= 28

    footer(c, *MODULE, "39")


def page_40(c):
    """Assessment Q11 (unit for hot water) and Q12 (198 + 474 = 672; 923 - 672 = 251)."""
    y = start(c, "TEKS 3.7D, 3.4A, 3.5A")
    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", [
        [("Liquids", True), (" (water, milk, juice)  →  ", False), ("cups", True), (", gallons, liters", False)],
        [("Weight", True), ("  →  pounds        ", False), ("Length", True), ("  →  yards        ", False),
         ("Flat space", True), ("  →  square meters", False)],
    ])

    y -= 26
    rich_line(c, MARGIN, y, [("11. ", True), ("Rob measures ", False), ("hot water", True),
                             (" for a recipe. Which unit could be on the container?", False)], 12)
    y -= 20
    rich_line(c, MARGIN + 30, y, [("Hint: water is a ", False), ("liquid", True), (".  Circle the letter.", False)], 11)
    y -= 26
    for k, (choice, cx) in enumerate(zip(["Square meters", "Pounds", "Yards", "Cups"], [0, 165, 285, 390])):
        rich_line(c, MARGIN + 30 + cx, y, [("FGHJ"[k] + "   ", True), (choice, False)], 13)

    y -= 22
    c.line(MARGIN, y, W - MARGIN, y)
    y -= 10
    y = learn_box(c, y, [
        [("Two steps:  ", True), ("1) Add the two alligators.   2) Subtract from the giraffe.", False)],
    ])

    y -= 26
    rich_line(c, MARGIN, y, [("12. ", True), ("Alligator 1 weighs ", False), ("121 pounds", True),
                             (".  Alligator 2 weighs ", False), ("234 pounds", True), (".", False)], 12)
    y -= 20
    rich_line(c, MARGIN + 30, y, [("The giraffe weighs ", False), ("678 pounds", True), (".", False)], 12)
    y -= 20
    rich_line(c, MARGIN + 30, y, [("How much ", False), ("more", True), (" does the giraffe weigh than ", False),
                                  ("both", True), (" alligators?", False)], 12)

    # strip diagram
    y -= 22
    x0, bw = MARGIN + 90, W - 2 * MARGIN - 110
    c.setFont("Sans", 10)
    c.drawRightString(x0 - 8, y - 18, "Giraffe")
    c.drawRightString(x0 - 8, y - 52, "Alligators")
    c.rect(x0, y - 28, bw, 26)
    c.setFont("Sans-Bold", 13)
    c.drawCentredString(x0 + bw / 2, y - 20, "678")
    parts = [(0.18, "121"), (0.34, "234"), (0.48, "?")]
    x = x0
    for frac, label in parts:
        w_ = bw * frac
        if label == "?":
            c.setDash(4, 3)
        c.rect(x, y - 62, w_, 26)
        c.setDash()
        c.drawCentredString(x + w_ / 2, y - 54, label)
        x += w_
    c.setFont("Sans", 9)
    c.setFillColor(GREY)
    c.drawCentredString(x0 + bw * 0.76, y - 74, "how much more")
    c.setFillColor(black)

    y -= 108
    rich_line(c, MARGIN + 10, y, [("Step 1:", False)], 11)
    rich_line(c, MARGIN + 70, y, [("Add the alligators.", False)], 11)
    sentence(c, MARGIN + 220, y, "121 + 234 = |______", size=15)
    y -= 44
    rich_line(c, MARGIN + 10, y, [("Step 2:", False)], 11)
    rich_line(c, MARGIN + 70, y, [("Subtract.", False)], 11)
    sentence(c, MARGIN + 220, y, "678 − |______| = |______", size=15)
    y -= 44
    rich_line(c, MARGIN + 10, y, [("Answer:", True)], 12)
    rich_line(c, MARGIN + 70, y, [("The giraffe weighs", False)], 12)
    sentence(c, MARGIN + 190, y, "______|  pounds more.", size=13)

    footer(c, *MODULE, "40")


PAGES = [page_37a, page_37b, page_38, page_39, page_40]

if __name__ == "__main__":
    main("G3_M2_MidModule_Reteach.pdf", PAGES, "Grade 3 Module 2 – Mid-Module Assessment Reteach")
