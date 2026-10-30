"""Grade 3 Module 3 Topic A TEKS Progress Check - MODIFIED (paper) + COMPUTER HELPER SHEET.

Built with modified_test_kit.py rules: one question per page, big print, short lines,
one picture that shows the math, one "Do this" step.
  PAPER  - 3 answer choices (most obviously wrong one removed), same numbers.
  HELPER - same pictures, all 4 computer choices in the computer's order (1st-4th),
           for students answering on the computer.

Run: python3 mod3_topicA_modified.py
  -> G3_M3_TopicA_Check_Modified.pdf, G3_M3_TopicA_Check_Helper.pdf
"""
from reportlab.lib.colors import HexColor, black

from build_module2 import MARGIN, W, footer, header, main, rich_line
from modified_test_kit import (INK, SOFT, answer_line, ask, brace_under, choice_boxes, dot_groups, step, strip)

MODE = "paper"
TAN, CHOC = HexColor("#E3C48F"), HexColor("#6B4A2F")
ORD = ["1st", "2nd", "3rd", "4th"]


def start(c):
    suffix = " (Modified)" if MODE == "paper" else " (Computer Helper)"
    return header(c, "Topic A Progress Check", suffix=suffix, unit="3 • 3") - 40


def foot(c, n):
    footer(c, "Module 3, Topic A:", "Progress Check (Modified)" if MODE == "paper" else "Computer Helper Sheet", n)


def pick(c, y, paper, computer, helper_size=99, **kw):
    """paper: [(letter, text)] (3 choices); computer: [text] (all 4, computer order)."""
    if MODE == "paper":
        return choice_boxes(c, y, paper, **kw)
    rich_line(c, MARGIN, y + 4, [("On the computer, the choices are in this order:", False)], 13)
    return choice_boxes(c, y - 14, list(zip(ORD, computer)), size=min(kw.get("size", 16) - 2, helper_size),
                        h=36, gap=10)


# ---------------------------------------------------------------- 1

def q1(c):
    y = start(c)
    y = ask(c, y, 1, [[("Yellow strip: ", False), ("9 units", True)],
                      [("Red strip: ", False), ("3 times as long", True)],
                      [("Which number sentence finds the red strip?", False)]])
    x = MARGIN + 60
    strip(c, x, y - 6, "Yellow", ["9"], 90, "yellow")
    end = strip(c, x, y - 50, "Red", ["9", "9", "9"], 90, "red")
    brace_under(c, x + 70, end, y - 86, "?")
    y = step(c, y - 150, [("3 times as long", True), (" = 3 strips of 9.", False)])
    pick(c, y, [("A", "9 ÷ 3 = 3"), ("B", "9 + 3 = 12"), ("C", "9 × 3 = 27")],
         ["9 ÷ 3 = 3", "9 − 3 = 6", "9 + 3 = 12", "9 × 3 = 27"], size=20)
    foot(c, 1)


# ---------------------------------------------------------------- 2

def q2(c):
    y = start(c)
    y = ask(c, y, 2, [[("Blue strip: ", False), ("9 cm", True)],
                      [("Red strip: ", False), ("9 × 4", True)],
                      [("Which is true?", False)]])
    x = MARGIN + 40
    strip(c, x, y - 6, "Blue", ["9"], 80, "blue")
    strip(c, x, y - 50, "Red", ["9", "9", "9", "9"], 80, "red")
    y = step(c, y - 110, [("Count the red boxes. ", False), ("Red", True), (" is how many ", False), ("blues", True), ("?", False)])
    pick(c, y, [("A", [("Red", True), (" is ", False), ("9 times", True), (" as long as ", False), ("blue", True), (".", False)]),
                ("B", [("Red", True), (" is ", False), ("4 times", True), (" as long as ", False), ("blue", True), (".", False)]),
                ("C", [("Blue", True), (" is ", False), ("4 times", True), (" as long as ", False), ("red", True), (".", False)])],
         ["The red strip is 9 times as long as the blue strip.", "The red strip is 4 times as long as the blue strip.",
          "The blue strip is 4 times as long as the red strip.", "The blue strip is 9 times as long as the red strip."])
    foot(c, 2)


# ---------------------------------------------------------------- 3

def card(c, x, y, w=14, h=19):
    c.setFillColor(HexColor("#FFFFFF"))
    c.roundRect(x, y - h, w, h, 2, stroke=1, fill=1)
    c.setFillColor(black)


