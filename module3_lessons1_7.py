"""Grade 3 Module 3, Lessons 1-7 (book pages 3-51): Modified and Simplified versions.

MODIFIED   - every problem, same numbers; strip diagrams / arrays / tables drawn,
             blank equation frames, plain layout.
SIMPLIFIED - fewer problems per page, more visuals (dot arrays, filled place
             value charts, "x n" rule shown on tables, partly filled frames).
Both keep the book's page numbers and problem numbers.

Run: python3 module3_lessons1_7.py  ->  G3_M3_L1-7_Modified.pdf and G3_M3_L1-7_Simplified.pdf
"""
from reportlab.lib.colors import HexColor, black

from build_module2 import MARGIN, W, blank, footer, header, main, rich_line, teks
from end_of_module_accommodated import table
from lessons_20_24 import bars, top_brace
from reteach_mid_module import sentence
from topic_e_simple import column

GREY = HexColor("#666666")
SIMP = False  # set by build()

L1 = (1, "Use multiplication to compare.")
L2 = (2, "Use tables to record multiplicative relationships.")
L3 = (3, "Solve multiplicative comparison word problems.")
L4 = (4, "Describe the relationships between place value units by using multiplicative comparison.")
L5 = (5, "Study commutativity to find known facts of 6, 7, 8, and 9.")
L6 = (6, "Apply the distributive and commutative properties to relate multiplication facts.")
L7 = (7, "Multiply and divide with familiar facts using a box to represent the unknown.")

TIMES = "\"Times as many\" means multiply. The bigger strip has that many equal parts."


# ---------------------------------------------------------------- helpers

def start(c, title, teks_label, tip):
    y = header(c, title, suffix=" (Simplified)" if SIMP else " (Modified)", unit="3 • 3")
    teks(c, y, teks_label)
    rich_line(c, MARGIN, y - 6, [("Tip: ", True), (tip, False)], 12)
    return y - 44


def text(c, y, num, lines, size=13.5):
    for k, parts in enumerate(lines):
        lead = [(num + "  ", True)] if (k == 0 and num) else []
        rich_line(c, MARGIN + (0 if k == 0 or not num else 24), y, lead + parts, size)
        y -= 21
    return y


def frame(c, x, y, s, size=15):
    sentence(c, x, y, s, size=size, blank_w=50, wide_w=70)


def times_strips(c, x, y, small, val, big, times, w=300, label=None):
    """Small strip = 1 part; big strip = `times` equal parts, each labeled `val`. '?' under the big strip."""
    lab = str(val) if label is None else label
    return bars(c, x, y, w, [(small, [(lab, 1, False)]), (big, [(lab, 1, False)] * times)], times,
                row_gap=34, h=26, brace=("?", 0, times))


def dots(c, x, y, rows, cols, gap=18, r=5, shape="dot"):
    for i in range(rows):
        for j in range(cols):
            cx, cy = x + j * gap, y - i * gap
            if shape == "diamond":
                p = c.beginPath()
                p.moveTo(cx, cy + r + 1)
                p.lineTo(cx + r + 1, cy)
                p.lineTo(cx, cy - r - 1)
                p.lineTo(cx - r - 1, cy)
                p.close()
                c.drawPath(p, stroke=1, fill=0)
            elif shape == "star":
                c.setFont("Sans", 13)
                c.drawCentredString(cx, cy - 4, "✦")
            else:
                c.circle(cx, cy, r, stroke=0, fill=1)
    return y - (rows - 1) * gap


def grid(c, x, y, rows, cols, cell=16, split=None):
    c.setLineWidth(0.8)
    for i in range(rows + 1):
        c.line(x, y - i * cell, x + cols * cell, y - i * cell)
    for j in range(cols + 1):
        c.line(x + j * cell, y, x + j * cell, y - rows * cell)
    if split:
        c.setLineWidth(3)
        c.line(x - 6, y - split * cell, x + cols * cell + 6, y - split * cell)
    c.setLineWidth(1)
    return y - rows * cell


def bond(c, cx, cy, whole, parts, r=18):
    c.circle(cx, cy, r + 4)
    c.setFont("Sans-Bold", 14)
    c.drawCentredString(cx, cy - 5, whole)
    n = len(parts)
    for k, p in enumerate(parts):
        px = cx + (k - (n - 1) / 2) * 52
        py = cy - 70
        c.line(cx, cy - r - 4, px, py + r)
        c.circle(px, py, r)
        c.drawCentredString(px, py - 5, p)
    return cy - 70 - r


def chart(c, x, y, title, rows, w=None, rh=22, first=None):
    """Two-column chart with lettered rows; `first` fills row a as an example."""
    w = w or (W - 2 * MARGIN - (x - MARGIN))
    c.rect(x, y - rh, w, rh)
    c.setFont("Sans-Bold", 11)
    c.drawCentredString(x + w / 2, y - 15, title)
    for k in range(rows):
        ry = y - rh * (k + 1)
        c.rect(x, ry - rh, w, rh)
        c.line(x + w / 2, ry, x + w / 2, ry - rh)
        c.setFont("Sans", 10)
        c.drawString(x + 4, ry - 15, "abcdefgh"[k] + ".")
        if k == 0 and first:
            c.setFont("Sans", 11)
            c.drawString(x + 22, ry - 15, first[0])
            c.drawString(x + w / 2 + 8, ry - 15, first[1])
    return y - rh * (rows + 1)


def read_draw_write(c, y=100):
    c.setFont("Sans-Bold", 12)
    for k, word in enumerate(["Read", "Draw", "Write"]):
        c.drawCentredString(MARGIN + 90 + k * 170, y, word)


def pv_row(c, x, y, digits, places=("HTh", "TTh", "Th", "H", "T", "O"), cw=62, shade=()):
    """Place value chart with x10 arrows. digits: string aligned to the right."""
    d = digits.rjust(len(places))
    for k, (p, ch) in enumerate(zip(places, d)):
        if k in shade:
            c.setFillColor(HexColor("#E6E6E6"))
            c.rect(x + k * cw + 3, y - 40, cw - 6, 40, stroke=0, fill=1)
            c.setFillColor(black)
        c.rect(x + k * cw + 3, y - 40, cw - 6, 40)
        c.setFont("Sans", 9)
        c.drawCentredString(x + k * cw + cw / 2, y - 12, p)
        c.setFont("Sans-Bold", 16)
        c.drawCentredString(x + k * cw + cw / 2, y - 33, ch.strip())
    for k in range(len(places) - 1):
        c.setFont("Sans", 8)
        c.setFillColor(GREY)
        c.drawCentredString(x + (k + 1) * cw, y + 6, "×10")
        c.setFillColor(black)
    return y - 40


