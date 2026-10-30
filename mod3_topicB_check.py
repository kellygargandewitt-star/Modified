"""Grade 3 Module 3 Topic B TEKS Progress Check (4 questions): COMPUTER HELPER + SIMPLIFIED paper.

Standing plan (MODIFIED_TEST_RULES.md):
  HELPER     - same pictures and "Do this" steps, all 4 choices in the computer's order (1st-4th).
  SIMPLIFIED - paper only: 2 choices, about one line of words, partly filled picture, big print.

Run: python3 mod3_topicB_check.py
  -> G3_M3_TopicB_Check_Helper.pdf, G3_M3_TopicB_Check_Simplified.pdf
"""
from reportlab.lib.colors import HexColor, black, white

from build_module2 import MARGIN, W, footer, header, main, rich_line
from modified_test_kit import COLORS, INK, ask, brace_under, choice_boxes, dot_groups, step, strip

MODE = "simp"
ORD = ["1st", "2nd", "3rd", "4th"]
BLUE = HexColor("#7FA8D8")


def simp():
    return MODE == "simp"


def start(c):
    return header(c, "Topic B Progress Check", suffix=" (Simplified)" if simp() else " (Computer Helper)", unit="3 • 3") - 44


def foot(c, n):
    footer(c, "Module 3, Topic B:", "Progress Check (Simplified)" if simp() else "Computer Helper Sheet", n)


def q_text(c, y, n, simple, helper):
    return ask(c, y, n, simple if simp() else helper, size=20 if simp() else 17)


def pick(c, y, two, four, ask_line, helper_size=15):
    """two: [(A text), (B text)] for SIMPLIFIED; four: computer choices in screen order for HELPER."""
    if simp():
        rich_line(c, MARGIN, y, [(ask_line, True)], 17)
        return choice_boxes(c, y - 20, [("A", two[0]), ("B", two[1])], size=22, h=56, gap=18)
    rich_line(c, MARGIN, y, [(ask_line, True)], 15)
    rich_line(c, MARGIN, y - 22, [("On the computer, the choices are in this order:", False)], 13)
    return choice_boxes(c, y - 36, list(zip(ORD, four)), size=helper_size, h=36, gap=10)


def jump_line(c, x, y, labels, gap, jump):
    c.setLineWidth(2)
    c.line(x - 10, y, x + (len(labels) - 1) * gap + 20, y)
    c.setLineWidth(1)
    for k, lab in enumerate(labels):
        px = x + k * gap
        c.line(px, y - 8, px, y + 8)
        c.setFont("Sans-Bold", 16)
        c.drawCentredString(px, y - 28, lab)
        if k:
            c.arc(px - gap, y + 2, px, y + 40, 0, 180)
            c.setFont("Sans", 11)
            c.drawCentredString(px - gap / 2, y + 45, jump)


# ---------------------------------------------------------------- 1

def q1(c):
    y = start(c)
    y = q_text(c, y, 1, [[("6", True), (" rows.  ", False), ("8", True), (" in each row.", False)]],
               [[("Geri wrote 4 number sentences for this array.", False)],
                [("Which one ", False), ("CANNOT", True), (" find the total?", False)]])
    r, gap, x0, top = 10, 30, MARGIN + 90, y - 10
    for row in range(6):
        for col in range(8):
            c.setFillColor(HexColor("#9A9A9A"))
            c.circle(x0 + col * gap, top - row * gap, r, stroke=1, fill=1)
        c.setFillColor(black)
        c.setFont("Sans-Bold", 13)
        c.drawRightString(x0 - 22, top - row * gap - 5, f"row {row + 1}")
    c.setFillColor(black)
    c.setFont("Sans-Bold", 14)
    c.drawString(x0 + 8 * gap, top - 5, "← 8")
    y = step(c, top - 6 * gap - 10, [("Each row has ", False), ("8", True), (".  Add ", False), ("8", True), (" six times, or ", False),
                                      ("6 × 8", True), (".", False)], size=16 if simp() else 15)
    pick(c, y, ["8 + 8 + 8 + 8 + 8 + 8", "6 + 6 + 6 + 6 + 6 + 6"],
         ["8 + 8 + 8 + 8 + 8 + 8 =", "8 × 6 =", "6 + 6 + 6 + 6 + 6 + 6 =", "6 × 8 ="],
         "Which one does NOT match?" if simp() else "Find the one that does NOT match.")
    foot(c, 1)


# ---------------------------------------------------------------- 2

def marbles(c, x, y, n, fill, r=9, gap=22):
    for k in range(n):
        c.setFillColor(fill)
        c.circle(x + k * gap, y, r, stroke=1, fill=1)
    c.setFillColor(black)