def q3(c):
    y = start(c)
    y = ask(c, y, 3, [[("Jin has ", False), ("8", True), (" cards.", False)],
                      [("Toni has ", False), ("3 times as many", True), (".", False)],
                      [("How many cards does ", False), ("Toni", True), (" have?", False)]])
    if MODE == "paper":
        x0, uw = MARGIN + 110, 110
        for k in range(8):
            card(c, MARGIN + 40 + k * 17, y - 4)
        rich_line(c, MARGIN + 190, y - 18, [("= 8 cards", True)], 13)
        y -= 46
        strip(c, x0 - 70, y, "Jin", [""], uw, label_w=70, h=36)
        end = strip(c, x0 - 70, y - 54, "Toni", ["", "", ""], uw, label_w=70, h=36)
        brace_under(c, x0, end, y - 96, "?")
        y = step(c, y - 160, [("Write ", False), ("8", True), (" in every box. Count by 8s:  8, 16, ___", False)])
        pick(c, y, [("A", "11 cards"), ("B", "24 cards"), ("C", "33 cards")], [], size=20)
    else:
        rich_line(c, MARGIN, y - 14, [("Word bank:  ", True), ("Toni   Jin   3   8   11   23   24   33", False)], 15)
        y -= 50
        bw, nx, x0 = 90, 90, MARGIN + 150
        for n, (bx, by, w) in enumerate([(MARGIN + 40, y, nx), (MARGIN + 40, y - 56, nx), (x0, y, bw),
                                         (x0, y - 56, bw), (x0 + bw, y - 56, bw), (x0 + 2 * bw, y - 56, bw)], 1):
            c.rect(bx, by - 40, w, 40)
            c.setFont("Sans-Bold", 11)
            c.drawString(bx + 4, by - 13, str(n))
        brace_under(c, x0, x0 + 3 * bw, y - 104, "?")
        y -= 150
        for line in ([("Box 1 and Box 2: ", True), ("names. ", False), ("Who has fewer? ", False), ("Box 1.", True)],
                     [("Box 3: ", True), ("Jin's number of cards.", False)],
                     [("Boxes 4, 5, 6: ", True), ("each one is the ", False), ("same", True), (" as Box 3.", False)]):
            rich_line(c, MARGIN + 20, y, line, 15)
            y -= 30
    foot(c, 3)


# ---------------------------------------------------------------- 4

def q4(c):
    y = start(c)
    y = ask(c, y, 4, [[("A machine changes numbers.", False)],
                      [("In", True), (" goes in.  ", False), ("Out", True), (" comes out.", False)]])
    rows = [(3, 12), (5, 20), (7, 28), (9, 36)]
    tx, rh = MARGIN + 40, 40
    c.setFont("Sans-Bold", 16)
    for j, head in enumerate(("In", "Out")):
        c.setFillColor(HexColor("#E6E6E6"))
        c.rect(tx + j * 70, y - rh, 70, rh, stroke=1, fill=1)
        c.setFillColor(black)
        c.drawCentredString(tx + j * 70 + 35, y - 26, head)
    for i, (a, b) in enumerate(rows):
        yy = y - (i + 2) * rh
        for j, v in enumerate((a, b)):
            c.rect(tx + j * 70, yy, 70, rh)
            c.drawCentredString(tx + j * 70 + 35, yy + 14, str(v))
    # picture of the first row: 3 -> 4 groups of 3
    px = tx + 180
    rich_line(c, px, y - 22, [("In ", False), ("3", True), (":", False)], 14)
    dot_groups(c, px + 75, y - 18, 1, 3)
    rich_line(c, px, y - 70, [("Out ", False), ("12", True), (":", False)], 14)
    dot_groups(c, px + 75, y - 66, 4, 3)
    rich_line(c, px, y - 118, [("12 = 4 groups of 3", True)], 14)
    y = step(c, y - 236, [("3 × ", False), ("___", True), (" = 12.   5 × ", False), ("___", True), (" = 20.  Same number?", False)])
    rich_line(c, MARGIN, y, [("The ", False), ("Out", True), (" number is  ______  the ", False), ("In", True), (" number.", False)], 16)
    y -= 34
    if MODE == "paper":
        choice_boxes(c, y, [("A", "4 more than"), ("B", "4 times as many as"), ("C", "9 times as many as")], size=18)
    else:
        rich_line(c, MARGIN, y, [("On the computer: ", True), ("click the drop-down. Find the choice with ", False),
                                 ("times as many", True), (".", False)], 13)
        rich_line(c, MARGIN, y - 24, [("Then check the number:  3 × ", False), ("?", True), (" = 12.", False)], 13)
    foot(c, 4)


# ---------------------------------------------------------------- 5

def mini_table(c, x, y, rows, cw=62, rh=24):
    c.setFont("Sans-Bold", 10)
    for j, head in enumerate(("Oatmeal", "Chocolate")):
        c.setFillColor(HexColor("#E6E6E6"))
        c.rect(x + j * cw, y - rh, cw, rh, stroke=1, fill=1)
        c.setFillColor(black)
        c.drawCentredString(x + j * cw + cw / 2, y - rh + 8, head)
    c.setFont("Sans-Bold", 15)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            c.rect(x + j * cw, y - (i + 2) * rh, cw, rh)
            c.drawCentredString(x + j * cw + cw / 2, y - (i + 2) * rh + 7, str(v))
    return y - (len(rows) + 1) * rh


