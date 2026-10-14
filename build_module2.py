"""Build modified pages for Bluebonnet Learning Grade 3, Module 2 (Learn book).

Supports for students with IEPs: friendlier numbers, number sentences set up,
simplified directions with bold key words, and a key-word helper box.
Each modified page keeps the original book's page number at the bottom.

Run: python3 build_module2.py  ->  writes G3_M2_Modified.pdf
"""
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("Sans", FONT_DIR + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Bold", FONT_DIR + "DejaVuSans-Bold.ttf"))

W, H = letter
MARGIN = 45
DARK = HexColor("#333333")
LIGHT = HexColor("#D9D9D9")
HELP_BG = HexColor("#EEF5FF")
HELP_LINE = HexColor("#4A78B5")


def rich_line(c, x, y, parts, size):
    """Draw text made of (text, bold) parts on one line."""
    for text, bold in parts:
        font = "Sans-Bold" if bold else "Sans"
        c.setFont(font, size)
        c.drawString(x, y, text)
        x += pdfmetrics.stringWidth(text, font, size)
    return x


def header(c, title, suffix=" (Modified)"):
    top = H - 40
    c.setFillColor(DARK)
    c.rect(MARGIN, top - 22, 240, 22, stroke=0, fill=1)
    c.setFillColor(LIGHT)
    c.rect(MARGIN + 242, top - 22, W - 2 * MARGIN - 242 - 44, 22, stroke=0, fill=1)
    c.setFillColor(DARK)
    c.rect(W - MARGIN - 42, top - 22, 42, 22, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Sans-Bold", 10)
    c.drawString(MARGIN + 8, top - 15, "BLUEBONNET LEARNING K–5 MATH")
    c.drawCentredString(W - MARGIN - 21, top - 16, "3 • 2")
    c.setFillColor(black)
    c.setFont("Sans-Bold", 9)
    c.drawRightString(W - MARGIN - 52, top - 15, title + suffix)

    c.setFont("Sans", 12)
    y = top - 52
    c.drawString(MARGIN, y, "Name")
    c.line(MARGIN + 42, y - 2, MARGIN + 300, y - 2)
    c.drawString(MARGIN + 330, y, "Date")
    c.line(MARGIN + 365, y - 2, W - MARGIN, y - 2)
    return y - 30


def footer(c, lesson, objective, page_no):
    c.setStrokeColor(LIGHT)
    c.setLineWidth(3)
    c.line(MARGIN, 62, W - MARGIN, 62)
    c.setLineWidth(1)
    c.setStrokeColor(black)
    c.setFont("Sans-Bold", 9)
    label = lesson if isinstance(lesson, str) else f"Lesson {lesson}:"
    c.drawString(MARGIN, 44, label)
    c.setFont("Sans", 9)
    c.drawString(MARGIN + pdfmetrics.stringWidth(label, "Sans-Bold", 9) + 8, 44, objective)
    c.setFont("Sans-Bold", 14)
    c.drawCentredString(W / 2, 22, f"Page {page_no}")


def helper_box(c, x, y, w, title, lines, bg=HELP_BG, edge=HELP_LINE):
    """Key-word helper box. lines are lists of (text, bold) parts."""
    h = 30 + 20 * len(lines)
    c.setFillColor(bg)
    c.setStrokeColor(edge)
    c.setLineWidth(1.5)
    c.roundRect(x, y - h, w, h, 8, stroke=1, fill=1)
    c.setFillColor(edge)
    c.setFont("Sans-Bold", 12)
    c.drawString(x + 12, y - 20, title)
    c.setFillColor(black)
    ty = y - 42
    for parts in lines:
        rich_line(c, x + 16, ty, parts, 12)
        ty -= 20
    c.setLineWidth(1)
    c.setStrokeColor(black)
    return y - h


def number_line(c, x0, x1, y, start, end, circle=None):
    c.setLineWidth(1.5)
    c.line(x0 - 12, y, x1 + 12, y)
    # arrows
    for xe, d in ((x0 - 12, -1), (x1 + 12, 1)):
        c.line(xe, y, xe - 7 * d, y + 5)
        c.line(xe, y, xe - 7 * d, y - 5)
    step = (x1 - x0) / (end - start)
    for i, n in enumerate(range(start, end + 1)):
        tx = x0 + i * step
        c.line(tx, y - 7, tx, y + 7)
        bold = n == circle
        c.setFont("Sans-Bold" if bold else "Sans", 12 if bold else 11)
        c.drawCentredString(tx, y - 24, str(n))
        if bold:
            c.circle(tx, y - 20, 16)
    c.setLineWidth(1)


def blank(c, x, y, w=70):
    c.line(x, y - 3, x + w, y - 3)
    return x + w


# ---------------------------------------------------------------- pages

def page_93(c):
    """Lesson 14 Application Problem.  Original: ___ < 407 < ___"""
    n = 405  # friendlier number (original 407)
    y = header(c, "Lesson 14 Application Problem")

    c.setFont("Sans", 9)
    c.setFillColor(HexColor("#666666"))
    c.drawRightString(W - MARGIN, y + 8, "TEKS 3.2D")
    c.setFillColor(black)

    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", [
        [("<", True), ("  means  ", False), ("less than", True), ("  (smaller)", False)],
        [(">", True), ("  means  ", False), ("greater than", True), ("  (bigger)", False)],
        [("The small point of  <  is next to the ", False), ("smaller", True), (" number.", False)],
    ])

    y -= 40
    rich_line(c, MARGIN, y, [("Write a ", False), ("smaller", True), (" number and a ", False),
                             ("bigger", True), (" number.", False)], 15)
    y -= 24
    rich_line(c, MARGIN, y, [("Use the number line to help.", False)], 15)

    y -= 60
    number_line(c, MARGIN + 30, W - MARGIN - 30, y, 400, 410, circle=n)

    y -= 80
    rich_line(c, MARGIN, y, [("Step 1:", True), ("  1 less than ", False), (str(n), True), (" is", False)], 15)
    x = rich_line(c, MARGIN + 270, y, [(f"{n} − 1 = ", True)], 18)
    blank(c, x + 4, y)

    y -= 50
    rich_line(c, MARGIN, y, [("Step 2:", True), ("  1 more than ", False), (str(n), True), (" is", False)], 15)
    x = rich_line(c, MARGIN + 270, y, [(f"{n} + 1 = ", True)], 18)
    blank(c, x + 4, y)

    y -= 60
    rich_line(c, MARGIN, y, [("Step 3:", True), ("  Write your numbers in the number sentence.", False)], 15)

    y -= 70
    size = 30
    parts_w = 110 + pdfmetrics.stringWidth(f"  <  {n}  <  ", "Sans-Bold", size) + 110
    x = (W - parts_w) / 2
    x = blank(c, x, y, 110)
    x = rich_line(c, x, y, [(f"  <  {n}  <  ", True)], size)
    blank(c, x, y, 110)
    c.setFont("Sans", 11)
    c.drawCentredString((W - parts_w) / 2 + 55, y - 22, "smaller")
    c.drawCentredString(x + 55, y - 22, "bigger")

    footer(c, 14, "Order whole numbers using place value and number lines.", 93)


