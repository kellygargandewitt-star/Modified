"""Simplified Topic E (Lessons 20-24, book pages 133-169) for Grade 3 Module 2.

Compared with lessons_20_24.py:
  * Readiness TEKS only: 3.4A (add/subtract within 1,000) and 3.5A (strip diagrams
    and equations for one- and two-step problems). Estimation (3.4B) is removed.
  * Less work: 1-4 problems per page. The book's problem numbers are kept so
    students can follow along; skipped problems are simply left out.
  * Less visual clutter: no colored boxes, pictures, or dashed lines; one plain
    tip line; larger print and more white space.

Run: python3 topic_e_simple.py  ->  writes G3_M2_TopicE_Simplified.pdf
"""
from reportlab.lib.colors import HexColor, black

from build_module2 import MARGIN, W, blank, footer, header, main, rich_line, teks
from lessons_20_24 import L20, L21, L22, L23, L24, bars, top_brace
from reteach_mid_module import sentence

SOFT = HexColor("#999999")


def start(c, title, teks_label, tip):
    y = header(c, title)
    teks(c, y, teks_label)
    rich_line(c, MARGIN, y - 6, [("Tip: ", True), (tip, False)], 12)
    return y - 44


def column(c, x, y, nums, op="+", cw=32, places=None):
    """Plain vertical frame: small regroup boxes, big digits, answer boxes. Returns bottom y.
    A None row is drawn as empty boxes for the student to copy a number into."""
    if places is None:
        known = [n for n in nums if n is not None]
        places = max(len(str(n)) for n in known)
        if op == "+" and None not in nums:
            places = max(places, len(str(sum(nums))))
    ox = x + 18
    c.setStrokeColor(SOFT)
    c.setLineWidth(0.6)
    lift = 8 if nums[0] is None else 0
    for k in range(places - 1):
        c.rect(ox + k * cw + 8, y - 16 + lift, cw - 16, 14)
    c.setStrokeColor(black)
    c.setLineWidth(1)
    ry = y - 38
    for r, n in enumerate(nums):
        if n is None:
            for k in range(places):
                c.rect(ox + k * cw + 3, ry - 5, cw - 6, 22)
        else:
            for k, d in enumerate(str(n).rjust(places)):
                c.setFont("Sans", 20)
                c.drawCentredString(ox + k * cw + cw / 2, ry, d)
        if r == len(nums) - 1:
            c.setFont("Sans", 20)
            c.drawCentredString(x + 6, ry, op)
        ry -= 26
    c.setLineWidth(1.5)
    c.line(x, ry + 18, ox + places * cw, ry + 18)
    c.setLineWidth(1)
    for k in range(places):
        c.rect(ox + k * cw + 3, ry - 16, cw - 6, 28)
    return ry - 16


def text(c, y, num, lines, size=14):
    for k, parts in enumerate(lines):
        if k == 0 and num:
            rich_line(c, MARGIN, y, [(num + "  ", True)] + parts, size)
        else:
            rich_line(c, MARGIN + (24 if num else 0), y, parts, size)
        y -= 22
    return y


def block(c, y, num, lines, model=None, sents=(), col=None, col_op="+"):
    """One word problem: text, optional strip diagram, number sentences (left), column (right)."""
    y = text(c, y, num, lines)
    top = y - 10
    if col:
        cb = column(c, W - MARGIN - 130, top, col, col_op)
    if model:
        y = model(c, y - 14) - 18
    else:
        y -= 10
    for s in sents:
        y -= 30
        sentence(c, MARGIN + 24, y, s, size=16, blank_w=60, wide_w=80)
        y -= 14
    if col:
        y = min(y, cb)
    return y


