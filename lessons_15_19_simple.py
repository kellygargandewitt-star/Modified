"""Simplified Lessons 15-19 (book pages 103-131) for Grade 3 Module 2.

Lessons 15-19 teach rounding and estimating (TEKS 3.4B, a supporting standard).
This version keeps each page's story and numbers but turns the work into the
readiness skills underneath it:
  * 3.2A  place value  (43 = 4 tens 3 ones)
  * 3.2D  compare/order with <, >, = (often against the halfway number)
  * 3.4A  add/subtract exactly (estimates become exact answers)
1-4 problems per page, plain layout, book page numbers kept.

Run: python3 lessons_15_19_simple.py  ->  writes G3_M2_Lessons15-19_Simplified.pdf
"""
from reportlab.lib.colors import black

from build_module2 import MARGIN, W, footer, main, rich_line
from lessons_15_19 import L15, L16, L17, L18, L19
from reteach_mid_module import sentence
from topic_e_simple import column, start, strip, sum_grid, text, two_step

TIP_COMPARE = "Compare from the left. The open side of < or > faces the bigger number."
TIP_PLACE = "Each digit has a place: hundreds, tens, ones."


def hline(c, x0, x1, y, lo, hi, step, label_every):
    """Plain horizontal number line."""
    c.setLineWidth(1.5)
    c.line(x0 - 8, y, x1 + 8, y)
    c.setLineWidth(1)
    n = (hi - lo) // step
    for k in range(n + 1):
        v = lo + k * step
        tx = x0 + k * (x1 - x0) / n
        big = (v - lo) % label_every == 0
        c.line(tx, y - (7 if big else 4), tx, y + (7 if big else 4))
        if big:
            c.setFont("Sans", 10)
            c.drawCentredString(tx, y - 20, f"{v:,}")


def compare_line(c, x, y, a, b, size=22):
    """a  (  )  b with an empty circle for <, >, =."""
    sentence(c, x, y, f"{a:,}  |O|  {b:,}", size=size)


