"""Grade 3 Module 3 Topic A TEKS Progress Check (6 questions) with visuals and supports.

Same questions, numbers, and answer choices in the same order (A-D added only so
students can point to a choice on paper). Supports: simpler words, strip
diagrams, In/Out frames, place value jumps, one short helper line per question.

Run: python3 mod3_topicA_check_supported.py  ->  writes G3_M3_TopicA_Check_Supported.pdf
"""
from reportlab.lib.colors import HexColor, black

from build_module2 import MARGIN, W, blank, footer, header, main, rich_line
from end_of_module_accommodated import answer_line, table
from end_of_module_modified import choices, q
from lessons_20_24 import bars, top_brace
from reteach_mid_module import sentence

GREY = HexColor("#666666")
TITLE = "Topic A Progress Check"
FOOT = ("Module 3, Topic A:", "Progress Check (with supports)")


def start(c):
    return header(c, TITLE, suffix=" (Supported)", unit="3 • 3") - 20


def helper(c, x, y, parts, size=12):
    rich_line(c, x, y, [("Helper: ", True)] + parts, size)


# ---------------------------------------------------------------- 1-2

def page_1(c):
    y = start(c)
    y = q(c, y, "1", [[("The yellow strip is ", False), ("9 units", True), (" long.", False)],
                      [("The red strip is ", False), ("3 times as long", True), (" as the yellow strip.", False)],
                      [("Which equation (number sentence) finds the length of the red strip?", False)]])
    bars(c, MARGIN + 80, y - 10, 300, [("Yellow", [("9", 9, False)]),
                                        ("Red", [("9", 9, False), ("9", 9, False), ("9", 9, False)])], 27,
         row_gap=34, h=26, brace=("?", 0, 27))
    helper(c, MARGIN + 26, y - 124, [("\"3 times as long\" = 3 strips of 9.", False)])
    choices(c, MARGIN + 30, y - 160, [("A", "9 ÷ 3 = 3"), ("B", "9 − 3 = 6"), ("C", "9 + 3 = 12"), ("D", "9 × 3 = 27")],
            gap=26)

    footer(c, *FOOT, 1)


def page_1b(c):
    y = start(c)
    y = q(c, y, "2", [[("The blue strip is ", False), ("9 centimeters", True), (" long.", False)],
                      [("9 × 4", True), (" finds the length of the red strip. Which sentence is true?", False)]])
    bars(c, MARGIN + 80, y - 10, 360, [("Blue", [("9", 9, False)]),
                                        ("Red", [("9", 9, False)] * 4)], 36, row_gap=34, h=26)
    helper(c, MARGIN + 26, y - 90, [("9 × 4 means ", False), ("4 strips of 9", True), (".", False)])
    choices(c, MARGIN + 30, y - 120, [
        ("A", "The red strip is 9 times as long as the blue strip."),
        ("B", "The red strip is 4 times as long as the blue strip."),
        ("C", "The blue strip is 4 times as long as the red strip."),
        ("D", "The blue strip is 9 times as long as the red strip.")], gap=26, size=13)
    footer(c, *FOOT, 2)


# ---------------------------------------------------------------- 3

def numbered_box(c, x, y, w, h, n):
    c.rect(x, y - h, w, h)
    c.setFillColor(HexColor("#555555"))
    c.rect(x + 3, y - 15, 13, 12, stroke=0, fill=1)
    c.setFillColor(HexColor("#FFFFFF"))
    c.setFont("Sans-Bold", 8)
    c.drawCentredString(x + 9.5, y - 12.5, str(n))
    c.setFillColor(black)


def page_2(c):
    y = start(c)
    y = q(c, y, "3", [[("Jin has ", False), ("8", True), (" baseball cards.", False)],
                      [("Toni has ", False), ("3 times as many", True), (" cards as Jin.", False)],
                      [("How many cards does Toni have? Fill in the strip diagram.", False)]])
    rich_line(c, MARGIN + 26, y - 6, [("Word bank:", True), ("    Toni     Jin     3     8     11     23     24     33", False)], 13)
    y -= 50
    bw, bh, nx, x0 = 90, 40, 100, MARGIN + 160
    # row 1: name box 1, one part box 3
    numbered_box(c, MARGIN + 40, y, nx, bh, 1)
    numbered_box(c, x0, y, bw, bh, 3)
    # row 2: name box 2, three parts 4-6
    y2 = y - 60
    numbered_box(c, MARGIN + 40, y2, nx, bh, 2)
    for k in range(3):
        numbered_box(c, x0 + k * bw, y2, bw, bh, 4 + k)
    top_y = y2 - bh - 6
    c.line(x0, top_y, x0, top_y - 6)
    c.line(x0 + 3 * bw, top_y, x0 + 3 * bw, top_y - 6)
    c.line(x0, top_y - 6, x0 + 3 * bw, top_y - 6)
    c.setFont("Sans-Bold", 14)
    c.drawCentredString(x0 + 1.5 * bw, top_y - 24, "?")

    y = top_y - 60
    helper(c, MARGIN + 26, y, [("Jin's bar is ", False), ("1", True), (" part. Toni's bar is ", False), ("3", True),
                               (" parts. Every part is the ", False), ("same size", True), (".", False)])
    y -= 40
    for n, what in ((1, "Box 1 (name):"), (2, "Box 2 (name):"), (3, "Box 3:"), (4, "Boxes 4, 5, 6:")):
        rich_line(c, MARGIN + 40, y, [(what, False)], 13)
        blank(c, MARGIN + 180, y, 120)
        y -= 32
    y -= 6
    answer_line(c, MARGIN + 40, y, "Toni has", "cards  (the ? )", w=70)
    footer(c, *FOOT, 3)