def wrap_center(c, text, cx, y, font, size, width):
    """Draw text centered, wrapping words onto extra lines as needed."""
    words, lines, cur = text.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = wd
    lines.append(cur)
    c.setFont(font, size)
    for i, ln in enumerate(lines):
        c.drawCentredString(cx, y - i * (size + 1), ln)


def pv_chart(c, x, y, w, places, numbers, shade):
    """Place value chart with the digits filled in. Returns bottom y."""
    cols = len(places)
    cw, hh, rh = w / cols, 34, 32
    rows = len(numbers)
    # shaded column = the place to compare first
    if shade is not None:
        c.setFillColor(HexColor("#FFF2B3"))
        c.rect(x + shade * cw, y - hh - rows * rh, cw, hh + rows * rh, stroke=0, fill=1)
        c.setFillColor(black)
    c.setLineWidth(1)
    c.rect(x, y - hh - rows * rh, w, hh + rows * rh)
    for i in range(1, cols):
        c.line(x + i * cw, y, x + i * cw, y - hh - rows * rh)
    for r in range(rows + 1):
        c.line(x, y - hh - r * rh, x + w, y - hh - r * rh)
    for i, p in enumerate(places):
        wrap_center(c, p, x + (i + 0.5) * cw, y - 14, "Sans-Bold", 7, cw - 6)
    for r, num in enumerate(numbers):
        digits = str(num).rjust(cols)
        for i, d in enumerate(digits):
            if d != " ":
                c.setFont("Sans-Bold" if i == shade else "Sans", 16)
                c.drawCentredString(x + (i + 0.5) * cw, y - hh - r * rh - 22, d)
    return y - hh - rows * rh


