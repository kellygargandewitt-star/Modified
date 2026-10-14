"""Modified pages for Bluebonnet Learning Grade 3 Module 2, Lessons 15-19 (book pages 103-131).

Problems keep the book's numbers, letters, and order so students can follow
along with the class lesson. Supports: friendlier numbers, pre-labeled number
lines, set-up number sentences, bold key words, and a Word Helper on each page.

Run: python3 lessons_15_19.py  ->  writes G3_M2_Lessons15-19_Modified.pdf
"""
from reportlab.lib.colors import HexColor, black
from reportlab.pdfbase import pdfmetrics

import build_module2 as bm
from build_module2 import (
    LIGHT, MARGIN, W, blank, footer, header, helper_box, main, rich_line, teks,
)

GREY = HexColor("#666666")
WATER = HexColor("#CFE6FA")

L15 = (15, "Round two-digit measurements to the nearest ten on the vertical number line.")
L16 = (16, "Round two- and three-digit numbers to the nearest ten on the vertical number line.")
L17 = (17, "Round to the nearest hundred on the vertical number line.")
L18 = (18, "Round four- and five-digit numbers using the vertical number line.")
L19 = (19, "Use compatible numbers to estimate solutions to addition and subtraction problems.")

HELP_TEN = bm.ROUND_TEN_HELP
HELP_HUNDRED = [
    [("Nearest hundred", True), (" → look at the ", False), ("tens", True), (" digit.", False)],
    [("0, 1, 2, 3, 4", True), (" → round ", False), ("down", True), ("        ", False),
     ("5, 6, 7, 8, 9", True), (" → round ", False), ("up", True)],
]
HELP_PLACE = [
    [("Nearest ten", True), (" → look at the ", False), ("ones", True), (" digit.    ", False),
     ("Nearest hundred", True), (" → the ", False), ("tens", True), (" digit.", False)],
    [("0, 1, 2, 3, 4", True), (" → round ", False), ("down", True), ("        ", False),
     ("5, 6, 7, 8, 9", True), (" → round ", False), ("up", True)],
]
HELP_ESTIMATE = [
    [("Compatible numbers", True), (" = friendly numbers ", False), ("close to", True),
     (" the real numbers. Easy to add!", False)],
    [("Example:  ", False), ("48 + 31", True), ("  →  ", False), ("50 + 30 = 80", True),
     ("        ≈ means ", False), ("about", True)],
]


def grey(c, x, y, text, size=9):
    c.setFont("Sans", size)
    c.setFillColor(GREY)
    c.drawString(x, y, text)
    c.setFillColor(black)


