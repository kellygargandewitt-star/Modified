"""Shared builder for Module 3 tests/checks: COMPUTER HELPER + SIMPLIFIED (see MODIFIED_TEST_RULES.md).

A test is a list of question functions q(c). Each one calls start(), qtext(), a picture, do_this(),
then pick() (multiple choice), yes_no() (select-all), or its own answer frames.
Global T holds the test being built; T.simp is True for the SIMPLIFIED version.
"""
from reportlab.lib.colors import HexColor, black, white

from build_module2 import MARGIN, W, footer, header, main, rich_line
from modified_test_kit import COLORS, INK, SOFT, ask, brace_under, choice_boxes, dot_groups, step, strip

ORD = ["1st", "2nd", "3rd", "4th", "5th"]
GREY = HexColor("#E6E6E6")


class T:
    title = ""
    foot = ""
    simp = False
    paper = False      # paper test: helper keeps the book's letters instead of 1st-4th


def start(c):
    suffix = " (Simplified)" if T.simp else (" (Helper)" if T.paper else " (Computer Helper)")
    return header(c, T.title, suffix=suffix, unit="3 • 3") - 44


def foot(c, n):
    footer(c, T.foot, ("Simplified" if T.simp else "Helper Sheet"), n)


def qtext(c, y, n, simple, helper=None):
    return ask(c, y, n, simple if (T.simp or helper is None) else helper, size=20 if T.simp else 17)


def do_this(c, y, parts):
    if isinstance(parts, str):
        parts = [(parts, False)]
    return step(c, y, parts, size=16 if T.simp else 15)


def pick(c, y, ask_line, two, four, size2=22, size4=15, h4=36):
    """two: [(label, text)] x2 for SIMPLIFIED; four: [(label or None, text)] for HELPER (None -> 1st, 2nd...)."""
    if T.simp:
        rich_line(c, MARGIN, y, [(ask_line, True)], 17)
        return choice_boxes(c, y - 20, two, size=size2, h=56, gap=18)
    rich_line(c, MARGIN, y, [(ask_line, True)], 15)
    if not T.paper:
        rich_line(c, MARGIN, y - 22, [("On the computer, the choices are in this order:", False)], 13)
        y -= 14
    items = [(lab or ORD[k], txt) for k, (lab, txt) in enumerate(four)]
    return choice_boxes(c, y - 22, items, size=size4, h=h4, gap=10)


def yes_no(c, y, ask_line, items, size=17):
    """Select-all questions as one yes / no per line."""
    rich_line(c, MARGIN, y, [(ask_line, True)], 17 if T.simp else 15)
    y -= 40
    for k, txt in enumerate(items):
        c.setStrokeColor(SOFT)
        c.roundRect(MARGIN + 20, y - 14, W - 2 * MARGIN - 40, 40, 8)
        c.setStrokeColor(black)
        rich_line(c, MARGIN + 36, y, txt if isinstance(txt, list) else [(txt, True)], size)
        rich_line(c, W - MARGIN - 130, y, [("yes    no", True)], 16)
        y -= 50
    return y


def fill(c, x, y, text, size=18, bw=46, bold=True):
    """Write text; every '___' is a blank line. Returns end x."""
    font = "Sans-Bold" if bold else "Sans"
    for k, chunk in enumerate(text.split("___")):
        if k:
            c.setLineWidth(1.5)
            c.line(x + 2, y - 4, x + bw, y - 4)
            c.setLineWidth(1)
            x += bw + 6
        c.setFont(font, size)
        c.drawString(x, y, chunk)
        x += c.stringWidth(chunk, font, size)
    return x


def lines(c, x, y, rows, size=18, gap=40):
    for r in rows:
        fill(c, x, y, r, size)
        y -= gap
    return y