def order_list(c, cx, y, sign, top_label, bottom_label, n=4):
    """Vertical answer blanks with < or > between them."""
    for i in range(n):
        c.line(cx - 55, y, cx + 55, y)
        c.setFont("Sans", 10)
        if i == 0:
            c.drawString(cx + 62, y + 2, top_label)
        if i == n - 1:
            c.drawString(cx + 62, y + 2, bottom_label)
        if i < n - 1:
            c.setFont("Sans-Bold", 16)
            c.drawCentredString(cx, y - 19, sign)
        y -= 36


def page_95(c):
    """Lesson 14 Problem Set.
    Original 1: 4,901  5,673  4,499  5,034  (least to greatest)
    Original 2: 66,675  67,689  66,896  67,547  (greatest to least)"""
    y = header(c, "Lesson 14 Problem Set")
    c.setFont("Sans", 9)
    c.setFillColor(HexColor("#666666"))
    c.drawRightString(W - MARGIN, y + 8, "TEKS 3.2D")
    c.setFillColor(black)

    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", [
        [("least", True), (" = smallest       ", False), ("greatest", True), (" = biggest", False)],
        [("Look at the ", False), ("yellow", True), (" place first. A bigger digit there = a bigger number.", False)],
    ])

    y -= 14
    gap = 16
    colw = (W - 2 * MARGIN - gap) / 2
    problems = [
        (1, [("Put the numbers in order", False)],
         [("from ", False), ("least", True), (" to ", False), ("greatest", True), (".", False)],
         ["Thousands", "Hundreds", "Tens", "Ones"],
         [4321, 6152, 2743, 5014], "<", "least", "greatest"),
        (2, [("Put the numbers in order", False)],
         [("from ", False), ("greatest", True), (" to ", False), ("least", True), (".", False)],
         ["Ten Thousands", "Thousands", "Hundreds", "Tens", "Ones"],
         [36215, 58402, 17630, 42571], ">", "greatest", "least"),
    ]
    box_top = y
    box_bottom = 80
    for k, (num, l1, l2, places, nums, sign, top, bottom) in enumerate(problems):
        x = MARGIN + k * (colw + gap)
        c.rect(x, box_bottom, colw, box_top - box_bottom)
        ty = box_top - 22
        rich_line(c, x + 10, ty, [(f"{num}. ", True)] + l1, 13)
        rich_line(c, x + 28, ty - 18, l2, 13)
        ty -= 44
        nums_txt = "   ".join(f"{n:,}" for n in nums)
        c.setFont("Sans-Bold", 12)
        c.drawCentredString(x + colw / 2, ty, nums_txt)
        ty = pv_chart(c, x + 10, ty - 14, colw - 20, places, nums, shade=0)
        ty -= 26
        c.setFont("Sans", 11)
        c.drawString(x + 10, ty, "Write the numbers in order:")
        order_list(c, x + colw / 2 - 25, ty - 34, sign, top, bottom)

    footer(c, 14, "Order whole numbers using place value and number lines.", 95)


