"""Accommodated Grade 3 Module 2 End-of-Module Assessment (12 questions).

Same math work as the original: no answers filled in, no steps worked out.
Same questions, numbers, and answer choices in the same order and letters,
so the computer test's answer key still applies.
Accommodations: fewer/simpler words (key math words get a short meaning),
pictures, tables, and strip diagrams with a "?" for the unknown.

Run: python3 end_of_module_accommodated.py  ->  writes G3_M2_EndOfModule_Accommodated.pdf
"""
import math

from reportlab.lib.colors import HexColor, black

from build_module2 import MARGIN, W, blank, footer, header, main, rich_line
from end_of_module_modified import FACTS, choices, q
from lessons_20_24 import bars, top_brace

FOOT = ("Module 2:", "Place Value and Problem Solving with Units of Measure")
TITLE = "End-of-Module Test"
LIGHT = HexColor("#DDDDDD")


def start(c):
    return header(c, TITLE, suffix=" (Accommodated)") - 20


def answer_line(c, x, y, label, unit="", w=110, size=14):
    x = rich_line(c, x, y, [(label, True)], size)
    blank(c, x + 6, y, w)
    if unit:
        rich_line(c, x + w + 12, y, [(unit, False)], size)


def work_box(c, x, y, w, h):
    c.setStrokeColor(LIGHT)
    c.rect(x, y - h, w, h)
    c.setStrokeColor(black)
    c.setFont("Sans", 9)
    c.setFillColor(HexColor("#888888"))
    c.drawString(x + 6, y - 12, "Work space")
    c.setFillColor(black)


def table(c, x, y, heads, rows, widths, rh=24):
    c.setFillColor(LIGHT)
    c.rect(x, y - rh, sum(widths), rh, stroke=0, fill=1)
    c.setFillColor(black)
    c.rect(x, y - rh * (len(rows) + 1), sum(widths), rh * (len(rows) + 1))
    xx = x
    for w in widths[:-1]:
        xx += w
        c.line(xx, y, xx, y - rh * (len(rows) + 1))
    for r in range(1, len(rows) + 1):
        c.line(x, y - rh * r, x + sum(widths), y - rh * r)
    for r, row in enumerate([heads] + rows):
        xx = x
        for w, cell in zip(widths, row):
            c.setFont("Sans-Bold" if r == 0 else "Sans", 11.5)
            c.drawCentredString(xx + w / 2, y - rh * r - 16, cell)
            xx += w
    return y - rh * (len(rows) + 1)


# ---------------------------------------------------------------- 1

def fact_blank(c, x, y, text, size=11.5, bw=26):
    left, right = text.split("_")
    x = rich_line(c, x, y, [(left, False)], size)
    c.setLineWidth(1.2)
    c.rect(x + 1, y - 6, bw, 20)
    c.setLineWidth(1)
    rich_line(c, x + bw + 3, y, [(right, False)], size)


