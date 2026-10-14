"""Reteach for the Grade 3 Module 2 Topic C TEKS Progress Check (5 questions, 3 pages).

Same order as the progress check. Each page starts with a "Let's Learn" worked
example, then the question with friendlier numbers and the steps set up.

Run: python3 reteach_topic_c_check.py  ->  writes G3_M2_TopicC_Check_Reteach.pdf
"""
from reportlab.lib.colors import HexColor, black

from build_module2 import (
    LIGHT, MARGIN, W, blank, footer, header, helper_box, main, pv_chart, rich_line, teks,
)
from reteach_mid_module import (
    GREY, LEARN_BG, LEARN_LINE, PLACES, compare_circle, digit_chart, learn_box, sentence,
)

TITLE = "Topic C Progress Check Reteach"
FOOT = ("Module 2, Topic C:", "Place value, expanded form, and comparing and ordering numbers")


def start(c, teks_label):
    y = header(c, TITLE, suffix="")
    teks(c, y, teks_label)
    return y


def choice_rows(c, x, y, choices, letters="ABCD", gap=26, size=13):
    for k, ch in enumerate(choices):
        rich_line(c, x, y, [(letters[k] + "     ", True), (ch, False)], size)
        y -= gap
    return y


def page_1a(c):
    """Q1: Which choices are equivalent to 10,649? (select three)"""
    y = start(c, "TEKS 3.2A")
    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", [
        [("equivalent", True), (" = the ", False), ("same value", True)],
        [("(2 × 1,000)", True), (" = 2,000       ", False), ("3 hundreds", True), (" = 300       ", False),
         ("4 tens", True), (" = 40", False)],
    ])
    y -= 10
    top = y
    y = learn_box(c, y, [[("", False)]] * 4)
    digit_chart(c, MARGIN + 16, top - 30, "1234")
    ty = top - 42
    for parts in (
        [("1,234", True), ("  =  (1 × 1,000) + (2 × 100) + (3 × 10) + (4 × 1)", False)],
        [("1,234", True), ("  =  1,000 + 200 + 30 + 4", False)],
        [("1,234", True), ("  =  1 thousand 2 hundreds 3 tens 4 ones", False)],
        [("All three show the ", False), ("same value", True), (".", False)],
    ):
        rich_line(c, MARGIN + 190, ty, parts, 11)
        ty -= 18

    y -= 26
    rich_line(c, MARGIN, y, [("1. ", True), ("Which choices are equal to ", False), ("2,345", True), ("?", False)], 14)
    y -= 20
    rich_line(c, MARGIN + 24, y, [("Find the value of each one. Then circle ", False), ("yes", True),
                                  (" or ", False), ("no", True), (". There are ", False), ("3", True),
                                  (" yes answers.", False)], 11.5)
    y -= 14
    rows = [
        "(2 × 1,000) + (3 × 100) + (4 × 10) + (5 × 1)",
        "two thousand, five hundred forty-three",
        "2,000 + 340 + 5",
        "2 thousands 3 hundreds 4 tens 5 ones",
        "3 thousands 2 hundreds 4 tens 5 ones",
        "2,000 + 300 + 5",
    ]
    rh = 46
    cols = [300, 110]
    c.setFillColor(LIGHT)
    c.rect(MARGIN, y - 22, W - 2 * MARGIN, 22, stroke=0, fill=1)
    c.setFillColor(black)
    c.setFont("Sans-Bold", 10.5)
    c.drawCentredString(MARGIN + cols[0] / 2, y - 15, "Choice")
    c.drawCentredString(MARGIN + cols[0] + cols[1] / 2, y - 15, "Value")
    c.drawCentredString(MARGIN + cols[0] + cols[1] + (W - 2 * MARGIN - sum(cols)) / 2, y - 15, "Same as 2,345?")
    y -= 22
    bottom = y - rh * len(rows)
    c.rect(MARGIN, bottom, W - 2 * MARGIN, y - bottom + 22)
    c.line(MARGIN + cols[0], y + 22, MARGIN + cols[0], bottom)
    c.line(MARGIN + sum(cols), y + 22, MARGIN + sum(cols), bottom)
    for k, text in enumerate(rows):
        ry = y - k * rh
        c.line(MARGIN, ry, W - MARGIN, ry)
        rich_line(c, MARGIN + 8, ry - 28, [("ABCDEF"[k] + "   ", True), (text, False)], 11)
        blank(c, MARGIN + cols[0] + 15, ry - 28, 80)
        rich_line(c, MARGIN + sum(cols) + 28, ry - 28, [("yes      no", True)], 13)

    footer(c, *FOOT, "1 (part 1)")


