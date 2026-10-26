"""Grade 3 Module 2 Topic F, Lessons 25-28 (book pages 171-195): Modified and Simplified (v2).

MODIFIED   - every problem with the book's numbers (estimation included); strip
             diagrams, column frames, estimate frames.
SIMPLIFIED - readiness TEKS (3.4A, 3.5A); friendlier numbers (one regroup), fewer
             problems, base-ten block pictures for every subtraction.
Both: the measuring problems on pages 191-193 have BLANK measurements, so the
teacher can fill them in with the class. Book page numbers kept.

Run: python3 topic_f_v2.py  ->  G3_M2_TopicF_Modified.pdf and G3_M2_TopicF_Simplified_v2.pdf
"""
from reportlab.lib.colors import HexColor, black

from build_module2 import MARGIN, W, blank, footer, header, main, rich_line, teks
from lessons_20_24 import bars, top_brace
from reteach_mid_module import sentence
from topic_e_simple import column, text
from topic_f_simple import L25, L26, L27, L28

SIMP = False
FLAT = HexColor("#C8D6E8")
GREY = HexColor("#666666")

TIP_SUB = "Subtract the ones first. If the top is smaller, trade 1 ten for 10 ones."
TIP_SUB0 = "Top digit is 0? Trade 1 hundred for 10 tens first."
TIP_PART = "Know the total and one part? Subtract to find the other part."
TIP_EST = "Estimate: round first, then subtract. Then find the exact answer."


def start(c, title, teks_mod, teks_simp, tip_mod, tip_simp=None):
    y = header(c, title, suffix=" (Simplified)" if SIMP else " (Modified)")
    teks(c, y, teks_simp if SIMP else teks_mod)
    rich_line(c, MARGIN, y - 6, [("Tip: ", True), ((tip_simp or tip_mod) if SIMP else tip_mod, False)], 12)
    return y - 44


def frame(c, x, y, s, size=15):
    sentence(c, x, y, s, size=size, blank_w=50, wide_w=70)


