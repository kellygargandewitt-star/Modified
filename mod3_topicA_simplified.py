"""Grade 3 Module 3 Topic A TEKS Progress Check - SIMPLIFIED (paper, level 2).

Even simpler than the Modified version (modified_test_kit.py rules, plus):
  - 2 answer choices (correct + closest wrong answer)
  - about one short line of words; the picture tells the story
  - the picture is partly filled in; students do one small fill-in, then pick
  - bigger print (20-24 pt)

Run: python3 mod3_topicA_simplified.py  ->  G3_M3_TopicA_Check_Simplified.pdf
"""
from reportlab.lib.colors import HexColor, black

from build_module2 import MARGIN, W, footer, header, main, rich_line
from modified_test_kit import ask, brace_under, choice_boxes, dot_groups, step, strip

TAN, CHOC = HexColor("#E3C48F"), HexColor("#6B4A2F")
Q, S, CH = 20, 17, 22          # question, step, choice sizes


def start(c):
    return header(c, "Topic A Progress Check", suffix=" (Simplified)", unit="3 • 3") - 44


def foot(c, n):
    footer(c, "Module 3, Topic A:", "Progress Check (Simplified)", n)


def two(c, y, a, b, size=CH):
    return choice_boxes(c, y, [("A", a), ("B", b)], size=size, h=56, gap=18)


def q1(c):
    y = start(c)
    y = ask(c, y, 1, [[("Red is ", False), ("3 times", True), (" as long as yellow.", False)]], size=Q)
    x = MARGIN + 50
    strip(c, x, y - 10, "Yellow", ["9"], 100, "yellow", h=40, size=18)
    end = strip(c, x, y - 66, "Red", ["9", "9", "9"], 100, "red", h=40, size=18)
    brace_under(c, x + 70, end, y - 112, "?", size=18)
    y = step(c, y - 180, [("Red has ", False), ("___", True), (" boxes of 9.", False)], size=S)
    rich_line(c, MARGIN, y, [("Which one finds red?", True)], S)
    two(c, y - 20, "9 + 3 = 12", "9 × 3 = 27")
    foot(c, 1)


def q2(c):
    y = start(c)
    y = ask(c, y, 2, [[("Red is ", False), ("9 × 4", True), (".", False)]], size=Q)
    x = MARGIN + 30
    strip(c, x, y - 10, "Blue", ["9"], 85, "blue", h=40, size=18)
    strip(c, x, y - 66, "Red", ["9", "9", "9", "9"], 85, "red", h=40, size=18)
    y = step(c, y - 150, [("Count the red boxes:  ", False), ("___", True)], size=S)
    rich_line(c, MARGIN, y, [("Which is true?", True)], S)
    two(c, y - 20, [("Red is ", False), ("4 times", True), (" as long as blue.", False)],
        [("Red is ", False), ("9 times", True), (" as long as blue.", False)], size=19)
    foot(c, 2)


def q3(c):
    y = start(c)
    y = ask(c, y, 3, [[("Jin has ", False), ("8", True), (".  Toni has ", False), ("3 times", True), (" as many.", False)]], size=Q)
    x = MARGIN + 50
    strip(c, x, y - 10, "Jin", ["8"], 110, h=40, size=18)
    end = strip(c, x, y - 66, "Toni", ["8", "8", "8"], 110, h=40, size=18)
    brace_under(c, x + 70, end, y - 112, "?", size=18)
    # jump line 0 -> 8 -> 16 -> ?
    ly, lx, gap = y - 210, MARGIN + 60, 130
    c.setLineWidth(2)
    c.line(lx - 10, ly, lx + 3 * gap + 20, ly)
    c.setLineWidth(1)
    for k, lab in enumerate(["0", "8", "16", "___"]):
        px = lx + k * gap
        c.line(px, ly - 8, px, ly + 8)
        c.setFont("Sans-Bold", 18)
        c.drawCentredString(px, ly - 30, lab)
        if k:
            c.arc(px - gap, ly + 2, px, ly + 50, 0, 180)
            c.setFont("Sans", 12)
            c.drawCentredString(px - gap / 2, ly + 56, "+ 8")
    y = step(c, ly - 70, [("Count by 8s:  8, 16, ", False), ("___", True)], size=S)
    rich_line(c, MARGIN, y, [("How many cards does ", False), ("Toni", True), (" have?", False)], S)
    two(c, y - 20, "11 cards", "24 cards")
    foot(c, 3)


def q4(c):
    y = start(c)
    y = ask(c, y, 4, [[("In", True), ("  3  →  ", False), ("Out", True), ("  12", False)]], size=Q)
    px = MARGIN + 40
    rich_line(c, px, y - 26, [("In  ", True), ("3", True)], 18)
    dot_groups(c, px + 110, y - 20, 1, 3, r=6, gap=15)
    rich_line(c, px, y - 90, [("Out  ", True), ("12", True)], 18)
    dot_groups(c, px + 110, y - 84, 4, 3, r=6, gap=15)
    rich_line(c, px, y - 140, [("Other rows:  5 → 20    7 → 28    9 → 36", False)], 14)
    y = step(c, y - 196, [("3 × ", False), ("___", True), (" = 12", False)], size=S)
    rich_line(c, MARGIN, y, [("Out", True), (" is  ______  ", False), ("In", True), (".", False)], S)
    two(c, y - 20, "4 more than", "4 times as many as")
    foot(c, 4)