def page_1b(c):
    """Q2: relationship between the thousands place and the tens place in 55,394."""
    y = start(c, "TEKS 3.2B")
    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", [
        [("Each place is ", False), ("10 times", True), (" the place to its right.", False)],
        [("1 jump", True), (" = 10 times          ", False), ("2 jumps", True), (" = 10 × 10 = ", False),
         ("100 times", True)],
    ])
    y -= 10
    top = y
    y = learn_box(c, y, [[("", False)]] * 6)
    # place chart with x10 jumps from Ones to Thousands
    cw = 82
    x0 = MARGIN + 40
    by = top - 118
    for k, p in enumerate(PLACES):
        c.rect(x0 + k * cw, by, cw - 8, 30)
        c.setFont("Sans-Bold", 10)
        c.drawCentredString(x0 + k * cw + (cw - 8) / 2, by + 11, p)
    for k in range(3):
        xa = x0 + (k + 1) * cw + (cw - 8) / 2
        xb = x0 + k * cw + (cw - 8) / 2
        c.setStrokeColor(LEARN_LINE)
        c.setLineWidth(1.5)
        c.arc(xb, by + 18, xa, by + 70, 0, 180)
        c.line(xb, by + 44, xb - 4, by + 51)
        c.line(xb, by + 44, xb + 5, by + 50)
        c.setLineWidth(1)
        c.setStrokeColor(black)
        c.setFillColor(LEARN_LINE)
        c.setFont("Sans-Bold", 11)
        c.drawCentredString((xa + xb) / 2, by + 74, "× 10")
        c.setFillColor(black)
    rich_line(c, x0 + 4 * cw + 6, by + 40, [("Tens → Hundreds:", False)], 10)
    rich_line(c, x0 + 4 * cw + 6, by + 24, [("1 jump = ", False), ("10 times", True)], 10)

    y -= 28
    rich_line(c, MARGIN, y, [("2. ", True), ("Look at the number ", False), ("4,382", True), (".", False)], 14)
    y -= 22
    rich_line(c, MARGIN + 24, y, [("How many times greater is the ", False), ("thousands", True),
                                  (" place than the ", False), ("tens", True), (" place?", False)], 13)
    y -= 16
    digit_chart(c, MARGIN + 24, y, "4382", cw=60)
    rich_line(c, MARGIN + 24 + 260, y - 30, [("Draw the jumps from ", False), ("Tens", True),
                                             (" to ", False), ("Thousands", True), (".", False)], 11)

    y -= 80
    rich_line(c, MARGIN + 10, y, [("Step 1:", False)], 11)
    sentence(c, MARGIN + 70, y, "Number of jumps from tens to thousands:  |___", size=13)
    y -= 36
    rich_line(c, MARGIN + 10, y, [("Step 2:", False)], 11)
    sentence(c, MARGIN + 70, y, "10 × 10 = |______", size=14)
    y -= 40
    rich_line(c, MARGIN + 10, y, [("Step 3:  Circle the letter that matches.", True)], 12)
    y -= 28
    choice_rows(c, MARGIN + 30, y, [
        "The thousands place is two times greater than the tens place.",
        "The thousands place is ten times greater than the tens place.",
        "The thousands place is one hundred times greater than the tens place.",
        "The thousands place is one thousand times greater than the tens place.",
    ], size=11.5, gap=26)

    footer(c, *FOOT, "1 (part 2)")


def page_2(c):
    """Q3: 3 ten thousands + 24 thousands in standard form (54,000)."""
    y = start(c, "TEKS 3.2A")
    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", [
        [("standard form", True), (" = the number written with digits, like ", False), ("4,200", True)],
        [("10 hundreds", True), (" = 1 thousand", False)],
    ])
    y -= 10
    y = learn_box(c, y, [
        [("2 thousands + 15 hundreds", True)],
        [("2 thousands = ", False), ("2,000", True), ("       15 hundreds = ", False), ("1,500", True),
         ("   (15 × 100)", False)],
        [("2,000 + 1,500 = ", False), ("3,500", True)],
    ])

    y -= 30
    rich_line(c, MARGIN, y, [("3. ", True), ("Write the sum in ", False), ("standard form", True), (".", False)], 14)
    y -= 40
    c.setFont("Sans-Bold", 22)
    c.drawCentredString(W / 2, y, "3 thousands  +  12 hundreds")

    y -= 30
    hundreds = 12
    # hundreds hint: draw 12 hundred-disks split 10 + 2
    x = MARGIN + 60
    for k in range(hundreds):
        cx = x + k * 30 + (16 if k >= 10 else 0)
        c.circle(cx, y - 14, 12)
        c.setFont("Sans", 8)
        c.drawCentredString(cx, y - 17, "100")
    c.setStrokeColor(LEARN_LINE)
    c.setLineWidth(1.5)
    c.roundRect(x - 16, y - 32, 10 * 30 + 2, 36, 10)
    c.setLineWidth(1)
    c.setStrokeColor(black)
    c.setFont("Sans", 9.5)
    c.setFillColor(LEARN_LINE)
    c.drawCentredString(x - 16 + 151, y - 46, "10 hundreds = 1 thousand")
    c.setFillColor(black)

    y -= 84
    rich_line(c, MARGIN + 10, y, [("Step 1:", False)], 11)
    sentence(c, MARGIN + 70, y, "3 thousands = |______", size=15)
    y -= 42
    rich_line(c, MARGIN + 10, y, [("Step 2:", False)], 11)
    sentence(c, MARGIN + 70, y, "12 hundreds = |______", size=15)
    y -= 42
    rich_line(c, MARGIN + 10, y, [("Step 3:", False)], 11)
    sentence(c, MARGIN + 70, y, "______|  +  |______|  =  |______", size=15)

    y -= 48
    rich_line(c, MARGIN + 10, y, [("Step 4:  Circle the letter that matches.", True)], 13)
    y -= 32
    for k, ch in enumerate(["1,500", "3,120", "4,200", "15,000"]):
        rich_line(c, MARGIN + 30 + k * 120, y, [("ABCD"[k] + "   ", True), (ch, False)], 15)

    footer(c, *FOOT, "2")