def base10(c, x, y, n, s=4):
    """Base-ten picture of n: flats (100), rods (10), units (1). (x, y) top-left."""
    h, t, o = n // 100, n // 10 % 10, n % 10
    c.setLineWidth(0.6)
    for k in range(h):
        c.setFillColor(FLAT)
        c.rect(x, y - 10 * s, 10 * s, 10 * s, stroke=1, fill=1)
        c.setFillColor(black)
        for g in range(1, 10):
            c.line(x + g * s, y, x + g * s, y - 10 * s)
            c.line(x, y - g * s, x + 10 * s, y - g * s)
        x += 10 * s + 6
    for k in range(t):
        c.rect(x, y - 10 * s, s, 10 * s)
        x += s + 3
    x += 4
    for k in range(o):
        c.rect(x + (k % 3) * (s + 2), y - 10 * s + (k // 3) * (s + 2), s, s)
    c.setLineWidth(1)
    c.setFont("Sans", 9)
    c.setFillColor(GREY)
    c.drawString(x + 40, y - 10 * s, f"= {n}")
    c.setFillColor(black)


def strip_total(label, parts, scale, w=280, x=None):
    def draw(c, y):
        top_brace(c, x or MARGIN + 90, y - 24, w, label)
        return bars(c, x or MARGIN + 90, y - 28, w, [("", parts)], scale, h=28)
    return draw


def strip_cmp(rows, scale, brace=None, w=280):
    return lambda c, y: bars(c, MARGIN + 90, y, w, rows, scale, brace=brace, row_gap=36, h=28)


def wp(c, y, num, lines, model, sents, col=None, op="−", show_blocks=True):
    """Word problem: text, model, column (right), sentences; base-ten picture of the top number in SIMPLIFIED."""
    y = text(c, y, num, lines)
    top = y - 10
    cb = column(c, W - MARGIN - 130, top, col, op) if col else top
    if model:
        y = model(c, y - 14) - 16
    if SIMP and col and op == "−" and show_blocks:
        base10(c, MARGIN + 30, y - 4, col[0])
        y -= 56
    for s in sents:
        y -= 26
        frame(c, MARGIN + 24, y, s)
        y -= 12
    return min(y, cb) - 24


def grid(c, y, items, bottom=80):
    """2-column grid of computation problems with column frames (and base-ten pictures in SIMPLIFIED)."""
    nc = 3 if len(items) > 4 else 2
    rows = (len(items) + nc - 1) // nc
    cw, ch = (W - 2 * MARGIN) / nc, (y - bottom) / rows
    for i, (lbl, a, b, op) in enumerate(items):
        x0, y0 = MARGIN + (i % nc) * cw, y - (i // nc) * ch
        if nc == 3:
            rich_line(c, x0 + 10, y0 - 14, [(f"{lbl}.   ", True), (f"{a} {op} {b}", True)], 14)
        else:
            frame(c, x0 + 10, y0 - 18, f"{lbl}.   {a} {op} {b} = |______", size=14)
        column(c, x0 + 20, y0 - (28 if nc == 3 else 40), [a, b], op, cw=26)
        if SIMP and op == "−":
            base10(c, x0 + 6, y0 - 160, a, s=2.2)


def mixed(c, x, y, lbl, big, small):
    (ba, bb, bu), (sa, sb, su) = big, small
    rich_line(c, x, y, [(f"{lbl}.  ", True), (f"{ba} {bu} {sa} {su}  −  {bb} {bu} {sb} {su}", True)], 13)
    frame(c, x + 20, y - 28, f"{su}:  {sa} − {sb} = |______|  {su}", size=12.5)
    frame(c, x + 20, y - 54, f"{bu}:  {ba} − {bb} = |___|  {bu}", size=12.5)
    sentence(c, x + 20, y - 80, f"Answer:  |___|  {bu}  |___|  {su}", size=12.5, blank_w=40)


def est(c, x, y, a, b, op="−", place="hundred"):
    rich_line(c, x, y, [(f"Estimate (nearest {place}):", False)], 12)
    frame(c, x + 180, y, f"___|  {op}  |___|  =  |______", size=13)


def rdw(c, y=100):
    c.setFont("Sans-Bold", 12)
    for k, word in enumerate(["Read", "Draw", "Write"]):
        c.drawCentredString(MARGIN + 90 + k * 170, y, word)


# ---------------------------------------------------------------- Lesson 25

def p171(c):
    y = start(c, "Lesson 25 Application Problem", "TEKS 3.4A, 3.5A", "TEKS 3.4A, 3.5A", "\"In all\" means add.")
    b = 254 if SIMP else 354
    wp(c, y, "", [[("Tara has 2 water bottles: ", False), ("471 mL", True), (" and ", False), (f"{b} mL", True), (".", False)],
                  [("How many milliliters in all?", False)]],
       lambda c, y: bars(c, MARGIN + 90, y, 280, [("", [("471", 471, False), (str(b), b, False)])], 471 + b, h=28,
                         brace=("?", 0, 471 + b)),
       [f"471 + {b} = |______|  mL"], [471, b], "+")
    rdw(c)
    footer(c, *L25, 171)


def p173(c):
    y = start(c, "Lesson 25 Problem Set", "TEKS 3.4A", "TEKS 3.4A", TIP_SUB)
    y = text(c, y, "1.", [[("Subtract.", False)]])
    if SIMP:
        grid(c, y - 10, [("a", 60, 24, "−"), ("b", 360, 24, "−"), ("c", 518, 21, "−"), ("d", 307, 130, "−")])
    else:
        grid(c, y - 10, [("a", 60, 24, "−"), ("b", 360, 24, "−"), ("c", 360, 224, "−"), ("d", 518, 21, "−"),
                         ("e", 629, 268, "−"), ("f", 938, 440, "−"), ("g", 307, 130, "−"), ("h", 307, 234, "−"),
                         ("i", 807, 732, "−")], bottom=185)
        mixed(c, MARGIN + 10, 160, "j", (2, 1, "km"), (770, 455, "m"))
        mixed(c, MARGIN + 285, 160, "k", (3, 1, "L"), (924, 893, "mL"))
    footer(c, *L25, 173)


def p174(c):
    y = start(c, "Lesson 25 Problem Set", "TEKS 3.4A, 3.5A", "TEKS 3.4A, 3.5A", TIP_PART)
    part = 230 if SIMP else 233
    y = wp(c, y, "2.", [[("Flour, sugar, and salt weigh ", False), ("405 oz", True), (" in all. Sugar and salt weigh ", False),
                         (f"{part} oz", True), (".", False)], [("How much does the flour weigh?", False)]],
           strip_total("405", [(str(part), part, False), ("? flour", 405 - part, False)], 405),
           [f"405 − {part} = |______|  oz"], [405, part])
    if SIMP:
        wp(c, y, "3.", [[("The Lost Ship", True), (" is ", False), ("117 minutes", True), (". ", False), ("Champions", True),
                        (" is ", False), ("22 minutes shorter", True), (".", False)], [("How long is Champions?", False)]],
           strip_cmp([("Lost Ship", [("117", 117, False)]), ("Champions", [("?", 95, False)])], 117),
           ["117 − 22 = |______|  minutes"], [117, 22])
    else:
        y = text(c, y, "3.", [[("Lost Ship: ", False), ("117 min", True), (".  Beautiful Forests: ", False), ("145 min", True), (".", False)],
                             [("Champions is ", False), ("22 min shorter", True), (" than Lost Ship.", False)]])
        frame(c, MARGIN + 24, y - 6, "a.  117 − 22 = |______|  minutes (Champions)", size=13)
        frame(c, MARGIN + 24, y - 40, "b.  145 − |______|  = |______|  minutes longer", size=13)
        y -= 80
        y = text(c, y, "4.", [[("A rope is ", False), ("208 cm", True), (". Scott cuts 3 pieces: ", False), ("80 cm", True), (", ", False),
                              ("94 cm", True), (", and ?", False)]])
        strip_total("208", [("80", 80, False), ("94", 94, False), ("?", 34, False)], 208)(c, y - 10)
        frame(c, MARGIN + 24, y - 80, "80 + 94 = |______|      208 − |______|  = |______|  cm", size=13)
    footer(c, *L25, 174)


def p175(c):
    y = start(c, "Lesson 25 Exit Ticket", "TEKS 3.4A, 3.5A", "TEKS 3.4A, 3.5A", TIP_SUB)
    y = text(c, y, "1.", [[("Subtract.", False)]])
    items = ([("a", 381, 146, "−"), ("b", 730, 420, "−")] if SIMP else
             [("a", 381, 146, "−"), ("b", 730, 426, "−"), ("c", 509, 384, "−")])
    grid(c, y - 10, items, bottom=y - (200 if SIMP else 330))
    y -= 220 if SIMP else 340
    if SIMP:
        wp(c, y, "2.", [[("A banner is ", False), ("408 cm", True), (". Carly paints ", False), ("180 cm", True), (".", False)],
                        [("How much is left to paint?", False)]],
           strip_total("408", [("180", 180, False), ("?", 228, False)], 408), ["408 − 180 = |______|  cm"], [408, 180])
    else:
        wp(c, y, "2.", [[("A banner is ", False), ("408 cm", True), (". The first 2 sections are ", False), ("187 cm", True),
                        (". How long is the third?", False)]],
           strip_total("408", [("187", 187, False), ("?", 221, False)], 408), ["408 − 187 = |______|  cm"], [408, 187])
    footer(c, *L25, 175)


# ---------------------------------------------------------------- Lesson 26

def p177(c):
    y = start(c, "Lesson 26 Application Problem", "TEKS 3.4A, 3.5A", "TEKS 3.4A, 3.5A", TIP_PART)
    wp(c, y, "", [[("A washer and dryer weigh ", False), ("417 lb", True), (". The washer weighs ", False), ("223 lb", True),
                   (".", False)], [("How much does the dryer weigh?", False)]],
       strip_total("417", [("223", 223, False), ("? dryer", 194, False)], 417), ["417 − 223 = |______|  lb"], [417, 223])
    rdw(c)
    footer(c, *L26, 177)


def p179(c):
    y = start(c, "Lesson 26 Problem Set", "TEKS 3.4A", "TEKS 3.4A", TIP_SUB0)
    y = text(c, y, "1.", [[("Subtract.", False)]])
    if SIMP:
        grid(c, y - 10, [("a", 340, 60, "−"), ("b", 340, 260, "−"), ("c", 513, 140, "−"), ("d", 700, 50, "−")])
    else:
        grid(c, y - 10, [("a", 340, 60, "−"), ("b", 340, 260, "−"), ("c", 513, 148, "−"), ("d", 641, 387, "−"),
                         ("e", 700, 52, "−"), ("f", 700, 452, "−")], bottom=185)
        mixed(c, MARGIN + 10, 160, "g", (6, 2, "km"), (802, 569, "m"))
        mixed(c, MARGIN + 285, 160, "h", (5, 3, "L"), (920, 869, "mL"))
    footer(c, *L26, 179)


def p180(c):
    y = start(c, "Lesson 26 Problem Set", "TEKS 3.4A, 3.5A", "TEKS 3.4A, 3.5A", TIP_PART)
    left = 480 if SIMP else 487
    y = wp(c, y, "2.", [[("The trip is ", False), ("672 km", True), (". David still has ", False), (f"{left} km", True), (" left.", False)],
                        [("How far has he driven so far?", False)]],
           strip_total("672", [("?", 672 - left, False), (str(left), left, False)], 672), [f"672 − {left} = |______|  km"], [672, left])
    if not SIMP:
        y = wp(c, y, "3.", [[("The piano weighs ", False), ("621 lb", True), (". It weighs ", False), ("597 lb more", True),
                            (" than the bench.", False)], [("How much does the bench weigh?", False)]],
               strip_cmp([("Piano", [("621", 621, False)]), ("Bench", [("?", 24, False)])], 621, w=300),
               ["621 − 597 = |______|  lb"], [621, 597])
    fewer = 150 if SIMP else 165
    wp(c, y, "4.", [[("Tank B holds ", False), ("400 L", True), (". Tank A holds ", False), (f"{fewer} L fewer", True), (".", False)],
                    [("How much does Tank A hold?", False)]],
       strip_cmp([("Tank B", [("400", 400, False)]), ("Tank A", [("?", 400 - fewer, False)])], 400),
       [f"400 − {fewer} = |______|  L"], [400, fewer])
    footer(c, *L26, 180)


def p181(c):
    y = start(c, "Lesson 26 Exit Ticket", "TEKS 3.4A, 3.5A", "TEKS 3.4A, 3.5A", TIP_SUB)
    y = text(c, y, "1.", [[("Subtract.", False)]])
    grid(c, y - 10, [("a", 346, 180 if SIMP else 187, "−"), ("b", 700, 590 if SIMP else 592, "−")], bottom=y - 200)
    y -= 220
    less = 600 if SIMP else 647
    wp(c, y, "2.", [[("The horse weighs ", False), ("725 lb", True), (". The pig weighs ", False), (f"{less} lb less", True), (".", False)],
                    [("How much does the pig weigh?", False)]],
       strip_cmp([("Horse", [("725", 725, False)]), ("Pig", [("?", 725 - less, False)])], 725), [f"725 − {less} = |______|  lb"],
       [725, less])
    footer(c, *L26, 181)


# ---------------------------------------------------------------- Lesson 27

def p183(c):
    y = start(c, "Lesson 27 Application Problem", "TEKS 3.4B, 3.4A", "TEKS 3.4A, 3.5A", TIP_EST, "\"Empties out\" means subtract.")
    out = 180 if SIMP else 185
    y = wp(c, y, "", [[("Millie's tank holds ", False), ("403 L", True), (". She empties out ", False), (f"{out} L", True), (".", False)],
                      [("How many liters are left?", False)]],
           strip_total("403", [(str(out), out, False), ("? left", 403 - out, False)], 403),
           [] if not SIMP else [f"403 − {out} = |______|  L"], [403, out] if SIMP else None)
    if not SIMP:
        frame(c, MARGIN + 24, y - 10, "a.  Round to the nearest hundred:   |___|  −  |___|  =  |______", size=13)
        frame(c, MARGIN + 24, y - 46, "b.  Round to the nearest ten:   |___|  −  |___|  =  |______", size=13)
    rdw(c)
    footer(c, *L27, 183)


def p184(c):
    y = start(c, "Lesson 27 Application Problem", "TEKS 3.4A, 3.4B", "TEKS 3.4A", "Check subtraction by adding back.")
    out = 180 if SIMP else 185
    if SIMP:
        y = text(c, y, "", [[("Check your answer from page 183. Add the part you took out back on.", False)]])
        frame(c, MARGIN + 24, y - 40, f"______|  +  {out}  =  |______", size=18)
        column(c, W - MARGIN - 130, y - 10, [None, out], "+", places=3)
        rich_line(c, MARGIN + 24, y - 110, [("Did you get ", False), ("403", True), ("?   ", False), ("yes  /  no", True)], 16)
    else:
        y = text(c, y, "c.", [[("How many liters are actually left in the tank?", False)]])
        frame(c, MARGIN + 24, y - 10, f"403 − {out} = |______|  liters")
        column(c, W - MARGIN - 130, y + 10, [403, out], "−")
        y -= 130
        y = text(c, y, "d.", [[("Is your answer reasonable? Which estimate was closer?", False)]])
        rich_line(c, MARGIN + 24, y - 10, [("Circle:  ", False), ("nearest hundred  /  nearest ten", True)], 14)
        frame(c, MARGIN + 24, y - 44, "Check:  |______|  + 185 = 403?   yes / no", size=14)
    rdw(c)
    footer(c, *L27, 184)


def p185(c):
    y = start(c, "Lesson 27 Problem Set", "TEKS 3.4B, 3.4A", "TEKS 3.4A", TIP_EST, TIP_SUB)
    if SIMP:
        y = text(c, y, "1.", [[("Find the exact differences.", False)]])
        grid(c, y - 10, [("A", 448, 153, "−"), ("B", 747, 261, "−"), ("C", 451, 141, "−"), ("D", 756, 248, "−")])
    else:
        y = text(c, y, "1.", [[("a. ", True), ("Find the actual difference.", False)],
                             [("Then round each number to the nearest ", False), ("hundred", True), (" and subtract.", False)]],
                 size=12.5)
        cols = {"A": [(448, 153), (451, 153), (448, 149), (451, 149)], "B": [(747, 261), (756, 261), (747, 249), (756, 248)]}
        cw = (W - 2 * MARGIN) / 2
        for k, (name, pairs) in enumerate(cols.items()):
            x0 = MARGIN + k * cw
            rich_line(c, x0 + cw / 2 - 6, y - 6, [(name, True)], 14)
            for j, (a, b) in enumerate(pairs):
                yy = y - 36 - j * 74
                frame(c, x0 + 10, yy, f"{a} − {b} = |______", size=12.5)
                frame(c, x0 + 10, yy - 28, "___|  −  |___|  =  |______", size=12.5)
            rich_line(c, x0 + 10, y - 340, [("Circle the closest estimates.", False)], 11)
        frame(c, MARGIN, y - 380, "b.  The closest estimates had numbers  close to / far from  a hundred.", size=12)
    footer(c, *L27, 185)


def p186(c):
    y = start(c, "Lesson 27 Problem Set", "TEKS 3.4B, 3.4A, 3.5A", "TEKS 3.4A, 3.5A", TIP_PART)
    m1 = 180 if SIMP else 184
    y = wp(c, y, "2.", [[("Camden uses ", False), ("372 L", True), (" of gas in 2 months. Month 1: ", False), (f"{m1} L", True),
                         (".", False)], [("How many liters in month 2?", False)]],
           strip_total("372", [(str(m1), m1, False), ("?", 372 - m1, False)], 372),
           ([] if SIMP else ["a.  Estimate:  |___|  −  |___|  = |______"]) + [f"{'' if SIMP else 'b.  '}372 − {m1} = |______|  L"],
           [372, m1])
    cr = 350 if SIMP else 384
    wp(c, y, "3.", [[("A cat, dog, and rabbit weigh ", False), ("800 oz", True), (". The cat and rabbit weigh ", False),
                     (f"{cr} oz", True), (".", False)], [("How much does the dog weigh?", False)]],
       strip_total("800", [(str(cr), cr, False), ("? dog", 800 - cr, False)], 800),
       ([] if SIMP else ["a.  Estimate:  |___|  −  |___|  = |______"]) + [f"{'' if SIMP else 'b.  '}800 − {cr} = |______|  oz"],
       [800, cr])
    footer(c, *L27, 186)


def p187(c):
    y = start(c, "Lesson 27 Exit Ticket", "TEKS 3.4B, 3.4A, 3.5A", "TEKS 3.4A, 3.5A", TIP_EST, TIP_PART)
    big = 320 if SIMP else 329
    y = wp(c, y, "", [[("A chef buys ", False), ("416 fl oz", True), (" of oil. The large container has ", False), (f"{big} fl oz", True),
                      (".", False)], [("How much is in the small container?", False)]],
           strip_total("416", [(str(big), big, False), ("? small", 416 - big, False)], 416),
           ([] if SIMP else ["a.  Nearest 100:  |___|  −  |___|  = |___", "b.  Nearest 10:  |___|  −  |___|  = |___"])
           + [f"{'' if SIMP else 'c.  '}416 − {big} = |______|  fl oz"], [416, big])
    if SIMP:
        frame(c, MARGIN + 24, y - 20, f"Check:  |______|  +  {big}  =  416?   yes / no", size=14)
    else:
        rich_line(c, MARGIN + 24, y - 20, [("d.  Which estimate was closer?  ", False), ("nearest hundred  /  nearest ten", True)], 13)
    footer(c, *L27, 187)


# ---------------------------------------------------------------- Lesson 28

def p189(c):
    y = start(c, "Lesson 28 Application Problem", "TEKS 3.4B, 3.4A", "TEKS 3.4A, 3.5A", TIP_EST, "Two balloons the same: add it twice.")
    y = wp(c, y, "", [[("Each water balloon has ", False), ("238 mL", True), (". How many mL in ", False), ("2", True), (" balloons?", False)]],
           lambda c, y: bars(c, MARGIN + 90, y, 280, [("", [("238", 1, False), ("238", 1, False)])], 2, h=28, brace=("?", 0, 2)),
           ["238 + 238 = |______|  mL"], [238, 238], "+")
    if not SIMP:
        frame(c, MARGIN + 24, y - 10, "Nearest 10:  |___|  +  |___|  =  |______", size=13)
        frame(c, MARGIN + 24, y - 44, "Nearest 100:  |___|  +  |___|  =  |______", size=13)
        rich_line(c, MARGIN + 24, y - 78, [("Closer estimate:  ", False), ("nearest 10  /  nearest 100", True)], 13)
    rdw(c)
    footer(c, *L28, 189)


def blank_pair(c, x, y, op):
    """Column frame with both numbers blank (measurements filled in with the class)."""
    column(c, x, y, [None, None], op, places=3)


def p191(c):
    y = start(c, "Lesson 28 Problem Set", "TEKS 3.4B, 3.4A", "TEKS 3.4A",
              "Fill in the weights with your teacher.", "Fill in the weights with your teacher. Total: add. Difference: subtract.")
    y = text(c, y, "1.", [[("Weigh the beans and rice. Write the weights.", False)]])
    for k, name in enumerate(("Beans", "Rice")):
        x0 = MARGIN + 40 + k * 230
        c.roundRect(x0, y - 60, 150, 50, 8)
        c.setFont("Sans-Bold", 14)
        c.drawCentredString(x0 + 75, y - 30, name.upper())
        blank(c, x0 + 30, y - 84, 70)
        c.setFont("Sans", 12)
        c.drawString(x0 + 106, y - 84, "oz")
    y -= 120
    rich_line(c, MARGIN + 10, y, [("a.  ", True), ("Total weight of beans and rice:", False)], 13)
    if not SIMP:
        frame(c, MARGIN + 30, y - 30, "Estimate:  |___|  +  |___|  ≈  |___|  +  |___|  =  |______", size=12.5)
    frame(c, MARGIN + 30, y - (64 if not SIMP else 34), "Actual:  |______|  +  |______|  =  |______|  oz", size=13)
    if SIMP:
        blank_pair(c, W - MARGIN - 105, y + 10, "+")
    y -= 120 if not SIMP else 150
    rich_line(c, MARGIN + 10, y, [("b.  ", True), ("Difference between beans and rice:", False)], 13)
    if not SIMP:
        frame(c, MARGIN + 30, y - 30, "Estimate:  |___|  −  |___|  ≈  |___|  −  |___|  =  |______", size=12.5)
    frame(c, MARGIN + 30, y - (64 if not SIMP else 34), "Actual:  |______|  −  |______|  =  |______|  oz", size=13)
    if SIMP:
        blank_pair(c, W - MARGIN - 105, y + 10, "−")
    if not SIMP:
        rich_line(c, MARGIN + 10, y - 104, [("c.  Are your answers reasonable?  ", False), ("yes  /  no", True)], 13)
    footer(c, *L28, 191)


def p192(c):
    y = start(c, "Lesson 28 Problem Set", "TEKS 3.4B, 3.4A, 3.5A", "TEKS 3.4A, 3.5A",
              "Measure the yarn with your teacher.", "Measure the yarn with your teacher. Step 1: add. Step 2: subtract.")
    y = text(c, y, "2.", [[("Measure the three pieces of yarn.", False)]])
    for k, name in enumerate("ABC"):
        yy = y - 14 - k * 34
        rich_line(c, MARGIN + 30, yy, [(f"Yarn {name}", True)], 13)
        blank(c, MARGIN + 110, yy, 60)
        c.setFont("Sans", 12)
        c.drawString(MARGIN + 176, yy, "cm" if SIMP else "cm  ≈")
        if not SIMP:
            blank(c, MARGIN + 220, yy, 60)
            c.drawString(MARGIN + 286, yy, "cm")
    y -= 130
    rich_line(c, MARGIN + 10, y, [("a.  ", True), ("Total length of Yarn A and Yarn C:", False)], 13)
    if not SIMP:
        frame(c, MARGIN + 30, y - 30, "Estimate:  |___|  +  |___|  =  |______", size=13)
    frame(c, MARGIN + 30, y - (64 if not SIMP else 34), "Step 1:  A + C = |______|  +  |______|  =  |______|  cm" if SIMP
          else "Actual:  |______|  +  |______|  =  |______|  cm", size=13)
    y -= 110
    rich_line(c, MARGIN + 10, y, [("b.  ", True), ("How much longer are A and C together than Yarn B?", False)], 13)
    bars(c, MARGIN + 100, y - 16, 280, [("A + C", [("", 1, False)]), ("B", [("", 0.7, False), ("?", 0.3, False)])], 1,
         row_gap=34, h=26)
    if not SIMP:
        frame(c, MARGIN + 30, y - 100, "Estimate:  |___|  −  |___|  =  |______", size=13)
    frame(c, MARGIN + 30, y - (134 if not SIMP else 100), "Step 2:  |______|  −  |______|  =  |______|  cm" if SIMP
          else "Actual:  |______|  −  |______|  =  |______|  cm", size=13)
    footer(c, *L28, 192)


def vblank(c, x, top, bottom):
    c.setLineWidth(2)
    c.line(x, bottom - 12, x, top + 12)
    for ye, d in ((top + 12, 1), (bottom - 12, -1)):
        c.line(x, ye, x - 5, ye - 7 * d)
        c.line(x, ye, x + 5, ye - 7 * d)
    c.setLineWidth(1)
    for yy in (top, (top + bottom) / 2, bottom):
        c.line(x - 8, yy, x + 8, yy)
        blank(c, x + 12, yy - 3, 40)


def p193(c):
    y = start(c, "Lesson 28 Problem Set", "TEKS 3.4B, 3.4A, 3.5A", "TEKS 3.4A, 3.5A",
              "Measure the containers with your teacher.", "Measure with your teacher. Total: add. Difference: subtract.")
    y = text(c, y, "3.", [[("Write the amount of liquid in each container.", False)]])
    for k, name in enumerate("DEF"):
        x0 = MARGIN + 50 + k * 170
        rich_line(c, x0 - 20, y - 6, [(f"Container {name}", True)], 12)
        if not SIMP:
            vblank(c, x0 + 20, y - 40, y - 150)
        else:
            c.rect(x0, y - 110, 60, 90)
            c.setFillColor(HexColor("#CFE6FA"))
            c.rect(x0, y - 110, 60, 50, stroke=0, fill=1)
            c.setFillColor(black)
        blank(c, x0 - 4, y - (186 if not SIMP else 136), 50)
        c.setFont("Sans", 11)
        c.drawString(x0 + 50, y - (186 if not SIMP else 136), "mL")
    y -= 220 if not SIMP else 170
    rich_line(c, MARGIN + 10, y, [("a.  ", True), ("Total of all three containers:", False)], 13)
    if not SIMP:
        frame(c, MARGIN + 30, y - 30, "Estimate:  |___|  +  |___|  +  |___|  =  |______", size=13)
    frame(c, MARGIN + 30, y - (64 if not SIMP else 34), "______|  +  |______|  +  |______|  =  |______|  mL", size=13)
    y -= 100 if not SIMP else 70
    rich_line(c, MARGIN + 10, y, [("b.  ", True), ("Difference between Container D and Container E:", False)], 13)
    if not SIMP:
        frame(c, MARGIN + 30, y - 30, "Estimate:  |___|  −  |___|  =  |______", size=13)
    frame(c, MARGIN + 30, y - (64 if not SIMP else 34), "______|  −  |______|  =  |______|  mL", size=13)
    footer(c, *L28, 193)


def p194(c):
    y = start(c, "Lesson 28 Problem Set", "TEKS 3.4A, 3.4B, 3.5A", "TEKS 3.4A, 3.5A",
              "Step 1: add the previews. Step 2: subtract from 115.")
    y = text(c, y, "4.", [[("A movie with previews is ", False), ("115 minutes", True), (". Previews: ", False),
                          ("5, 4, 3, 5, and 4", True), (" minutes.", False)]])
    strip_total("115", [("previews", 40, False), ("? movie", 75, False)], 115)(c, y - 10)
    y -= 100
    frame(c, MARGIN + 24, y, "a.  5 + 4 + 3 + 5 + 4 = |______|  minutes")
    if not SIMP:
        frame(c, MARGIN + 24, y - 40, "b.  Estimate:  |___|  −  |___|  =  |______", size=14)
    frame(c, MARGIN + 24, y - (80 if not SIMP else 50), "115 − |______|  = |______|  minutes")
    column(c, W - MARGIN - 130, y - (52 if not SIMP else 22), [115, None], "−", places=3)
    if SIMP:
        base10(c, MARGIN + 30, y - 90, 115)
    else:
        rich_line(c, MARGIN + 24, y - 120, [("c.  Is your answer reasonable?  ", False), ("yes  /  no", True)], 13)
    footer(c, *L28, 194)


def p195(c):
    y = start(c, "Lesson 28 Exit Ticket", "TEKS 3.4A, 3.4B, 3.5A", "TEKS 3.4A, 3.5A",
              "Total: add.  How much more: subtract.")
    b, d = (230, 170) if SIMP else (237, 177)
    y = text(c, y, "", [[("Rogelio drinks ", False), (f"{b} mL", True), (" at breakfast, ", False), ("300 mL", True), (" at lunch,", False)],
                        [("and ", False), (f"{d} mL", True), (" at dinner.", False)]])
    bars(c, MARGIN + 90, y - 10, 300, [("", [(str(b), b, False), ("300", 300, False), (str(d), d, False)])], b + 300 + d, h=26,
         brace=("?", 0, b + 300 + d))
    y -= 80
    rich_line(c, MARGIN, y, [("a.  ", True), ("How much water in all?", False)], 13)
    if not SIMP:
        frame(c, MARGIN + 30, y - 28, "Estimate:  |___|  +  |___|  +  |___|  =  |______", size=13)
    frame(c, MARGIN + 30, y - (60 if not SIMP else 30), f"{b} + 300 = |______|      |______|  +  {d}  =  |______|  mL", size=13)
    y -= 110 if not SIMP else 80
    rich_line(c, MARGIN, y, [("b.  ", True), ("How much ", False), ("more", True), (" at lunch than at dinner?", False)], 13)
    if not SIMP:
        frame(c, MARGIN + 30, y - 28, "Estimate:  |___|  −  |___|  =  |______", size=13)
    frame(c, MARGIN + 30, y - (60 if not SIMP else 30), f"300 − {d} = |______|  mL", size=13)
    column(c, W - MARGIN - 130, y - 10, [300, d], "−")
    if SIMP:
        base10(c, MARGIN + 30, y - 60, 300)
    footer(c, *L28, 195)


PAGES = [p171, p173, p174, p175, p177, p179, p180, p181, p183, p184, p185, p186, p187, p189, p191, p192, p193, p194, p195]


def build():
    global SIMP
    for simp, name in ((False, "G3_M2_TopicF_Modified.pdf"), (True, "G3_M2_TopicF_Simplified_v2.pdf")):
        SIMP = simp
        main(name, PAGES, "Grade 3 Module 2 Topic F – " + ("Simplified" if simp else "Modified"))


if __name__ == "__main__":
    build()