def vertical_line(c, x, top, bottom, low, example=None):
    """Vertical number line labeled low, low+5, low+10 (bottom to top)."""
    c.setLineWidth(2)
    c.line(x, bottom - 14, x, top + 14)
    for ye, d in ((top + 14, 1), (bottom - 14, -1)):
        c.line(x, ye, x - 5, ye - 7 * d)
        c.line(x, ye, x + 5, ye - 7 * d)
    mid = (top + bottom) / 2
    for yy, n in ((bottom, low), (mid, low + 5), (top, low + 10)):
        c.line(x - 9, yy, x + 9, yy)
        c.setFont("Sans", 12)
        c.drawString(x + 14, yy - 4, str(n))
    if example is not None:
        ey = bottom + (example - low) / 10 * (top - bottom)
        c.circle(x, ey, 3.5, stroke=0, fill=1)
        c.setFont("Sans-Bold", 12)
        c.drawString(x + 14, ey - 4, str(example))
    c.setLineWidth(1)


def page_109(c):
    """Lesson 16 Problem Set: round to the nearest ten on a vertical number line.
    Original: a 32 (modeled), b 36, c 62, d 162, e 278, f 405"""
    y = header(c, "Lesson 16 Problem Set")
    c.setFont("Sans", 9)
    c.setFillColor(HexColor("#666666"))
    c.drawRightString(W - MARGIN, y + 8, "TEKS 3.4B")
    c.setFillColor(black)

    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", [
        [("≈", True), ("  means  ", False), ("about", True)],
        [("Look at the ", False), ("ones", True), (" digit:   ", False),
         ("0, 1, 2, 3, 4", True), (" → round ", False), ("down", True), ("     ", False),
         ("5, 6, 7, 8, 9", True), (" → round ", False), ("up", True)],
    ])

    y -= 22
    rich_line(c, MARGIN, y, [("1. ", True), ("Round to the nearest ", False), ("ten", True),
                             (". Put a dot on the number line.", False)], 13)

    items = [("a", 32, True), ("b", 36, False), ("c", 64, False),
             ("d", 17, False), ("e", 128, False), ("f", 143, False)]
    top, bottom = y - 14, 80
    cw, ch = (W - 2 * MARGIN) / 2, (top - bottom) / 3
    for i, (letter_, n, shown) in enumerate(items):
        col, row = i % 2, i // 2
        x0, y0 = MARGIN + col * cw, top - row * ch
        c.rect(x0, y0 - ch, cw, ch)
        low = n // 10 * 10
        ty = y0 - 26
        x = rich_line(c, x0 + 10, ty, [(f"{letter_}.  ", False), (f"{n} ≈ ", True)], 16)
        blank(c, x + 2, ty, 55)
        rich_line(c, x0 + 10, ty - 32, [("Between ", False), (str(low), True),
                                        (" and ", False), (str(low + 10), True)], 11)
        rich_line(c, x0 + 10, ty - 58, [("Closer to:", False)], 11)
        blank(c, x0 + 80, ty - 58, 55)
        if shown:
            c.setFont("Sans", 9)
            c.setFillColor(HexColor("#666666"))
            c.drawString(x0 + 10, ty - 84, "(Example: the dot is shown.)")
            c.setFillColor(black)
        vertical_line(c, x0 + cw - 70, y0 - 28, y0 - ch + 28, low,
                      example=n if shown else None)

    footer(c, 16, "Round two- and three-digit numbers to the nearest ten on the vertical number line.", 109)


def teks(c, y, label):
    c.setFont("Sans", 9)
    c.setFillColor(HexColor("#666666"))
    c.drawRightString(W - MARGIN, y + 8, label)
    c.setFillColor(black)


ROUND_TEN_HELP = [
    [("≈", True), ("  means  ", False), ("about", True)],
    [("Look at the ", False), ("ones", True), (" digit:   ", False),
     ("0, 1, 2, 3, 4", True), (" → round ", False), ("down", True), ("     ", False),
     ("5, 6, 7, 8, 9", True), (" → round ", False), ("up", True)],
]