def q2(c):
    y = start(c)
    y = q_text(c, y, 2, [[("3", True), (" white marbles.  ", False), ("9", True), (" blue marbles.", False)]],
               [[("Each marble set has ", False), ("white", True), (" and ", False), ("blue", True), (" marbles.", False)],
                [("Look at the table.", False)]])
    tx, cw, rh = MARGIN + 20, 100, 30
    rows = [(3, 9), (5, 15), (7, 21), (9, 27)]
    for j, head in enumerate(("White", "Blue")):
        c.setFillColor(HexColor("#FFFFFF") if j == 0 else COLORS["blue"])
        c.rect(tx + j * cw, y - rh, cw, rh, stroke=1, fill=1)
        c.setFillColor(black)
        c.setFont("Sans-Bold", 14)
        c.drawCentredString(tx + j * cw + cw / 2, y - rh + 10, head)
    c.setFont("Sans-Bold", 17)
    for i, (a, b) in enumerate(rows):
        yy = y - (i + 2) * rh
        if i == 0:
            c.setFillColor(HexColor("#F2F2F2"))
            c.rect(tx, yy, 2 * cw, rh, stroke=0, fill=1)
            c.setFillColor(black)
        for j, v in enumerate((a, b)):
            c.rect(tx + j * cw, yy, cw, rh)
            c.drawCentredString(tx + j * cw + cw / 2, yy + 9, str(v))
    # picture of the first row
    px = tx + 2 * cw + 30
    rich_line(c, px, y - 20, [("White  3", True)], 14)
    marbles(c, px + 90, y - 15, 3, white)
    rich_line(c, px, y - 66, [("Blue  9", True)], 14)
    for g in range(3):
        c.setStrokeColor(HexColor("#9A9A9A"))
        c.roundRect(px + 78 + g * 74, y - 78, 70, 26, 8)
        c.setStrokeColor(black)
        marbles(c, px + 90 + g * 74, y - 65, 3, BLUE)
    rich_line(c, px, y - 110, [("9 = 3 groups of 3", True)], 14)
    y = step(c, y - 5 * rh - 40, [("3 × ", False), ("___", True), (" = 9.   Blue is ", False), ("___", True), (" times white.", False)],
             size=16 if simp() else 15)
    pick(c, y, [[("Blue", True), (" is ", False), ("6 times", True), (" white.", False)],
                [("Blue", True), (" is ", False), ("3 times", True), (" white.", False)]],
         ["The number of blue marbles equals 6 times the number of white marbles.",
          "The number of white marbles equals 6 times the number of blue marbles.",
          "The number of blue marbles equals 3 times the number of white marbles.",
          "The number of white marbles equals 3 times the number of blue marbles."],
         "Which is true?", helper_size=11.5)
    foot(c, 2)


# ---------------------------------------------------------------- 3

def q3(c):
    y = start(c)
    y = q_text(c, y, 3, [[("9", True), (" pages every day.  ", False), ("6", True), (" days.", False)]],
               [[("Maryan reads ", False), ("9 pages", True), (" every day.", False)],
                [("How many pages after ", False), ("6 days", True), ("?", False)]])
    x = MARGIN + 30
    rich_line(c, x, y - 4, [("Day:", False)], 12)
    for k in range(6):
        c.setFont("Sans", 12)
        c.drawCentredString(x + 70 + k * 70 + 35, y - 4, str(k + 1))
    end = strip(c, x, y - 12, "Pages", ["9"] * 6, 70, h=40, size=18)
    brace_under(c, x + 70, end, y - 58, "?", size=18)
    labels = ["0", "9", "18", "27", "36", "45", "___"] if simp() else ["0", "9", "18", "", "", "", ""]
    jump_line(c, MARGIN + 50, y - 150, labels, 70, "+ 9")
    y = step(c, y - 210, [("Count by 9s six times, or ", False), ("6 × 9", True), (".", False)], size=16 if simp() else 15)
    pick(c, y, ["45 pages", "54 pages"], ["15", "36", "45", "54"], "How many pages?")
    foot(c, 3)


# ---------------------------------------------------------------- 4

def q4(c):
    y = start(c)
    y = q_text(c, y, 4, [[("☐ × 3 = 21", True)]],
               [[("What number goes in the box?", False)], [("☐ × 3 = 21", True)]])
    rich_line(c, MARGIN + 40, y - 4, [("21", True), (" dots in groups of ", False), ("3", True), (":", False)], 15)
    if simp():
        dot_groups(c, MARGIN + 50, y - 40, 7, 3, r=6, gap=15, group_gap=18)
    else:
        for k in range(21):
            c.setFillColor(INK)
            c.circle(MARGIN + 56 + k * 22, y - 40, 6, stroke=0, fill=1)
        c.setFillColor(black)
        rich_line(c, MARGIN + 40, y - 76, [("Circle groups of 3.", False)], 13)
    y = step(c, y - 110, [("Count the groups:  ", False), ("___", True), ("  groups of 3 = 21", False)], size=16 if simp() else 15)
    pick(c, y, ["6", "7"], ["6", "7", "18", "24"], "What number goes in the box?")
    foot(c, 4)


PAGES = [q1, q2, q3, q4]


def build():
    global MODE
    for mode, out, title in (("helper", "G3_M3_TopicB_Check_Helper.pdf", "Computer Helper Sheet"),
                             ("simp", "G3_M3_TopicB_Check_Simplified.pdf", "Simplified")):
        MODE = mode
        main(out, PAGES, "Grade 3 Module 3 Topic B Progress Check – " + title)


if __name__ == "__main__":
    build()
