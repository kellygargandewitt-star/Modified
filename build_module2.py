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


def header(c, title):
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
    c.drawRightString(W - MARGIN - 52, top - 15, title + " (Modified)")

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
    c.drawString(MARGIN, 44, f"Lesson {lesson}:")
    c.setFont("Sans", 9)
    c.drawString(MARGIN + 62, 44, objective)
    c.setFont("Sans-Bold", 14)
    c.drawCentredString(W / 2, 22, f"Page {page_no}")


def helper_box(c, x, y, w, title, lines):
    """Key-word helper box. lines are lists of (text, bold) parts."""
    h = 30 + 20 * len(lines)
    c.setFillColor(HELP_BG)
    c.setStrokeColor(HELP_LINE)
    c.setLineWidth(1.5)
    c.roundRect(x, y - h, w, h, 8, stroke=1, fill=1)
    c.setFillColor(HELP_LINE)
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


PAGES = [page_93, page_95, page_109]


def main(out="G3_M2_Modified.pdf"):
    c = canvas.Canvas(out, pagesize=letter)
    c.setTitle("Bluebonnet Learning Grade 3 Module 2 – Modified")
    for draw in PAGES:
        draw(c)
        c.showPage()
    c.save()
    print("wrote", out)


if __name__ == "__main__":
    main()