def table(c, x, y, rows, cw=80, rh=32):
    for j, (head, col) in enumerate((("Oatmeal", TAN), ("Chocolate", CHOC))):
        c.setFillColor(col)
        c.rect(x + j * cw, y - rh, cw, rh, stroke=1, fill=1)
        c.setFillColor(black if j == 0 else HexColor("#FFFFFF"))
        c.setFont("Sans-Bold", 12)
        c.drawCentredString(x + j * cw + cw / 2, y - rh + 11, head)
    c.setFillColor(black)
    c.setFont("Sans-Bold", 18)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            c.rect(x + j * cw, y - (i + 2) * rh, cw, rh)
            c.drawCentredString(x + j * cw + cw / 2, y - (i + 2) * rh + 10, str(v))


def q5(c):
    y = start(c)
    y = ask(c, y, 5, [[("3", True), (" oatmeal for every ", False), ("9", True), (" chocolate.", False)]], size=Q)
    for k in range(3):
        c.setFillColor(TAN)
        c.circle(MARGIN + 170 + k * 28, y - 12, 11, stroke=1, fill=1)
    for k in range(9):
        c.setFillColor(CHOC)
        c.circle(MARGIN + 170 + k * 28, y - 48, 11, stroke=1, fill=1)
    c.setFillColor(black)
    rich_line(c, MARGIN + 40, y - 18, [("Oatmeal  3", True)], 15)
    rich_line(c, MARGIN + 40, y - 54, [("Chocolate  9", True)], 15)
    y = step(c, y - 100, [("Find ", False), ("3", True), (" under Oatmeal. Is ", False), ("9", True), (" next to it?", False)], size=S)
    rich_line(c, MARGIN, y, [("Which table shows this?", True)], S)
    cw = (W - 2 * MARGIN) / 2
    for k, (lab, rows) in enumerate((("A", [(2, 6), (3, 9), (6, 18), (9, 27)]), ("B", [(6, 2), (9, 3), (18, 6), (27, 9)]))):
        x0 = MARGIN + k * cw + (cw - 160) / 2
        c.circle(x0 + 12, y - 36, 14)
        c.setFont("Sans-Bold", 16)
        c.drawCentredString(x0 + 12, y - 42, lab)
        table(c, x0, y - 60, rows)
    foot(c, 5)


def q6(c):
    y = start(c)
    y = ask(c, y, 6, [[("36,476", True), (":  ", False), ("thousands", True), (" or ", False), ("ones", True), ("?", False)]], size=Q)
    places = [("Thousands", "6", "1,000"), ("Hundreds", "4", "100"), ("Tens", "7", "10"), ("Ones", "6", "1")]
    cw, x0, by = 112, MARGIN + 36, y - 150
    for k, (p, d, v) in enumerate(places):
        shade = k in (0, 3)
        c.setFillColor(HexColor("#E6E6E6") if shade else HexColor("#FFFFFF"))
        c.rect(x0 + k * cw + 4, by, cw - 8, 60, stroke=1, fill=1)
        c.setFillColor(black)
        c.setFont("Sans", 11)
        c.drawCentredString(x0 + k * cw + cw / 2, by + 44, p)
        c.setFont("Sans-Bold", 24)
        c.drawCentredString(x0 + k * cw + cw / 2, by + 12, d)
        c.setFont("Sans-Bold", 16)
        c.drawCentredString(x0 + k * cw + cw / 2, by - 24, v)
    for k in (2, 1, 0):
        xa, xb = x0 + (k + 1) * cw + cw / 2, x0 + k * cw + cw / 2
        c.arc(xb, by + 46, xa, by + 100, 0, 180)
        c.line(xb, by + 73, xb - 4, by + 80)
        c.line(xb, by + 73, xb + 5, by + 79)
        c.setFont("Sans-Bold", 13)
        c.drawCentredString((xa + xb) / 2, by + 104, "× 10")
    y = step(c, by - 70, [("Ones = ", False), ("1", True), (".   Thousands = ", False), ("1,000", True), (".", False)], size=S)
    rich_line(c, MARGIN, y, [("The thousands place is ...", True)], S)
    two(c, y - 20, [("100", True), (" times greater", False)], [("1,000", True), (" times greater", False)])
    foot(c, 6)


if __name__ == "__main__":
    main("G3_M3_TopicA_Check_Simplified.pdf", [q1, q2, q3, q4, q5, q6], "Grade 3 Module 3 Topic A Progress Check – Simplified")