def jump_line(c, x, y, labels, gap, jump, size=16):
    c.setLineWidth(2)
    c.line(x - 10, y, x + (len(labels) - 1) * gap + 20, y)
    c.setLineWidth(1)
    for k, lab in enumerate(labels):
        px = x + k * gap
        c.line(px, y - 8, px, y + 8)
        c.setFont("Sans-Bold", size)
        c.drawCentredString(px, y - 28, lab)
        if k:
            c.arc(px - gap, y + 2, px, y + 40, 0, 180)
            c.setFont("Sans", 10)
            c.drawCentredString(px - gap / 2, y + 45, jump)
    return y - 50


def strips(c, x, y, rows, uw, h=36, size=17, total=None, label_w=80):
    """rows: [(name, [labels], color)]. total: label under the last row (brace). Returns bottom y."""
    end = x
    for k, (name, parts, color) in enumerate(rows):
        end = strip(c, x, y - k * (h + 14), name, parts, uw, color, h=h, size=size, label_w=label_w)
    y -= len(rows) * (h + 14)
    if total:
        brace_under(c, x + label_w, end, y + 8, total, size=17)
        y -= 50
    return y - 10


def table(c, x, y, heads, rows, cw=90, rh=30, size=17, arrows=None):
    """Simple table. arrows: label drawn to the right between rows (e.g. '+ 7')."""
    for j, hd in enumerate(heads):
        c.setFillColor(GREY)
        c.rect(x + j * cw, y - rh, cw, rh, stroke=1, fill=1)
        c.setFillColor(black)
        c.setFont("Sans-Bold", 11 if len(hd) > 10 else 13)
        c.drawCentredString(x + j * cw + cw / 2, y - rh + 10, hd)
    for i, row in enumerate(rows):
        yy = y - (i + 2) * rh
        for j, v in enumerate(row):
            c.rect(x + j * cw, yy, cw, rh)
            c.setFont("Sans-Bold", size)
            c.drawCentredString(x + j * cw + cw / 2, yy + 9, str(v))
        if arrows and i:
            ax = x + len(heads) * cw + 8
            c.arc(ax - 12, yy + rh / 2, ax + 12, yy + rh * 1.5, -90, 180)
            c.setFont("Sans-Bold", 12)
            c.drawString(ax + 16, yy + rh - 4, arrows)
    return y - (len(rows) + 1) * rh


def place_chart(c, x, y, names, digits, cw=96, shade=(), values=None):
    for k, (p, d) in enumerate(zip(names, digits)):
        c.setFillColor(GREY if k in shade else white)
        c.rect(x + k * cw + 4, y - 60, cw - 8, 60, stroke=1, fill=1)
        c.setFillColor(black)
        c.setFont("Sans", 10)
        c.drawCentredString(x + k * cw + cw / 2, y - 16, p)
        c.setFont("Sans-Bold", 24)
        c.drawCentredString(x + k * cw + cw / 2, y - 48, d)
        if values:
            c.setFont("Sans-Bold", 14)
            c.drawCentredString(x + k * cw + cw / 2, y - 82, values[k])
    return y - (100 if values else 72)


def even_odd(c, x, y):
    """Ones-digit helper: even 0 2 4 6 8 / odd 1 3 5 7 9."""
    rich_line(c, x, y, [("Even ones digit:  ", False), ("0  2  4  6  8", True)], 15)
    rich_line(c, x, y - 26, [("Odd ones digit:   ", False), ("1  3  5  7  9", True)], 15)
    return y - 50


def build(spec, pages, paper=False):
    """spec: (title, footer label, out prefix). Writes <prefix>_Helper.pdf and <prefix>_Simplified.pdf."""
    T.title, T.foot = spec[0], spec[1]
    T.paper = paper
    for simp, suffix in ((False, "Helper"), (True, "Simplified")):
        T.simp = simp
        main(f"{spec[2]}_{suffix}.pdf", pages, f"Grade 3 Module 3 {spec[0]} – {suffix}")


__all__ = ["T", "start", "foot", "qtext", "do_this", "pick", "yes_no", "fill", "lines", "jump_line", "strips",
           "table", "place_chart", "even_odd", "build", "dot_groups", "rich_line", "MARGIN", "W", "INK", "SOFT",
           "GREY", "COLORS", "black", "white", "HexColor", "brace_under", "strip"]