def page_110(c):
    """Lesson 16 Problem Set (continued).
    Original 2: animals 26, 52, 142 pounds.  Original 3: 29 min + 19 min, then round."""
    y = header(c, "Lesson 16 Problem Set")
    teks(c, y, "TEKS 3.4A, 3.4B")
    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", ROUND_TEN_HELP)

    y -= 22
    rich_line(c, MARGIN, y, [("2. ", True), ("Round each animal's weight to the nearest ", False),
                             ("10 pounds", True), (".", False)], 13)
    y -= 12
    cols = [140, 190, W - 2 * MARGIN - 330]
    heads = ["Animal", "Number Line", "Round to the nearest 10"]
    hh, rh = 26, 96
    x = MARGIN
    c.setFillColor(LIGHT)
    c.rect(MARGIN, y - hh, W - 2 * MARGIN, hh, stroke=0, fill=1)
    c.setFillColor(black)
    for w_, h_ in zip(cols, heads):
        c.setFont("Sans-Bold", 11)
        c.drawCentredString(x + w_ / 2, y - 17, h_)
        x += w_
    animals = [("cheetah", 27), ("dog", 53), ("sheep", 84)]
    table_bottom = y - hh - rh * len(animals)
    c.rect(MARGIN, table_bottom, W - 2 * MARGIN, y - table_bottom)
    c.line(MARGIN + cols[0], y, MARGIN + cols[0], table_bottom)
    c.line(MARGIN + cols[0] + cols[1], y, MARGIN + cols[0] + cols[1], table_bottom)
    for i, (img, n) in enumerate(animals):
        ry = y - hh - i * rh
        c.line(MARGIN, ry, W - MARGIN, ry)
        c.drawImage(f"images/{img}.png", MARGIN + 14, ry - 66, width=64, height=58,
                    preserveAspectRatio=True, mask="auto")
        c.setFont("Sans-Bold", 13)
        c.drawRightString(MARGIN + cols[0] - 10, ry - 86, f"{n} pounds")
        low = n // 10 * 10
        vertical_line(c, MARGIN + cols[0] + 80, ry - 22, ry - rh + 22, low)
        x2 = MARGIN + cols[0] + cols[1] + 14
        rich_line(c, x2, ry - 38, [("Between ", False), (str(low), True), (" and ", False),
                                   (str(low + 10), True)], 11)
        xx = rich_line(c, x2, ry - 70, [(f"{n} ≈ ", True)], 15)
        blank(c, xx + 2, ry - 70, 50)
        c.setFont("Sans", 11)
        c.drawString(xx + 58, ry - 70, "pounds")

    y = table_bottom - 26
    rich_line(c, MARGIN, y, [("3. ", True), ("Mrs. Smith washes her car for ", False), ("22 minutes", True),
                             (". She weeds her garden for ", False), ("15 minutes", True), (".", False)], 12)
    y -= 30
    rich_line(c, MARGIN + 18, y, [("a. ", True), ("How many minutes in all?", True),
                                  ("   (in all → +)", False)], 12)
    y -= 30
    xx = rich_line(c, MARGIN + 40, y, [("22 + 15 = ", True)], 18)
    blank(c, xx + 4, y, 70)
    c.setFont("Sans", 12)
    c.drawString(xx + 82, y, "minutes")
    y -= 32
    rich_line(c, MARGIN + 18, y, [("b. ", True), ("Round your answer to the nearest ", False),
                                  ("10 minutes", True), (".", False)], 12)
    y -= 30
    x = blank(c, MARGIN + 40, y, 60)
    x = rich_line(c, x + 6, y, [(" ≈ ", True)], 18)
    blank(c, x + 6, y, 60)
    c.setFont("Sans", 12)
    c.drawString(x + 72, y, "minutes")

    footer(c, 16, "Round two- and three-digit numbers to the nearest ten on the vertical number line.", 110)