# ---------------------------------------------------------------- 4

def page_3(c):
    y = start(c)
    y = q(c, y, "4", [[("A number machine changes numbers. ", False), ("In", True), (" goes in. ", False),
                       ("Out", True), (" comes out.", False)],
                      [("How is the Out number related to the In number?", False)]])
    ty = table(c, MARGIN + 40, y - 6, ["In", "Out"], [["3", "12"], ["5", "20"], ["7", "28"], ["9", "36"]], [80, 80], rh=30)
    helper(c, MARGIN + 240, y - 20, [("Look at each row:", False)], 13)
    ry = y - 50
    for a, b in ((3, 12), (5, 20), (7, 28), (9, 36)):
        sentence(c, MARGIN + 250, ry, f"{a} × |___|  =  {b}", size=15, blank_w=50)
        ry -= 32
    y = min(ty, ry) - 40
    rich_line(c, MARGIN + 26, y, [("Finish the sentence:", True)], 13)
    y -= 34
    rich_line(c, MARGIN + 26, y, [("The number that comes out of the machine is", False)], 14)
    y -= 30
    x = blank(c, MARGIN + 26, y, 60)
    rich_line(c, x + 8, y, [("times as many", True), (" as the number that goes into the machine.", False)], 14)
    footer(c, *FOOT, 4)


# ---------------------------------------------------------------- 5

def page_4(c):
    y = start(c)
    y = q(c, y, "5", [[("Mario makes ", False), ("3", True), (" batches of oatmeal cookies", False)],
                      [("for every ", False), ("9", True), (" batches of chocolate cookies.", False)],
                      [("Which table shows this?", False)]])
    helper(c, MARGIN + 26, y - 2, [("Find 3 in the ", False), ("Oatmeal", True), (" column. Is ", False), ("9", True),
                                   (" next to it in the ", False), ("Chocolate", True), (" column?", False)])
    tables = [("A", [(2, 6), (3, 9), (6, 18), (9, 27)]), ("B", [(6, 2), (9, 3), (18, 6), (27, 9)]),
              ("C", [(1, 4), (3, 6), (5, 8), (7, 10)]), ("D", [(2, 11), (3, 12), (6, 15), (9, 18)])]
    cw = (W - 2 * MARGIN) / 2
    for i, (letter, rows) in enumerate(tables):
        x0, y0 = MARGIN + (i % 2) * cw, y - 40 - (i // 2) * 230
        rich_line(c, x0 + 6, y0 - 4, [(letter, True)], 16)
        table(c, x0 + 30, y0 + 10, ["Oatmeal", "Chocolate"], [[str(a), str(b)] for a, b in rows], [95, 95], rh=26)
        rich_line(c, x0 + 30, y0 - 136, [("3 oatmeal → ", False)], 12)
        blank(c, x0 + 115, y0 - 136, 40)
        rich_line(c, x0 + 160, y0 - 136, [("chocolate", False)], 12)
    footer(c, *FOOT, 5)


# ---------------------------------------------------------------- 6

def page_5(c):
    y = start(c)
    y = q(c, y, "6", [[("Look at the number ", False), ("36,476", True), (".", False)],
                      [("How many times greater is the ", False), ("thousands", True), (" place than the ", False),
                       ("ones", True), (" place?", False)]])
    places = ["Ten Thousands", "Thousands", "Hundreds", "Tens", "Ones"]
    digits = "36476"
    cw, x0, by = 92, MARGIN + 20, y - 110
    for k, (p, d) in enumerate(zip(places, digits)):
        c.rect(x0 + k * cw + 4, by, cw - 8, 44)
        c.setFont("Sans", 9)
        c.drawCentredString(x0 + k * cw + cw / 2, by + 32, p)
        c.setFont("Sans-Bold", 18)
        c.drawCentredString(x0 + k * cw + cw / 2, by + 8, d)
    # x10 jumps from Ones back to Thousands
    for k in (3, 2, 1):
        xa = x0 + (k + 1) * cw + cw / 2
        xb = x0 + k * cw + cw / 2
        c.arc(xb, by + 30, xa, by + 80, 0, 180)
        c.line(xb, by + 55, xb - 4, by + 62)
        c.line(xb, by + 55, xb + 5, by + 61)
        c.setFont("Sans-Bold", 11)
        c.drawCentredString((xa + xb) / 2, by + 84, "× 10")
    y = by - 30
    helper(c, MARGIN + 26, y, [("Each jump to the left is ", False), ("× 10", True), (". Count the jumps from ones to thousands.", False)])
    y -= 36
    sentence(c, MARGIN + 40, y, "Jumps:  |___|       10 × 10 × 10 = |______", size=15, blank_w=50, wide_w=80)
    y -= 46
    choices(c, MARGIN + 30, y, [
        ("A", "The thousands place is three times greater than the ones place."),
        ("B", "The thousands place is one hundred times greater than the ones place."),
        ("C", "The thousands place is one thousand times greater than the ones place."),
        ("D", "The thousands place is six times greater than the ones place.")], gap=28, size=12.5)
    footer(c, *FOOT, 6)


PAGES = [page_1, page_1b, page_2, page_3, page_4, page_5]

if __name__ == "__main__":
    main("G3_M3_TopicA_Check_Supported.pdf", PAGES, "Grade 3 Module 3 Topic A Progress Check – Supported")