def q5(c):
    y = start(c)
    y = ask(c, y, 5, [[("Mario makes ", False), ("3", True), (" oatmeal batches", False)],
                      [("for every ", False), ("9", True), (" chocolate batches.", False)],
                      [("Which table shows this?", False)]])
    for k in range(3):
        c.setFillColor(TAN)
        c.circle(MARGIN + 160 + k * 26, y - 6, 10, stroke=1, fill=1)
    for k in range(9):
        c.setFillColor(CHOC)
        c.circle(MARGIN + 160 + k * 26, y - 40, 10, stroke=1, fill=1)
    c.setFillColor(black)
    rich_line(c, MARGIN + 40, y - 11, [("Oatmeal  3", True)], 13)
    rich_line(c, MARGIN + 40, y - 45, [("Chocolate  9", True)], 13)
    y = step(c, y - 80, [("Find ", False), ("3", True), (" under Oatmeal. Look across. Is it ", False), ("9", True), ("?", False)])
    tables = [[(2, 6), (3, 9), (6, 18), (9, 27)], [(6, 2), (9, 3), (18, 6), (27, 9)],
              [(1, 4), (3, 6), (5, 8), (7, 10)], [(2, 11), (3, 12), (6, 15), (9, 18)]]
    show = [("A", 0), ("B", 1), ("C", 3)] if MODE == "paper" else list(zip(ORD, range(4)))
    n = len(show)
    cw = (W - 2 * MARGIN) / n
    for k, (lab, t) in enumerate(show):
        tw = 124 if n == 3 else 112
        x0 = MARGIN + k * cw + (cw - tw) / 2
        if MODE == "paper":
            c.circle(x0 + 10, y - 8, 11)
        c.setFont("Sans-Bold", 11 if MODE != "paper" else 13)
        c.drawCentredString(x0 + 10, y - 12.5, lab)
        mini_table(c, x0, y - 26, tables[t], cw=tw / 2)
    foot(c, 5)


# ---------------------------------------------------------------- 6

def q6(c):
    y = start(c)
    y = ask(c, y, 6, [[("Look at ", False), ("36,476", True), (".", False)],
                      [("Compare the ", False), ("thousands", True), (" place to the ", False), ("ones", True), (" place.", False)]])
    places = ["Ten\nThousands", "Thousands", "Hundreds", "Tens", "Ones"]
    cw, x0, by = 92, MARGIN + 20, y - 130
    for k, (p, d) in enumerate(zip(places, "36476")):
        shade = k in (1, 4)
        c.setFillColor(HexColor("#E6E6E6") if shade else HexColor("#FFFFFF"))
        c.rect(x0 + k * cw + 4, by, cw - 8, 54, stroke=1, fill=1)
        c.setFillColor(black)
        c.setFont("Sans", 9)
        c.drawCentredString(x0 + k * cw + cw / 2, by + 40, p.replace("\n", " "))
        c.setFont("Sans-Bold", 22)
        c.drawCentredString(x0 + k * cw + cw / 2, by + 10, d)
    for k in (3, 2, 1):
        xa, xb = x0 + (k + 1) * cw + cw / 2, x0 + k * cw + cw / 2
        c.arc(xb, by + 40, xa, by + 90, 0, 180)
        c.line(xb, by + 65, xb - 4, by + 72)
        c.line(xb, by + 65, xb + 5, by + 71)
        c.setFont("Sans-Bold", 12)
        c.drawCentredString((xa + xb) / 2, by + 94, "× 10")
    y = step(c, by - 40, [("3 jumps:  ", False), ("10 × 10 × 10 = ", True), ("______", True)])
    pick(c, y, [("A", [("3", True), (" times greater", False)]), ("B", [("100", True), (" times greater", False)]),
                ("C", [("1,000", True), (" times greater", False)])],
         ["The thousands place is three times greater than the ones place.",
          "The thousands place is one hundred times greater than the ones place.",
          "The thousands place is one thousand times greater than the ones place.",
          "The thousands place is six times greater than the ones place."], size=18, helper_size=11.5)
    foot(c, 6)


PAGES = [q1, q2, q3, q4, q5, q6]


def build():
    global MODE
    for mode, out, title in (("paper", "G3_M3_TopicA_Check_Modified.pdf", "Modified"),
                             ("helper", "G3_M3_TopicA_Check_Helper.pdf", "Computer Helper Sheet")):
        MODE = mode
        main(out, PAGES, "Grade 3 Module 3 Topic A Progress Check – " + title)


if __name__ == "__main__":
    build()
