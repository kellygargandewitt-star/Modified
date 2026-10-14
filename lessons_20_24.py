"""Modified pages for Bluebonnet Learning Grade 3 Module 2, Topic E: Lessons 20-24 (book pages 133-169).

Problems keep the book's numbers, letters, and order so students can follow
along with the class lesson. Supports: friendlier numbers (fewer regroupings),
place value column frames with regrouping boxes, pre-drawn strip diagrams,
step-by-step number sentences, and a Word Helper on each page.

Run: python3 lessons_20_24.py  ->  writes G3_M2_Lessons20-24_Modified.pdf
"""
from reportlab.lib.colors import HexColor, black

from build_module2 import MARGIN, W, blank, footer, main, rich_line
from lessons_15_19 import grey, problem, read_draw_write, start
from reteach_mid_module import sentence

L20 = (20, "Add measurements using the standard algorithm to compose larger units once.")
L21 = (21, "Add measurements using the standard algorithm to compose larger units twice.")
L22 = (22, "Estimate sums by rounding and apply to solve measurement word problems.")
L23 = (23, "Represent and solve one- and two-step problems involving addition.")
L24 = (24, "Represent and solve one- and two-step problems involving subtraction.")

HELP_ADD = [
    [("Line up the places. ", False), ("Add the ones first.", True)],
    [("10 ones", True), (" → 1 ten.  ", False), ("10 tens", True), (" → 1 hundred.  Write the 1 in the ", False),
     ("little box", True), (" on top.", False)],
]
HELP_ESTIMATE = [
    [("Estimate", True), (" = round, then add.  ", False), ("≈", True), (" means ", False), ("about", True), (".", False)],
    [("Nearest hundred → look at the ", False), ("tens", True), (" digit.   0–4 round ", False), ("down", True),
     (",  5–9 round ", False), ("up", True), (".", False)],
]
HELP_WORD_ADD = [
    [("more than", True), (" / ", False), ("in all", True), (" / ", False), ("total", True), (" / ", False),
     ("altogether", True), (" → add  ( + )", False)],
    [("Two steps:", True), (" find the missing part first, then find the total.", False)],
]
HELP_WORD_SUB = [
    [("left", True), (" / ", False), ("still", True), (" / ", False), ("how much more", True),
     (" → subtract  ( − )", False)],
    [("Two steps:", True), (" add the parts you know, then subtract from the whole.", False)],
]
CARRY = HexColor("#4A78B5")


# ---------------------------------------------------------------- building blocks

def column(c, x, y, nums, op="+", places=3, cw=24):
    """Vertical algorithm frame: place headers, regroup boxes, digits, answer boxes.
    (x, y) is the top-left. Returns the bottom y."""
    ox = x + 14
    for k, p in enumerate(["H", "T", "O"][3 - places:]):
        c.setFont("Sans-Bold", 8)
        c.setFillColor(HexColor("#888888"))
        c.drawCentredString(ox + k * cw + cw / 2, y - 8, p)
        c.setFillColor(black)
    # regroup boxes over every place except the ones
    c.setStrokeColor(CARRY)
    c.setDash(2, 2)
    for k in range(places - 1):
        c.rect(ox + k * cw + 5, y - 26, cw - 10, 13)
    c.setDash()
    c.setStrokeColor(black)
    ry = y - 44
    for r, n in enumerate(nums):
        for k, d in enumerate(str(n).rjust(places)):
            c.setFont("Sans", 15)
            c.drawCentredString(ox + k * cw + cw / 2, ry, d)
        if r == len(nums) - 1:
            c.setFont("Sans-Bold", 15)
            c.drawCentredString(x + 5, ry, op)
        ry -= 20
    c.setLineWidth(1.5)
    c.line(x, ry + 13, ox + places * cw, ry + 13)
    c.setLineWidth(1)
    for k in range(places):
        c.rect(ox + k * cw + 2, ry - 14, cw - 4, 22)
    return ry - 14


def sum_cell(c, x0, y0, cw, ch, label, a, b, unit, op="+"):
    c.rect(x0, y0 - ch, cw, ch)
    rich_line(c, x0 + 8, y0 - 18, [(f"{label}.  ", False), (f"{a} {unit} {op} {b} {unit}", True)], 11.5)
    places = max(len(str(a)), len(str(b)), 2)
    places = min(places + (1 if places < 3 and a + b >= 100 else 0), 3)
    bottom = column(c, x0 + 22, y0 - 24, [a, b], op, places)
    c.setFont("Sans", 11)
    c.drawString(x0 + 22 + 14 + places * 24 + 6, bottom + 8, unit)


def mixed_cell(c, x0, y0, cw, ch, label, big, small):
    """big = (a, b, unit), small = (a, b, unit): e.g. 1 L 245 mL + 2 L 412 mL."""
    (ba, bb, bu), (sa, sb, su) = big, small
    c.rect(x0, y0 - ch, cw, ch)
    rich_line(c, x0 + 8, y0 - 18, [(f"{label}.  ", False), (f"{ba} {bu} {sa} {su}  +  {bb} {bu} {sb} {su}", True)], 11.5)
    ty = y0 - 46
    rich_line(c, x0 + 14, ty, [(f"{bu}:", False)], 10.5)
    sentence(c, x0 + 50, ty, f"{ba} + {bb} = |___|  {bu}", size=12, blank_w=40)
    ty -= 28
    rich_line(c, x0 + 14, ty, [(f"{su}:", False)], 10.5)
    sentence(c, x0 + 50, ty, f"{sa} + {sb} = |___|  {su}", size=12, blank_w=40)
    ty -= 30
    sentence(c, x0 + 14, ty, f"Answer:  |___|  {bu}   |___|  {su}", size=12, blank_w=40)