def compare_grid(c, y, items, bottom=80):
    """items: (label, a, b, line) where line is (lo, hi, step, label_every) or None."""
    cols = 1 if len(items) == 1 else 2
    rows = (len(items) + cols - 1) // cols
    cw, ch = (W - 2 * MARGIN) / cols, (y - bottom) / rows
    for i, (lbl, a, b, line) in enumerate(items):
        x0, y0 = MARGIN + (i % cols) * cw, y - (i // cols) * ch
        rich_line(c, x0 + 6, y0 - 24, [(f"{lbl}.", True)], 16)
        compare_line(c, x0 + 40, y0 - 26, a, b)
        if line:
            lo, hi, step, every = line
            hline(c, x0 + 20, x0 + cw - 30, y0 - 80, lo, hi, step, every)


def stacked(c, x, y, nums, size=22):
    """Numbers lined up by place so students can compare digit by digit."""
    width = max(len(f"{n:,}") for n in nums)
    for k, n in enumerate(nums):
        c.setFont("Sans", size)
        c.drawRightString(x + width * size * 0.62, y - k * (size + 8), f"{n:,}")


def place_rows(c, y, rows, x=None, gap=56, size=18):
    for s in rows:
        sentence(c, x or MARGIN + 24, y, s, size=size, blank_w=50, wide_w=80)
        y -= gap
    return y


def order_blanks(c, x, y, n=3, size=18):
    sentence(c, x, y, "  <  ".join(["______"] * n).replace("______", "|______|").strip("|"), size=size, wide_w=80)


# ---------------------------------------------------------------- Lesson 15

def page_103(c):
    y = start(c, "Lesson 15 Problem Set", "TEKS 3.2D", TIP_COMPARE)
    y = text(c, y, "1.", [[("A shoe is ", False), ("23 cm", True), (" long. A pencil is ", False), ("19 cm", True), (" long.", False)],
                          [("Which is longer? Compare.", False)]])
    stacked(c, MARGIN + 60, y - 30, [23, 19])
    compare_line(c, MARGIN + 220, y - 44, 23, 19)
    sentence(c, MARGIN + 24, y - 120, "The  |______|  is longer.", size=16)
    y -= 200
    y = text(c, y, "2.", [[("Bag A weighs ", False), ("8 oz", True), (". Bag B weighs ", False), ("14 oz", True), (".", False)],
                          [("Which is heavier? Compare.", False)]])
    stacked(c, MARGIN + 60, y - 30, [8, 14])
    compare_line(c, MARGIN + 220, y - 44, 8, 14)
    sentence(c, MARGIN + 24, y - 120, "Bag  |___|  is heavier.", size=16)
    footer(c, *L15, 103)


def page_104(c):
    y = start(c, "Lesson 15 Problem Set", "TEKS 3.2D, 3.4A", TIP_COMPARE)
    y = text(c, y, "3.", [[("Container A has ", False), ("33 mL", True), (". Container B has ", False), ("25 mL", True), (".", False)]])
    rich_line(c, MARGIN + 24, y - 20, [("a.  Compare.", False)], 14)
    compare_line(c, MARGIN + 60, y - 64, 33, 25)
    rich_line(c, MARGIN + 24, y - 140, [("b.  How much water in both?", False)], 14)
    sentence(c, MARGIN + 60, y - 184, "33 + 25 = |______|  mL", size=18, wide_w=80)
    column(c, W - MARGIN - 130, y - 150, [33, 25])
    footer(c, *L15, 104)


def page_105(c):
    y = start(c, "Lesson 15 Exit Ticket", "TEKS 3.2A, 3.2D", TIP_PLACE)
    y = text(c, y, "", [[("The beaker has ", False), ("43 mL", True), (" of water.", False)]])
    y -= 20
    rich_line(c, MARGIN, y, [("a.", True)], 16)
    sentence(c, MARGIN + 40, y, "43 = |___|  tens  |___|  ones", size=20, blank_w=50)
    y -= 90
    rich_line(c, MARGIN, y, [("b.", True), ("  Compare 43 to the halfway number, 45.", False)], 14)
    compare_line(c, MARGIN + 60, y - 50, 43, 45)
    hline(c, MARGIN + 40, W - MARGIN - 40, y - 110, 40, 50, 1, 1)
    footer(c, *L15, 105)


# ---------------------------------------------------------------- Lesson 16

def page_107(c):
    y = start(c, "Lesson 16 Application Problem", "TEKS 3.4A, 3.5A", "Make a ten first:  4 + 6 = 10")
    y = text(c, y, "", [[("3 groups dance: ", False), ("4 minutes", True), (", ", False), ("10 minutes", True), (", and ", False),
                         ("6 minutes", True), (".", False)],
                        [("How many minutes in all?", False)]])
    strip([("", [("4", 4, False), ("10", 10, False), ("6", 6, False)])], 20, brace=("?", 0, 20))(c, y - 14)
    y -= 130
    place_rows(c, y, ["4 + 6 = |______", "10 + 10 = |______|  minutes"])
    footer(c, *L16, 107)


def page_109(c):
    y = start(c, "Lesson 16 Problem Set", "TEKS 3.2D", "Is the number less than or greater than the halfway number?")
    y = text(c, y, "1.", [[("Compare each number to the halfway number. Use the number line.", False)]])
    compare_grid(c, y - 10, [("a", 32, 35, (30, 40, 1, 1)), ("b", 36, 35, (30, 40, 1, 1)),
                             ("c", 64, 65, (60, 70, 1, 1)), ("d", 17, 15, (10, 20, 1, 1))])
    footer(c, *L16, 109)


def page_110(c):
    y = start(c, "Lesson 16 Problem Set", "TEKS 3.2D, 3.4A", "Least = smallest.  Greatest = biggest.")
    y = text(c, y, "2.", [[("The animals weigh ", False), ("27", True), (", ", False), ("53", True), (", and ", False),
                          ("84", True), (" pounds.", False)],
                         [("Order them from least to greatest.", False)]])
    order_blanks(c, MARGIN + 30, y - 40)
    rich_line(c, MARGIN + 30, y - 66, [("least", False)], 11)
    rich_line(c, MARGIN + 330, y - 66, [("greatest", False)], 11)
    y -= 140
    y = text(c, y, "3.", [[("Mrs. Smith washes her car for ", False), ("22 minutes", True), (".", False)],
                          [("She weeds for ", False), ("15 minutes", True), (". How many minutes in all?", False)]])
    sentence(c, MARGIN + 30, y - 50, "22 + 15 = |______|  minutes", size=18, wide_w=80)
    column(c, W - MARGIN - 130, y - 10, [22, 15])
    footer(c, *L16, 110)


def page_111(c):
    y = start(c, "Lesson 16 Exit Ticket", "TEKS 3.2A, 3.2D", TIP_PLACE)
    y = text(c, y, "1.", [[("Write the place value.", False)]])
    y = place_rows(c, y - 30, ["a.   24 = |___|  tens  |___|  ones", "b.   137 = |___|  hundred  |___|  tens  |___|  ones"])
    y -= 20
    y = text(c, y, "2.", [[("Compare 42 to the halfway number, 45.", False)]])
    compare_line(c, MARGIN + 60, y - 40, 42, 45)
    hline(c, MARGIN + 40, W - MARGIN - 40, y - 100, 40, 50, 1, 1)
    footer(c, *L16, 111)


# ---------------------------------------------------------------- Lesson 17

def page_113(c):
    y = start(c, "Lesson 17 Application Problem", "TEKS 3.2A", "10 tens = 1 hundred.  10 hundreds = 1 thousand.")
    y = text(c, y, "", [[("Fill in the blanks.", False)]])
    place_rows(c, y - 30, ["a.   10 tens = |___|  hundred = |______",
                           "b.   12 tens = |___|  hundred  |___|  tens = |______",
                           "c.   12 hundreds = |___|  thousand  |___|  hundreds",
                           "       = |______"], gap=60, size=16)
    footer(c, *L17, 113)


def page_115(c):
    y = start(c, "Lesson 17 Problem Set", "TEKS 3.2D", "Is the number less than or greater than the halfway number?")
    y = text(c, y, "1.", [[("Compare each number to the halfway number. Use the number line.", False)]])
    compare_grid(c, y - 10, [("a", 143, 150, (100, 200, 10, 50)), ("b", 286, 250, (200, 300, 10, 50)),
                             ("c", 320, 350, (300, 400, 10, 50)), ("d", 470, 450, (400, 500, 10, 50))])
    footer(c, *L17, 115)


def page_116(c):
    y = start(c, "Lesson 17 Problem Set", "TEKS 3.2A, 3.2D", TIP_PLACE)
    y = text(c, y, "2.", [[("Write each number in expanded form.", False)]])
    y = place_rows(c, y - 30, ["a.   480 = |______|  +  |______", "b.   520 = |______|  +  |______"], gap=60)
    y -= 20
    y = text(c, y, "3.", [[("Order from least to greatest:   ", False), ("639     527     603", True)]])
    order_blanks(c, MARGIN + 30, y - 40)
    rich_line(c, MARGIN + 30, y - 66, [("least", False)], 11)
    rich_line(c, MARGIN + 330, y - 66, [("greatest", False)], 11)
    footer(c, *L17, 116)


def page_117(c):
    y = start(c, "Lesson 17 Exit Ticket", "TEKS 3.2A, 3.2D", TIP_COMPARE)
    y = text(c, y, "1.", [[("Compare to the halfway number.", False)]])
    compare_grid(c, y - 10, [("a", 137, 150, (100, 200, 10, 50)), ("b", 761, 750, (700, 800, 10, 50))], bottom=y - 150)
    y -= 190
    y = text(c, y, "2.", [[("There are ", False), ("685", True), (" people at a concert.", False)]])
    sentence(c, MARGIN + 30, y - 40, "685 = |___|  hundreds  |___|  tens  |___|  ones", size=16, blank_w=50)
    footer(c, *L17, 117)


# ---------------------------------------------------------------- Lesson 18

def page_121(c):
    y = start(c, "Lesson 18 Application Problem", "TEKS 3.2A, 3.2D", TIP_PLACE)
    y = text(c, y, "", [[("Look at the number ", False), ("345", True), (".", False)]])
    rich_line(c, MARGIN, y - 30, [("a.", True)], 16)
    sentence(c, MARGIN + 40, y - 30, "345 = |______|  +  |______|  +  |______", size=18, wide_w=70)
    rich_line(c, MARGIN, y - 130, [("b.", True), ("  Compare 345 to the halfway number, 350.", False)], 14)
    compare_line(c, MARGIN + 60, y - 180, 345, 350)
    hline(c, MARGIN + 40, W - MARGIN - 40, y - 240, 300, 400, 10, 50)
    footer(c, *L18, 121)


def page_123(c):
    y = start(c, "Lesson 18 Problem Set", "TEKS 3.2D", TIP_COMPARE)
    y = text(c, y, "1.", [[("Compare. Line up the digits and look from the left.", False)]])
    items = [("a", 2143, 2150), ("b", 2886, 2885), ("c", 959, 950), ("d", 1627, 1625)]
    cw, ch = (W - 2 * MARGIN) / 2, (y - 90) / 2
    for i, (lbl, a, b) in enumerate(items):
        x0, y0 = MARGIN + (i % 2) * cw, y - 10 - (i // 2) * ch
        rich_line(c, x0 + 6, y0 - 24, [(f"{lbl}.", True)], 16)
        stacked(c, x0 + 50, y0 - 30, [a, b], size=20)
        compare_line(c, x0 + 40, y0 - 130, a, b, size=20)
    footer(c, *L18, 123)


def page_124(c):
    y = start(c, "Lesson 18 Problem Set", "TEKS 3.2A, 3.2D", TIP_COMPARE)
    y = text(c, y, "2.", [[("Order from least to greatest:   ", False), ("7,530     7,472     7,499", True)]])
    order_blanks(c, MARGIN + 30, y - 40)
    y -= 110
    y = text(c, y, "3.", [[("Jayden's family drove ", False), ("759", True), (" miles. Jordan's family drove ", False),
                          ("882", True), (" miles.", False)],
                         [("Compare. Who drove more?", False)]])
    compare_line(c, MARGIN + 60, y - 40, 759, 882)
    sentence(c, MARGIN + 260, y - 40, "|______|  drove more.", size=14)
    y -= 110
    y = text(c, y, "4.", [[("Write ", False), ("452", True), (" in expanded form.", False)]])
    sentence(c, MARGIN + 30, y - 40, "452 = |______|  +  |______|  +  |______", size=18, wide_w=70)
    footer(c, *L18, 124)


def page_125(c):
    y = start(c, "Lesson 18 Exit Ticket", "TEKS 3.2A, 3.2D", TIP_PLACE)
    y = text(c, y, "1.", [[("Write the place value.", False)]])
    sentence(c, MARGIN + 30, y - 30, "137 = |___|  hundred  |___|  tens  |___|  ones", size=16, blank_w=50)
    y -= 90
    y = text(c, y, "2.", [[("Compare 560 to the halfway number, 550.", False)]])
    compare_line(c, MARGIN + 60, y - 40, 560, 550)
    hline(c, MARGIN + 40, W - MARGIN - 40, y - 100, 500, 600, 10, 50)
    y -= 150
    y = text(c, y, "3.", [[("A stadium cooked ", False), ("583", True), (" hot dogs. Write 583 in expanded form.", False)]])
    sentence(c, MARGIN + 30, y - 40, "583 = |______|  +  |______|  +  |______", size=18, wide_w=70)
    footer(c, *L18, 125)


# ---------------------------------------------------------------- Lesson 19 (estimates become exact answers)

def page_127(c):
    two_step(c, 127, L19, "Lesson 19 Application Problem", "",
             [[("Matt turns in ", False), ("52", True), (", ", False), ("31", True), (", and ", False), ("48", True),
               (" pounds of metal.", False)],
              [("How many pounds in all?", False)]],
             strip([("", [("52", 52, False), ("31", 31, False), ("48", 48, False)])], 131, brace=("?", 0, 131)),
             "52 + 48 = |______", "______| + 31 = |______|  pounds", [52, 48], [None, 31],
             tip="Add 52 + 48 first. It makes 100!")


def page_129(c):
    two_step(c, 129, L19, "Lesson 19 Problem Set", "1.",
             [[("Sam buys a chair for ", False), ("$320", True), (", a table for ", False), ("$180", True), (",", False)],
              [("and a lamp for ", False), ("$110", True), (". How much in all?", False)]],
             strip([("", [("320", 320, False), ("180", 180, False), ("110", 110, False)])], 610, brace=("?", 0, 610)),
             "320 + 180 = |______", "______| + 110 = |______|  dollars", [320, 180], [None, 110],
             tip="Add 320 + 180 first. It makes 500!")


def page_130(c):
    y = start(c, "Lesson 19 Problem Set", "TEKS 3.4A", "Add or subtract the ones first.")
    y = text(c, y, "2.", [[("Find the exact answer.", False)]])
    sum_grid(c, y - 10, [("a", 39, 21, "+"), ("b", 98, 41, "+"), ("c", 52, 19, "−"), ("d", 81, 30, "−")])
    footer(c, *L19, 130)


def page_131(c):
    y = start(c, "Lesson 19 Exit Ticket", "TEKS 3.4A", "Add or subtract the ones first.")
    y = text(c, y, "", [[("Find the exact answer.", False)]])
    sum_grid(c, y - 10, [("1", 73, 24, "+"), ("2", 61, 29, "−")], bottom=y - 220)
    footer(c, *L19, 131)


BOOK = {103: page_103, 104: page_104, 105: page_105, 107: page_107, 109: page_109, 110: page_110,
        111: page_111, 113: page_113, 115: page_115, 116: page_116, 117: page_117, 121: page_121,
        123: page_123, 124: page_124, 125: page_125, 127: page_127, 129: page_129, 130: page_130,
        131: page_131}

if __name__ == "__main__":
    main("G3_M2_Lessons15-19_Simplified.pdf", [BOOK[k] for k in sorted(BOOK)],
         "Bluebonnet Learning Grade 3 Module 2 Lessons 15-19 – Simplified")