# ---------------------------------------------------------------- Lesson 1

def p3(c):
    y = start(c, "Lesson 1 Application Problem", "TEKS 3.4A, 3.5A", "\"How many more\" means subtract.")
    y = text(c, y, "", [[("Ken has ", False), ("975", True), (" blocks. Robert has ", False), ("1,027", True), (" blocks.", False)],
                        [("How many ", False), ("more", True), (" blocks does Robert have?", False)]])
    bars(c, MARGIN + 80, y - 10, 300, [("Robert", [("1,027", 1027, False)]),
                                        ("Ken", [("975", 975, False), ("?", 52, False)])], 1027, row_gap=34, h=26)
    frame(c, MARGIN + 24, y - 100, "1,027 − 975 = |______|  blocks")
    if SIMP:
        column(c, W - MARGIN - 160, y - 90, [1027, 975], "−")
    read_draw_write(c)
    footer(c, *L1, 3)


def strip_problem(c, y, num, lines, small, val, big, times, eq_simp, w=300):
    y = text(c, y, num, lines)
    times_strips(c, MARGIN + 90, y - 8, small, val, big, times, w=w)
    frame(c, MARGIN + 24, y - 116, eq_simp if SIMP else "___| × |___| = |______")
    return y - 140


def p5(c):
    y = start(c, "Lesson 1 Problem Set", "TEKS 3.4K, 3.5B", TIMES)
    rich_line(c, MARGIN, y, [("Example (done for you): ", True), ("Red = 1 unit. Blue = 3 times as long.", False)], 12)
    bars(c, MARGIN + 60, y - 10, 120, [("Red", [("1", 1, False)]), ("Blue", [("1", 1, False)] * 3)], 3, row_gap=26, h=20)
    rich_line(c, MARGIN + 220, y - 40, [("3 × 1 = 3 units", True)], 13)
    y -= 76
    y = strip_problem(c, y, "1.", [[("Blue = ", False), ("1 unit", True), (". Red is ", False), ("4 times as long", True),
                                    (". How long is red?", False)]], "Blue", 1, "Red", 4, "4 × 1 = |______|  units")
    if not SIMP:
        y = strip_problem(c, y, "2.", [[("Red is ", False), ("twice (2 times) as long", True), (" as blue. Blue = ", False),
                                        ("1 unit", True), (".", False)]], "Blue", 1, "Red", 2, "2 × 1 = |______|  units")
    strip_problem(c, y, "3.", [[("Yellow = ", False), ("5 units", True), (". Red is ", False), ("5 times as long", True),
                                (". How long is red?", False)]], "Yellow", 5, "Red", 5, "5 × 5 = |______|  units")
    footer(c, *L1, 5)


def p6(c):
    y = start(c, "Lesson 1 Problem Set", "TEKS 3.4K, 3.5B", TIMES)
    y = strip_problem(c, y, "4.", [[("The walk to the library is ", False), ("5 blocks", True), (".", False)],
                                   [("The walk to the book store is ", False), ("3 times as long", True), (". How long?", False)]],
                      "Library", 5, "Store", 3, "3 × 5 = |______|  blocks")
    y = strip_problem(c, y, "5.", [[("Beth's ring costs ", False), ("$8", True), (". Kristen's costs ", False),
                                    ("4 times as much", True), (".", False)]], "Beth", "$8", "Kristen", 4,
                      "4 × 8 = |______|  dollars")
    if not SIMP:
        strip_problem(c, y, "6.", [[("A hoop is ", False), ("8 feet", True), (" tall. A tree is ", False), ("5 times as tall", True),
                                    (".", False)]], "Hoop", 8, "Tree", 5, "", w=320)
    footer(c, *L1, 6)


def p7(c):
    y = start(c, "Lesson 1 Exit Ticket", "TEKS 3.4K, 3.5B", TIMES)
    y = strip_problem(c, y, "1.", [[("Red = ", False), ("3 units", True), (". Yellow is ", False), ("3 times as long", True),
                                    (".", False)]], "Red", 3, "Yellow", 3, "3 × 3 = |______|  units")
    strip_problem(c, y, "2.", [[("Blue = ", False), ("2 cm", True), (". Red is ", False), ("3 times as long", True), (".", False)]],
                  "Blue", 2, "Red", 3, "3 × 2 = |______|  cm")
    footer(c, *L1, 7)


# ---------------------------------------------------------------- Lesson 2

def p9(c):
    y = start(c, "Lesson 2 Application Problem", "TEKS 3.4K, 3.5B", TIMES)
    strip_problem(c, y, "", [[("Diane walks ", False), ("5 laps", True), (". Ellen walks ", False), ("3 times as many", True),
                              (" laps.", False)], [("How many laps does Ellen walk?", False)]],
                  "Diane", 5, "Ellen", 3, "3 × 5 = |______|  laps")
    read_draw_write(c)
    footer(c, *L2, 9)


def rule_table(c, x, y, heads, rows, rule, rh=26):
    """Vertical In/Out style table; blanks are ''. In SIMPLIFIED the rule is shown beside it."""
    bottom = table(c, x, y, heads, [[a, b] for a, b in rows], [90, 90], rh=rh)
    if SIMP:
        c.setFont("Sans-Bold", 13)
        c.drawString(x + 195, y - rh * 2 - 6, f"→ {rule} →")
        c.setFont("Sans", 10)
        c.setFillColor(GREY)
        c.drawString(x + 195, y - rh * 2 - 22, f"{heads[0]} {rule} = {heads[1]}")
        c.setFillColor(black)
    return bottom