def sum_grid(c, top, items, bottom=80):
    """items: 9 (label, a, b, unit) in a 3x3 grid + 2 mixed-unit items in a final row."""
    simple, mixed = items[:9], items[9:]
    rows = 3 + (1 if mixed else 0)
    ch = (top - bottom) / rows
    cw = (W - 2 * MARGIN) / 3
    for i, (lbl, a, b, unit) in enumerate(simple):
        sum_cell(c, MARGIN + (i % 3) * cw, top - (i // 3) * ch, cw, ch, lbl, a, b, unit)
    mw = (W - 2 * MARGIN) / 2
    for i, (lbl, big, small) in enumerate(mixed):
        mixed_cell(c, MARGIN + i * mw, top - 3 * ch, mw, ch, lbl, big, small)


def bars(c, x, y, w, rows, scale_max, brace=None, row_gap=36, h=26):
    """Strip diagram. rows: [(name, [(label, value, dashed)])]. Returns bottom y.
    brace: (label, start_value, end_value) drawn under the last row."""
    unit = w / scale_max
    for r, (name, parts) in enumerate(rows):
        ry = y - r * row_gap
        c.setFont("Sans", 10)
        c.drawRightString(x - 6, ry - h + 9, name)
        xx = x
        for label, value, dashed in parts:
            pw = value * unit
            if dashed:
                c.setDash(4, 3)
            c.rect(xx, ry - h, pw, h)
            c.setDash()
            c.setFont("Sans-Bold", 12)
            c.drawCentredString(xx + pw / 2, ry - h + 9, label)
            xx += pw
    bottom = y - (len(rows) - 1) * row_gap - h
    if brace:
        label, s, e = brace
        bx0, bx1, by = x + s * unit, x + e * unit, bottom - 8
        c.line(bx0, by, bx0, by - 6)
        c.line(bx1, by, bx1, by - 6)
        c.line(bx0, by - 6, bx1, by - 6)
        c.setFont("Sans-Bold", 12)
        c.drawCentredString((bx0 + bx1) / 2, by - 22, label)
        bottom = by - 26
    return bottom


def top_brace(c, x, y, w, label):
    """Bracket above a bar spanning width w, labeled on top."""
    c.line(x, y, x, y + 6)
    c.line(x + w, y, x + w, y + 6)
    c.line(x, y + 6, x + w, y + 6)
    c.setFont("Sans-Bold", 12)
    c.drawCentredString(x + w / 2, y + 12, label)


def part(c, y, letter, title, size=12.5):
    rich_line(c, MARGIN + 6, y, [(f"{letter}. ", True), (title, False)], size)


def steps(c, x, y, lines, gap=34, size=14):
    for k, ln in enumerate(lines):
        rich_line(c, x, y, [(f"Step {k + 1}:", False)], 10.5)
        sentence(c, x + 58, y, ln, size=size)
        y -= gap
    return y


def picture(c, path, x, y, w, h):
    c.drawImage(path, x, y, width=w, height=h, preserveAspectRatio=True, mask="auto")


# ---------------------------------------------------------------- Lesson 20

def page_133(c):
    """Lesson 20 Application Problem: mental math 46+5, 39+8, 125+7, 108+4."""
    y = start(c, "Lesson 20 Application Problem", "TEKS 3.4A", [
        [("Make a ten:", True), ("  46 + 5  →  46 + ", False), ("4", True), (" = 50,  then  50 + ", False),
         ("1", True), (" = 51", False)],
        [("Break apart the small number to get to the next ten.", False)],
    ])
    y -= 22
    problem(c, y, "", [("Use mental math. Fill in the steps.", False)])
    items = [("a", 46, 5, "mL"), ("b", 39, 8, "cm"), ("c", 125, 7, "lb"), ("d", 108, 4, "L")]
    top, bottom = y - 12, 80
    cw, ch = (W - 2 * MARGIN) / 2, (top - bottom) / 2
    for i, (lbl, a, b, unit) in enumerate(items):
        x0, y0 = MARGIN + (i % 2) * cw, top - (i // 2) * ch
        c.rect(x0, y0 - ch, cw, ch)
        rich_line(c, x0 + 10, y0 - 26, [(f"{lbl}.  ", False), (f"{a} {unit} + {b} {unit}", True)], 16)
        ten = (a // 10 + 1) * 10
        ty = y0 - 70
        sentence(c, x0 + 24, ty, f"{a} + |___|  =  {ten}", size=14)
        ty -= 40
        sentence(c, x0 + 24, ty, f"{ten} + |___|  =  |______", size=14)
        ty -= 50
        sentence(c, x0 + 24, ty, f"{a} {unit} + {b} {unit} = |______| {unit}", size=12)
    footer(c, *L20, 133)


def page_135(c):
    """Lesson 20 Problem Set. Original: 46+5, 46+25, 46+125, 59+30, 509+83, 597+30, 29+63,
    345+294, 480+476, 1 L 245 mL + 2 L 412 mL, 500 lb 2 oz + 376 lb 3 oz."""
    y = start(c, "Lesson 20 Problem Set", "TEKS 3.4A", HELP_ADD)
    y -= 22
    problem(c, y, "1.", [("Find the sums. Use the boxes to line up the places.", False)])
    sum_grid(c, y - 10, [
        ("a", 46, 5, "mL"), ("b", 46, 25, "mL"), ("c", 46, 125, "mL"),
        ("d", 59, 30, "cm"), ("e", 509, 83, "cm"), ("f", 197, 30, "cm"),
        ("g", 29, 63, "lb"), ("h", 145, 192, "lb"), ("i", 280, 176, "lb"),
        ("j", (1, 2, "L"), (245, 412, "mL")), ("k", (200, 176, "lb"), (2, 3, "oz")),
    ])
    footer(c, *L20, 135)


def page_136(c):
    """Lesson 20 Problem Set (continued).
    Original 2: soap is 63 oz more than 44 oz cookies.  3: 475 mL + 317 mL (782 vs 792).
    4: Greg 15 min, back lawn 17 min more, total."""
    y = start(c, "Lesson 20 Problem Set", "TEKS 3.4A, 3.5A", HELP_WORD_ADD)
    y -= 22
    problem(c, y, "2.", [("The soap weighs ", False), ("26 ounces more", True), (" than the cookies.", False)])
    y -= 18
    rich_line(c, MARGIN + 22, y, [("The cookies weigh ", False), ("44 ounces", True), (". How much does the ", False),
                                  ("soap", True), (" weigh?", False)], 12)
    picture(c, "images/soap_cookies.png", W - MARGIN - 130, y - 92, 130, 80)
    bars(c, MARGIN + 80, y - 18, 250, [("Cookies", [("44", 44, False)]),
                                       ("Soap", [("44", 44, False), ("26", 26, False)])], 75,
         row_gap=32, h=24)
    c.setFont("Sans-Bold", 12)
    c.drawString(MARGIN + 80 + 250 * 70 / 75 + 8, y - 58, "?")
    sentence(c, MARGIN + 22, y - 112, "44 + 26 = |______|  ounces", size=14)

    y -= 150
    problem(c, y, "3.", [("Jason and Andrea add the water in 2 beakers:  ", False), ("175 mL", True), (" and ", False),
                         ("117 mL", True), (".", False)])
    y -= 18
    rich_line(c, MARGIN + 22, y, [("Jason says ", False), ("282 mL", True), (".  Andrea says ", False), ("292 mL", True),
                                  (".  Who is correct?", False)], 12)
    column(c, MARGIN + 30, y - 10, [175, 117])
    ty = y - 40
    for text in ("Circle:   Jason   /   Andrea   is correct.",
                 "The other student forgot to regroup",
                 "10 ones as 1 ten."):
        rich_line(c, MARGIN + 200, ty, [(text, text.startswith("Circle"))], 12)
        ty -= 22

    y -= 128
    problem(c, y, "4.", [("Greg mows the front lawn in ", False), ("15 minutes", True), (". The back lawn takes ", False),
                         ("17 minutes more", True), (".", False)])
    y -= 18
    rich_line(c, MARGIN + 22, y, [("What is the ", False), ("total", True), (" time?", False)], 12)
    bars(c, MARGIN + 80, y - 12, 230, [("Front", [("15", 15, False)]),
                                       ("Back", [("15", 15, False), ("17", 17, False)])], 47,
         row_gap=30, h=22, brace=None)
    steps(c, MARGIN + 10, y - 86, ["15 + 17 = |___|  minutes  (back lawn)", "15 + |___| = |___|  minutes  (total)"],
          gap=30, size=12)
    footer(c, *L20, 136)


def page_137(c):
    """Lesson 20 Exit Ticket. Original: 24+36 cm, 562+180 m, 345+239 km; Brianna 26 min, 15 more."""
    y = start(c, "Lesson 20 Exit Ticket", "TEKS 3.4A", HELP_ADD)
    y -= 22
    problem(c, y, "1.", [("Find the sums.", False)])
    top = y - 10
    cw, ch = (W - 2 * MARGIN) / 3, 140
    for i, (lbl, a, b, unit) in enumerate([("a", 24, 36, "cm"), ("b", 162, 180, "m"), ("c", 145, 139, "km")]):
        sum_cell(c, MARGIN + i * cw, top, cw, ch, lbl, a, b, unit)
    y = top - ch - 34
    problem(c, y, "2.", [("Brianna jogs ", False), ("26 minutes", True), (" on Saturday. On Sunday she jogs ", False),
                         ("15 minutes more", True), (".", False)])
    y -= 18
    bars(c, MARGIN + 90, y - 10, 300, [("Saturday", [("26", 26, False)]),
                                       ("Sunday", [("26", 26, False), ("15", 15, False)])], 67, row_gap=32, h=24)
    y -= 100
    part(c, y, "a", "How many minutes on Sunday?")
    sentence(c, MARGIN + 260, y, "26 + 15 = |______|  minutes", size=14)
    y -= 50
    part(c, y, "b", "How many minutes in total?")
    sentence(c, MARGIN + 260, y, "26 + |______| = |______|  minutes", size=14, wide_w=50)
    column(c, MARGIN + 30, y - 20, [26, 15])
    footer(c, *L20, 137)


# ---------------------------------------------------------------- Lesson 21

def page_139(c):
    """Lesson 21 Application Problem: 93 oz + 152 oz."""
    y = start(c, "Lesson 21 Application Problem", "TEKS 3.4A, 3.5A", HELP_ADD)
    y -= 26
    rich_line(c, MARGIN, y, [("A bag of apples weighs ", False), ("93 ounces", True), (". A bag of pears weighs ", False),
                             ("152 ounces", True), (".", False)], 13)
    y -= 22
    rich_line(c, MARGIN, y, [("What is the ", False), ("total", True), (" weight?", False)], 13)
    y -= 40
    rich_line(c, MARGIN, y, [("Draw:", True)], 12)
    bars(c, MARGIN + 100, y + 10, 330, [("", [("93 apples", 93, False), ("152 pears", 152, False)])], 245,
         brace=("?  ounces", 0, 245))
    y -= 100
    rich_line(c, MARGIN, y, [("Write:", True)], 12)
    column(c, MARGIN + 80, y + 10, [93, 152])
    sentence(c, MARGIN + 260, y - 40, "93 + 152 = |______|  ounces", size=14)
    read_draw_write(c, 100)
    footer(c, *L21, 139)


def page_141(c):
    """Lesson 21 Problem Set. Original: 52+68, 352+68, 352+468, 56+94, 506+94, 506+394, 697+138,
    345+597, 486+497, 3 L 251 mL + 1 L 549 mL, 384 lb 4 oz + 467 lb 2 oz."""
    y = start(c, "Lesson 21 Problem Set", "TEKS 3.4A", HELP_ADD)
    y -= 22
    problem(c, y, "1.", [("Find the sums. Use the boxes to line up the places.", False)])
    sum_grid(c, y - 10, [
        ("a", 52, 38, "mL"), ("b", 352, 38, "mL"), ("c", 352, 438, "mL"),
        ("d", 56, 34, "cm"), ("e", 506, 84, "cm"), ("f", 506, 384, "cm"),
        ("g", 147, 138, "oz"), ("h", 345, 147, "oz"), ("i", 286, 107, "oz"),
        ("j", (3, 1, "L"), (251, 529, "mL")), ("k", (184, 113, "lb"), (4, 2, "oz")),
    ])
    footer(c, *L21, 141)


def page_142(c):
    """Lesson 21 Problem Set (continued).
    Original 2: dog 907 oz + kitten 93 oz.  3: 86 + 58 muffins.  4: juice 279 mL, milk 183 mL more, total."""
    y = start(c, "Lesson 21 Problem Set", "TEKS 3.4A, 3.5A", HELP_WORD_ADD)
    y -= 22
    problem(c, y, "2.", [("Lane's dog weighs ", False), ("207 oz", True), (". His kitten weighs ", False), ("93 oz", True),
                         (". Find the ", False), ("total", True), (".", False)])
    picture(c, "images/pets.png", W - MARGIN - 120, y - 112, 120, 96)
    c.setFont("Sans-Bold", 10)
    c.drawCentredString(W - MARGIN - 92, y - 122, "207 oz")
    c.drawCentredString(W - MARGIN - 28, y - 122, "93 oz")
    bars(c, MARGIN + 60, y - 18, 280, [("", [("207 dog", 207, False), ("93", 93, False)])], 300,
         brace=("?  oz", 0, 300))
    sentence(c, MARGIN + 60, y - 108, "207 + 93 = |______|  oz", size=14)

    y -= 140
    problem(c, y, "3.", [("Sue wraps ", False), ("46", True), (" muffins. She still has ", False), ("38", True),
                         (" muffins cooling.", False)])
    rich_line(c, MARGIN + 22, y - 18, [("How many did she bake ", False), ("altogether", True), ("?", False)], 12)
    y -= 16
    bars(c, MARGIN + 60, y - 16, 260, [("", [("46 wrapped", 46, False), ("38 cooling", 38, False)])], 84,
         brace=("?  muffins", 0, 84))
    column(c, MARGIN + 360, y - 8, [46, 38], places=2)
    sentence(c, MARGIN + 60, y - 100, "46 + 38 = |______|  muffins", size=14)

    y -= 132
    problem(c, y, "4.", [("The juice box holds ", False), ("120 mL", True), (". The milk carton holds ", False),
                         ("150 mL more", True), (".", False)])
    y -= 18
    rich_line(c, MARGIN + 22, y, [("What is the ", False), ("total", True), (" of both?", False)], 12)
    picture(c, "images/drinks.png", W - MARGIN - 110, y - 104, 110, 90)
    bars(c, MARGIN + 80, y - 10, 280, [("Juice", [("120", 120, False)]),
                                       ("Milk", [("120", 120, False), ("150", 150, False)])], 270,
         row_gap=30, h=22)
    steps(c, MARGIN + 10, y - 90, ["120 + 150 = |______|  mL  (milk)", "120 + |______| = |______|  mL  (total)"],
          gap=30, size=12)
    footer(c, *L21, 142)


def page_143(c):
    """Lesson 21 Exit Ticket. Original: 78+29 oz, 328+289 lb, 509+293 L; lemonade 58 L + 46 L."""
    y = start(c, "Lesson 21 Exit Ticket", "TEKS 3.4A", HELP_ADD)
    y -= 22
    problem(c, y, "1.", [("Find the sums.", False)])
    top = y - 10
    cw, ch = (W - 2 * MARGIN) / 3, 140
    for i, (lbl, a, b, unit) in enumerate([("a", 48, 29, "oz"), ("b", 328, 159, "lb"), ("c", 509, 283, "L")]):
        sum_cell(c, MARGIN + i * cw, top, cw, ch, lbl, a, b, unit)
    y = top - ch - 34
    problem(c, y, "2.", [("The class sells ", False), ("38 liters", True), (" of lemonade. They still have ", False),
                         ("46 liters", True), (" left.", False)])
    y -= 18
    rich_line(c, MARGIN + 22, y, [("How many liters did they have at the ", False), ("beginning", True), ("?", False)], 12)
    bars(c, MARGIN + 60, y - 16, 300, [("", [("38 sold", 38, False), ("46 left", 46, False)])], 84,
         brace=("?  liters", 0, 84))
    column(c, MARGIN + 400, y - 10, [38, 46], places=2)
    sentence(c, MARGIN + 60, y - 110, "38 + 46 = |______|  liters", size=14)
    footer(c, *L21, 143)


# ---------------------------------------------------------------- Lesson 22

def round_pair(c, x, y, a, b, unit=""):
    """a ≈ ___   b ≈ ___   then ___ + ___ = ___"""
    sentence(c, x, y, f"{a} ≈ |______|        {b} ≈ |______", size=13)
    sentence(c, x, y - 30, f"______|  +  |______|  =  |______|  {unit}", size=13)


def page_145(c):
    """Lesson 22 Application Problem. Original: 175 mL + 256 mL; estimate, then exact."""
    y = start(c, "Lesson 22 Application Problem", "TEKS 3.4B, 3.4A", HELP_ESTIMATE)
    y -= 26
    rich_line(c, MARGIN, y, [("The doctor gives ", False), ("180 mL", True), (" of medicine on Monday and ", False),
                             ("210 mL", True), (" on Tuesday.", False)], 13)
    y -= 40
    part(c, y, "a", "Estimate the total. Round to the nearest hundred.")
    round_pair(c, MARGIN + 30, y - 34, 180, 210, "mL")
    y -= 120
    part(c, y, "b", "Find the exact total.")
    column(c, MARGIN + 40, y - 8, [180, 210])
    sentence(c, MARGIN + 220, y - 50, "180 + 210 = |______|  mL", size=14)
    y -= 130
    rich_line(c, MARGIN + 6, y, [("Check: Is the exact answer close to the estimate?   ", False), ("yes  /  no", True)], 12)
    read_draw_write(c, 100)
    footer(c, *L22, 145)


def page_147(c):
    """Lesson 22 Problem Set: actual sums vs. rounded estimates in columns A, B, C."""
    y = start(c, "Lesson 22 Problem Set", "TEKS 3.4B, 3.4A", HELP_ESTIMATE)
    y -= 22
    problem(c, y, "1.", [("a. ", True), ("Find the real sum. Then round each number to the nearest ", False),
                         ("hundred", True), (" and add.", False)], 12)
    cols = {
        "A": [(421, 252), (421, 248), (448, 241)],
        "B": [(356, 131), (352, 146), (347, 142)],
        "C": [(652, 136), (643, 156), (641, 146)],
    }
    top = y - 14
    cw = (W - 2 * MARGIN) / 3
    for k, (name, pairs) in enumerate(cols.items()):
        x0 = MARGIN + k * cw
        c.rect(x0, top - 400, cw, 400)
        c.setFont("Sans-Bold", 14)
        c.drawCentredString(x0 + cw / 2, top - 20, name)
        ty = top - 52
        for a, b in pairs:
            sentence(c, x0 + 10, ty, f"{a} + {b} = |______", size=12, wide_w=50)
            grey(c, x0 + 14, ty - 18, "rounded:")
            sentence(c, x0 + 10, ty - 38, "___| + |___| = |______", size=12, blank_w=32, wide_w=42)
            ty -= 96
        c.setFont("Sans", 9.5)
        for j, ln in enumerate(["Circle the estimate that is", "closest to its real sum."]):
            c.drawString(x0 + 10, top - 352 + 0 - j * 13, ln)
    y = top - 430
    problem(c, y, "", [("b. ", True), ("Look at the closest estimates. What do they have in common?", False)], 12)
    y -= 26
    rich_line(c, MARGIN + 22, y, [("Circle:  The numbers were ", False), ("close to  /  far from", True),
                                  (" a hundred.", False)], 12.5)
    footer(c, *L22, 147)


def page_148(c):
    """Lesson 22 Problem Set (continued). Original 2: 94 + 151 minutes.  3: Sadie 282 lb + cub 74 lb."""
    y = start(c, "Lesson 22 Problem Set", "TEKS 3.4B, 3.4A, 3.5A", HELP_ESTIMATE)
    y -= 22
    problem(c, y, "2.", [("Janet watches a ", False), ("94", True), ("-minute movie and a ", False), ("121", True),
                         ("-minute movie.", False)])
    y -= 30
    part(c, y, "a", "Estimate. Round to the nearest ten.")
    sentence(c, MARGIN + 280, y, "90 + 120 = |______", size=13)
    y -= 34
    part(c, y, "b", "Find the exact total.")
    column(c, MARGIN + 200, y + 14, [94, 121])
    sentence(c, MARGIN + 340, y - 40, "= |______|  minutes", size=13)
    y -= 100
    part(c, y, "c", "Round a different way: to the nearest hundred.")
    y -= 28
    sentence(c, MARGIN + 30, y, "100 + 100 = |______", size=13)
    y -= 28
    rich_line(c, MARGIN + 30, y, [("Which estimate is closer to the exact answer?  ", False),
                                  ("nearest ten  /  nearest hundred", True)], 12)

    y -= 44
    problem(c, y, "3.", [("Sadie the bear weighs ", False), ("262 pounds", True), (". Her cub weighs ", False),
                         ("34 pounds", True), (".", False)])
    y -= 30
    part(c, y, "a", "Estimate the total. Round to the nearest ten.")
    sentence(c, MARGIN + 320, y, "260 + 30 = |______", size=13)
    y -= 34
    part(c, y, "b", "Find the exact total. Use the strip diagram.")
    bars(c, MARGIN + 30, y - 12, 300, [("", [("262 Sadie", 262, False), ("34", 34, False)])], 296,
         brace=("?  pounds", 0, 296))
    column(c, MARGIN + 380, y - 4, [262, 34])
    footer(c, *L22, 148)


def page_149(c):
    """Lesson 22 Exit Ticket: Jesse 165 + 245 minutes, estimate to 10 and to 100."""
    y = start(c, "Lesson 22 Exit Ticket", "TEKS 3.4B", HELP_ESTIMATE)
    y -= 26
    rich_line(c, MARGIN, y, [("Jesse practices trumpet ", False), ("165 minutes", True), (" in week 1 and ", False),
                             ("245 minutes", True), (" in week 2.", False)], 13)
    y -= 44
    part(c, y, "a", "Estimate. Round to the nearest 10 minutes.")
    round_pair(c, MARGIN + 30, y - 34, 165, 245, "minutes")
    y -= 120
    part(c, y, "b", "Estimate. Round to the nearest 100 minutes.")
    round_pair(c, MARGIN + 30, y - 34, 165, 245, "minutes")
    y -= 120
    part(c, y, "c", "Why are the two estimates so close? Circle.")
    y -= 30
    rich_line(c, MARGIN + 30, y, [("165 rounds ", False), ("up  /  down", True), (" to 200.      245 rounds ", False),
                                  ("up  /  down", True), (" to 200.", False)], 12.5)
    y -= 28
    rich_line(c, MARGIN + 30, y, [("One goes up and one goes down, so the estimates stay close.", False)], 12.5)
    footer(c, *L22, 149)


# ---------------------------------------------------------------- Lesson 23

def page_151(c):
    """Lesson 23 Application Problem: estimate 144 lb + 235 lb."""
    y = start(c, "Lesson 23 Application Problem", "TEKS 3.4B", HELP_ESTIMATE)
    y -= 26
    rich_line(c, MARGIN, y, [("The librarian packs ", False), ("144 lb", True), (" of books in one truck and ", False),
                             ("235 lb", True), (" in another.", False)], 13)
    y -= 22
    rich_line(c, MARGIN, y, [("About", True), (" how many pounds? ", False), ("Estimate", True), (". Do not solve.", False)], 13)
    y -= 40
    bars(c, MARGIN + 60, y, 360, [("", [("144", 144, False), ("235", 235, False)])], 379, brace=("about ?  lb", 0, 379))
    y -= 110
    rich_line(c, MARGIN, y, [("Round to the nearest hundred:", True)], 12)
    round_pair(c, MARGIN + 30, y - 34, 144, 235, "lb")
    read_draw_write(c, 100)
    footer(c, *L23, 151)


def solve_page(c, title, lesson, page_no, teks_label, helper, num, text, est, model, solve, another, extra=None):
    """Lesson 23/24 word problem layout: a. Estimate, b. Represent, c. Solve, d. Solve another way."""
    y = start(c, title, teks_label, helper)
    y -= 22
    for k, parts in enumerate(text):
        if k == 0:
            problem(c, y, num, parts)
        else:
            rich_line(c, MARGIN + 22, y, parts, 12.5)
        y -= 20
    y -= 14
    part(c, y, "a", "Estimate. Round to the nearest hundred.")
    y -= 30
    for ln in est:
        sentence(c, MARGIN + 30, y, ln, size=13)
        y -= 28
    y -= 8
    part(c, y, "b", "Represent the problem. The strip diagram is started for you.")
    y = model(c, y - 16) - 26
    part(c, y, "c", solve[0])
    y -= 30
    y = steps(c, MARGIN + 30, y, solve[1], gap=32, size=13)
    if another:
        y -= 4
        part(c, y, "d", another[0])
        y -= 30
        steps(c, MARGIN + 30, y, another[1], gap=32, size=13)
    if extra:
        extra(c, y)
    footer(c, *lesson, page_no)


def page_153(c):
    """Lesson 23 Problem Set 1. Original: 144 + 235 + 221 lb."""
    solve_page(
        c, "Lesson 23 Problem Set", L23, 153, "TEKS 3.4A, 3.4B, 3.5A", HELP_WORD_ADD, "1.",
        [[("The librarian packs ", False), ("144 lb", True), (" and ", False), ("235 lb", True),
          (" of books. She has ", False), ("120 lb", True), (" left to pack.", False)],
         [("How many pounds of books in ", False), ("all", True), ("?", False)]],
        ["144 ≈ |___|     235 ≈ |___|     120 ≈ |___", "≈  |___|  +  |___|  +  |___|  =  |______"],
        lambda c, y: bars(c, MARGIN + 60, y, 380, [("", [("144", 144, False), ("235", 235, False), ("120", 120, False)])],
                          499, brace=("?  lb", 0, 499)),
        ("Solve.", ["144 + 235 = |______", "______| + 120 = |______|  lb"]),
        ("Solve another way. Add in a different order.", ["144 + 120 = |______", "______| + 235 = |______|  lb"]),
    )


def page_154(c):
    """Lesson 23 Problem Set 2. Original: 312 miles, then 272 miles farther, altogether."""
    solve_page(
        c, "Lesson 23 Problem Set", L23, 154, "TEKS 3.4A, 3.4B, 3.5A", HELP_WORD_ADD, "2.",
        [[("A family drives ", False), ("312 miles", True), (" on day 1. On day 2 they drive ", False),
          ("172 miles farther", True), (".", False)],
         [("How many miles ", False), ("altogether", True), ("?", False)]],
        ["Day 1 ≈ |___|      Day 2 ≈ 300 + 200 = |___", "Total ≈  |___|  +  |___|  =  |______"],
        lambda c, y: bars(c, MARGIN + 70, y, 300, [("Day 1", [("312", 312, False)]),
                                                   ("Day 2", [("312", 312, False), ("172", 172, False)])], 484,
                          row_gap=32, h=24),
        ("Solve. Two steps.", ["312 + 172 = |______|  (day 2)", "312 + |______| = |______|  miles"]),
        ("Solve another way.", ["312 + 312 = |______", "______| + 172 = |______|  miles"]),
    )


def page_155(c):
    """Lesson 23 Problem Set 3. Original: $443 + $158 + $117."""
    solve_page(
        c, "Lesson 23 Problem Set", L23, 155, "TEKS 3.4A, 3.4B, 3.5A", HELP_WORD_ADD, "3.",
        [[("A restaurant sells ", False), ("$243", True), (" of pizza and ", False), ("$150", True),
          (" of other food. Drinks sell for ", False), ("$105", True), (".", False)],
         [("What is the ", False), ("total", True), (" for the day?", False)]],
        ["243 ≈ |___|     150 ≈ |___|     105 ≈ |___", "≈  |___|  +  |___|  +  |___|  =  |______"],
        lambda c, y: bars(c, MARGIN + 60, y, 380, [("", [("$243", 243, False), ("$150", 150, False), ("$105", 105, False)])],
                          498, brace=("?  dollars", 0, 498)),
        ("Solve.", ["243 + 150 = |______", "______| + 105 = |______|  dollars"]),
        ("Solve another way.", ["243 + 105 = |______", "______| + 150 = |______|  dollars"]),
    )


def page_156(c):
    """Lesson 23 Problem Set 4. Original: 297 L last summer, 152 L more this summer, combined."""
    def check(c, y):
        y -= 8
        part(c, y, "d", "Look at your estimate. Does your answer make sense?")
        y -= 28
        rich_line(c, MARGIN + 30, y, [("Is my answer close to my estimate?  ", False), ("yes  /  no", True)], 13)
        y -= 26
        rich_line(c, MARGIN + 30, y, [("My answer ", False), ("makes sense  /  does not make sense", True), (".", False)], 13)

    solve_page(
        c, "Lesson 23 Problem Set", L23, 156, "TEKS 3.4A, 3.4B, 3.5A", HELP_WORD_ADD, "4.",
        [[("Sandy used ", False), ("210 liters", True), (" of water last summer. She used ", False),
          ("150 liters more", True), (" this summer.", False)],
         [("How many liters ", False), ("combined", True), ("?", False)]],
        ["Last ≈ |___|      This ≈ 200 + 200 = |___", "Total ≈  |___|  +  |___|  =  |______"],
        lambda c, y: bars(c, MARGIN + 90, y, 300, [("Last summer", [("210", 210, False)]),
                                                   ("This summer", [("210", 210, False), ("150", 150, False)])], 360,
                          row_gap=32, h=24),
        ("Solve. Two steps.", ["210 + 150 = |______|  (this summer)", "210 + |______| = |______|  liters"]),
        None, extra=check,
    )


def page_157(c):
    """Lesson 23 Problem Set 5. Original: Shari 336 oz, Vinnie 124 oz more; two models."""
    y = start(c, "Lesson 23 Problem Set", "TEKS 3.4A, 3.5A", HELP_WORD_ADD)
    y -= 22
    problem(c, y, "5.", [("Shari drinks ", False), ("230 ounces", True), (" of water in a week. Vinnie drinks ", False),
                         ("120 ounces more", True), (".", False)])
    y -= 20
    rich_line(c, MARGIN + 22, y, [("How much does ", False), ("each", True), (" drink? How much ", False),
                                  ("together", True), ("?", False)], 12.5)
    y -= 34
    rich_line(c, MARGIN, y, [("Vinnie's model:", True)], 12)
    x0, w = MARGIN + 60, 380
    top_brace(c, x0, y - 26, w, "?")
    bars(c, x0, y - 30, w, [("", [("230", 230, False), ("230", 230, False), ("120", 120, False)])], 580)
    y -= 90
    rich_line(c, MARGIN, y, [("Shari's model:", True)], 12)
    y -= 14
    rich_line(c, MARGIN + 20, y - 14, [("Step 1", False)], 10)
    bars(c, x0, y, w * 350 / 580, [("", [("230", 230, False), ("120", 120, False)])], 350)
    y -= 40
    rich_line(c, MARGIN + 20, y - 14, [("Step 2", False)], 10)
    bars(c, x0, y, w, [("", [("230", 230, False), ("350", 350, False)])], 580, brace=("?", 0, 580))
    y -= 92
    rich_line(c, MARGIN, y, [("Circle the model you will use:   ", False), ("Vinnie's   /   Shari's", True)], 12.5)
    y -= 34
    sentence(c, MARGIN + 20, y, "Shari  =  230  ounces", size=13)
    y -= 32
    sentence(c, MARGIN + 20, y, "Vinnie  =  230 + 120  =  |______|  ounces", size=13)
    y -= 32
    sentence(c, MARGIN + 20, y, "Together  =  230 + |______|  =  |______|  ounces", size=13)
    footer(c, *L23, 157)


def page_159(c):
    """Lesson 23 Exit Ticket. Original: rider 149 lb, horse 573 lb more; together."""
    solve_page(
        c, "Lesson 23 Exit Ticket", L23, 159, "TEKS 3.4A, 3.4B, 3.5A", HELP_WORD_ADD, "1.",
        [[("A rider weighs ", False), ("120 lb", True), (". The horse weighs ", False), ("450 lb more", True),
          (" than the rider.", False)],
         [("How much do they weigh ", False), ("together", True), ("?", False)]],
        ["Rider ≈ |___|      Horse ≈ 100 + 500 = |___", "Total ≈  |___|  +  |___|  =  |______"],
        lambda c, y: bars(c, MARGIN + 70, y, 330, [("Rider", [("120", 120, False)]),
                                                   ("Horse", [("120", 120, False), ("450", 450, False)])], 570,
                          row_gap=32, h=24),
        ("Solve. Two steps.", ["120 + 450 = |______|  (horse)", "120 + |______| = |______|  lb"]),
        None,
    )


# ---------------------------------------------------------------- Lesson 24

def page_161(c):
    """Lesson 24 Application Problem: estimate $242 + $198 + $218."""
    y = start(c, "Lesson 24 Application Problem", "TEKS 3.4B", HELP_ESTIMATE)
    y -= 26
    rich_line(c, MARGIN, y, [("You spend ", False), ("$242", True), (" on food, ", False), ("$198", True),
                             (" on a place to stay, and ", False), ("$218", True), (" on fun.", False)], 13)
    y -= 22
    rich_line(c, MARGIN, y, [("About", True), (" how much did you spend? ", False), ("Estimate", True),
                             (". Do not solve.", False)], 13)
    y -= 40
    bars(c, MARGIN + 60, y, 380, [("", [("$242", 242, False), ("$198", 198, False), ("$218", 218, False)])], 658,
         brace=("about ?", 0, 658))
    y -= 110
    sentence(c, MARGIN + 30, y, "242 ≈ |___|     198 ≈ |___|     218 ≈ |___", size=14)
    y -= 36
    sentence(c, MARGIN + 30, y, "≈  |___|  +  |___|  +  |___|  =  |______|  dollars", size=14)
    read_draw_write(c, 100)
    footer(c, *L24, 161)


def page_163(c):
    """Lesson 24 Problem Set 1. Original: $825 - ($242 + $198 + $218)."""
    solve_page(
        c, "Lesson 24 Problem Set", L24, 163, "TEKS 3.4A, 3.4B, 3.5A", HELP_WORD_SUB, "1.",
        [[("You have ", False), ("$800", True), (". You spend ", False), ("$240", True), (" on food, ", False),
          ("$200", True), (" on a hotel, and ", False), ("$210", True), (" on fun.", False)],
         [("How much money is ", False), ("left", True), ("?", False)]],
        ["800 − (200 + 200 + 200)  =  800 − |___|  =  |______"],
        lambda c, y: (top_brace(c, MARGIN + 60, y - 22, 380, "$800"),
                      bars(c, MARGIN + 60, y - 26, 380, [("", [("240", 240, False), ("200", 200, False),
                                                                ("210", 210, False), ("?", 150, True)])], 800))[1],
        ("Solve. Two steps.", ["240 + 200 + 210 = |______|  (spent)", "800 − |______| = |______|  dollars"]),
        ("Solve another way. Take away one at a time.", ["800 − 240 = |______", "______| − 200 = |______",
                                                          "______| − 210 = |______"]),
    )


def page_164(c):
    """Lesson 24 Problem Set 2. Original: 600 lb max; 186 + 245; third rider."""
    solve_page(
        c, "Lesson 24 Problem Set", L24, 164, "TEKS 3.4A, 3.4B, 3.5A", HELP_WORD_SUB, "2.",
        [[("A ride holds ", False), ("600 pounds", True), (". Person 1 weighs ", False), ("180 lb", True),
          (". Person 2 weighs ", False), ("210 lb", True), (".", False)],
         [("What is the ", False), ("most", True), (" the third rider can weigh?", False)]],
        ["600 − (200 + 200)  =  600 − |___|  =  |______"],
        lambda c, y: (top_brace(c, MARGIN + 60, y - 22, 380, "600 lb"),
                      bars(c, MARGIN + 60, y - 26, 380, [("", [("180", 180, False), ("210", 210, False),
                                                                ("?", 210, True)])], 600))[1],
        ("Solve. Two steps.", ["180 + 210 = |______", "600 − |______| = |______|  lb"]),
        ("Solve another way. Take away one at a time.", ["600 − 180 = |______", "______| − 210 = |______|  lb"]),
    )


def mini_model(c, x, y, letter, w, top_label, parts, brace_below=None, second=None):
    """Small labeled strip-diagram choice for 'which model' questions."""
    c.setFont("Sans-Bold", 12)
    c.drawString(x - 22, y - 18, letter + ".")
    total = sum(p[1] for p in parts)
    if top_label:
        top_brace(c, x, y - 4, w, top_label)
    bars(c, x, y - 8, w, [("", parts)], total, h=22,
         brace=(brace_below, 0, total) if brace_below else None)
    if second:
        bars(c, x, y - 36, w * second[1] / total, [("", [second])], second[1], h=22)


def page_165(c):
    """Lesson 24 Problem Set 3. Original: 845 total; 362 Monday; 262 Tuesday; Wednesday?"""
    y = start(c, "Lesson 24 Problem Set", "TEKS 3.4A, 3.4B, 3.5A", HELP_WORD_SUB)
    y -= 22
    problem(c, y, "3.", [("The Stark family drives ", False), ("790 miles", True), (" in 3 days.", False)])
    y -= 20
    rich_line(c, MARGIN + 22, y, [("Monday: ", False), ("350", True), (" miles.   Tuesday: ", False), ("230", True),
                                  (" miles.   How many miles on ", False), ("Wednesday", True), ("?", False)], 12.5)
    y -= 32
    part(c, y, "a", "Estimate. Round to the nearest hundred.")
    sentence(c, MARGIN + 290, y, "800 − |___| − |___| = |______", size=12.5)
    y -= 34
    part(c, y, "b", "Which model shows the problem? Circle the letter.")
    y -= 30
    w = 200
    xl, xr = MARGIN + 40, MARGIN + 300
    mini_model(c, xl, y, "A", w, None, [("790", 790, False), ("350", 350, False), ("230", 230, False)], brace_below="?")
    mini_model(c, xr, y, "B", w, None, [("790", 790, False), ("230", 230, False)], second=("350", 350, False))
    y -= 100
    mini_model(c, xl, y - 12, "C", w, "790", [("350", 350, False), ("230", 230, False), ("?", 210, True)])
    mini_model(c, xr, y - 12, "D", w, "?", [("350", 350, False), ("230", 230, False)])
    y -= 80
    part(c, y, "c", "Solve. Add the miles you know, then subtract.")
    y -= 30
    steps(c, MARGIN + 30, y, ["350 + 230 = |______", "790 − |______| = |______|  miles"], gap=34, size=13)
    footer(c, *L24, 165)


def page_166(c):
    """Lesson 24 Problem Set 4. Original: $325 - $59."""
    y = start(c, "Lesson 24 Problem Set", "TEKS 3.4A, 3.4B, 3.5A", [
        HELP_WORD_SUB[0],
        [("Subtract the ones first. If the top digit is smaller, ", False), ("trade 1 ten for 10 ones", True), (".", False)],
    ])
    y -= 22
    problem(c, y, "4.", [("Dylan saved ", False), ("$325", True), (". He buys a game for ", False), ("$50", True), (".", False)])
    rich_line(c, MARGIN + 22, y - 18, [("How much money does he have ", False), ("now", True), ("?", False)], 12.5)
    y -= 50
    part(c, y, "a", "Estimate. Round to the nearest ten.")
    sentence(c, MARGIN + 290, y, "330 − 50 = |______", size=13)
    y -= 36
    part(c, y, "b", "Represent the problem.")
    top_brace(c, MARGIN + 80, y - 22, 360, "$325")
    bars(c, MARGIN + 80, y - 26, 360, [("", [("$50", 50, False), ("?", 275, True)])], 325)
    y -= 92
    part(c, y, "c", "Solve.")
    column(c, MARGIN + 60, y - 6, [325, 50], op="−")
    sentence(c, MARGIN + 240, y - 50, "325 − 50 = |______|  dollars", size=14)
    y -= 140
    part(c, y, "d", "Look back at your estimate. Does your answer make sense?")
    y -= 28
    rich_line(c, MARGIN + 30, y, [("Is my answer close to my estimate?  ", False), ("yes  /  no", True)], 13)
    y -= 26
    rich_line(c, MARGIN + 30, y, [("My answer ", False), ("makes sense  /  does not make sense", True), (".", False)], 13)
    footer(c, *L24, 166)


def page_167(c):
    """Lesson 24 Problem Set 5. Original: 375 oz punch; 125 oz pineapple; 175 oz ginger ale; orange juice?"""
    y = start(c, "Lesson 24 Problem Set", "TEKS 3.4A, 3.5A", HELP_WORD_SUB)
    y -= 22
    problem(c, y, "5.", [("The punch needs ", False), ("375 ounces", True), (".", False)])
    y -= 20
    rich_line(c, MARGIN + 22, y, [("They have ", False), ("125 oz", True), (" pineapple juice and ", False),
                                  ("175 oz", True), (" ginger ale.", False)], 12.5)
    y -= 20
    rich_line(c, MARGIN + 22, y, [("How many ounces of ", False), ("orange juice", True), (" do they need to add?", False)], 12.5)
    y -= 34
    w = 200
    xl, xr = MARGIN + 40, MARGIN + 300
    mini_model(c, xl, y - 12, "A", w, "?", [("375", 375, False), ("175", 175, False), ("125", 125, False)])
    mini_model(c, xr, y - 12, "B", w, "375", [("175", 175, False), ("?", 75, True), ("125", 125, False)])
    y -= 74
    c.setFont("Sans-Bold", 12)
    c.drawString(xl - 22, y, "C.")
    c.drawString(xl, y, "375 + 175 + 125 = ?")
    c.drawString(xr - 22, y, "D.")
    c.drawString(xr, y, "175 + 125 = ▢")
    c.drawString(xr, y - 22, "375 − ▢ = ?")
    y -= 52
    part(c, y, "a", "Circle a model that works:   A    B    C    D     Then solve.")
    y -= 30
    y = steps(c, MARGIN + 30, y, ["175 + 125 = |______", "375 − |______| = |______|  ounces"], gap=34, size=13)
    y -= 4
    part(c, y, "b", "Label model B. Write a word under each part.")
    y -= 18
    grey(c, MARGIN + 30, y, "Word bank:   pineapple juice     ginger ale     orange juice", size=10.5)
    y -= 14
    bars(c, MARGIN + 80, y, 360, [("", [("175", 175, False), ("?", 75, True), ("125", 125, False)])], 375)
    for s, e in ((0, 175), (175, 250), (250, 375)):
        blank(c, MARGIN + 80 + 360 * s / 375 + 6, y - 50, 360 * (e - s) / 375 - 12)
    footer(c, *L24, 167)


def page_169(c):
    """Lesson 24 Exit Ticket. Original: 431 mL - 135 mL."""
    solve_page(
        c, "Lesson 24 Exit Ticket", L24, 169, "TEKS 3.4A, 3.4B, 3.5A", HELP_WORD_SUB, "1.",
        [[("A beaker has ", False), ("435 mL", True), (" of a mixture. The scientist pours out ", False),
          ("120 mL", True), (".", False)],
         [("How many mL are ", False), ("still", True), (" in the beaker?", False)]],
        ["435 ≈ |___|      120 ≈ |___", "≈  |___|  −  |___|  =  |______|  mL"],
        lambda c, y: (top_brace(c, MARGIN + 60, y - 22, 380, "435 mL"),
                      bars(c, MARGIN + 60, y - 26, 380, [("", [("120 poured", 120, False), ("?", 315, True)])], 435))[1],
        ("Solve.", ["435 − 120 = |______|  mL"]),
        None,
        extra=lambda c, y: column(c, MARGIN + 330, y + 70, [435, 120], op="−"),
    )


BOOK = {133: page_133, 135: page_135, 136: page_136, 137: page_137, 139: page_139, 141: page_141,
        142: page_142, 143: page_143, 145: page_145, 147: page_147, 148: page_148, 149: page_149,
        151: page_151, 153: page_153, 154: page_154, 155: page_155, 156: page_156, 157: page_157,
        159: page_159, 161: page_161, 163: page_163, 164: page_164, 165: page_165, 166: page_166,
        167: page_167, 169: page_169}

if __name__ == "__main__":
    main("G3_M2_Lessons20-24_Modified.pdf", [BOOK[k] for k in sorted(BOOK)],
         "Bluebonnet Learning Grade 3 Module 2 Lessons 20-24 – Modified")