def sum_grid(c, y, items, bottom=80):
    """2x2 (or 1x2/1x3) grid of computation problems, each with a big column frame."""
    n = len(items)
    cols = 1 if n == 1 else 2
    rows = (n + cols - 1) // cols
    cw, ch = (W - 2 * MARGIN) / cols, (y - bottom) / rows
    for i, (lbl, a, b, op) in enumerate(items):
        x0, y0 = MARGIN + (i % cols) * cw, y - (i // cols) * ch
        sentence(c, x0 + 10, y0 - 20, f"{lbl}.   {a} {op} {b} = |______", size=16, wide_w=70)
        column(c, x0 + cw / 2 - 60, y0 - 50, [a, b], op)


def strip(rows, scale, brace=None, x=None, w=260):
    return lambda c, y: bars(c, x or MARGIN + 90, y, w, rows, scale, brace=brace, row_gap=36, h=28)


def strip_total(total_label, parts, scale, w=260):
    def draw(c, y):
        top_brace(c, MARGIN + 90, y - 24, w, total_label)
        return bars(c, MARGIN + 90, y - 28, w, [("", parts)], scale, h=28)
    return draw


# ---------------------------------------------------------------- Lesson 20

def page_133(c):
    y = start(c, "Lesson 20 Application Problem", "TEKS 3.4A", "Make a ten first.  46 + 4 = 50")
    for lbl, a, b in (("a", 46, 5), ("b", 39, 8)):
        ten = (a // 10 + 1) * 10
        sentence(c, MARGIN, y, f"{lbl}.   {a} + {b} = |______", size=18, wide_w=80)
        y -= 50
        sentence(c, MARGIN + 40, y, f"{a} + |___| = {ten}", size=16, blank_w=50)
        y -= 40
        sentence(c, MARGIN + 40, y, f"{ten} + |___| = |______", size=16, blank_w=50, wide_w=70)
        y -= 90
    footer(c, *L20, 133)


def page_135(c):
    y = start(c, "Lesson 20 Problem Set", "TEKS 3.4A", "Add the ones first. 10 ones = 1 ten. Write the 1 in the small box.")
    y = text(c, y, "1.", [[("Find the sums.", False)]])
    sum_grid(c, y - 10, [("a", 46, 25, "+"), ("b", 59, 30, "+"), ("c", 29, 63, "+"), ("d", 145, 132, "+")])
    footer(c, *L20, 135)


def page_136(c):
    y = start(c, "Lesson 20 Problem Set", "TEKS 3.4A, 3.5A", "\"More than\" means add.")
    y = block(c, y, "2.", [[("The cookies weigh ", False), ("44 ounces", True), (".", False)],
                           [("The soap weighs ", False), ("26 ounces more", True), (".", False)],
                           [("How much does the soap weigh?", False)]],
              strip([("Cookies", [("44", 44, False)]), ("Soap", [("44", 44, False), ("26", 26, False)])], 70),
              ["44 + 26 = |______|  ounces"], [44, 26])
    y -= 40
    block(c, y, "4.", [[("Greg mows the front lawn in ", False), ("15 minutes", True), (".", False)],
                       [("The back lawn takes ", False), ("17 minutes", True), (".", False)],
                       [("How many minutes in all?", False)]],
          strip([("", [("15", 15, False), ("17", 17, False)])], 32, brace=("?", 0, 32)),
          ["15 + 17 = |______|  minutes"], [15, 17])
    footer(c, *L20, 136)


def page_137(c):
    y = start(c, "Lesson 20 Exit Ticket", "TEKS 3.4A, 3.5A", "Add the ones first.")
    y = text(c, y, "1.", [[("Find the sums.", False)]])
    sum_grid(c, y - 10, [("a", 24, 36, "+"), ("b", 162, 125, "+")], bottom=y - 200)
    y -= 240
    block(c, y, "2.", [[("Brianna jogs ", False), ("26 minutes", True), (" on Saturday.", False)],
                       [("On Sunday she jogs ", False), ("15 minutes more", True), (".", False)],
                       [("How many minutes does she jog on Sunday?", False)]],
          strip([("Saturday", [("26", 26, False)]), ("Sunday", [("26", 26, False), ("15", 15, False)])], 41),
          ["26 + 15 = |______|  minutes"], [26, 15])
    footer(c, *L20, 137)


# ---------------------------------------------------------------- Lesson 21

def page_139(c):
    y = start(c, "Lesson 21 Application Problem", "TEKS 3.4A, 3.5A", "\"Total\" means add.")
    block(c, y, "", [[("A bag of apples weighs ", False), ("93 ounces", True), (".", False)],
                     [("A bag of pears weighs ", False), ("152 ounces", True), (".", False)],
                     [("What is the ", False), ("total", True), (" weight?", False)]],
          strip([("", [("93", 93, False), ("152", 152, False)])], 245, brace=("?", 0, 245)),
          ["93 + 152 = |______|  ounces"], [93, 152])
    footer(c, *L21, 139)


def page_141(c):
    y = start(c, "Lesson 21 Problem Set", "TEKS 3.4A", "Add the ones first. 10 ones = 1 ten. Write the 1 in the small box.")
    y = text(c, y, "1.", [[("Find the sums.", False)]])
    sum_grid(c, y - 10, [("a", 52, 38, "+"), ("b", 352, 38, "+"), ("c", 147, 138, "+"), ("d", 345, 147, "+")])
    footer(c, *L21, 141)


def page_142(c):
    y = start(c, "Lesson 21 Problem Set", "TEKS 3.4A, 3.5A", "\"Total\" and \"altogether\" mean add.")
    y = block(c, y, "2.", [[("The dog weighs ", False), ("205 ounces", True), (". The kitten weighs ", False),
                            ("93 ounces", True), (".", False)],
                           [("What is the ", False), ("total", True), (" weight?", False)]],
              strip([("", [("205", 205, False), ("93", 93, False)])], 298, brace=("?", 0, 298)),
              ["205 + 93 = |______|  ounces"], [205, 93])
    y -= 40
    block(c, y, "3.", [[("Sue wraps ", False), ("46", True), (" muffins. ", False), ("38", True),
                        (" muffins are still cooling.", False)],
                       [("How many muffins ", False), ("altogether", True), ("?", False)]],
          strip([("", [("46", 46, False), ("38", 38, False)])], 84, brace=("?", 0, 84)),
          ["46 + 38 = |______|  muffins"], [46, 38])
    footer(c, *L21, 142)


def page_143(c):
    y = start(c, "Lesson 21 Exit Ticket", "TEKS 3.4A, 3.5A", "Add the ones first.")
    y = text(c, y, "1.", [[("Find the sums.", False)]])
    sum_grid(c, y - 10, [("a", 48, 29, "+"), ("b", 328, 159, "+")], bottom=y - 200)
    y -= 240
    block(c, y, "2.", [[("The class sells ", False), ("38 liters", True), (" of lemonade. ", False),
                        ("46 liters", True), (" are left.", False)],
                       [("How many liters did they have at the beginning?", False)]],
          strip([("", [("38", 38, False), ("46", 46, False)])], 84, brace=("?", 0, 84)),
          ["38 + 46 = |______|  liters"], [38, 46])
    footer(c, *L21, 143)


# ---------------------------------------------------------------- Lesson 22 (estimation removed)

def page_145(c):
    y = start(c, "Lesson 22 Application Problem", "TEKS 3.4A, 3.5A", "\"Both days\" means add.")
    block(c, y, "", [[("The doctor gives ", False), ("180 mL", True), (" of medicine on Monday.", False)],
                     [("He gives ", False), ("210 mL", True), (" on Tuesday.", False)],
                     [("How much medicine on ", False), ("both days", True), ("?", False)]],
          strip([("", [("180", 180, False), ("210", 210, False)])], 390, brace=("?", 0, 390)),
          ["180 + 210 = |______|  mL"], [180, 210])
    footer(c, *L22, 145)


def page_147(c):
    y = start(c, "Lesson 22 Problem Set", "TEKS 3.4A", "Add the ones first.")
    y = text(c, y, "1.", [[("Find the sums.", False)]])
    sum_grid(c, y - 10, [("A", 421, 252, "+"), ("B", 356, 131, "+"), ("C", 652, 136, "+")])
    footer(c, *L22, 147)


def page_148(c):
    y = start(c, "Lesson 22 Problem Set", "TEKS 3.4A, 3.5A", "\"In all\" means add.")
    y = block(c, y, "2.", [[("Janet watches a ", False), ("94", True), ("-minute movie and a ", False), ("121", True),
                            ("-minute movie.", False)],
                           [("How many minutes in all?", False)]],
              strip([("", [("94", 94, False), ("121", 121, False)])], 215, brace=("?", 0, 215)),
              ["94 + 121 = |______|  minutes"], [94, 121])
    y -= 40
    block(c, y, "3.", [[("Sadie the bear weighs ", False), ("262 pounds", True), (". Her cub weighs ", False),
                        ("34 pounds", True), (".", False)],
                       [("How much do they weigh together?", False)]],
          strip([("", [("262", 262, False), ("34", 34, False)])], 296, brace=("?", 0, 296)),
          ["262 + 34 = |______|  pounds"], [262, 34])
    footer(c, *L22, 148)


def page_149(c):
    y = start(c, "Lesson 22 Exit Ticket", "TEKS 3.4A, 3.5A", "\"Total\" means add.")
    block(c, y, "", [[("Jesse practices trumpet ", False), ("160 minutes", True), (" in week 1.", False)],
                     [("He practices ", False), ("240 minutes", True), (" in week 2.", False)],
                     [("What is the ", False), ("total", True), ("?", False)]],
          strip([("", [("160", 160, False), ("240", 240, False)])], 400, brace=("?", 0, 400)),
          ["160 + 240 = |______|  minutes"], [160, 240])
    footer(c, *L22, 149)


# ---------------------------------------------------------------- Lesson 23

def page_151(c):
    y = start(c, "Lesson 23 Application Problem", "TEKS 3.4A, 3.5A", "\"In all\" means add.")
    block(c, y, "", [[("The librarian packs ", False), ("144 lb", True), (" of books in one truck.", False)],
                     [("She packs ", False), ("235 lb", True), (" in another truck.", False)],
                     [("How many pounds in all?", False)]],
          strip([("", [("144", 144, False), ("235", 235, False)])], 379, brace=("?", 0, 379)),
          ["144 + 235 = |______|  lb"], [144, 235])
    footer(c, *L23, 151)


def two_step(c, page_no, lesson, title, num, lines, model, s1, s2, col1, col2, op2="+", tip=None):
    """col1: numbers for Step 1 (or None to skip); col2: Step 2 frame, None = copy your Step 1 answer."""
    y = start(c, title, "TEKS 3.4A, 3.5A",
              tip or "Two steps. Do Step 1 first. Use that answer in Step 2.")
    y = text(c, y, num, lines)
    y = model(c, y - 14) - 40
    rich_line(c, MARGIN, y, [("Step 1:", True)], 13)
    sentence(c, MARGIN + 70, y, s1, size=16, blank_w=60, wide_w=80)
    if col1:
        column(c, W - MARGIN - 112, y + 22, col1)
    y -= 150
    rich_line(c, MARGIN, y, [("Step 2:", True)], 13)
    sentence(c, MARGIN + 70, y, s2, size=16, blank_w=60, wide_w=80)
    column(c, W - MARGIN - 112, y + 22, col2, op2, places=3)
    footer(c, *lesson, page_no)


def page_153(c):
    two_step(c, 153, L23, "Lesson 23 Problem Set", "1.",
             [[("The librarian packs ", False), ("144 lb", True), (" and ", False), ("235 lb", True), (" of books.", False)],
              [("She has ", False), ("120 lb", True), (" left to pack. How many pounds in all?", False)]],
             strip([("", [("144", 144, False), ("235", 235, False), ("120", 120, False)])], 499, brace=("?", 0, 499)),
             "144 + 235 = |______", "______| + 120 = |______|  lb", [144, 235], [None, 120])


def page_154(c):
    two_step(c, 154, L23, "Lesson 23 Problem Set", "2.",
             [[("A family drives ", False), ("312 miles", True), (" on day 1.", False)],
              [("On day 2 they drive ", False), ("172 miles more", True), (" than day 1.", False)],
              [("How many miles altogether?", False)]],
             strip([("Day 1", [("312", 312, False)]), ("Day 2", [("312", 312, False), ("172", 172, False)])], 484),
             "312 + 172 = |______|", "312 + |______| = |______|  miles", [312, 172], [312, None])


def page_155(c):
    two_step(c, 155, L23, "Lesson 23 Problem Set", "3.",
             [[("Pizza sales: ", False), ("$243", True), (".  Other food: ", False), ("$150", True),
               (".  Drinks: ", False), ("$105", True), (".", False)],
              [("What is the total?", False)]],
             strip([("", [("243", 243, False), ("150", 150, False), ("105", 105, False)])], 498, brace=("?", 0, 498)),
             "243 + 150 = |______", "______| + 105 = |______|  dollars", [243, 150], [None, 105])


def page_156(c):
    two_step(c, 156, L23, "Lesson 23 Problem Set", "4.",
             [[("Sandy used ", False), ("210 liters", True), (" of water last summer.", False)],
              [("This summer she used ", False), ("150 liters more", True), (".", False)],
              [("How many liters in both summers?", False)]],
             strip([("Last", [("210", 210, False)]), ("This", [("210", 210, False), ("150", 150, False)])], 360),
             "210 + 150 = |______|", "210 + |______| = |______|  liters", [210, 150], [210, None])


def page_157(c):
    two_step(c, 157, L23, "Lesson 23 Problem Set", "5.",
             [[("Shari drinks ", False), ("230 ounces", True), (" of water.", False)],
              [("Vinnie drinks ", False), ("120 ounces more", True), (" than Shari.", False)],
              [("How much do they drink together?", False)]],
             strip([("Shari", [("230", 230, False)]), ("Vinnie", [("230", 230, False), ("120", 120, False)])], 350),
             "230 + 120 = |______|", "230 + |______| = |______|  ounces", [230, 120], [230, None])


def page_159(c):
    two_step(c, 159, L23, "Lesson 23 Exit Ticket", "1.",
             [[("A rider weighs ", False), ("120 lb", True), (".", False)],
              [("The horse weighs ", False), ("450 lb more", True), (" than the rider.", False)],
              [("How much do they weigh together?", False)]],
             strip([("Rider", [("120", 120, False)]), ("Horse", [("120", 120, False), ("450", 450, False)])], 570),
             "120 + 450 = |______|", "120 + |______| = |______|  lb", [120, 450], [120, None])


# ---------------------------------------------------------------- Lesson 24

def page_161(c):
    two_step(c, 161, L24, "Lesson 24 Application Problem", "",
             [[("You spend ", False), ("$200", True), (" on food, ", False), ("$300", True), (" on a hotel,", False)],
              [("and ", False), ("$150", True), (" on fun. How much did you spend in all?", False)]],
             strip([("", [("200", 200, False), ("300", 300, False), ("150", 150, False)])], 650, brace=("?", 0, 650)),
             "200 + 300 = |______", "______| + 150 = |______|  dollars", [200, 300], [None, 150])


def page_163(c):
    two_step(c, 163, L24, "Lesson 24 Problem Set", "1.",
             [[("You have ", False), ("$850", True), (". You spend ", False), ("$200", True), (", ", False),
               ("$300", True), (", and ", False), ("$150", True), (".", False)],
              [("How much money is ", False), ("left", True), ("?", False)]],
             strip_total("$850", [("200", 200, False), ("300", 300, False), ("150", 150, False), ("?", 200, False)], 850),
             "200 + 300 + 150 = |______|", "850 − |______| = |______|  dollars", None, [850, None], "−",
             tip="Add what you spent. Then subtract from what you had.")


def page_164(c):
    two_step(c, 164, L24, "Lesson 24 Problem Set", "2.",
             [[("A ride holds ", False), ("650 pounds", True), (".", False)],
              [("Person 1 weighs ", False), ("200 lb", True), (". Person 2 weighs ", False), ("150 lb", True), (".", False)],
              [("How much can the third rider weigh?", False)]],
             strip_total("650", [("200", 200, False), ("150", 150, False), ("?", 300, False)], 650),
             "200 + 150 = |______", "650 − |______| = |______|  lb", [200, 150], [650, None], "−",
             tip="Add the two riders. Then subtract from 650.")


def page_165(c):
    two_step(c, 165, L24, "Lesson 24 Problem Set", "3.",
             [[("The family drives ", False), ("790 miles", True), (" in 3 days.", False)],
              [("Monday: ", False), ("350", True), (" miles.  Tuesday: ", False), ("230", True), (" miles.", False)],
              [("How many miles on Wednesday?", False)]],
             strip_total("790", [("350", 350, False), ("230", 230, False), ("?", 210, False)], 790),
             "350 + 230 = |______", "790 − |______| = |______|  miles", [350, 230], [790, None], "−",
             tip="Add the days you know. Then subtract from the total.")


def page_166(c):
    y = start(c, "Lesson 24 Problem Set", "TEKS 3.4A, 3.5A",
              "Subtract the ones first. If the top is smaller, trade 1 ten for 10 ones.")
    block(c, y, "4.", [[("Dylan has ", False), ("$325", True), (". He buys a game for ", False), ("$50", True), (".", False)],
                       [("How much money does he have now?", False)]],
          strip_total("$325", [("50", 50, False), ("?", 275, False)], 325),
          ["325 − 50 = |______|  dollars"], [325, 50], col_op="−")
    footer(c, *L24, 166)


def page_167(c):
    two_step(c, 167, L24, "Lesson 24 Problem Set", "5.",
             [[("The punch needs ", False), ("375 ounces", True), (".", False)],
              [("They have ", False), ("175 oz", True), (" ginger ale and ", False), ("125 oz", True), (" pineapple juice.", False)],
              [("How much orange juice do they need?", False)]],
             strip_total("375", [("175", 175, False), ("?", 75, False), ("125", 125, False)], 375),
             "175 + 125 = |______", "375 − |______| = |______|  ounces", [175, 125], [375, None], "−",
             tip="Add the juice you have. Then subtract from 375.")


def page_169(c):
    y = start(c, "Lesson 24 Exit Ticket", "TEKS 3.4A, 3.5A", "\"Pours out\" means subtract.")
    block(c, y, "1.", [[("A beaker has ", False), ("435 mL", True), (". The scientist pours out ", False),
                        ("120 mL", True), (".", False)],
                       [("How many mL are still in the beaker?", False)]],
          strip_total("435", [("120", 120, False), ("?", 315, False)], 435),
          ["435 − 120 = |______|  mL"], [435, 120], col_op="−")
    footer(c, *L24, 169)


BOOK = {133: page_133, 135: page_135, 136: page_136, 137: page_137, 139: page_139, 141: page_141,
        142: page_142, 143: page_143, 145: page_145, 147: page_147, 148: page_148, 149: page_149,
        151: page_151, 153: page_153, 154: page_154, 155: page_155, 156: page_156, 157: page_157,
        159: page_159, 161: page_161, 163: page_163, 164: page_164, 165: page_165, 166: page_166,
        167: page_167, 169: page_169}

if __name__ == "__main__":
    main("G3_M2_TopicE_Simplified.pdf", [BOOK[k] for k in sorted(BOOK)],
         "Bluebonnet Learning Grade 3 Module 2 Topic E – Simplified")
