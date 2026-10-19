"""Simplified homework for the week: Lessons 8, 14-18 (book homework pages 34-80).

Readiness focus: 3.2D (compare/order) and 3.4A (add). Rounding (3.4B) is kept
at the teacher's request but made visual with a "rounding hill":
numbers on the left side roll back to the lower ten/hundred, numbers at or
past the top roll forward. Dial and beaker readings are given as numbers.
2-4 problems per page, plain layout, book page numbers kept.

Run: python3 homework_week.py  ->  writes G3_M2_Homework_Simplified.pdf
"""
from reportlab.lib.colors import HexColor, black

from build_module2 import MARGIN, W, blank, footer, header, main, rich_line, teks
from lessons_15_19_simple import order_blanks, stacked
from reteach_mid_module import sentence

GREY = HexColor("#777777")
ZONE = HexColor("#E6E6E6")

L8 = (8, "Determine when to use weight or liquid volume.")
L14 = (14, "Order whole numbers using place value and number lines.")
L15 = (15, "Round two-digit measurements to the nearest ten on the vertical number line.")
L16 = (16, "Round two- and three-digit numbers to the nearest ten on the vertical number line.")
L17 = (17, "Round to the nearest hundred on the vertical number line.")
L18 = (18, "Round four- and five-digit numbers using the vertical number line.")

HILL_TIP = "Find the number on the hill. Left side: roll back. Top or right side: roll forward."


def start(c, title, teks_label, tip):
    y = header(c, title, suffix="")
    teks(c, y, teks_label)
    rich_line(c, MARGIN, y - 6, [("Tip: ", True), (tip, False)], 12)
    return y - 44


def text(c, y, num, lines, size=14):
    for k, parts in enumerate(lines):
        lead = [(num + "  ", True)] if (k == 0 and num) else []
        rich_line(c, MARGIN + (0 if k == 0 or not num else 24), y, lead + parts, size)
        y -= 22
    return y


def fmt(v):
    return f"{v:,}"