def p11(c):
    y = start(c, "Lesson 2 Problem Set", "TEKS 3.5E, 3.4K", "Use the rule to fill in each empty box.")
    y = text(c, y, "1.", [[("4 times as many", True), (" daisies as roses.", False)]])
    rule_table(c, MARGIN + 40, y - 4, ["Roses", "Daisies"],
               [("1", ""), ("2", ""), ("", "12"), ("4", ""), ("5", ""), ("", "40")], "× 4", rh=24)
    y2 = text(c, y, "", [])
    if SIMP:
        footer(c, *L2, 11)
        y = y - 190
        y = text(c, y, "2.", [[("There are ", False), ("10 times as many", True), (" fish as dolphins.", False)]])
        rule_table(c, MARGIN + 40, y - 4, ["Dolphins", "Fish"],
                   [("1", ""), ("2", ""), ("", "30"), ("4", ""), ("5", ""), ("", "100")], "× 10", rh=24)
        return
    x2 = MARGIN + 270
    rich_line(c, x2, y + 21, [("2.  ", True), ("10 times as many", True), (" fish as dolphins.", False)], 13.5)
    table(c, x2, y - 4, ["Dolphins", "Fish"],
          [["1", ""], ["2", ""], ["", "30"], ["4", ""], ["5", ""], ["", "100"]], [90, 90], rh=24)
    y -= 200
    y = text(c, y, "3.", [[("There are ", False), ("3 times as many", True), (" cars as buses.", False)]])
    cells = [("Buses", ["1", "3", "", "", "5", ""]), ("Cars", ["", "", "24", "21", "", "27"])]
    cw = 62
    for r, (name, vals) in enumerate(cells):
        ry = y - 6 - r * 30
        c.rect(MARGIN + 20, ry - 30, 80, 30)
        c.setFont("Sans-Bold", 12)
        c.drawCentredString(MARGIN + 60, ry - 20, name)
        for k, v in enumerate(vals):
            c.rect(MARGIN + 100 + k * cw, ry - 30, cw, 30)
            c.setFont("Sans", 13)
            c.drawCentredString(MARGIN + 100 + k * cw + cw / 2, ry - 20, v)
    footer(c, *L2, 11)


def p12(c):
    y = start(c, "Lesson 2 Problem Set", "TEKS 3.5E, 3.4K", "Find the rule. Then fill in the empty boxes.")
    y = text(c, y, "4.", [[("Fill in the table. Then finish the sentence.", False)]])
    rule_table(c, MARGIN + 40, y - 4, ["Crayons", "Markers"],
               [("9", "18"), ("8", ""), ("", "10"), ("3", "6"), ("1", "")], "× 2", rh=24)
    sentence(c, MARGIN + 24, y - 170, "There are |______|  times as many markers as crayons.", size=13, wide_w=60)
    y -= 210
    if not SIMP:
        y = text(c, y, "5.", [[("Fill in the table. Then finish the sentence.", False)]])
        table(c, MARGIN + 40, y - 4, ["Singers", "Dancers"],
              [["4", ""], ["", "30"], ["8", "40"], ["10", "50"], ["", "15"]], [90, 90], rh=24)
        sentence(c, MARGIN + 24, y - 170, "There are |______|  times as many dancers as singers.", size=13, wide_w=60)
        y -= 210
    y = text(c, y, "6.", [[("A magician puts ", False), ("4", True), (" cards in. ", False), ("16", True), (" cards come out.", False)]])
    if SIMP:
        dots(c, MARGIN + 40, y - 10, 1, 4, gap=20)
        rich_line(c, MARGIN + 140, y - 14, [("→", True)], 16)
        dots(c, MARGIN + 180, y - 10, 1, 16, gap=18)
        y -= 40
    sentence(c, MARGIN + 24, y - 14, "16 is |______|  times as much as 4.", size=14, wide_w=60)
    footer(c, *L2, 12)


def p13(c):
    y = start(c, "Lesson 2 Exit Ticket", "TEKS 3.5E, 3.4K", "Use the rule to fill in each empty box.")
    y = text(c, y, "1.", [[("Nora saves ", False), ("3 times as much", True), (" as Iggy. Fill in the table.", False)]])
    rule_table(c, MARGIN + 40, y - 4, ["Iggy", "Nora"], [("1", ""), ("", "9"), ("5", ""), ("10", ""), ("", "27")], "× 3", rh=24)
    y -= 200
    y = text(c, y, "2.", [[("A magic box changes numbers.", False)]])
    rule_table(c, MARGIN + 40, y - 4, ["In", "Out"], [("2", "4"), ("10", "20"), ("8", "16"), ("3", "6")], "× ?", rh=24)
    sentence(c, MARGIN + 24, y - 160, "The number that comes out is |______|  times as much", size=13, wide_w=60)
    rich_line(c, MARGIN + 24, y - 182, [("as the number that goes in.", True)], 13)
    footer(c, *L2, 13)


# ---------------------------------------------------------------- Lesson 3

def p15(c):
    y = start(c, "Lesson 3 Problem Set", "TEKS 3.4K, 3.5B", TIMES)
    y = strip_problem(c, y, "1.", [[("George found ", False), ("9", True), (" pennies. Carol found ", False), ("4 times as many", True),
                                    (".", False)]], "George", 9, "Carol", 4, "4 × 9 = |______|  pennies")
    y = strip_problem(c, y, "2.", [[("Bruce rode ", False), ("5 miles", True), (" Monday. Friday he rode ", False),
                                    ("6 times as far", True), (".", False)]], "Monday", 5, "Friday", 6, "6 × 5 = |______|  miles",
                      w=330)
    y = text(c, y, "3.", [[("Look at the strip diagram.", False)]])
    bars(c, MARGIN + 90, y - 8, 330, [("", [("6", 1, False)]), ("", [("6", 1, False)] * 7)], 7, row_gap=34, h=26,
         brace=("42", 0, 7))
    frame(c, MARGIN + 24, y - 122, "42 is |___|  times as much as 6." if SIMP else "42 is |______|  as much as 6.")
    footer(c, *L3, 15)