def page_111(c):
    """Lesson 16 Exit Ticket.  Original 1: a 26, b 276.  Original 2: Phong rounds 603 to 610."""
    y = header(c, "Lesson 16 Exit Ticket")
    teks(c, y, "TEKS 3.4B")
    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", ROUND_TEN_HELP)

    y -= 22
    rich_line(c, MARGIN, y, [("1. ", True), ("Round to the nearest ", False), ("ten", True),
                             (". Put a dot on the number line.", False)], 13)
    top = y - 14
    ch = 150
    cw = (W - 2 * MARGIN) / 2
    for i, (letter_, n) in enumerate([("a", 24), ("b", 137)]):
        x0 = MARGIN + i * cw
        c.rect(x0, top - ch, cw, ch)
        low = n // 10 * 10
        ty = top - 26
        x = rich_line(c, x0 + 10, ty, [(f"{letter_}.  ", False), (f"{n} ≈ ", True)], 16)
        blank(c, x + 2, ty, 55)
        rich_line(c, x0 + 10, ty - 34, [("Between ", False), (str(low), True),
                                        (" and ", False), (str(low + 10), True)], 11)
        rich_line(c, x0 + 10, ty - 60, [("Closer to:", False)], 11)
        blank(c, x0 + 80, ty - 60, 55)
        vertical_line(c, x0 + cw - 70, top - 28, top - ch + 28, low)

    y = top - ch - 34
    rich_line(c, MARGIN, y, [("2. ", True), ("Phong rounds ", False), ("42", True), (" to the nearest ten. He says it is ", False),
                             ("50", True), (".", False)], 13)
    y -= 22
    rich_line(c, MARGIN + 22, y, [("Is he correct?", True), ("  Use the number line to check.", False)], 13)

    vertical_line(c, W - MARGIN - 45, y - 30, y - 230, 40)

    ty = y - 50
    lines = [
        [("Put a dot on ", False), ("42", True), (" on the number line.", False)],
        None,
        [("42", True), (" is closer to  ", False)],
        None,
        [("42 ≈ ", True)],
        None,
        [("Circle one:     Phong is ", False), ("correct", True), ("   /   ", False), ("not correct", True)],
    ]
    for parts in lines:
        if parts is None:
            ty -= 18
            continue
        x = rich_line(c, MARGIN + 22, ty, parts, 13)
        if parts[0][0] in ("42",) or parts[0][0] == "42 ≈ ":
            blank(c, x + 4, ty, 60)
        ty -= 22

    ty -= 14
    rich_line(c, MARGIN + 22, ty, [("Finish the sentence:", True)], 13)
    ty -= 30
    x = rich_line(c, MARGIN + 22, ty, [("The ones digit is ", False)], 13)
    x = blank(c, x + 2, ty, 40)
    rich_line(c, x + 6, ty, [(", so I round  ", False), ("up", True), ("  /  ", False),
                             ("down", True), (".", False)], 13)

    footer(c, 16, "Round two- and three-digit numbers to the nearest ten on the vertical number line.", 111)


def disk(c, x, y, label, r=9):
    c.circle(x, y, r)
    c.setFont("Sans", 7 if len(label) > 2 else 8)
    c.drawCentredString(x, y - 3, label)