def vline(c, x, top, bottom, low, step, dot=None, size=11):
    """Vertical number line labeled low, halfway, high."""
    c.setLineWidth(2)
    c.line(x, bottom - 12, x, top + 12)
    for ye, d in ((top + 12, 1), (bottom - 12, -1)):
        c.line(x, ye, x - 5, ye - 7 * d)
        c.line(x, ye, x + 5, ye - 7 * d)
    mid = (top + bottom) / 2
    for yy, n in ((bottom, low), (mid, low + step // 2), (top, low + step)):
        c.line(x - 8, yy, x + 8, yy)
        c.setFont("Sans", size)
        c.drawString(x + 12, yy - 4, f"{n:,}")
    c.setFont("Sans", 7.5)
    c.setFillColor(GREY)
    c.drawRightString(x - 11, mid - 3, "halfway")
    c.setFillColor(black)
    if dot is not None:
        dy = bottom + (dot - low) / step * (top - bottom)
        c.circle(x, dy, 3.5, stroke=0, fill=1)
        c.setFont("Sans-Bold", size)
        ly = dy - 4 if abs(dy - mid) > 14 else dy - 18
        c.drawRightString(x - 11, ly, f"{dot:,}")
    c.setLineWidth(1)


def round_cell(c, x0, y0, cw, ch, label, n, step, example=False, place=None):
    c.rect(x0, y0 - ch, cw, ch)
    low = n // step * step
    ty = y0 - 22
    if place:
        rich_line(c, x0 + 10, ty, [(f"{label}.  ", False), (place, True)], 11.5)
        ty -= 22
        x = rich_line(c, x0 + 28, ty, [(f"{n:,} ≈ ", True)], 14)
    else:
        x = rich_line(c, x0 + 10, ty, [(f"{label}.  ", False), (f"{n:,} ≈ ", True)], 15)
    blank(c, x + 2, ty, 56)
    rich_line(c, x0 + 10, ty - 28, [("Between ", False), (f"{low:,}", True), (" and ", False),
                                    (f"{low + step:,}", True)], 10.5)
    rich_line(c, x0 + 10, ty - 50, [("Closer to:", False)], 10.5)
    blank(c, x0 + 72, ty - 50, 56)
    if example:
        grey(c, x0 + 10, ty - 72, "(Example: the dot is shown.)")
    vline(c, x0 + cw - 62, y0 - 26, y0 - ch + 22, low, step, dot=n if example else None, size=10)


def round_grid(c, top, items, bottom=80, step=10):
    """items: (label, n, step, example, place) in a 2-column grid."""
    rows = (len(items) + 1) // 2
    cw, ch = (W - 2 * MARGIN) / 2, (top - bottom) / rows
    for i, (label, n, st, ex, place) in enumerate(items):
        round_cell(c, MARGIN + (i % 2) * cw, top - (i // 2) * ch, cw, ch, label, n, st, ex, place)


def start(c, title, teks_label, helper):
    y = header(c, title)
    teks(c, y, teks_label)
    return helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", helper)


def no_name_start(c, title, teks_label, helper):
    """Continuation pages (no Name/Date line in the book)."""
    return start(c, title, teks_label, helper)


def problem(c, y, num, parts, size=12.5):
    return rich_line(c, MARGIN, y, [(f"{num} ", True)] + parts, size)


# ---------------------------------------------------------------- Lesson 15

def measure_table(c, y, unit, first_col, example, rows, heads):
    cols = [150, 92, 172, W - 2 * MARGIN - 414]
    hh, rh = 40, 32
    c.setFillColor(LIGHT)
    c.rect(MARGIN, y - hh, W - 2 * MARGIN, hh, stroke=0, fill=1)
    c.setFillColor(black)
    x = MARGIN
    for w_, h_ in zip(cols, [first_col] + heads):
        lines = h_.split("\n")
        for k, ln in enumerate(lines):
            c.setFont("Sans-Bold", 9.5)
            c.drawCentredString(x + w_ / 2, y - 16 - 12 * k + (6 if len(lines) == 1 else 0), ln)
        x += w_
    n = len(rows) + 1
    bottom = y - hh - rh * n
    c.rect(MARGIN, bottom, W - 2 * MARGIN, y - bottom)
    x = MARGIN
    for w_ in cols[:-1]:
        x += w_
        c.line(x, y, x, bottom)
    for r, row in enumerate([example] + rows):
        ry = y - hh - r * rh
        c.line(MARGIN, ry, W - MARGIN, ry)
        cy = ry - 21
        is_ex = r == 0
        c.setFont("Sans", 10.5)
        c.drawCentredString(MARGIN + cols[0] / 2, cy, ("Example: " if is_ex else "") + row[0])
        bx = MARGIN + cols[0] + cols[1]
        if is_ex:
            c.setFont("Sans", 11)
            c.drawCentredString(MARGIN + cols[0] + cols[1] / 2, cy, row[1])
            c.drawCentredString(bx + cols[2] / 2, cy, f"{row[2]}  and  {row[3]}  {unit}")
            c.drawCentredString(bx + cols[2] + cols[3] / 2, cy, row[4])
        else:
            blank(c, bx + 10, cy, 52)
            c.setFont("Sans", 10.5)
            c.drawString(bx + 68, cy, "and")
            blank(c, bx + 92, cy, 52)
            c.drawString(bx + 148, cy, unit)
    return bottom


def page_103(c):
    """Lesson 15 Problem Set: measure objects (cm) and bags of rice (oz), round to nearest ten."""
    y = start(c, "Lesson 15 Problem Set", "TEKS 3.4B", [
        [("The two tens: ", True), ("the ten ", False), ("before", True), (" and the ten ", False),
         ("after", True), (" your number.  23 → ", False), ("20", True), (" and ", False), ("30", True)],
        HELP_TEN[1],
    ])
    y -= 24
    problem(c, y, "1.", [("With a partner, use a ", False), ("ruler", True), (". Measure. Then round to the nearest ", False),
                         ("10 cm", True), (".", False)])
    y = measure_table(c, y - 10, "cm", "Object", ("My shoe", "23 cm", "20", "30", "20 cm"),
                      [("Long side of a desk",), ("A new pencil",), ("Short side of paper",), ("Long side of paper",)],
                      ["Measurement\n(cm)", "Between which\ntwo tens?", "Round to\nnearest 10 cm"])
    y -= 30
    problem(c, y, "2.", [("With a partner, use a ", False), ("scale", True), (". Weigh each bag. Round to the nearest ", False),
                         ("10 oz", True), (".", False)])
    measure_table(c, y - 10, "oz", "Bag", ("Bag A", "8 oz", "0", "10", "10 oz"),
                  [("Bag B",), ("Bag C",), ("Bag D",), ("Bag E",)],
                  ["Measurement\n(oz)", "Between which\ntwo tens?", "Round to\nnearest 10 oz"])
    footer(c, *L15, 103)


def page_104(c):
    """Lesson 15 Problem Set (continued): beaker (mL) and clock times."""
    y = start(c, "Lesson 15 Problem Set", "TEKS 3.4B", [
        [("mL", True), (" = milliliters (liquid)        For time, the two tens are like ", False),
         ("10:00", True), (" and ", False), ("10:10", True)],
        HELP_TEN[1],
    ])
    y -= 24
    problem(c, y, "3.", [("With a partner, use a ", False), ("beaker", True), (". Measure. Round to the nearest ", False),
                         ("10 mL", True), (".", False)])
    y = measure_table(c, y - 10, "mL", "Container", ("Container A", "33 mL", "30", "40", "30 mL"),
                      [("Container B",), ("Container C",), ("Container D",), ("Container E",)],
                      ["Measurement\n(mL)", "Between which\ntwo tens?", "Round to\nnearest 10 mL"])
    y -= 30
    problem(c, y, "4.", [("Use a ", False), ("clock", True), (". Write the time. Round to the nearest ", False),
                         ("10 minutes", True), (".", False)])
    measure_table(c, y - 10, "", "Activity", ("Started math", "10:03", "10:00", "10:10", "10:00"),
                  [("I started the Problem Set",), ("I finished Station 1",), ("I finished Station 2",),
                   ("I finished Station 3",)],
                  ["Actual time", "Between which\ntwo tens?", "Round to nearest\n10 minutes"])
    footer(c, *L15, 104)


def beaker(c, x, y, h, level, top_val=70):
    """Beaker with 10 mL marks. (x, y) is the bottom-left corner."""
    w = 70
    c.setFillColor(WATER)
    c.rect(x, y, w, h * level / top_val, stroke=0, fill=1)
    c.setFillColor(black)
    c.setLineWidth(2)
    c.line(x, y, x, y + h + 12)
    c.line(x + w, y, x + w, y + h + 12)
    c.line(x, y, x + w, y)
    c.setLineWidth(1)
    for v in range(10, top_val + 1, 10):
        yy = y + h * v / top_val
        c.line(x + w - 16, yy, x + w, yy)
        c.setFont("Sans", 9)
        c.drawString(x + w + 4, yy - 3, f"{v} mL")
    for v in range(5, top_val, 10):
        yy = y + h * v / top_val
        c.line(x + w - 8, yy, x + w, yy)


def page_105(c):
    """Lesson 15 Exit Ticket. Original: beaker shows 46 mL."""
    n = 43
    y = start(c, "Lesson 15 Exit Ticket", "TEKS 3.4B", HELP_TEN)
    y -= 24
    rich_line(c, MARGIN, y, [("The beaker shows the water.", False)], 13)
    bx, by, bh = MARGIN + 150, y - 190, 160
    beaker(c, bx, by, bh, n)
    ly = by + bh * n / 70
    c.setFillColor(black)
    c.rect(bx - 90, ly - 10, 54, 20)
    c.setFont("Sans-Bold", 11)
    c.drawCentredString(bx - 63, ly - 4, f"{n} mL")
    c.line(bx - 36, ly, bx - 2, ly)
    vline(c, W - MARGIN - 110, y - 30, y - 170, 40, 10)

    y -= 230
    x = rich_line(c, MARGIN, y, [("a. ", True), ("The water in the beaker is ", False)], 13)
    blank(c, x + 2, y, 60)
    c.setFont("Sans", 13)
    c.drawString(x + 68, y, "mL.")
    y -= 36
    rich_line(c, MARGIN, y, [("b. ", True), ("Put a dot on ", False), (f"{n}", True),
                             (" on the number line. Round to the nearest ", False), ("10 mL", True), (".", False)], 13)
    y -= 36
    x = rich_line(c, MARGIN, y, [("c. ", True), ("There are about ", False)], 13)
    blank(c, x + 2, y, 60)
    c.setFont("Sans", 13)
    c.drawString(x + 68, y, "mL of water in the beaker.")
    y -= 40
    rich_line(c, MARGIN, y, [("d. ", True), ("Finish the sentence. Circle the words.", False)], 13)
    y -= 30
    rich_line(c, MARGIN + 24, y, [("The halfway point is ", False), ("45", True), (".  ", False), (f"{n}", True),
                                  (" is ", False), ("below  /  above", True), (" halfway,", False)], 13)
    y -= 26
    x = rich_line(c, MARGIN + 24, y, [("so I round ", False), ("down  /  up", True), ("  to ", False)], 13)
    blank(c, x + 2, y, 60)
    c.setFont("Sans", 13)
    c.drawString(x + 68, y, "mL.")
    footer(c, *L15, 105)


# ---------------------------------------------------------------- Lesson 16

def read_draw_write(c, y):
    c.setFont("Sans-Bold", 12)
    for k, word in enumerate(["Read", "Draw", "Write"]):
        c.drawCentredString(MARGIN + 90 + k * 170, y, word)


def strip(c, x, y, w, parts, total):
    """Strip diagram: parts [(value_label, fraction)] with a bracket for the total."""
    xx = x
    c.setFont("Sans-Bold", 13)
    for label, frac in parts:
        pw = w * frac
        c.rect(xx, y - 30, pw, 30)
        c.drawCentredString(xx + pw / 2, y - 20, label)
        xx += pw
    c.line(x, y - 40, x, y - 48)
    c.line(x + w, y - 40, x + w, y - 48)
    c.line(x, y - 48, x + w, y - 48)
    c.drawCentredString(x + w / 2, y - 66, total)


def page_107(c):
    """Lesson 16 Application Problem. Original: 9 + 11 + 8 minutes."""
    y = start(c, "Lesson 16 Application Problem", "TEKS 3.4A, 3.5A", [
        [("How many in all / how long", True), (" → add  ( + )", False)],
        [("Make a ten first:  ", False), ("4 + 6 = 10", True)],
    ])
    y -= 26
    rich_line(c, MARGIN, y, [("3 groups dance at the ballet recital.", False)], 13)
    y -= 26
    for t in (("Group 1 dances", "4 minutes"), ("Group 2 dances", "10 minutes"), ("Group 3 dances", "6 minutes")):
        rich_line(c, MARGIN + 30, y, [("•  " + t[0] + " ", False), (t[1], True), (".", False)], 13)
        y -= 22
    y -= 6
    rich_line(c, MARGIN, y, [("How many minutes long", True), (" is the recital?", False)], 13)

    y -= 40
    rich_line(c, MARGIN, y, [("Draw:", True)], 12)
    strip(c, MARGIN + 60, y + 10, W - 2 * MARGIN - 80, [("4", 0.24), ("10", 0.46), ("6", 0.30)], "?  minutes")

    y -= 110
    rich_line(c, MARGIN, y, [("Write:", True)], 12)
    x = rich_line(c, MARGIN + 60, y, [("4 + 10 + 6 = ", True)], 18)
    blank(c, x + 4, y, 70)
    y -= 40
    rich_line(c, MARGIN + 60, y, [("Make a ten:  ", False), ("4 + 6 = 10", True), (",  then  10 + 10 = ", False)], 13)
    blank(c, MARGIN + 340, y, 60)
    y -= 48
    x = rich_line(c, MARGIN, y, [("Answer:", True), ("  The recital is ", False)], 13)
    blank(c, x + 2, y, 60)
    c.setFont("Sans", 13)
    c.drawString(x + 68, y, "minutes long.")

    read_draw_write(c, 100)
    footer(c, *L16, 107)


# ---------------------------------------------------------------- Lesson 17

def page_115(c):
    """Lesson 17 Problem Set. Original: 143, 286, 320, 1,320, 1,572, 1,250 to nearest hundred."""
    y = start(c, "Lesson 17 Problem Set", "TEKS 3.4B", HELP_HUNDRED)
    y -= 22
    problem(c, y, "1.", [("Round to the nearest ", False), ("hundred", True), (". Put a dot on the number line.", False)])
    round_grid(c, y - 12, [("a", 143, 100, True, None), ("b", 286, 100, False, None),
                           ("c", 320, 100, False, None), ("d", 470, 100, False, None),
                           ("e", 615, 100, False, None), ("f", 250, 100, False, None)])
    footer(c, *L17, 115)


def page_116(c):
    """Lesson 17 Problem Set (continued).
    Original 2: 480, 525, 750, $1,297, 1,842.  3: which round to 600.  4: 1,865 -> 1,900 / 19 hundreds."""
    y = start(c, "Lesson 17 Problem Set", "TEKS 3.4B", HELP_HUNDRED)
    y -= 22
    problem(c, y, "2.", [("Round each number to the nearest ", False), ("hundred", True), (".", False)])
    rows = [
        ("a.", "Shauna has ", "480", " stickers."),
        ("b.", "A book has ", "520", " pages."),
        ("c.", "A container holds ", "750", " mL of water."),
        ("d.", "Glen spends ", "$310", " on a computer."),
        ("e.", "The drive is ", "860", " kilometers."),
    ]
    y -= 8
    rh = 28
    for k, (lbl, a, num, b) in enumerate(rows):
        ry = y - (k + 1) * rh
        rich_line(c, MARGIN + 14, ry, [(lbl + "  ", True), (a, False), (num, True), (b, False)], 11.5)
        v = int(num.strip("$"))
        low = v // 100 * 100
        pre = "$" if num.startswith("$") else ""
        rich_line(c, MARGIN + 300, ry, [(f"{pre}{low} or {pre}{low + 100}?", False)], 10.5)
        x = rich_line(c, MARGIN + 410, ry, [(f"{num} ≈ ", True)], 11.5)
        blank(c, x + 2, ry, 40)
    y -= rh * 5 + 34

    problem(c, y, "3.", [("Circle the numbers that round to ", False), ("600", True), (".", False)])
    y -= 46
    x0, x1 = MARGIN + 30, W - MARGIN - 30
    c.setFillColor(HexColor("#FFF2B3"))
    c.rect(x0 + (x1 - x0) / 4, y - 10, (x1 - x0) / 2, 20, stroke=0, fill=1)
    c.setFillColor(black)
    c.setLineWidth(1.5)
    c.line(x0 - 8, y, x1 + 8, y)
    c.setLineWidth(1)
    for k, v in enumerate([500, 550, 600, 650, 700]):
        tx = x0 + k * (x1 - x0) / 4
        c.line(tx, y - 8, tx, y + 8)
        c.setFont("Sans-Bold" if v == 600 else "Sans", 11)
        c.drawCentredString(tx, y - 24, str(v))
    grey(c, x0 + (x1 - x0) / 4 + 4, y + 14, "Numbers in the yellow part round to 600.")
    y -= 50
    c.setFont("Sans-Bold", 16)
    for k, v in enumerate([527, 550, 639, 681, 713, 603]):
        c.drawCentredString(MARGIN + 45 + k * 86, y, str(v))

    y -= 42
    problem(c, y, "4.", [("Round ", False), ("865", True), (" to the nearest hundred.", False)])
    y -= 22
    rich_line(c, MARGIN + 24, y, [("Christian says ", False), ("nine hundred", True), (".   Alexis says ", False),
                                  ("9 hundreds", True), (".", False)], 12)
    y -= 28
    sx = rich_line(c, MARGIN + 24, y, [("865 ≈ ", True)], 13)
    blank(c, sx + 2, y, 50)
    sx = rich_line(c, MARGIN + 180, y, [("nine hundred = ", False)], 12)
    blank(c, sx + 2, y, 50)
    sx = rich_line(c, MARGIN + 350, y, [("9 hundreds = ", False)], 12)
    blank(c, sx + 2, y, 50)
    y -= 28
    rich_line(c, MARGIN + 24, y, [("Who is correct?  Circle:   ", False), ("Christian    Alexis    Both", True)], 12)
    footer(c, *L17, 116)


def page_117(c):
    """Lesson 17 Exit Ticket. Original: 137, 1,761; 685 people."""
    y = start(c, "Lesson 17 Exit Ticket", "TEKS 3.4B", HELP_HUNDRED)
    y -= 22
    problem(c, y, "1.", [("Round to the nearest ", False), ("hundred", True), (". Put a dot on the number line.", False)])
    round_grid(c, y - 12, [("a", 137, 100, False, None), ("b", 761, 100, False, None)], bottom=y - 182)
    y -= 222
    problem(c, y, "2.", [("There are ", False), ("685", True), (" people at a concert. Round to the nearest ", False),
                         ("hundred", True), (".", False)])
    vline(c, W - MARGIN - 90, y - 34, y - 214, 600, 100)
    ty = y - 50
    rich_line(c, MARGIN + 24, ty, [("Put a dot on ", False), ("685", True), (" on the number line.", False)], 13)
    ty -= 40
    rich_line(c, MARGIN + 24, ty, [("Between ", False), ("600", True), (" and ", False), ("700", True)], 13)
    ty -= 40
    x = rich_line(c, MARGIN + 24, ty, [("The tens digit is ", False)], 13)
    blank(c, x + 2, ty, 36)
    rich_line(c, x + 46, ty, [(", so I round ", False), ("down  /  up", True), (".", False)], 13)
    ty -= 40
    x = rich_line(c, MARGIN + 24, ty, [("685 ≈ ", True)], 16)
    blank(c, x + 2, ty, 70)
    c.setFont("Sans", 13)
    c.drawString(x + 78, ty, "people")
    footer(c, *L17, 117)


# ---------------------------------------------------------------- Lesson 18

def page_121(c):
    """Lesson 18 Application Problem. Original: Rebecca rounds 2,145 to the nearest hundred and says 2,000."""
    y = start(c, "Lesson 18 Application Problem", "TEKS 3.4B", HELP_HUNDRED)
    y -= 26
    rich_line(c, MARGIN, y, [("Rebecca rounds ", False), ("345", True), (" to the nearest ", False), ("hundred", True),
                             (". She says it is ", False), ("400", True), (".", False)], 13)
    y -= 22
    rich_line(c, MARGIN, y, [("Do you agree?", True), (" Use the number line and words.", False)], 13)
    vline(c, W - MARGIN - 90, y - 40, y - 240, 300, 100)
    ty = y - 56
    for parts, bl in (
        ([("Put a dot on ", False), ("345", True), (" on the number line.", False)], False),
        ([("345 is between ", False), ("300", True), (" and ", False), ("400", True), (".", False)], False),
        ([("The tens digit is", False)], True),
        ([("345 ≈ ", True)], True),
    ):
        x = rich_line(c, MARGIN + 24, ty, parts, 13)
        if bl:
            blank(c, x + 6, ty, 60)
        ty -= 40
    rich_line(c, MARGIN + 24, ty, [("Circle:   I ", False), ("agree  /  do not agree", True), (" with Rebecca.", False)], 13)
    ty -= 40
    x = rich_line(c, MARGIN + 24, ty, [("Because 345 rounds to", False)], 13)
    blank(c, x + 6, ty, 60)
    c.drawString(x + 72, ty, ", not 400.")
    read_draw_write(c, 100)
    footer(c, *L18, 121)


def page_123(c):
    """Lesson 18 Problem Set. Original: 2,143 (H), 2,886 (T), 959 (H), 16,927 (T), 28,572 (T), 98,245 (H)."""
    y = start(c, "Lesson 18 Problem Set", "TEKS 3.4B", HELP_PLACE)
    y -= 22
    problem(c, y, "1.", [("Round to the place in ", False), ("bold", True), (". Put a dot on the number line.", False)])
    round_grid(c, y - 12, [("a", 2143, 100, True, "Nearest hundred"), ("b", 2886, 10, False, "Nearest ten"),
                           ("c", 959, 100, False, "Nearest hundred"), ("d", 1627, 10, False, "Nearest ten"),
                           ("e", 3572, 10, False, "Nearest ten"), ("f", 4245, 100, False, "Nearest hundred")])
    footer(c, *L18, 123)


def page_124(c):
    """Lesson 18 Problem Set (continued).
    Original 2: which round to 7,500.  3: 1,759 and 1,882 miles.  4: 3,452.  5: 78,205."""
    y = start(c, "Lesson 18 Problem Set", "TEKS 3.4B", HELP_PLACE)
    y -= 22
    problem(c, y, "2.", [("Circle the numbers that round to ", False), ("7,500", True), (" (nearest hundred).", False)])
    y -= 40
    x0, x1 = MARGIN + 30, W - MARGIN - 30
    c.setFillColor(HexColor("#FFF2B3"))
    c.rect(x0 + (x1 - x0) / 4, y - 10, (x1 - x0) / 2, 20, stroke=0, fill=1)
    c.setFillColor(black)
    c.setLineWidth(1.5)
    c.line(x0 - 8, y, x1 + 8, y)
    c.setLineWidth(1)
    for k, v in enumerate([7400, 7450, 7500, 7550, 7600]):
        tx = x0 + k * (x1 - x0) / 4
        c.line(tx, y - 8, tx, y + 8)
        c.setFont("Sans-Bold" if v == 7500 else "Sans", 11)
        c.drawCentredString(tx, y - 24, f"{v:,}")
    grey(c, x0 + (x1 - x0) / 4 + 4, y + 14, "Numbers in the yellow part round to 7,500.")
    y -= 48
    c.setFont("Sans-Bold", 15)
    for k, v in enumerate([7499, 7599, 7639, 7530, 7472, 7549]):
        c.drawCentredString(MARGIN + 45 + k * 86, y, f"{v:,}")

    y -= 38
    problem(c, y, "3.", [("Jayden's family drove ", False), ("759", True), (" miles. Jordan's family drove ", False),
                         ("882", True), (" miles.", False)])
    y -= 22
    rich_line(c, MARGIN + 24, y, [("Round to the nearest hundred. Who drove ", False), ("about 800", True), (" miles?", False)], 12)
    y -= 28
    x = rich_line(c, MARGIN + 24, y, [("Jayden:  759 ≈ ", True)], 13)
    blank(c, x + 2, y, 50)
    x = rich_line(c, MARGIN + 220, y, [("Jordan:  882 ≈ ", True)], 13)
    blank(c, x + 2, y, 50)
    rich_line(c, MARGIN + 400, y, [("Circle:  ", False), ("Jayden / Jordan", True)], 11)

    y -= 40
    problem(c, y, "4.", [("Round ", False), ("452", True), (" two ways.", False)])
    vline(c, MARGIN + 250, y - 26, y - 106, 400, 100, size=10)
    vline(c, MARGIN + 420, y - 26, y - 106, 450, 10, size=10)
    rich_line(c, MARGIN + 24, y - 50, [("Nearest hundred:", False)], 12)
    blank(c, MARGIN + 24, y - 72, 70)
    rich_line(c, MARGIN + 24, y - 100, [("Nearest ten:", False)], 12)
    blank(c, MARGIN + 24, y - 122, 70)
    grey(c, MARGIN + 230, y - 130, "hundred")
    grey(c, MARGIN + 405, y - 130, "ten")

    y -= 158
    problem(c, y, "5.", [("Round ", False), ("8,205", True), (" to the nearest ", False), ("hundred", True), (".", False)])
    vline(c, MARGIN + 420, y - 18, y - 90, 8200, 100, size=10)
    x = rich_line(c, MARGIN + 24, y - 50, [("8,205 ≈ ", True)], 15)
    blank(c, x + 2, y - 50, 70)
    footer(c, *L18, 124)


def page_125(c):
    """Lesson 18 Exit Ticket. Original: 2,137 (ten); 17,560 (hundred); 9,583 hot dogs (ten and hundred)."""
    y = start(c, "Lesson 18 Exit Ticket", "TEKS 3.4B", HELP_PLACE)
    y -= 22
    problem(c, y, "", [("Round. Put a dot on the number line.", False)])
    round_grid(c, y - 12, [("1", 137, 10, False, "Nearest ten"), ("2", 560, 100, False, "Nearest hundred")],
               bottom=y - 182)
    y -= 222
    problem(c, y, "3.", [("A stadium cooked ", False), ("583", True), (" hot dogs. Round to the nearest ", False),
                         ("ten", True), (" and ", False), ("hundred", True), (".", False)])
    vline(c, MARGIN + 270, y - 40, y - 180, 580, 10)
    vline(c, MARGIN + 430, y - 40, y - 180, 500, 100)
    grey(c, MARGIN + 255, y - 206, "nearest ten")
    grey(c, MARGIN + 405, y - 206, "nearest hundred")
    x = rich_line(c, MARGIN + 10, y - 70, [("Ten:  583 ≈ ", True)], 13)
    blank(c, x + 2, y - 70, 50)
    x = rich_line(c, MARGIN + 10, y - 140, [("Hundred:  583 ≈ ", True)], 13)
    blank(c, x + 2, y - 140, 50)
    footer(c, *L18, 125)


def cw_half():
    return (W - 2 * MARGIN) / 2


# ---------------------------------------------------------------- Lesson 19

def estimate_frame(c, x, y, terms, op="+"):
    """≈ ___ + ___ (+ ___) = ___"""
    x = rich_line(c, x, y, [("≈ ", True)], 13)
    for k in range(terms):
        x = blank(c, x + 2, y, 36) + 4
        if k < terms - 1:
            x = rich_line(c, x, y, [(op + " ", True)], 13)
    x = rich_line(c, x, y, [("= ", True)], 13)
    blank(c, x + 2, y, 44)


def page_127(c):
    """Lesson 19 Application Problem. Original: 52 + 91 + 56 pounds, estimate."""
    y = start(c, "Lesson 19 Application Problem", "TEKS 3.4B", HELP_ESTIMATE)
    y -= 26
    rich_line(c, MARGIN, y, [("Matt turns in metal at the scrap yard.", False)], 13)
    y -= 26
    for d, n in (("Monday", 52), ("Wednesday", 31), ("Friday", 48)):
        rich_line(c, MARGIN + 30, y, [(f"•  {d}:  ", False), (f"{n} pounds", True)], 13)
        y -= 22
    y -= 6
    rich_line(c, MARGIN, y, [("About", True), (" how many pounds in all? ", False), ("Estimate", True),
                             (". Do not solve.", False)], 13)
    y -= 50
    for n in (52, 31, 48):
        x = rich_line(c, MARGIN + 30, y, [(f"{n}", True), (" is close to ", False)], 14)
        blank(c, x + 4, y, 50)
        y -= 36
    y -= 10
    rich_line(c, MARGIN, y, [("Write:", True)], 12)
    estimate_frame(c, MARGIN + 60, y, 3)
    y -= 44
    x = rich_line(c, MARGIN, y, [("Answer:", True), ("  Matt turned in about ", False)], 13)
    blank(c, x + 2, y, 60)
    c.setFont("Sans", 13)
    c.drawString(x + 68, y, "pounds.")
    read_draw_write(c, 100)
    footer(c, *L19, 127)


def column_add(c, x, y, nums):
    """Vertical addition with place value headers and an answer row."""
    cw = 30
    for k, p in enumerate(["H", "T", "O"]):
        c.setFont("Sans-Bold", 10)
        c.drawCentredString(x + 20 + k * cw + cw / 2, y, p)
    for r, n in enumerate(nums):
        ry = y - 22 - r * 22
        if r == len(nums) - 1:
            c.setFont("Sans-Bold", 14)
            c.drawCentredString(x + 8, ry, "+")
        for k, d in enumerate(str(n).rjust(3)):
            c.setFont("Sans", 15)
            c.drawCentredString(x + 20 + k * cw + cw / 2, ry, d)
    ly = y - 22 - len(nums) * 22 + 12
    c.setLineWidth(1.5)
    c.line(x, ly, x + 20 + 3 * cw, ly)
    c.setLineWidth(1)
    for k in range(3):
        c.rect(x + 22 + k * cw, ly - 28, cw - 4, 24)


def page_129(c):
    """Lesson 19 Problem Set. Original: $358 + $225 + $178."""
    y = start(c, "Lesson 19 Problem Set", "TEKS 3.4B, 3.4A", HELP_ESTIMATE)
    y -= 26
    problem(c, y, "1.", [("Sam buys a chair for ", False), ("$320", True), (", a table for ", False), ("$180", True),
                         (", and a lamp for ", False), ("$110", True), (".", False)])
    y -= 20
    rich_line(c, MARGIN + 24, y, [("About", True), (" how much will all 3 cost?", False)], 12.5)

    y -= 36
    rich_line(c, MARGIN + 10, y, [("a. ", True), ("Round to the nearest ", False), ("$100", True), (".", False)], 12.5)
    y -= 26
    for k, n in enumerate((320, 180, 110)):
        x = rich_line(c, MARGIN + 34 + k * 150, y, [(f"${n} ≈ ", True)], 12.5)
        blank(c, x + 2, y, 46)
    y -= 30
    x = rich_line(c, MARGIN + 34, y, [("Total: ", False)], 12.5)
    estimate_frame(c, x + 4, y, 3)

    y -= 40
    rich_line(c, MARGIN + 10, y, [("b. ", True), ("Use compatible numbers. ", False),
                                  ("Hint: 320 + 180 = 500", True), (" (2 + 8 = 10)", False)], 12.5)
    y -= 30
    x = rich_line(c, MARGIN + 34, y, [("500 + ", True)], 13)
    x = blank(c, x + 2, y, 46)
    x = rich_line(c, x + 6, y, [("≈ ", True)], 13)
    blank(c, x + 2, y, 50)

    y -= 40
    rich_line(c, MARGIN + 10, y, [("c. ", True), ("Find the ", False), ("exact", True), (" answer.", False)], 12.5)
    column_add(c, MARGIN + 60, y - 20, [320, 180, 110])
    x = rich_line(c, MARGIN + 260, y - 70, [("Exact total: $", True)], 13)
    blank(c, x + 2, y - 70, 60)

    y -= 150
    rich_line(c, MARGIN + 10, y, [("d. ", True), ("Which way was closest to the exact answer? Circle:", False)], 12.5)
    y -= 26
    rich_line(c, MARGIN + 34, y, [("rounding (a)      compatible numbers (b)", True)], 12.5)
    footer(c, *L19, 129)


def page_130(c):
    """Lesson 19 Problem Set (continued). Original: 239+364, 98+47, 76+39+23, 576-249, 804-351,
    28+38+72, 368+121+226, 298+142."""
    y = start(c, "Lesson 19 Problem Set", "TEKS 3.4B", HELP_ESTIMATE)
    y -= 22
    problem(c, y, "2.", [("Estimate with compatible numbers. Change each number to a ", False), ("friendly ten", True),
                         (".", False)])
    items = [("a", "39 + 21", 2, "+"), ("b", "98 + 47", 2, "+"), ("c", "76 + 39 + 23", 3, "+"),
             ("d", "52 − 19", 2, "−"), ("e", "81 − 39", 2, "−"), ("f", "28 + 38 + 72", 3, "+"),
             ("g", "61 + 21 + 19", 3, "+"), ("h", "198 + 42", 2, "+")]
    top, bottom = y - 12, 80
    cw, ch = cw_half(), (top - bottom) / 4
    for i, (lbl, expr, terms, op) in enumerate(items):
        x0, y0 = MARGIN + (i % 2) * cw, top - (i // 2) * ch
        c.rect(x0, y0 - ch, cw, ch)
        rich_line(c, x0 + 10, y0 - 26, [(f"{lbl}.  ", False), (expr, True)], 16)
        estimate_frame(c, x0 + 20, y0 - ch + 30, terms, op)
    footer(c, *L19, 130)


def page_131(c):
    """Lesson 19 Exit Ticket. Original: 73+41+24, 474-148, 607-248, 31+46+68."""
    y = start(c, "Lesson 19 Exit Ticket", "TEKS 3.4B", HELP_ESTIMATE)
    top = y - 12
    cw = cw_half()
    for blk, (num, items) in enumerate((
        ("1.", [("a", "73 + 41 + 24", 3, "+"), ("b", "47 − 18", 2, "−")]),
        ("2.", [("a", "61 − 29", 2, "−"), ("b", "31 + 46 + 68", 3, "+")]),
    )):
        y = top - blk * 270
        problem(c, y - 10, num, [("Estimate with compatible numbers.", False)])
        ch = 220
        for i, (lbl, expr, terms, op) in enumerate(items):
            x0, y0 = MARGIN + i * cw, y - 24
            c.rect(x0, y0 - ch, cw, ch)
            rich_line(c, x0 + 10, y0 - 28, [(f"{lbl}.  ", False), (expr, True)], 16)
            rich_line(c, x0 + 10, y0 - 70, [("Friendly numbers:", False)], 11)
            estimate_frame(c, x0 + 20, y0 - 110, terms, op)
    footer(c, *L19, 131)


BOOK = {103: page_103, 104: page_104, 105: page_105, 107: page_107, 115: page_115, 116: page_116,
        117: page_117, 121: page_121, 123: page_123, 124: page_124, 125: page_125, 127: page_127,
        129: page_129, 130: page_130, 131: page_131}

if __name__ == "__main__":
    book = {**BOOK, 109: bm.page_109, 110: bm.page_110, 111: bm.page_111, 113: bm.page_113}
    main("G3_M2_Lessons15-19_Modified.pdf", [book[k] for k in sorted(book)],
         "Bluebonnet Learning Grade 3 Module 2 Lessons 15-19 – Modified")
