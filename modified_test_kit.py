"""Reusable layout kit for MODIFIED tests and checks (Grade 3).

Design rules (apply to every modified test):
  1. One question per page. Lots of white space. Nothing decorative.
  2. Big, plain print: question 17 pt, choices 16 pt. Short sentences, one idea per line.
  3. Key numbers in bold. Color only when the word names the color (yellow strip, red strip).
  4. One picture per question that SHOWS the math (strip diagram, groups, chart).
  5. One "Do this" step line, then the answer. No extra helper boxes.
  6. Paper test: 3 answer choices (most obviously wrong choice removed), big bubbles.
  7. Computer helper sheet: same picture, all 4 choices in the computer's order.
"""
from reportlab.lib.colors import HexColor, black, white

from build_module2 import MARGIN, W, rich_line

INK = HexColor("#222222")
SOFT = HexColor("#9A9A9A")
STEP_BG = HexColor("#F2F2F2")
COLORS = {"yellow": HexColor("#FBE7A1"), "red": HexColor("#F4B6B0"), "blue": HexColor("#BFD8F2"),
          "grey": HexColor("#E6E6E6"), "none": white}


def ask(c, y, num, lines, size=17, lead=26):
    """Question number in a dark circle, then short lines."""
    c.setFillColor(INK)
    c.circle(MARGIN + 13, y + 6, 14, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Sans-Bold", 14)
    c.drawCentredString(MARGIN + 13, y + 1, str(num))
    c.setFillColor(black)
    for parts in lines:
        rich_line(c, MARGIN + 40, y, parts, size)
        y -= lead
    return y


def step(c, y, parts, size=15):
    """The single 'Do this' line, on a light grey band."""
    c.setFillColor(STEP_BG)
    c.roundRect(MARGIN, y - 10, W - 2 * MARGIN, 32, 6, stroke=0, fill=1)
    c.setFillColor(black)
    rich_line(c, MARGIN + 12, y, [("Do this: ", True)] + parts, size)
    return y - 44


def choice_boxes(c, y, items, size=16, h=44, gap=14, pics=None):
    """Big answer boxes: bubble, letter, text. pics[i](c, x, y_mid) can draw a small picture on the right."""
    for k, (letter, text) in enumerate(items):
        top = y - k * (h + gap)
        c.setStrokeColor(SOFT)
        c.roundRect(MARGIN + 20, top - h, W - 2 * MARGIN - 40, h, 8)
        c.setStrokeColor(black)
        if len(letter) == 1:
            c.circle(MARGIN + 46, top - h / 2, 11)
        c.setFont("Sans-Bold", 13 if len(letter) == 1 else 11)
        c.drawCentredString(MARGIN + 46, top - h / 2 - 4.5, letter)
        rich_line(c, MARGIN + 72, top - h / 2 - 6, text if isinstance(text, list) else [(text, False)], size)
        if pics and pics[k]:
            pics[k](c, W - MARGIN - 150, top - h / 2)
    return y - len(items) * (h + gap)


def strip(c, x, y, name, parts, unit_w, color="none", h=30, label_w=70, size=14):
    """One bar: name on the left, equal boxes. parts = list of labels. Returns right edge x."""
    c.setFont("Sans-Bold", 13)
    c.drawRightString(x + label_w - 10, y - h / 2 - 5, name)
    x0 = x + label_w
    for k, lab in enumerate(parts):
        c.setFillColor(COLORS[color])
        c.rect(x0 + k * unit_w, y - h, unit_w, h, stroke=1, fill=1)
        c.setFillColor(black)
        c.setFont("Sans-Bold", size)
        c.drawCentredString(x0 + k * unit_w + unit_w / 2, y - h / 2 - 5, lab)
    return x0 + len(parts) * unit_w


def brace_under(c, x0, x1, y, label, size=15):
    c.line(x0, y, x0, y - 7)
    c.line(x1, y, x1, y - 7)
    c.line(x0, y - 7, x1, y - 7)
    c.setFont("Sans-Bold", size)
    c.drawCentredString((x0 + x1) / 2, y - 26, label)


def dot_groups(c, x, y, groups, per, r=5, gap=13, group_gap=22, fill=INK, ring=True):
    """Draw `groups` groups of `per` dots in rows of 3, each group in a light ring. Returns right edge."""
    rows = (per + 2) // 3
    gw = 3 * gap
    for g in range(groups):
        gx = x + g * (gw + group_gap)
        if ring:
            c.setStrokeColor(SOFT)
            c.roundRect(gx - 8, y - rows * gap - 4, gw + 4, rows * gap + 12, 8)
            c.setStrokeColor(black)
        c.setFillColor(fill)
        for k in range(per):
            c.circle(gx + (k % 3) * gap + r - 2, y - (k // 3) * gap, r, stroke=0, fill=1)
        c.setFillColor(black)
    return x + groups * (gw + group_gap)


def answer_line(c, x, y, before, after="", w=80, size=17):
    c.setFont("Sans-Bold", size)
    c.drawString(x, y, before)
    x += c.stringWidth(before, "Sans-Bold", size) + 8
    c.setLineWidth(1.5)
    c.line(x, y - 4, x + w, y - 4)
    c.setLineWidth(1)
    c.drawString(x + w + 8, y, after)