def page_113(c):
    """Lesson 17 Application Problem: draw place value disks.
    Original: 10 tens, 10 hundreds, 13 tens, 13 hundreds, 13 tens 8 ones, 13 hundreds 8 tens 7 ones"""
    y = header(c, "Lesson 17 Application Problem")
    teks(c, y, "TEKS 3.2A")
    y = helper_box(c, MARGIN, y, W - 2 * MARGIN, "Word Helper", [
        [("10 ones", True), (" = 1 ten      ", False), ("10 tens", True), (" = 1 hundred      ", False),
         ("10 hundreds", True), (" = 1 thousand", False)],
        [("Draw a circle for each disk. Write 1, 10, or 100 inside.", False)],
    ])
    y -= 22
    rich_line(c, MARGIN, y, [("Draw place value disks in the chart. Then fill in the blanks.", False)], 13)

    items = [
        ("10 tens", "10 tens = ___ hundred = ___", True),
        ("10 hundreds", "10 hundreds = ___ thousand = ___", False),
        ("12 tens", "12 tens = ___ hundred|___ tens = ___", False),
        ("12 hundreds", "12 hundreds = ___ thousand|___ hundreds = ___", False),
        ("12 tens 3 ones", "12 tens 3 ones = ___", False),
        ("11 hundreds 2 tens 4 ones", "11 hundreds 2 tens 4 ones = ___", False),
    ]
    top, bottom = y - 12, 80
    cw, ch = (W - 2 * MARGIN) / 2, (top - bottom) / 3
    places = ["Thousands", "Hundreds", "Tens", "Ones"]
    for i, (title, sentence, example) in enumerate(items):
        col, row = i % 2, i // 2
        x0, y0 = MARGIN + col * cw, top - row * ch
        c.rect(x0, y0 - ch, cw, ch)
        c.setFont("Sans-Bold", 13)
        c.drawString(x0 + 10, y0 - 20, f"{'abcdef'[i]}.  {title}")
        # labeled chart
        gx, gy, gw, gh = x0 + 10, y0 - 30, cw - 20, ch - 82
        pw = gw / 4
        c.rect(gx, gy - gh, gw, gh)
        for k in range(1, 4):
            c.line(gx + k * pw, gy, gx + k * pw, gy - gh)
        c.line(gx, gy - 14, gx + gw, gy - 14)
        for k, p in enumerate(places):
            c.setFont("Sans-Bold", 7.5)
            c.drawCentredString(gx + (k + 0.5) * pw, gy - 10, p)
        if example:
            # 10 ten-disks in the tens column, circled, arrow to 1 hundred
            tx = gx + 2.5 * pw
            for d in range(10):
                disk(c, tx - 13 + (d % 2) * 26, gy - 26 - (d // 2) * 15, "10", r=7)
            hx = gx + 1.5 * pw
            c.setStrokeColor(HELP_LINE)
            c.line(tx - 26, gy - 50, hx + 12, gy - 50)
            c.line(hx + 12, gy - 50, hx + 18, gy - 46)
            c.line(hx + 12, gy - 50, hx + 18, gy - 54)
            c.setStrokeColor(black)
            disk(c, hx, gy - 50, "100", r=10)
        # number sentence with blanks
        rows = sentence.split("|")
        sy = y0 - ch + 14 + 16 * (len(rows) - 1)
        for k, row_txt in enumerate(rows):
            parts = row_txt.split("___")
            x = x0 + 10 + (20 if k else 0)
            for j, part in enumerate(parts):
                x = rich_line(c, x, sy, [(part, True)], 10.5)
                if j < len(parts) - 1:
                    x = blank(c, x + 2, sy, 34) + 2
            sy -= 16
        if example:
            c.setFont("Sans", 8)
            c.setFillColor(HexColor("#666666"))
            c.drawRightString(x0 + cw - 8, y0 - 20, "(Example)")
            c.setFillColor(black)

    footer(c, 17, "Round to the nearest hundred on the vertical number line.", 113)


BOOK = {93: page_93, 95: page_95, 109: page_109, 110: page_110, 111: page_111, 113: page_113}


def all_pages():
    """Every modified page in book order, including the lesson files that import this one."""
    from lessons_15_19_simple import BOOK as l15  # simplified Lessons 15-19 (readiness TEKS only)
    from topic_e_simple import BOOK as l20  # simplified Topic E (readiness TEKS only)
    book = {**BOOK, **l15, **l20}
    return [book[k] for k in sorted(book)]


PAGES = list(BOOK.values())


def main(out="G3_M2_Modified.pdf", pages=None, title="Bluebonnet Learning Grade 3 Module 2 – Modified"):
    c = canvas.Canvas(out, pagesize=letter)
    c.setTitle(title)
    for draw in pages or PAGES:
        draw(c)
        c.showPage()
    c.save()
    print("wrote", out)


if __name__ == "__main__":
    main(pages=all_pages())