def p16(c):
    y = start(c, "Lesson 3 Problem Set", "TEKS 3.4K, 3.5B", "Find each one first. Then add them all.")
    y = text(c, y, "4.", [[("Mittens take ", False), ("2", True), (" balls of yarn.", False)],
                          [("A shawl takes ", False), ("3 times as much", True), (". A sweater takes ", False),
                           ("6 times as much", True), (".", False)],
                          [("How many balls of yarn for ", False), ("all three", True), ("?", False)]])
    bars(c, MARGIN + 90, y - 8, 360, [("Mittens", [("2", 1, False)]), ("Shawl", [("2", 1, False)] * 3),
                                      ("Sweater", [("2", 1, False)] * 6)], 6, row_gap=34, h=26)
    y -= 130
    for k, s in enumerate(["Shawl:  3 × 2 = |______", "Sweater:  6 × 2 = |______",
                           "All three:  2 + |______| + |______| = |______"]):
        frame(c, MARGIN + 24, y - k * 44, s)
    footer(c, *L3, 16)


def p17(c):
    y = start(c, "Lesson 3 Exit Ticket", "TEKS 3.4K, 3.5B", TIMES)
    y = text(c, y, "1.", [[("Joan owes ", False), ("$6", True), (". Stan owes ", False), ("4 times as much", True),
                           (". Draw an array.", False)]])
    if SIMP:
        dots(c, MARGIN + 60, y - 10, 4, 6, gap=20)
        rich_line(c, MARGIN + 200, y - 40, [("4 rows of 6", True)], 13)
    else:
        c.setStrokeColor(HexColor("#BBBBBB"))
        c.rect(MARGIN + 24, y - 90, 200, 90)
        c.setStrokeColor(black)
    frame(c, MARGIN + 24, y - 120, "4 × 6 = |______|  dollars" if SIMP else "___| × |___| = |______")
    y -= 160
    strip_problem(c, y, "2.", [[("Ellie practiced ", False), ("9 minutes", True), (" Tuesday. Friday she practiced ", False),
                                ("5 times as much", True), (".", False)]], "Tuesday", 9, "Friday", 5,
                  "5 × 9 = |______|  minutes")
    footer(c, *L3, 17)


# ---------------------------------------------------------------- Lesson 4

def ten_strip(c, x, y, small_label, w=330):
    """One small box (the smaller value) above a strip of 10 equal boxes."""
    c.rect(x, y - 26, w / 10, 26)
    c.setFont("Sans-Bold", 11 if len(small_label) <= 3 else 7.5)
    c.drawCentredString(x + w / 20, y - 17, small_label)
    for k in range(10):
        c.rect(x + k * w / 10, y - 66, w / 10, 26)
        if SIMP:
            c.setFont("Sans", 8 if len(small_label) <= 3 else 5.5)
            c.drawCentredString(x + k * w / 10 + w / 20, y - 57, small_label)
    top_brace(c, x, y - 82, w, "")
    c.line(x, y - 70, x, y - 76)
    c.rect(x + w / 2 - 40, y - 108, 80, 24)
    return y - 108


def p19(c):
    y = start(c, "Lesson 4 Problem Set", "TEKS 3.2B", "Each place is 10 times as much as the place to its right.")
    y = text(c, y, "1.", [[("In ", False), ("119,500", True), (", compare the two ", False), ("1s", True), (".", False)]])
    if SIMP:
        pv_row(c, MARGIN + 30, y - 4, "119500", shade=(0, 1))
        y -= 56
    ten_strip(c, MARGIN + 60, y - 6, "10,000")
    sentence(c, MARGIN + 24, y - 128, "1 |__________|  is |___|  times as much as 1 ten thousand.", size=13, wide_w=110)
    frame(c, MARGIN + 24, y - 156, "10 × 10,000 = |______")
    y -= 186
    y = text(c, y, "2.", [[("Carl wrote ", False), ("3,246", True), (". Kyle wrote ", False), ("24,765", True),
                          (". Compare the ", False), ("6s", True), (".", False)]])
    if SIMP:
        pv_row(c, MARGIN + 30, y - 4, "3246", shade=(5,))
        pv_row(c, MARGIN + 30, y - 48, "24765", shade=(4,))
        y -= 92
    ten_strip(c, MARGIN + 60, y - 6, "6")
    sentence(c, MARGIN + 24, y - 128, "6 |______|  is |___|  times as much as 6 |______", size=13, wide_w=70)
    frame(c, MARGIN + 24, y - 156, "10 × 6 = |______")
    footer(c, *L4, 19)


def p20(c):
    y = start(c, "Lesson 4 Problem Set", "TEKS 3.2B", "Each place is 10 times as much as the place to its right.")
    y = text(c, y, "3.", [[("Kason has ", False), ("4,628", True), (" cards. Nick has ", False), ("3,268", True),
                          (". Compare the ", False), ("2s", True), (".", False)]])
    if SIMP:
        pv_row(c, MARGIN + 30, y - 4, "4628", shade=(4,))
        pv_row(c, MARGIN + 30, y - 50, "3268", shade=(3,))
        y -= 100
    sentence(c, MARGIN + 24, y - 14, "2 |______|  is |___|  times as much as 2 |______", size=13, wide_w=70)
    frame(c, MARGIN + 24, y - 50, "10 × 20 = |______" if SIMP else "___| × |___| = |______")
    y -= 90
    if not SIMP:
        y = text(c, y, "4.", [[("Ann underlines the two 8s in ", False), ("168,348", True), (".", False)]])
        pv_row(c, MARGIN + 30, y - 4, "168348")
        sentence(c, MARGIN + 24, y - 64, "8 |______|  is |______|  times as much as 8 |______", size=13, wide_w=70)
        frame(c, MARGIN + 24, y - 98, "___| × |___| = |______")
        y -= 136
    y = text(c, y, "5.", [[("Cleo has ", False), ("$20", True), (". Cooper has ", False), ("$2,000", True), (".", False)]])
    if SIMP:
        pv_row(c, MARGIN + 30, y - 4, "20", places=("Th", "H", "T", "O"), shade=(2,))
        pv_row(c, MARGIN + 30, y - 50, "2000", places=("Th", "H", "T", "O"), shade=(0,))
        y -= 100
    sentence(c, MARGIN + 24, y - 14, "$2,000 is |______|  times as much as $20.", size=13, wide_w=70)
    frame(c, MARGIN + 24, y - 50, "100 × 20 = |______" if SIMP else "___| × |___| = |______")
    y -= 90
    if not SIMP:
        y = text(c, y, "6.", [[("Write a number with a 6 that is ", False), ("10 times as much", True),
                              (" as the 6 in ", False), ("34,671", True), (".", False)]])
        frame(c, MARGIN + 24, y - 14, "My number: |__________")
    footer(c, *L4, 20)