def page_3(c):
    """Q4: order 12,914 13,278 12,184 12,466 least to greatest.  Q5: 25,928 ? 25,711."""
    y = start(c, "TEKS 3.2D")
    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", [
        [("least", True), (" = smallest      ", False), ("greatest", True), (" = biggest      ", False),
         (">", True), (" greater than      ", False), ("<", True), (" less than", False)],
        [("Compare from the ", False), ("left", True), (". If the digits are the same, move to the next place.", False)],
    ])

    y -= 26
    rich_line(c, MARGIN, y, [("4. ", True), ("Friends counted their steps. Order the steps from ", False),
                             ("least", True), (" to ", False), ("greatest", True), (".", False)], 12)
    y -= 12
    names = ["Lea", "Kim", "Tyrell", "Hosni"]
    nums = [2914, 3278, 2184, 2466]
    cx = MARGIN + 50
    c.setFont("Sans-Bold", 10)
    c.drawCentredString(cx, y - 14 - 12, "Friend")
    for k, n in enumerate(names):
        c.setFont("Sans", 12)
        c.drawCentredString(cx, y - 34 - 32 * k - 22, n)
    bottom = pv_chart(c, MARGIN + 100, y, 230, PLACES, nums, shade=1)
    tips = [
        [("Step 1: ", True), ("Thousands. Who has 3?", False)],
        [("That one is ", False), ("greatest", True), (".", False)],
        [("Step 2: ", True), ("The rest have 2 thousands.", False)],
        [("Look at the ", False), ("yellow", True), (" hundreds.", False)],
    ]
    ty = y - 30
    for parts in tips:
        rich_line(c, MARGIN + 345, ty, parts, 10.5)
        ty -= 20

    y = bottom - 30
    bw, gap = 92, 26
    x = MARGIN + 20
    for k in range(4):
        c.rect(x, y - 30, bw, 34)
        if k < 3:
            c.setFont("Sans-Bold", 18)
            c.drawCentredString(x + bw + gap / 2, y - 18, "<")
        x += bw + gap
    c.setFont("Sans", 10)
    c.drawString(MARGIN + 20, y - 46, "Least")
    c.drawRightString(x - gap, y - 46, "Greatest")

    y -= 78
    c.line(MARGIN, y + 14, W - MARGIN, y + 14)
    y -= 10
    rich_line(c, MARGIN, y, [("5. ", True), ("Compare. Write ", False), (">", True), (", ", False), ("<", True),
                             (", or ", False), ("=", True), (" in the circle.", False)], 12)
    y -= 12
    pv_chart(c, MARGIN + 20, y, 200, PLACES, [5928, 5711], shade=None)
    ty = y - 22
    for parts in (
        [("Thousands: ", False), ("5", True), (" and ", False), ("5", True), ("  same? ", False), ("yes  /  no", True)],
        [("Hundreds: ", False), ("9", True), (" and ", False), ("7", True), ("  same? ", False), ("yes  /  no", True)],
        [("Which is bigger?  9  or  7", False)],
    ):
        rich_line(c, MARGIN + 240, ty, parts, 11)
        ty -= 22
    sentence(c, MARGIN + 240, ty - 20, "5,928  |O|  5,711", size=18)

    footer(c, *FOOT, "3")


PAGES = [page_1a, page_1b, page_2, page_3]

if __name__ == "__main__":
    main("G3_M2_TopicC_Check_Reteach.pdf", PAGES, "Grade 3 Module 2 – Topic C Progress Check Reteach")