def hill(c, x0, y, w, low, step, labels=None, h=None):
    """Rounding hill: a curve from low (left) up to halfway (top) and down to low+step (right).
    labels: optional list of 3 strings for left / middle / right."""
    h = h or min(w * 0.32, 62)
    pts = []
    for k in range(41):
        t = k / 40
        pts.append((x0 + t * w, y + h * (1 - (2 * t - 1) ** 2)))
    c.setLineWidth(2)
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    c.drawPath(p, stroke=1, fill=0)
    c.setLineWidth(1)
    c.line(x0 - 6, y, x0 + w + 6, y)
    # 11 ticks along the hill
    for k in range(11):
        t = k / 10
        tx, ty = x0 + t * w, y + h * (1 - (2 * t - 1) ** 2)
        c.circle(tx, ty, 2, stroke=0, fill=1)
        lab = fmt(low + step * k // 10)
        if k not in (0, 5, 10) and len(lab) <= 3 and w / 10 >= 18:
            c.setFont("Sans", 7)
            c.setFillColor(GREY)
            c.drawCentredString(tx, ty + 6, lab)
            c.setFillColor(black)
    left, mid, right = labels or (fmt(low), fmt(low + step // 2), fmt(low + step))
    c.setFont("Sans-Bold", 12)
    c.drawCentredString(x0, y - 16, left)
    c.drawCentredString(x0 + w, y - 16, right)
    c.drawCentredString(x0 + w / 2, y + h + 8, mid)
    if w >= 150:
        c.setFont("Sans", 8)
        c.setFillColor(GREY)
        c.drawCentredString(x0 + w * 0.22, y - 28, "← roll back")
        c.drawCentredString(x0 + w * 0.78, y - 28, "roll forward →")
        c.setFillColor(black)


def hill_item(c, x, y, w, label, n, low, step, unit="", labels=None):
    """Label, the hill, then 'n ≈ ___ unit'."""
    rich_line(c, x, y, [(f"{label}  ", True), (f"{n if isinstance(n, str) else fmt(n)}", True)], 15)
    hw = min(w - 70, 300)
    hill(c, x + 30, y - 100, hw, low, step, labels)
    s = f"{n if isinstance(n, str) else fmt(n)} ≈ |______" + (f"  {unit}" if unit else "")
    sentence(c, x + 4, y - 150, s, size=14, wide_w=64)


def hill_grid(c, y, items, cols=2, row_h=190):
    cw = (W - 2 * MARGIN) / cols
    for i, it in enumerate(items):
        x0, y0 = MARGIN + (i % cols) * cw, y - (i // cols) * row_h
        hill_item(c, x0, y0, cw - 10, *it)


def zone_line(c, y, lo, hi, step, zone, title):
    """Number line with a shaded zone of numbers that round to the middle value."""
    x0, x1 = MARGIN + 30, W - MARGIN - 30
    z0, z1 = zone
    c.setFillColor(ZONE)
    c.rect(x0 + (z0 - lo) / (hi - lo) * (x1 - x0), y - 10, (z1 - z0) / (hi - lo) * (x1 - x0), 20, stroke=0, fill=1)
    c.setFillColor(black)
    c.setLineWidth(1.5)
    c.line(x0 - 8, y, x1 + 8, y)
    c.setLineWidth(1)
    v = lo
    while v <= hi:
        tx = x0 + (v - lo) / (hi - lo) * (x1 - x0)
        c.line(tx, y - 8, tx, y + 8)
        c.setFont("Sans", 11)
        c.drawCentredString(tx, y - 24, fmt(v))
        v += step
    c.setFont("Sans", 9)
    c.setFillColor(GREY)
    c.drawCentredString(x0 + ((z0 + z1) / 2 - lo) / (hi - lo) * (x1 - x0), y + 14, title)
    c.setFillColor(black)


# ---------------------------------------------------------------- Lesson 8

def page_34(c):
    y = start(c, "Lesson 8 Homework", "TEKS 3.7E", "Weight = how heavy.  Liquid volume = how much liquid it holds.")
    y = text(c, y, "", [[("Circle ", False), ("weight", True), (" or ", False), ("liquid", True), (" for each one.", False)]])
    items = ["a bag of apples", "a glass of juice", "a dog", "a jug of milk", "a backpack", "water in a pool"]
    y -= 10
    for k, it in enumerate(items):
        rich_line(c, MARGIN + 30, y, [(it, False)], 15)
        rich_line(c, MARGIN + 300, y, [("weight      liquid", True)], 15)
        y -= 40
    y -= 20
    y = text(c, y, "2.", [[("Write 1 more thing you could ", False), ("weigh", True), (":", False)]])
    blank(c, MARGIN + 30, y - 16, 300)
    y -= 70
    y = text(c, y, "3.", [[("Write 1 more thing that is a ", False), ("liquid", True), (":", False)]])
    blank(c, MARGIN + 30, y - 16, 300)
    footer(c, *L8, 34)


# ---------------------------------------------------------------- Lesson 14

def page_63(c):
    y = start(c, "Lesson 14 Homework", "TEKS 3.2D", "Line up the numbers. Compare from the left.")
    y = text(c, y, "1.", [[("Order from ", False), ("greatest", True), (" to ", False), ("least", True), (".", False)]])
    nums = [2410, 4422, 2130, 5080]
    stacked(c, MARGIN + 60, y - 20, nums, size=20)
    sentence(c, MARGIN + 30, y - 160, "______|  >  |______|  >  |______|  >  |______", size=16, wide_w=70)
    rich_line(c, MARGIN + 30, y - 184, [("greatest", False)], 11)
    rich_line(c, W - MARGIN - 110, y - 184, [("least", False)], 11)
    y -= 250
    y = text(c, y, "2.", [[("Order from ", False), ("least", True), (" to ", False), ("greatest", True), (".", False)]])
    stacked(c, MARGIN + 60, y - 20, [9120, 3908, 6666, 6660], size=20)
    sentence(c, MARGIN + 30, y - 160, "______|  <  |______|  <  |______|  <  |______", size=16, wide_w=70)
    rich_line(c, MARGIN + 30, y - 184, [("least", False)], 11)
    rich_line(c, W - MARGIN - 110, y - 184, [("greatest", False)], 11)
    footer(c, *L14, 63)


# ---------------------------------------------------------------- Lesson 15

def page_67(c):
    y = start(c, "Lesson 15 Homework", "TEKS 3.4B", HILL_TIP)
    y = text(c, y, "1.", [[("Round each length to the nearest ", False), ("10 cm", True), (".", False)]])
    hill_grid(c, y - 10, [("a. Desk length", 66, 60, 10, "cm"), ("b. Desk width", 48, 40, 10, "cm"),
                          ("c. Door width", 81, 80, 10, "cm")], cols=3)
    y -= 230
    y = text(c, y, "2.", [[("Gym class ends at ", False), ("10:27", True), (". Round to the nearest ", False),
                          ("10 minutes", True), (".", False)]])
    hill(c, MARGIN + 80, y - 120, 300, 20, 10, labels=("10:20", "10:25", "10:30"))
    sentence(c, MARGIN + 30, y - 170, "Gym ends at about  |______|  a.m.", size=15, wide_w=80)
    footer(c, *L15, 67)


def page_68(c):
    y = start(c, "Lesson 15 Homework", "TEKS 3.4B", HILL_TIP)
    y = text(c, y, "", [[("Round each to the nearest ", False), ("10", True), (".", False)]])
    hill_grid(c, y - 10, [("3. Water in the beaker:", 23, 20, 10, "mL"),
                          ("4. The dog weighs:", 47, 40, 10, "pounds"),
                          ("5. The apples weigh:", 57, 50, 10, "ounces")], cols=1, row_h=180)
    footer(c, *L15, 68)


# ---------------------------------------------------------------- Lesson 16

def page_71(c):
    y = start(c, "Lesson 16 Homework", "TEKS 3.4B", HILL_TIP)
    y = text(c, y, "1.", [[("Round to the nearest ", False), ("ten", True), (".", False)]])
    hill_grid(c, y - 10, [("a.", 43, 40, 10), ("b.", 48, 40, 10), ("c.", 73, 70, 10), ("d.", 173, 170, 10)],
              cols=2, row_h=230)
    footer(c, *L16, 71)


def page_72(c):
    y = start(c, "Lesson 16 Homework", "TEKS 3.4B, 3.4A", HILL_TIP)
    y = text(c, y, "2.", [[("Round each weight to the nearest ", False), ("10 ounces", True), (".", False)]])
    hill_grid(c, y - 10, [("a. Oranges", 45, 40, 10, "oz"), ("b. Apples", 672, 670, 10, "oz")], cols=2)
    y -= 220
    y = text(c, y, "3.", [[("One water bottle holds ", False), ("17", True), (" fluid ounces. How much do ", False),
                          ("2", True), (" bottles hold?", False)]])
    sentence(c, MARGIN + 30, y - 20, "17 + 17 = |______|  fluid ounces", size=16, wide_w=70)
    rich_line(c, MARGIN + 30, y - 60, [("Now round your answer to the nearest 10:", False)], 13)
    hill(c, MARGIN + 80, y - 180, 300, 30, 10)
    sentence(c, MARGIN + 30, y - 226, "______|  ≈  |______|  fluid ounces", size=15, wide_w=70)
    footer(c, *L16, 72)


# ---------------------------------------------------------------- Lesson 17

def page_75(c):
    y = start(c, "Lesson 17 Homework", "TEKS 3.4B", HILL_TIP)
    y = text(c, y, "1.", [[("Round to the nearest ", False), ("hundred", True), (".", False)]])
    hill_grid(c, y - 10, [("a.", 156, 100, 100), ("b.", 342, 300, 100), ("c.", 260, 200, 100), ("d.", 1260, 1200, 100)],
              cols=2, row_h=230)
    footer(c, *L17, 75)


def page_76(c):
    y = start(c, "Lesson 17 Homework", "TEKS 3.4B", HILL_TIP)
    y = text(c, y, "2.", [[("Round each to the nearest ", False), ("hundred", True), (".", False)]])
    hill_grid(c, y - 10, [("a. Cards", 217, 200, 100), ("b. People", 462, 400, 100),
                          ("c. Juice", 386, 300, 100, "mL")], cols=3)
    y -= 240
    y = text(c, y, "3.", [[("Circle the numbers that round to ", False), ("400", True), (".", False)]])
    zone_line(c, y - 40, 300, 500, 50, (350, 450), "these round to 400")
    c.setFont("Sans-Bold", 18)
    for k, v in enumerate([368, 342, 420, 492, 449, 464]):
        c.drawCentredString(MARGIN + 45 + k * 86, y - 110, str(v))
    footer(c, *L17, 76)


# ---------------------------------------------------------------- Lesson 18

def page_79(c):
    y = start(c, "Lesson 18 Homework", "TEKS 3.4B", "Nearest ten: look at the ones.  Nearest hundred: look at the tens.")
    y = text(c, y, "1.", [[("Round to the place in ", False), ("bold", True), (".", False)]])
    hill_grid(c, y - 10, [("a. hundred:", 1242, 1200, 100), ("b. ten:", 2976, 2970, 10),
                          ("c. hundred:", 923, 900, 100), ("d. ten:", 15819, 15810, 10)], cols=2, row_h=230)
    footer(c, *L18, 79)


def page_80(c):
    y = start(c, "Lesson 18 Homework", "TEKS 3.4B, 3.2D", HILL_TIP)
    y = text(c, y, "2.", [[("Circle the number that rounds to ", False), ("6,000", True), (" (nearest hundred).", False)]])
    zone_line(c, y - 40, 5900, 6100, 50, (5950, 6050), "these round to 6,000")
    c.setFont("Sans-Bold", 17)
    for k, v in enumerate([5499, 6729, 6192, 5932, 6004]):
        c.drawCentredString(MARGIN + 50 + k * 104, y - 100, fmt(v))
    y -= 140
    y = text(c, y, "3.", [[("Saturday: ", False), ("4,519", True), (" fans.  Sunday: ", False), ("4,572", True), (" fans.", False)],
                         [("Which day had about ", False), ("4,600", True), (" fans?", False)]])
    hill(c, MARGIN + 80, y - 100, 300, 4500, 100)
    sentence(c, MARGIN + 30, y - 150, "4,519 ≈ |______|      4,572 ≈ |______", size=14, wide_w=64)
    rich_line(c, MARGIN + 30, y - 180, [("Circle:  ", False), ("Saturday    Sunday", True)], 14)
    y -= 220
    y = text(c, y, "4.", [[("Round ", False), ("4,358", True), (" two ways.", False)]])
    sentence(c, MARGIN + 30, y - 20, "Nearest hundred:  |______          Nearest ten:  |______", size=14, wide_w=64)
    footer(c, *L18, 80)


BOOK = {34: page_34, 63: page_63, 67: page_67, 68: page_68, 71: page_71, 72: page_72,
        75: page_75, 76: page_76, 79: page_79, 80: page_80}

if __name__ == "__main__":
    main("G3_M2_Homework_Simplified.pdf", [BOOK[k] for k in sorted(BOOK)], "Grade 3 Module 2 Homework – Simplified")