def p21(c):
    y = start(c, "Lesson 4 Exit Ticket", "TEKS 3.2B", "Each place is 10 times as much as the place to its right.")
    y = text(c, y, "1.", [[("Eric wrote ", False), ("3,624", True), (". Luke wrote ", False), ("27,365", True),
                          (". Compare the ", False), ("3s", True), (".", False)]])
    if SIMP:
        pv_row(c, MARGIN + 30, y - 4, "3624", shade=(2,))
        pv_row(c, MARGIN + 30, y - 50, "27365", shade=(3,))
        y -= 100
    sentence(c, MARGIN + 24, y - 14, "3 |______|  is |___|  times as much as 3 hundreds.", size=13, wide_w=70)
    frame(c, MARGIN + 24, y - 50, "10 × 300 = |______")
    y -= 90
    y = text(c, y, "2.", [[("Maria underlines the two 7s in ", False), ("627,875", True), (".", False)]])
    if SIMP:
        pv_row(c, MARGIN + 30, y - 4, "627875", shade=(2, 4))
        y -= 52
    sentence(c, MARGIN + 24, y - 14, "7 |______|  is |______|  times as much as 7 |______", size=13, wide_w=70)
    frame(c, MARGIN + 24, y - 50, "___| × |___| = |______")
    y -= 90
    y = text(c, y, "3.", [[("Jack wrote ", False), ("9,999", True), (". Compare the 9 in the ", False), ("thousands", True),
                          (" and the 9 in the ", False), ("tens", True), (".", False)]])
    if SIMP:
        pv_row(c, MARGIN + 30, y - 4, "9999", places=("Th", "H", "T", "O"), shade=(0, 2))
        y -= 52
    sentence(c, MARGIN + 24, y - 14, "9 thousands is |______|  times as much as 9 tens.", size=13, wide_w=70)
    frame(c, MARGIN + 24, y - 50, "___| × 90 = 9,000" if SIMP else "___| × |___| = |______")
    footer(c, *L4, 21)


def p23(c):
    y = start(c, "Lesson 4 Template", "TEKS 3.2B", "Use this chart to help with Lesson 4.")
    rich_line(c, MARGIN, y, [("PLACE VALUE CHART", True)], 14)
    pv_row(c, MARGIN + 10, y - 30, "", cw=84)
    places = ["100,000", "10,000", "1,000", "100", "10", "1"]
    for k, v in enumerate(places):
        c.setFont("Sans", 11)
        c.drawCentredString(MARGIN + 10 + k * 84 + 42, y - 88, v)
    y -= 140
    rich_line(c, MARGIN, y, [("Sentence Stems", True)], 14)
    sentence(c, MARGIN, y - 40, "1 |__________|  is |______|  times as much as 1 |__________", size=13, wide_w=100)
    sentence(c, MARGIN, y - 90, "______|  is |______|  times as much as |______", size=13, wide_w=100)
    footer(c, *L4, 23)


# ---------------------------------------------------------------- Lesson 5

def p25(c):
    y = start(c, "Lesson 5 Application Problem", "TEKS 3.4K, 3.5B", "Same amount each day: multiply.")
    y = text(c, y, "", [[("Geri travels ", False), ("3 miles", True), (" each day. How many miles in ", False),
                         ("6 days", True), ("?", False)]])
    bars(c, MARGIN + 60, y - 10, 360, [("", [("3", 1, False)] * 6)], 6, h=28, brace=("?  miles", 0, 6))
    frame(c, MARGIN + 24, y - 100, "6 × 3 = |______|  miles" if SIMP else "___| × |___| = |______")
    read_draw_write(c)
    footer(c, *L5, 25)


def p27(c):
    y = start(c, "Lesson 5 Problem Set", "TEKS 3.4K, 3.5B", "You can turn an array around: 4 × 6 = 6 × 4.")
    y = text(c, y, "1.", [[("Use the array to write ", False), ("two", True), (" multiplication equations.", False)]])
    dots(c, MARGIN + 50, y - 10, 4, 6, gap=20, shape="diamond")
    if SIMP:
        rich_line(c, MARGIN + 30, y - 90, [("4 rows of 6", False)], 11)
    frame(c, MARGIN + 220, y - 20, "4 × 6 = |______" if SIMP else "______| = |___| × |___")
    frame(c, MARGIN + 220, y - 60, "6 × 4 = |______" if SIMP else "______| = |___| × |___")
    y -= 120
    if not SIMP:
        y = text(c, y, "2.", [[("Use the area model to write ", False), ("two", True), (" multiplication equations.", False)]])
        c.rect(MARGIN + 60, y - 120, 90, 110)
        c.setFont("Sans-Bold", 13)
        c.drawCentredString(MARGIN + 105, y, "5")
        c.drawRightString(MARGIN + 52, y - 70, "6")
        frame(c, MARGIN + 220, y - 40, "______| = |___| × |___")
        frame(c, MARGIN + 220, y - 80, "______| = |___| × |___")
        y -= 150
    y = text(c, y, "3.", [[("Fill in the number bond. Then write the equations.", False)]])
    bond(c, MARGIN + 120, y - 30, "", ["6", "6", "6", "6"])
    frame(c, MARGIN + 270, y - 40, "4 × 6 = |______" if SIMP else "a.  |___| × |___| = |______")
    frame(c, MARGIN + 270, y - 90, "6 × 4 = |______" if SIMP else "b.  |___| × |___| = |______")
    footer(c, *L5, 27)