def page_1(c):
    y = start(c)
    y = q(c, y, "1", [[("Multiply and divide. Write the missing number in each box.", False)]])
    y -= 30
    cw = (W - 2 * MARGIN) / 5
    for i, (text, _, _) in enumerate(FACTS):
        fact_blank(c, MARGIN + (i % 5) * cw, y - (i // 5) * 62, text)
    footer(c, *FOOT, 1)


# ---------------------------------------------------------------- 2-3

def page_2(c):
    y = start(c)
    y = q(c, y, "2", [[("Trail mix box: ", False), ("56 ounces", True)],
                      [("Almond box: ", False), ("18 ounces", True)],
                      [("What is the ", False), ("difference", True), (" (how much heavier is the trail mix)?", False)]])
    bars(c, MARGIN + 90, y - 14, 300, [("Trail mix", [("56", 56, False)]),
                                        ("Almonds", [("18", 18, False), ("?", 38, False)])], 56, row_gap=34, h=26)
    work_box(c, MARGIN + 26, y - 90, 260, 90)
    answer_line(c, MARGIN + 310, y - 150, "Answer:", "ounces", w=70)

    y -= 230
    y = q(c, y, "3", [[("An airplane gets ", False), ("3,746", True), (" liters of fuel each minute.", False)],
                      [("Use the number line. ", False), ("Round", True), (" 3,746 to the nearest ", False),
                       ("hundred", True), (".", False)]])
    x0, x1, ly = MARGIN + 50, W - MARGIN - 50, y - 50
    c.setLineWidth(1.5)
    c.line(x0 - 10, ly, x1 + 10, ly)
    c.setLineWidth(1)
    for k in range(3):
        tx = x0 + k * (x1 - x0) / 2
        c.line(tx, ly - 8, tx, ly + 8)
        blank(c, tx - 30, ly - 30, 60)
    answer_line(c, MARGIN + 26, ly - 90, "3,746 rounds to", w=100)
    footer(c, *FOOT, 2)


# ---------------------------------------------------------------- 4-5

def page_3(c):
    y = start(c)
    y = q(c, y, "4", [[("The scale shows how much ", False), ("one", True), (" bag weighs.", False)],
                      [("A worker lifts ", False), ("3", True), (" bags. Each bag weighs the same.", False)]])
    c.drawImage("images/eom_scale.png", W - MARGIN - 130, y - 100, width=130, height=115,
                preserveAspectRatio=True, mask="auto")
    bars(c, MARGIN + 70, y - 14, 260, [("", [("bag", 1, False), ("bag", 1, False), ("bag", 1, False)])], 3,
         brace=("? pounds", 0, 3), h=26)
    y -= 110
    answer_line(c, MARGIN + 26, y, "One bag weighs", "pounds", w=60)
    y -= 40
    rich_line(c, MARGIN + 26, y, [("a.  ", True), ("Round", True), (" to ", False), ("estimate", True),
                                  (" (about how much):", False)], 13)
    answer_line(c, MARGIN + 330, y, "", "pounds", w=80)
    y -= 40
    rich_line(c, MARGIN + 26, y, [("b.  ", True), ("Exact", True), (" answer:", False)], 13)
    answer_line(c, MARGIN + 330, y, "", "pounds", w=80)

    y -= 60
    y = q(c, y, "5", [[("Passenger 1's bags: ", False), ("120 pounds", True)],
                      [("Passenger 2's bags: ", False), ("97 pounds", True)],
                      [("How much ", False), ("more", True), (" do passenger 1's bags weigh?", False)],
                      [("Write an ", False), ("equation", True), (" (number sentence) and solve it.", False)]])
    bars(c, MARGIN + 100, y - 14, 280, [("Passenger 1", [("120", 120, False)]),
                                         ("Passenger 2", [("97", 97, False), ("?", 23, False)])], 120, row_gap=34, h=26)
    y -= 100
    answer_line(c, MARGIN + 26, y, "Equation:", w=200)
    answer_line(c, MARGIN + 26, y - 40, "Answer:", "pounds", w=80)
    footer(c, *FOOT, 3)


# ---------------------------------------------------------------- 6-7

def page_4(c):
    y = start(c)
    y = q(c, y, "6", [[("The table shows how many people flew from 3 airports.", False)],
                      [("Put the airports in order from ", False), ("greatest", True), (" (most) to ", False),
                       ("least", True), (" (fewest).", False)]])
    y = table(c, MARGIN + 40, y - 6, ["Airport", "People"],
              [["Biggs Army Airfield", "26,730"], ["East Texas Regional", "22,480"], ["Jack Brooks Regional", "26,518"]],
              [220, 120])
    y -= 30
    for lbl in ("Greatest:", "", "Least:"):
        rich_line(c, MARGIN + 40, y, [(lbl, True)], 13)
        blank(c, MARGIN + 130, y, 230)
        y -= 32

    y -= 20
    y = q(c, y, "7", [[("Which list goes from ", False), ("least", True), (" (smallest) to ", False),
                       ("greatest", True), (" (biggest)?", False)]])
    choices(c, MARGIN + 30, y - 10, [("A", "53,607;   53,670;   53,760;   56,370"),
                                     ("B", "53,670;   53,607;   53,760;   56,370"),
                                     ("C", "56,370;   53,760;   53,670;   53,607"),
                                     ("D", "53,607;   53,760;   53,670;   56,370")], gap=30)
    footer(c, *FOOT, 4)


# ---------------------------------------------------------------- 8-9

def page_5(c):
    y = start(c)
    y = q(c, y, "8", [[("Mr. Diaz buys ", False), ("2", True), (" pumpkins. Together they weigh ", False),
                       ("200 ounces", True), (".", False)],
                      [("Which 2 pumpkins did he buy?", False)]])
    table(c, W - MARGIN - 180, y - 4, ["Pumpkin", "Weight (oz)"],
          [["A", "110"], ["B", "108"], ["C", "114"], ["D", "94"], ["E", "86"]], [80, 100], rh=22)
    bars(c, MARGIN + 30, y - 10, 230, [("", [("?", 1, False), ("?", 1, False)])], 2, brace=("200 ounces", 0, 2), h=24)
    choices(c, MARGIN + 30, y - 100, [("F", "Pumpkins C and E"), ("G", "Pumpkins A and B"),
                                      ("H", "Pumpkins B and D"), ("J", "Pumpkins D and E")], gap=26)
    y -= 230
    y = q(c, y, "9", [[("What number is the same as  ", False), ("80,000 + 100 + 50 + 6", True), ("?", False)]])
    cw, x0 = 70, MARGIN + 30
    for k, p in enumerate(["Ten\nThousands", "Thousands", "Hundreds", "Tens", "Ones"]):
        for j, ln in enumerate(p.split("\n")):
            c.setFont("Sans", 9)
            c.drawCentredString(x0 + k * cw + cw / 2, y - 10 - 10 * j, ln)
        c.rect(x0 + k * cw + 6, y - 58, cw - 12, 30)
    choices(c, x0 + 5 * cw + 30, y - 8, [("A", "81,056"), ("B", "80,156"), ("C", "8,516"), ("D", "80,516")], gap=22, size=13)
    footer(c, *FOOT, 5)


# ---------------------------------------------------------------- 10

def clock(c, cx, cy, r):
    c.setLineWidth(2)
    c.circle(cx, cy, r)
    c.setLineWidth(1)
    for h in range(1, 13):
        a = math.radians(90 - h * 30)
        c.line(cx + (r - 6) * math.cos(a), cy + (r - 6) * math.sin(a), cx + r * math.cos(a), cy + r * math.sin(a))
        c.setFont("Sans", 10)
        c.drawCentredString(cx + (r - 16) * math.cos(a), cy + (r - 16) * math.sin(a) - 3, str(h))
    c.circle(cx, cy, 2.5, stroke=0, fill=1)


def page_6(c):
    y = start(c)
    y = q(c, y, "10", [[("The table shows how long 3 friends read.", False)],
                       [("What is the ", False), ("total", True), (" (all together) time?", False)],
                       [("If it is more than 1 hour, write it in ", False), ("hours and minutes", True), (".", False)]])
    ty = table(c, MARGIN + 30, y - 6, ["Student", "Time reading"],
               [["Ana", "24 minutes"], ["Ben", "35 minutes"], ["Carlos", "23 minutes"]], [130, 150])
    clock(c, W - MARGIN - 80, y - 50, 50)
    rich_line(c, W - MARGIN - 135, y - 132, [("60 minutes = 1 hour", True)], 11)
    bars(c, MARGIN + 60, ty - 50, 360, [("", [("24", 24, False), ("35", 35, False), ("23", 23, False)])], 82,
         brace=("? minutes", 0, 82), h=26)
    work_box(c, MARGIN + 26, ty - 136, W - 2 * MARGIN - 52, 120)
    answer_line(c, MARGIN + 26, ty - 296, "Answer:", w=60)
    rich_line(c, MARGIN + 190, ty - 296, [("hour", False)], 14)
    blank(c, MARGIN + 240, ty - 296, 60)
    rich_line(c, MARGIN + 310, ty - 296, [("minutes", False)], 14)
    footer(c, *FOOT, 6)


# ---------------------------------------------------------------- 11-12

def page_7(c):
    y = start(c)
    y = q(c, y, "11", [[("A big shipping box is full of bricks.", False)],
                       [("Which units measure its ", False), ("weight", True), (" (how heavy)? Pick ", False),
                        ("TWO", True), (".", False)]])
    choices(c, MARGIN + 30, y - 10, [("A", "Gallons"), ("B", "Pounds"), ("C", "Feet"), ("D", "Milliliters"),
                                     ("F", "Fluid Ounces"), ("G", "Tons")], gap=28)
    y -= 210
    y = q(c, y, "12", [[("About how much liquid is in the container?", False)],
                       [("Round to the nearest ", False), ("liter", True), (" (L).", False)]])
    c.drawImage("images/eom_beaker.png", MARGIN + 40, y - 230, width=180, height=220,
                preserveAspectRatio=True, mask="auto")
    answer_line(c, MARGIN + 260, y - 120, "About", "liters", w=60, size=16)
    footer(c, *FOOT, 7)


PAGES = [page_1, page_2, page_3, page_4, page_5, page_6, page_7]

if __name__ == "__main__":
    main("G3_M2_EndOfModule_Accommodated.pdf", PAGES, "Grade 3 Module 2 End-of-Module Assessment – Accommodated")