def p28(c):
    y = start(c, "Lesson 5 Problem Set", "TEKS 3.4K, 3.4F", "One array makes 2 multiplication and 2 division facts.")
    y = text(c, y, "4.", [[("Write the ", False), ("4", True), (" equations the array shows.", False)]])
    dots(c, MARGIN + 50, y - 10, 3, 7, gap=20)
    eqs = (["3 × 7 = |______", "7 × 3 = |______", "21 ÷ 3 = |______", "21 ÷ 7 = |______"] if SIMP
           else ["a.  |__________", "b.  |__________", "c.  |__________", "d.  |__________"])
    for k, e in enumerate(eqs):
        frame(c, MARGIN + 220 + (k // 2) * 150, y - 14 - (k % 2) * 40, e, size=13)
    y -= 100
    y = text(c, y, "5.", [[("Complete the equations.", False)]])
    items = [("a.", "4 sevens = |___|  fours = 28"), ("b.", "3 |______|  = 6 threes = |___"),
             ("c.", "5 sevens = 7 |______|  = |___"), ("d.", "4 × |___|  = 6 × 4 = |___"),
             ("e.", "8 × 5 = |___|  × 8 = |___"), ("f.", "___|  × 7 = 7 × |___|  = 14")]
    if SIMP:
        items = [items[0], items[1], items[3], items[4]]
    for k, (lbl, e) in enumerate(items):
        rich_line(c, MARGIN + 24, y - 14 - k * 46, [(lbl, True)], 13)
        frame(c, MARGIN + 50, y - 14 - k * 46, e, size=14)
    footer(c, *L5, 28)


def jump_line(c, x, y, w, step, jumps):
    n = jumps
    c.setLineWidth(1.5)
    c.line(x - 8, y, x + w + 8, y)
    c.setLineWidth(1)
    for k in range(n + 1):
        tx = x + k * w / n
        c.line(tx, y - 7, tx, y + 7)
        c.setFont("Sans", 11)
        c.drawCentredString(tx, y - 22, str(k * step))
        if k < n:
            c.arc(tx, y + 2, tx + w / n, y + 34, 0, 180)
            c.setFont("Sans", 9)
            c.drawCentredString(tx + w / (2 * n), y + 38, f"+{step}")


def p29(c):
    y = start(c, "Lesson 5 Problem Set", "TEKS 3.4K, 3.5B", "Count the jumps. Each jump is the same size.")
    y = text(c, y, "6.", [[("Use the number line.", False)]])
    jump_line(c, MARGIN + 40, y - 70, 400, 6, 5)
    y -= 110
    frame(c, MARGIN + 24, y, "a.  |___| × 6 = |______" if SIMP else "a.  |__________")
    frame(c, MARGIN + 24, y - 40, "b.  6 × |___| = |______" if SIMP else "b.  |__________")
    if not SIMP:
        rich_line(c, MARGIN + 24, y - 80, [("c.  ", True), ("Draw a number line for the related fact.", False)], 13)
        c.setStrokeColor(HexColor("#BBBBBB"))
        c.line(MARGIN + 40, y - 120, W - MARGIN - 40, y - 120)
        c.setStrokeColor(black)
        y -= 50
    y -= 110
    y = text(c, y, "7.", [[("Show that ", False), ("3 × 9 = 9 × 3", True), (".", False)]])
    if SIMP:
        rich_line(c, MARGIN + 24, y - 6, [("3 groups of 9:", False)], 12)
        dots(c, MARGIN + 150, y - 2, 3, 9, gap=14, r=4)
        rich_line(c, MARGIN + 24, y - 66, [("9 groups of 3:", False)], 12)
        dots(c, MARGIN + 150, y - 62, 9, 3, gap=12, r=3.5)
        frame(c, MARGIN + 300, y - 80, "3 × 9 = |______")
        frame(c, MARGIN + 300, y - 120, "9 × 3 = |______")
    else:
        c.setStrokeColor(HexColor("#BBBBBB"))
        c.rect(MARGIN + 24, y - 150, W - 2 * MARGIN - 48, 140)
        c.setStrokeColor(black)
    footer(c, *L5, 29)


def p31(c):
    y = start(c, "Lesson 5 Exit Ticket", "TEKS 3.4K, 3.5B", "You can turn an array around: 4 × 7 = 7 × 4.")
    y = text(c, y, "1.", [[("Use the array to write ", False), ("two", True), (" multiplication facts.", False)]])
    dots(c, MARGIN + 50, y - 10, 4, 7, gap=20, shape="star")
    frame(c, MARGIN + 250, y - 20, "4 × 7 = |______" if SIMP else "______| = |___| × |___")
    frame(c, MARGIN + 250, y - 60, "7 × 4 = |______" if SIMP else "______| = |___| × |___")
    y -= 130
    y = text(c, y, "2.", [[("Karen says: If I know ", False), ("3 × 8 = 24", True), (", then I know ", False), ("8 × 3", True),
                          (". Show she is correct.", False)]])
    if SIMP:
        dots(c, MARGIN + 50, y - 10, 3, 8, gap=18)
        rich_line(c, MARGIN + 220, y - 26, [("3 rows of 8 = 8 rows of 3 (turn it!)", False)], 12)
        frame(c, MARGIN + 24, y - 80, "8 × 3 = |______")
    else:
        c.setStrokeColor(HexColor("#BBBBBB"))
        c.rect(MARGIN + 24, y - 160, W - 2 * MARGIN - 48, 150)
        c.setStrokeColor(black)
    footer(c, *L5, 31)


# ---------------------------------------------------------------- Lesson 6

def p33(c):
    y = start(c, "Lesson 6 Application Problem", "TEKS 3.4K", "3 sevens + 2 sevens = 5 sevens.")
    y = text(c, y, "", [[("Jocelyn says ", False), ("7 fives", True), (" is the same as ", False), ("3 sevens + 2 sevens", True),
                         (". Is she correct?", False)]])
    if SIMP:
        dots(c, MARGIN + 60, y - 10, 5, 7, gap=18)
        c.setLineWidth(2.5)
        c.line(MARGIN + 48, y - 10 - 2.5 * 18, MARGIN + 60 + 6 * 18 + 12, y - 10 - 2.5 * 18)
        c.setLineWidth(1)
        rich_line(c, MARGIN + 210, y - 24, [("top: 3 sevens", False)], 12)
        rich_line(c, MARGIN + 210, y - 80, [("bottom: 2 sevens", False)], 12)
        y -= 110
    frame(c, MARGIN + 24, y - 20, "7 × 5 = |______")
    frame(c, MARGIN + 24, y - 60, "3 × 7 = |______|      2 × 7 = |______")
    frame(c, MARGIN + 24, y - 100, "______|  +  |______|  =  |______")
    rich_line(c, MARGIN + 24, y - 140, [("Circle:  Jocelyn is  ", False), ("correct  /  not correct", True)], 14)
    read_draw_write(c)
    footer(c, *L6, 33)


def p35(c):
    y = start(c, "Lesson 6 Problem Set", "TEKS 3.4K", "Cut the array into 2 smaller arrays. Add their products.")
    y = text(c, y, "1.", [[("Break the ", False), ("8 × 6", True), (" array (8 rows of 6) into two smaller arrays.", False)]])
    grid(c, MARGIN + 30, y - 6, 8, 6, cell=15, split=5 if SIMP else None)
    if SIMP:
        rich_line(c, MARGIN + 130, y - 40, [("5 × 6", True)], 12)
        rich_line(c, MARGIN + 130, y - 100, [("3 × 6", True)], 12)
    chart(c, MARGIN + 170, y - 6, "8 × 6", 3 if SIMP else 7, first=("5 × 6 = 30", "3 × 6 = 18"))
    y -= 190
    if SIMP:
        frame(c, MARGIN + 24, y, "30 + 18 = |______|      so  8 × 6 = |______")
    else:
        y = text(c, y, "2.", [[("Break the ", False), ("6 × 8", True), (" array (6 rows of 8) into two smaller arrays.", False)]])
        grid(c, MARGIN + 30, y - 6, 6, 8, cell=15)
        chart(c, MARGIN + 170, y - 6, "6 × 8", 5)
    footer(c, *L6, 35)


def p36(c):
    y = start(c, "Lesson 6 Problem Set", "TEKS 3.4K", "6 groups = 5 groups + 1 more group.")
    y = text(c, y, "3.", [[("Use a number bond to show ", False), ("6 × 9", True), (".", False)]])
    bond(c, MARGIN + 110, y - 30, "6 × 9", ["5 × 9", "1 × 9"] if SIMP else ["", ""], r=26)
    frame(c, MARGIN + 260, y - 30, "5 × 9 = |______")
    frame(c, MARGIN + 260, y - 70, "1 × 9 = |______")
    frame(c, MARGIN + 260, y - 110, "6 × 9 = |______|  + |______|  = |______", size=13)
    y -= 160
    if not SIMP:
        y = text(c, y, "4.", [[("Break ", False), ("6 × 7", True), (" into two smaller facts.", False)]])
        frame(c, MARGIN + 24, y - 10, "a.  |___| × |___| = |___|      |___| × |___| = |___")
        frame(c, MARGIN + 24, y - 50, "b.  6 × 7 = |______")
        y -= 90
    y = text(c, y, "5.", [[("Use the first fact to find the second fact.", False)]])
    for k, s in enumerate(["a.  5 × 6 = 30, so 6 × 6 = |______", "b.  3 × 8 = 24, so 6 × 8 = |______",
                           "c.  7 × 5 = 35, so 7 × 6 = |______", "d.  5 × 9 = 45, so 6 × 9 = |______"]):
        frame(c, MARGIN + 24, y - 10 - k * 38, s, size=14)
    if SIMP:
        rich_line(c, MARGIN + 24, y - 166, [("Hint: one more group!  30 + 6, 24 + 24, 35 + 7, 45 + 9", False)], 11)
    footer(c, *L6, 36)


def p37(c):
    y = start(c, "Lesson 6 Problem Set", "TEKS 3.4K", "Cut the array into 2 smaller arrays. Add their products.")
    if not SIMP:
        y = text(c, y, "6.", [[("Break the ", False), ("9 × 6", True), (" array into two smaller arrays. Record the equations.", False)]])
        grid(c, MARGIN + 30, y - 6, 6, 9, cell=15)
        chart(c, MARGIN + 190, y - 6, "9 × 6", 8, rh=20)
        y -= 200
    y = text(c, y, "7.", [[("An author writes ", False), ("9", True), (" pages each week. How many pages in ", False),
                          ("6", True), (" weeks?", False)], [("Use a fives fact.", False)]])
    if SIMP:
        grid(c, MARGIN + 30, y - 6, 6, 9, cell=15, split=5)
        rich_line(c, MARGIN + 180, y - 40, [("5 × 9", True)], 12)
        rich_line(c, MARGIN + 180, y - 84, [("1 × 9", True)], 12)
        y -= 110
    frame(c, MARGIN + 24, y - 14, "5 × 9 = |______|      1 × 9 = |______")
    frame(c, MARGIN + 24, y - 54, "6 × 9 = |______|  + |______|  = |______|  pages")
    footer(c, *L6, 37)


def p39(c):
    y = start(c, "Lesson 6 Exit Ticket", "TEKS 3.4K", "Use a fives fact, then add the rest.")
    y = text(c, y, "1.", [[("Use a fives fact to solve ", False), ("7 × 6", True), (".", False)]])
    if SIMP:
        grid(c, MARGIN + 30, y - 6, 7, 6, cell=15, split=5)
        rich_line(c, MARGIN + 130, y - 40, [("5 × 6", True)], 12)
        rich_line(c, MARGIN + 130, y - 92, [("2 × 6", True)], 12)
    frame(c, MARGIN + 220, y - 20, "5 × 6 = |______")
    frame(c, MARGIN + 220, y - 60, "2 × 6 = |______")
    frame(c, MARGIN + 220, y - 100, "7 × 6 = |______|  + |______|  = |______", size=13)
    y -= 150
    y = text(c, y, "2.", [[("Use the first fact to find the second fact.", False)]])
    for k, s in enumerate(["a.  3 × 8 = 24, so 6 × 8 = |______", "b.  5 × 6 = 30, so 6 × 6 = |______",
                           "c.  9 × 5 = 45, so 9 × 6 = |______"]):
        frame(c, MARGIN + 24, y - 10 - k * 40, s, size=14)
    footer(c, *L6, 39)


# ---------------------------------------------------------------- Lesson 7

def p45(c):
    y = start(c, "Lesson 7 Application Problem", "TEKS 3.4K, 3.5B", "Share into equal groups: divide.")
    y = text(c, y, "", [[("24", True), (" people use canoes. ", False), ("3", True), (" people go in each canoe.", False)],
                        [("How many canoes are used?", False)]])
    if SIMP:
        for g in range(8):
            gx = MARGIN + 30 + g * 58
            c.roundRect(gx, y - 40, 50, 28, 8)
            dots(c, gx + 12, y - 26, 1, 3, gap=13, r=4)
        y -= 60
    frame(c, MARGIN + 24, y - 20, "24 ÷ 3 = |______|  canoes" if SIMP else "___| ÷ |___| = |______")
    read_draw_write(c)
    footer(c, *L7, 45)


EQS_47 = ["5 × 4 = □", "21 ÷ 3 = □", "24 ÷ □ = 4", "21 = □ × 7", "32 = □ × 8", "□ ÷ 10 = 7",
          "8 = 80 ÷ □", "24 ÷ □ = 12", "4 = 36 ÷ □", "35 = 7 × □", "8 = □ ÷ 3"]


def p47(c):
    y = start(c, "Lesson 7 Problem Set", "TEKS 3.4K", "The box □ is the missing number. Use a fact you know.")
    y = text(c, y, "1.", [[("Find the value of each unknown (□).", False)]])
    eqs = [EQS_47[i] for i in (0, 1, 2, 3, 5, 9)] if SIMP else EQS_47
    cw = (W - 2 * MARGIN) / 2
    for k, e in enumerate(eqs):
        x0, y0 = MARGIN + (k % 2) * cw, y - 20 - (k // 2) * (80 if SIMP else 62)
        rich_line(c, x0 + 10, y0, [(e, True)], 16)
        frame(c, x0 + 30, y0 - 28, "□ = |______", size=14)
    footer(c, *L7, 47)


def p48(c):
    y = start(c, "Lesson 7 Problem Set", "TEKS 3.4K, 3.4A", "Use □ for the number you do not know.")
    y = text(c, y, "2.", [[("Lonna buys ", False), ("3", True), (" t-shirts for ", False), ("$8", True), (" each.", False)]])
    if SIMP:
        bars(c, MARGIN + 80, y - 6, 240, [("", [("$8", 1, False)] * 3)], 3, h=26, brace=("□", 0, 3))
        y -= 80
    rich_line(c, MARGIN + 24, y - 10, [("a.  ", True), ("How much does she spend?", False)], 13)
    frame(c, MARGIN + 50, y - 50, "3 × 8 = □      □ = |______|  dollars" if SIMP else "______|  =  □      □ = |______")
    rich_line(c, MARGIN + 24, y - 100, [("b.  ", True), ("She pays with ", False), ("3 ten-dollar bills", True),
                                        (" ($30). How much change?", False)], 13)
    frame(c, MARGIN + 50, y - 140, "30 − |______|  = □      □ = |______|  dollars" if SIMP else "______|  =  □      □ = |______")
    footer(c, *L7, 48)


def p49(c):
    y = start(c, "Lesson 7 Problem Set", "TEKS 3.4K, 3.5B", "Use □ for the number you do not know.")
    y = text(c, y, "3.", [[("Miss Potts used ", False), ("28", True), (" cups of flour. Each loaf used ", False), ("4", True),
                          (" cups.", False)], [("How many loaves did she bake?", False)]])
    if SIMP:
        bars(c, MARGIN + 80, y - 6, 350, [("", [("4", 1, False)] * 7)], 7, h=26, brace=("28 cups", 0, 7))
        rich_line(c, MARGIN + 80, y - 82, [("How many 4s make 28?", False)], 11)
        y -= 100
    frame(c, MARGIN + 24, y - 14, "□ × 4 = 28" if SIMP else "___| × |___| = |______")
    frame(c, MARGIN + 24, y - 54, "28 ÷ 4 = □      □ = |______|  loaves" if SIMP else "___| ÷ |___| = |______")
    y -= 100
    if not SIMP:
        y = text(c, y, "4.", [[("Two games took ", False), ("32 minutes", True), (" in all. One game took ", False),
                              ("12 minutes longer", True), (".", False)], [("How long was each game?", False)]])
        bars(c, MARGIN + 90, y - 6, 300, [("Game 1", [("□", 10, False)]), ("Game 2", [("□", 10, False), ("12", 12, False)])],
             22, row_gap=34, h=26)
        frame(c, MARGIN + 24, y - 90, "32 − 12 = |______|      |______|  ÷ 2 = □")
        frame(c, MARGIN + 24, y - 130, "Game 1 = |______|  min      Game 2 = |______|  min")
    footer(c, *L7, 49)


def p51(c):
    y = start(c, "Lesson 7 Exit Ticket", "TEKS 3.4K, 3.5B", "The box □ is the missing number.")
    for k, e in enumerate(["□ = 5 × 9", "30 ÷ 6 = □", "8 × □ = 24", "□ ÷ 4 = 7"]):
        x0, y0 = MARGIN + (k % 2) * 260, y - (k // 2) * 80
        rich_line(c, x0, y0, [(f"{k + 1}.  ", True), (e, True)], 16)
        frame(c, x0 + 30, y0 - 30, "□ = |______", size=14)
    y -= 180
    y = text(c, y, "5.", [[("Mr. Strand waters roses for ", False), ("15 minutes", True), (". Each bush takes ", False),
                          ("3 minutes", True), (".", False)], [("How many bushes?", False)]])
    if SIMP:
        bars(c, MARGIN + 80, y - 6, 300, [("", [("3", 1, False)] * 5)], 5, h=26, brace=("15 minutes", 0, 5))
        y -= 70
    frame(c, MARGIN + 24, y - 14, "□ × 3 = 15" if SIMP else "___| × |___| = |______")
    frame(c, MARGIN + 24, y - 54, "15 ÷ 3 = □      □ = |______|  bushes" if SIMP else "___| ÷ |___| = |______")
    footer(c, *L7, 51)


PAGES = [p3, p5, p6, p7, p9, p11, p12, p13, p15, p16, p17, p19, p20, p21, p23, p25, p27, p28, p29, p31,
         p33, p35, p36, p37, p39, p45, p47, p48, p49, p51]


def build():
    global SIMP
    for simp, name in ((False, "Modified"), (True, "Simplified")):
        SIMP = simp
        main(f"G3_M3_L1-7_{name}.pdf", PAGES, f"Grade 3 Module 3 Lessons 1-7 – {name}")


if __name__ == "__main__":
    build()
