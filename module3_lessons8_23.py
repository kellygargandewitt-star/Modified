"""Grade 3 Module 3, Lessons 8-23 (book pages 53-151): Modified and Simplified versions.

MODIFIED   - every problem, same numbers; models drawn (strips, arrays, number lines,
             place value charts, area models), blank frames, plain layout.
SIMPLIFIED - fewer problems per page, more visuals (dots/disks drawn, skip-count
             number lines, partly filled frames). Same numbers.
Both keep the book's page and problem numbers.

Run: python3 module3_lessons8_23.py  ->  four PDFs (L8-12 and L13-23, Modified and Simplified)
"""
from reportlab.lib.colors import HexColor, black

import module3_lessons1_7 as M
from build_module2 import MARGIN, W, blank, footer, main, rich_line
from end_of_module_accommodated import table
from lessons_20_24 import bars
from reteach_mid_module import sentence

GREY = HexColor("#666666")
LIGHT = HexColor("#DDDDDD")
DARK = HexColor("#777777")
SIMP = False

L8 = (8, "Count by units of 6 to multiply and divide using number bonds to decompose.")
L9 = (9, "Count by units of 7 to multiply and divide using number bonds to decompose.")
L10 = (10, "Interpret the unknown in multiplication and division using units of 6 and 7.")
L11 = (11, "Understand the function of parentheses and apply to solving problems.")
L12 = (12, "Model the associative property as a strategy to multiply.")
L13 = (13, "Apply the distributive property and the fact 9 = 10 − 1 as a strategy to multiply.")
L14 = (14, "Interpret the unknown in multiplication and division to model and solve problems.")
L15 = (15, "Reason about and explain arithmetic patterns using units of 0 and 1.")
L16 = (16, "Determine if a number is even or odd using the divisibility rule for 2.")
L17 = (17, "Solve two-step word problems involving all four operations.")
L18 = (18, "Multiply by multiples of 10 using the place value chart.")
L19 = (19, "Use strategies to multiply a one-digit number by a two-digit number.")
L20 = (20, "Use concrete models to represent two-digit by one-digit multiplication.")
L21 = (21, "Draw models to represent two-digit by one-digit multiplication.")
L22 = (22, "Use commutative and distributive properties to multiply.")
L23 = (23, "Multiply two-digit numbers by one-digit numbers using the standard algorithm.")

start = M.start
text = M.text
frame = M.frame
dots = M.dots
rdw = M.read_draw_write


def pick(mod, simp):
    return simp if SIMP and simp is not None else mod


def eqs(c, y, items, cols=2, gap=44, size=14, x0=None):
    """Frames laid out in columns. Returns bottom y."""
    cw = (W - 2 * MARGIN - 20) / cols
    for k, s in enumerate(items):
        frame(c, (x0 or MARGIN + 20) + (k % cols) * cw, y - (k // cols) * gap, s, size=size)
    return y - ((len(items) + cols - 1) // cols) * gap


def wp(c, y, num, lines, model=None, frames=(), simp=None, gap=40):
    """Word problem: text, optional model, then frames (simp frames in SIMPLIFIED)."""
    y = text(c, y, num, lines)
    if model:
        y = model(c, y - 10) - 20
    for s in pick(frames, simp):
        frame(c, MARGIN + 24, y - 10, s)
        y -= gap
    return y - 10


def strip(parts, total, brace="?", w=300, x=None, name=""):
    return lambda c, y: bars(c, x or MARGIN + 90, y, w, [(name, [(p, 1, False) for p in parts])], len(parts) if total is None else total,
                             h=26, brace=(brace, 0, len(parts) if total is None else total) if brace else None)


def seq(c, x, y, tokens, size=15, gap=40):
    """Number sequence; '_' = blank, arrows drawn as given."""
    for t in tokens:
        if t == "_":
            blank(c, x, y, 34)
            x += 42
        elif t in ("↑", "↓"):
            rich_line(c, x, y, [(t, True)], size + 2)
            x += 20
        else:
            rich_line(c, x, y, [(t + ",", False)], size)
            x += 12 + 9 * len(t)
        if x > W - MARGIN - 40:
            x, y = MARGIN + 30, y - 34
    return y


def skipline(c, y, step, n, shown, x0=None, x1=None):
    """Number line 0..n*step with jumps; labels for k in shown, boxes for the rest."""
    x0, x1 = x0 or MARGIN + 30, x1 or W - MARGIN - 30
    c.setLineWidth(1.5)
    c.line(x0 - 8, y, x1 + 8, y)
    c.setLineWidth(1)
    for k in range(n + 1):
        tx = x0 + k * (x1 - x0) / n
        c.line(tx, y - 7, tx, y + 7)
        if k in shown:
            c.setFont("Sans", 11)
            c.drawCentredString(tx, y - 22, str(k * step))
        else:
            c.rect(tx - 13, y - 30, 26, 18)
        if k < n:
            c.arc(tx, y + 2, tx + (x1 - x0) / n, y + 26, 0, 180)
            c.setFont("Sans", 8)
            c.drawCentredString(tx + (x1 - x0) / (2 * n), y + 29, f"+{step}")


def blocks(c, x, y, dark, light, s=18, label=None):
    for k in range(dark + light):
        c.setFillColor(DARK if k < dark else LIGHT)
        c.rect(x + k * s, y - s, s, s, stroke=1, fill=1)
    c.setFillColor(black)
    if label:
        c.setFont("Sans-Bold", 9)
        c.setFillColor(HexColor("#FFFFFF") if dark else black)
        c.drawCentredString(x + s / 2, y - s + 5, label)
        c.setFillColor(black)


def disk_chart(c, x, y, rows, tens, ones, cols=("tens", "ones"), w=230, draw=True, hundreds=0, rh=20):
    """Place value chart with disks: `rows` rows of `tens` ten-disks and `ones` one-disks."""
    n = len(cols)
    cw = w / n
    h = 22 + (rows if draw else min(rows, 3)) * rh + 6
    c.rect(x, y - h, w, h)
    for k in range(1, n):
        c.line(x + k * cw, y, x + k * cw, y - h)
    c.line(x, y - 20, x + w, y - 20)
    for k, name in enumerate(cols):
        c.setFont("Sans-Bold", 10)
        c.drawCentredString(x + k * cw + cw / 2, y - 14, name)
    if draw:
        counts = ([hundreds] if n == 3 else []) + [tens, ones]
        labels = (["100"] if n == 3 else []) + ["10", "1"]
        for r in range(rows):
            for k, (cnt, lab) in enumerate(zip(counts, labels)):
                step = min(17, (cw - 14) / max(cnt, 1))
                rad = min(7.5, step / 2 - 0.5, rh / 2 - 1)
                for d in range(cnt):
                    cx = x + k * cw + 10 + d * step
                    cy = y - 22 - rh / 2 - r * rh
                    c.circle(cx, cy, rad)
                    c.setFont("Sans", 6 if len(lab) > 1 else 7)
                    c.drawCentredString(cx, cy - 2.5, lab)
    return y - h


def pp(c, x, y, a, n, filled=False):
    """Vertical partial products frame for n × a."""
    t, o = divmod(a, 10)
    c.setFont("Sans", 16)
    c.drawRightString(x + 70, y, str(a))
    c.drawRightString(x + 70, y - 22, f"× {n}")
    c.setLineWidth(1.5)
    c.line(x + 10, y - 28, x + 74, y - 28)
    c.setLineWidth(1)
    rows = [(str(n * o) if filled else None, f"{n} × {o} ones"), (str(n * t * 10) if filled else None, f"{n} × {t} tens")]
    yy = y - 48
    for k, (val, note) in enumerate(rows):
        if k == 1:
            c.drawString(x + 2, yy, "+")
        if val:
            c.drawRightString(x + 70, yy, val)
        else:
            blank(c, x + 20, yy, 52)
        c.setFont("Sans", 10)
        c.setFillColor(GREY)
        c.drawString(x + 84, yy, note)
        c.setFillColor(black)
        c.setFont("Sans", 16)
        yy -= 24
    c.setLineWidth(1.5)
    c.line(x + 10, yy + 18, x + 74, yy + 18)
    c.setLineWidth(1)
    blank(c, x + 20, yy - 4, 52)
    return yy - 10


def area(c, x, y, n, tens, ones, w=260, h=60, inside=False):
    wt = w * 0.72
    c.rect(x, y - h, wt, h)
    c.rect(x + wt, y - h, w - wt, h)
    c.setFont("Sans-Bold", 13)
    c.drawCentredString(x + wt / 2, y + 6, str(tens))
    c.drawCentredString(x + wt + (w - wt) / 2, y + 6, str(ones))
    c.drawRightString(x - 8, y - h / 2 - 5, str(n))
    if inside:
        c.setFont("Sans", 11)
        c.drawCentredString(x + wt / 2, y - h / 2 - 4, f"{n} × {tens}")
        c.drawCentredString(x + wt + (w - wt) / 2, y - h / 2 - 4, f"{n} × {ones}")
    return y - h


DIST = "(|___| × |___|) + (|___| × |___|) = |___| + |___| = |______"


def dist(c, x, y, s, size=12):
    sentence(c, x, y, s, size=size, blank_w=30, wide_w=50)


# ================================================================ Lessons 8-12

def p53(c):
    y = start(c, "Lesson 8 Application Problem", "TEKS 3.4K", "Equal groups: multiply.")
    wp(c, y, "", [[("Marshall puts ", False), ("6", True), (" pictures on each of ", False), ("6", True), (" pages.", False)],
                  [("How many pictures in all?", False)]],
       (lambda c, y: dots(c, MARGIN + 60, y - 6, 6, 6, gap=18) - 10) if SIMP else strip(["6"] * 6, None),
       ["___| × |___| = |______"], ["6 × 6 = |______|  pictures"])
    rdw(c)
    footer(c, *L8, 53)


SIXES = ["9 × 6", "6 × 6", "4 × 6", "7 × 6", "2 × 6", "1 × 6", "3 × 6", "10 × 6", "5 × 6", "8 × 6"]


def p55(c):
    y = start(c, "Lesson 8 Problem Set", "TEKS 3.4F", "Count by 6: add 6 each time.")
    y = text(c, y, "1.", [[("Skip-count by six. Match each number with its multiplication fact.", False)]])
    if SIMP:
        skipline(c, y - 40, 6, 10, {0, 1, 3, 5, 6, 8, 10})
        y -= 90
        rows = [f"{6 * k} = |___| × 6" if k in (2, 4, 7, 9) else f"{6 * k} = {k} × 6" for k in range(1, 11)]
        eqs(c, y, ["___| = 2 × 6" if r.startswith("12") else r for r in rows], cols=2, gap=36)
    else:
        vals = ["6", "_", "18", "_", "30", "36", "_", "48", "_", "60"]
        for k, (v, f) in enumerate(zip(vals, SIXES)):
            yy = y - 20 - k * 44
            c.circle(MARGIN + 60, yy + 5, 18)
            if v == "_":
                blank(c, MARGIN + 46, yy, 28)
            else:
                c.setFont("Sans-Bold", 13)
                c.drawCentredString(MARGIN + 60, yy, v)
            c.rect(W - MARGIN - 130, yy - 8, 90, 28)
            c.setFont("Sans", 13)
            c.drawCentredString(W - MARGIN - 85, yy, f)
    footer(c, *L8, 55)


def p56(c):
    y = start(c, "Lesson 8 Problem Set", "TEKS 3.4F, 3.4K", "Count by 6: add 6 each time.")
    y = text(c, y, "2.", [[("Count by six.", False)]])
    seq(c, MARGIN + 30, y - 6, ["6", "_", "_", "_"])
    eqs(c, y - 46, ["6 × |___| = |______", "______| ÷ 6 = |___"], cols=2)
    y -= 110
    y = text(c, y, "3.", [[("Count by six.", False)]])
    seq(c, MARGIN + 30, y - 6, ["6", "_", "_", "_", "_", "_", "_"])
    eqs(c, y - 46, ["6 × |___| = |______", "______| ÷ 6 = |___"], cols=2)
    y -= 110
    if not SIMP:
        y = text(c, y, "4.", [[("The class counts up ↑ and down ↓ by six.", False)]])
        y = seq(c, MARGIN + 30, y - 6, ["0", "6", "_", "18", "_", "↓", "_", "12", "↑", "_", "24", "30", "_", "↓", "30", "24",
                                        "_", "↑", "24", "_", "36", "_", "48"], size=13)
        eqs(c, y - 40, ["b.  6 × |___| = 48", "48 ÷ 6 = |___"], cols=2)
        y -= 90
    y = text(c, y, "5.", [[("Julie counts by six to solve ", False), ("6 × 7", True), (". She says ", False), ("36", True),
                          (". Is she right?", False)]])
    if SIMP:
        skipline(c, y - 40, 6, 7, {0, 7}, x1=MARGIN + 380)
        y -= 84
    frame(c, MARGIN + 24, y - 14, "6 × 7 = |______|      Circle:  yes  /  no")
    footer(c, *L8, 56)


def p57(c):
    y = start(c, "Lesson 8 Exit Ticket", "TEKS 3.4F", "Break apart 6 to make the next ten.")
    y = text(c, y, "1.", [[("Sylvia solves ", False), ("6 × 9", True), (" by adding ", False), ("48 + 6", True),
                          (". Break apart the 6 to make a ten.", False)]])
    M.bond(c, MARGIN + 120, y - 30, "6", ["2", "4"] if SIMP else ["", ""])
    eqs(c, y - 30, ["48 + |___| = 50", "50 + |___| = |______", "6 × 9 = |______"], cols=1, x0=MARGIN + 260, gap=40)
    y -= 150
    y = text(c, y, "2.", [[("Skip-count by six to solve.", False)]])
    if SIMP:
        skipline(c, y - 40, 6, 10, {0, 5, 10})
        y -= 84
    eqs(c, y - 14, ["a.  8 × 6 = |______", "b.  54 ÷ 6 = |______"], cols=2)
    footer(c, *L8, 57)


def p59(c):
    y = start(c, "Lesson 9 Application Problem", "TEKS 3.4K", "Rows of the same size: multiply.")
    wp(c, y, "", [[("Gracie draws ", False), ("7", True), (" rows of stars. Each row has ", False), ("4", True), (" stars.", False)],
                  [("How many stars? Use □ for the unknown.", False)]],
       (lambda c, y: dots(c, MARGIN + 60, y - 6, 7, 4, gap=18, shape="star") - 10),
       ["___| × |___| = □      □ = |______"], ["7 × 4 = □      □ = |______|  stars"])
    rdw(c)
    footer(c, *L9, 59)


FISH = [7, 3, 8, 7, 1, 10, 9, 4, 2, 5]   # 7 × n, in the book's fish order (7×6 first)
FISH[0] = 6


def p61(c):
    y = start(c, "Lesson 9 Problem Set", "TEKS 3.4F", "Count by 7: add 7 each time.")
    y = text(c, y, "1.", [[("Skip-count by seven. Match each count to its fact. Then write the division fact.", False)]])
    if SIMP:
        skipline(c, y - 40, 7, 10, {0, 1, 3, 6, 7, 10})
        y -= 100
        rows = [f"7 × {k} = |______|      |______| ÷ 7 = {k}" for k in (2, 4, 5, 8, 9)]
        eqs(c, y, rows, cols=1, gap=38)
    else:
        bowls = ["7", "_", "21", "_", "_", "42", "49", "_", "_", "_"]
        for k, (b, f) in enumerate(zip(bowls, FISH)):
            yy = y - 18 - k * 44
            c.roundRect(MARGIN + 30, yy - 10, 60, 30, 10)
            if b == "_":
                blank(c, MARGIN + 42, yy, 36)
            else:
                c.setFont("Sans-Bold", 13)
                c.drawCentredString(MARGIN + 60, yy, b)
            c.setFont("Sans", 13)
            c.drawString(MARGIN + 180, yy, f"7 × {f}")
            frame(c, MARGIN + 300, yy, "______| ÷ 7 = |______", size=13)
    footer(c, *L9, 61)


def p62(c):
    y = start(c, "Lesson 9 Problem Set", "TEKS 3.4F", "Count by 7: add 7 each time.")
    y = text(c, y, "2.", [[("Finish the count-by-seven. Write the facts for each blank.", False)]])
    seq(c, MARGIN + 30, y - 6, ["7", "14", "_", "28", "_", "42", "_", "_", "63", "_"], size=14)
    rows = ["___| × 7 = |______      ______| ÷ 7 = |___"] * 5
    y = eqs(c, y - 46, [f"{'abcde'[k]}.  " + r for k, r in enumerate(rows)], cols=1, gap=34, size=13)
    if not SIMP:
        y = text(c, y - 6, "3.", [[("Abe says 3 sevens = ", False), ("14 + 6 + 1", True), (" = 21. Why did he add 6 and 1?", False)]])
        frame(c, MARGIN + 24, y - 10, "He broke 7 into |___| and |___| so 14 + 6 makes |______", size=13)
        y -= 50
    y = text(c, y, "4.", [[("Molly counts by 7 six times. James counts by 6 seven times. Who is right?", False)]])
    frame(c, MARGIN + 24, y - 10, "7 × 6 = |______|     6 × 7 = |______|     Circle:  Molly   James   Both", size=13)
    footer(c, *L9, 62)


def p63(c):
    y = start(c, "Lesson 9 Exit Ticket", "TEKS 3.4F", "Count by 7: add 7 each time.")
    y = text(c, y, "", [[("Finish the count-by-seven. Write a multiplication and a division fact.", False)]])
    seq(c, MARGIN + 30, y - 6, ["7", "14", "_", "28", "_", "42", "_", "_", "63", "_"], size=14)
    if SIMP:
        rows = [f"{k} × 7 = |______      ______| ÷ 7 = {k}" for k in (3, 5, 7, 8, 10)]
    else:
        rows = ["___| × 7 = |______      ______| ÷ 7 = |___"] * 10
    eqs(c, y - 46, [f"{'abcdefghij'[k]}.  " + r for k, r in enumerate(rows)], cols=1, gap=31, size=13)
    footer(c, *L9, 63)


WORDS_65 = ["a number times 6 equals 30", "7 times a number equals 42", "6 times 7 equals a number",
            "63 divided by a number equals 9", "36 divided by a number equals 6", "a number times 7 equals 21"]
EQ_65 = ["□ × 7 = 21", "□ × 6 = 30", "6 × 7 = □", "7 × □ = 42", "36 ÷ □ = 6", "63 ÷ □ = 9"]
MATCH_65 = ["□ × 6 = 30", "7 × □ = 42", "6 × 7 = □", "63 ÷ □ = 9", "36 ÷ □ = 6", "□ × 7 = 21"]


def p65(c):
    y = start(c, "Lesson 10 Problem Set", "TEKS 3.4K, 3.5B", "\"A number\" means the box □.")
    y = text(c, y, "1.", [[("Match the words to the correct equation.", False)]])
    for k, w in enumerate(WORDS_65):
        yy = y - 14 - k * 36
        rich_line(c, MARGIN + 24, yy, [(w, False)], 13)
        if SIMP:
            frame(c, MARGIN + 290, yy, MATCH_65[k] + "     □ = |___", size=13)
        else:
            c.rect(MARGIN + 340, yy - 8, 110, 26)
            c.setFont("Sans", 13)
            c.drawCentredString(MARGIN + 395, yy, EQ_65[k])
    y -= 240
    y = text(c, y, "2.", [[("Write an equation with □ for the strip diagram. Solve.", False)]])
    bars(c, MARGIN + 90, y - 10, 300, [("", [("8", 1, False)] * 6)], 6, h=26, brace=("?", 0, 6))
    frame(c, MARGIN + 24, y - 90, "6 × 8 = □      □ = |______" if SIMP else "Equation: |__________|      □ = |______")
    footer(c, *L10, 65)


def p66(c):
    y = start(c, "Lesson 10 Problem Set", "TEKS 3.4K, 3.5B", "Total and group size known? Divide. Groups known? Multiply.")
    y = text(c, y, "3.", [[("Draw a model. Write an equation with □. Solve.", False)]])
    probs = [
        ("a.", [("Each student gets ", False), ("3", True), (" pencils. There are ", False), ("21", True), (" pencils. How many students?", False)],
         strip(["3"] * 7, None, brace="21"), "21 ÷ 3 = □      □ = |______|  students"),
        ("b.", [("Henry spends ", False), ("24", True), (" minutes on ", False), ("6", True), (" drills equally. Minutes on each?", False)],
         strip(["?"] * 6, None, brace="24"), "24 ÷ 6 = □      □ = |______|  minutes"),
        ("c.", [("Jessica has ", False), ("8", True), (" pieces of yarn, each ", False), ("6 cm", True), (". Total length?", False)],
         strip(["6"] * 8, None, w=320), "8 × 6 = □      □ = |______|  cm"),
        ("d.", [("Ginny pours ", False), ("6 mL", True), (" in each beaker. Total ", False), ("54 mL", True), (". How many beakers?", False)],
         strip(["6"] * 9, None, brace="54", w=340), "54 ÷ 6 = □      □ = |______|  beakers"),
    ]
    if SIMP:
        probs = [probs[0], probs[2]]
    for lbl, parts, model, simp_frame in probs:
        rich_line(c, MARGIN + 10, y, [(lbl + " ", True)] + parts, 12.5)
        if SIMP:
            model(c, y - 16)
            frame(c, MARGIN + 24, y - 100, simp_frame)
            y -= 140
        else:
            frame(c, MARGIN + 24, y - 30, "Equation: |__________|      □ = |______")
            y -= 70
    footer(c, *L10, 66)


def p67(c):
    y = start(c, "Lesson 10 Exit Ticket", "TEKS 3.4K, 3.5B", "Equal groups: multiply. Equal sharing: divide.")
    y = wp(c, y, "1.", [[("Six", True), (" students each buy ", False), ("7", True), (" bookmarks. How many in all?", False)]],
           strip(["7"] * 6, None), ["Equation: |__________|      □ = |______"], ["6 × 7 = □      □ = |______|  bookmarks"])
    wp(c, y - 10, "2.", [[("Seven", True), (" friends share a ", False), ("$56", True), (" meal equally. How much each?", False)]],
       strip(["?"] * 7, None, brace="$56"), ["Equation: |__________|      □ = |______"], ["56 ÷ 7 = □      □ = |______|  dollars"])
    footer(c, *L10, 67)


def p69(c):
    y = start(c, "Lesson 11 Application Problem", "TEKS 3.4K, 3.4A", "Do the part in ( ) first.")
    wp(c, y, "", [[("Richard has ", False), ("2", True), (" cartons with ", False), ("6", True), (" eggs each. He drops ", False),
                   ("2", True), (" eggs.", False)], [("How many unbroken eggs are left?", False)]],
       (lambda c, y: (dots(c, MARGIN + 60, y - 6, 2, 6, gap=20) - 10)),
       ["(|___| × |___|) − |___| = |______"], ["(2 × 6) − 2 = |___|  − 2 = |______|  eggs"])
    rdw(c)
    footer(c, *L11, 69)


Q71 = ["(12 – 4) + 6", "12 – (4 + 6)", "15 – (7 + 3)", "(15 – 7) + 3", "(3 + 2) × 6", "3 + (2 × 6)", "4 × (7 – 2)",
       "(4 × 7) – 2", "(12 ÷ 2) + 4", "12 ÷ (2 + 4)", "9 + (15 ÷ 3)", "(9 + 15) ÷ 3", "60 ÷ (10 – 4)", "(60 ÷ 10) – 4",
       "35 + (10 ÷ 5)", "(35 + 10) ÷ 5"]
Q71b = ["16 – 4 + 7 = 19", "16 – 4 + 7 = 5", "2 = 22 – 15 + 5", "12 = 22 – 15 + 5", "3 + 7 × 6 = 60", "3 + 7 × 6 = 45",
        "5 = 10 ÷ 10 × 5", "50 = 100 ÷ 10 × 5", "26 – 5 ÷ 7 = 3", "36 = 4 × 25 – 16"]


def p71(c):
    y = start(c, "Lesson 11 Problem Set", "TEKS 3.4K", "Always solve the part in ( ) first.")
    y = text(c, y, "1.", [[("Solve.", False)]])
    idx = (0, 1, 4, 5, 6, 7) if SIMP else range(16)
    items = [f"{'abcdefghijklmnop'[k]}.  {Q71[k]} = |______" for k in idx]
    y = eqs(c, y - 6, items, cols=2, gap=30 if not SIMP else 40, size=12.5)
    y = text(c, y - 6, "2.", [[("Use ( ) to make each equation true.", False)]])
    idx2 = (0, 1, 4, 5) if SIMP else range(10)
    for k, i in enumerate(idx2):
        rich_line(c, MARGIN + 24 + (k % 2) * 250, y - 10 - (k // 2) * 30, [(f"{'abcdefghij'[i]}.  ", True), (Q71b[i], False)], 13)
    footer(c, *L11, 71)


def p72(c):
    y = start(c, "Lesson 11 Problem Set", "TEKS 3.4K", "Moving the ( ) can change the answer.")
    y = text(c, y, "3.", [[("24 ÷ 4 + 2", True), (". Chad says ", False), ("8", True), (". Samir says ", False), ("4", True),
                          (". Show how both can be true.", False)]])
    y = eqs(c, y - 10, ["Chad:  (24 ÷ 4) + 2 = |______", "Samir:  24 ÷ (4 + 2) = |______"] if SIMP else
            ["Chad:  |____________________|  = 8", "Samir:  |____________________|  = 4"], cols=1, gap=40)
    y = text(c, y - 10, "4.", [[("Natasha finds the sum of 5 and 12. Put in the ( ). Then solve.", False)]])
    frame(c, MARGIN + 24, y - 10, "12 + (15 ÷ 3) = 12 + |___|  = |______" if SIMP else "12 + 15 ÷ 3 = |______")
    y -= 70
    if not SIMP:
        y = text(c, y, "5.", [[("Find two answers for ", False), ("7 + 3 × 2", True), (" by moving the ( ).", False)]])
        eqs(c, y - 10, ["______________|  = |______", "______________|  = |______"], cols=1)
    footer(c, *L11, 72)


def p73(c):
    y = start(c, "Lesson 11 Exit Ticket", "TEKS 3.4K", "Always solve the part in ( ) first.")
    y = text(c, y, "1.", [[("Use ( ) to make each equation true.", False)]])
    for k, s in enumerate(["24 = 32 – 14 + 6", "12 = 32 – 14 + 6", "2 + 8 × 7 = 70", "2 + 8 × 7 = 58"]):
        rich_line(c, MARGIN + 24 + (k % 2) * 250, y - 10 - (k // 2) * 34, [(f"{'abcd'[k]}.  ", True), (s, False)], 14)
    y -= 100
    y = text(c, y, "2.", [[("24 ÷ 6 + 2", True), (". Marcos says ", False), ("6", True), (". Iris says ", False), ("3", True),
                          (". Show both.", False)]])
    eqs(c, y - 10, ["Marcos:  (24 ÷ 6) + 2 = |______", "Iris:  24 ÷ (6 + 2) = |______"] if SIMP else
        ["Marcos:  |____________________|  = 6", "Iris:  |____________________|  = 3"], cols=1, gap=40)
    footer(c, *L11, 73)


PAIRS_75 = [("7 + (6 + 4)", "(7 + 6) + 4"), ("(3 × 2) × 4", "3 × (2 × 4)"), ("(2 × 1) × 5", "2 × (1 × 5)"),
            ("(4 × 2) × 2", "4 × (2 × 2)"), ("(3 + 2) × 5", "3 + (2 × 5)"), ("(8 ÷ 2) × 2", "8 ÷ (2 × 2)"),
            ("(9 – 5) + 3", "9 – (5 + 3)"), ("(8 × 5) – 4", "8 × (5 – 4)")]


def p75(c):
    y = start(c, "Lesson 12 Application Problems", "TEKS 3.4K", "Solve the ( ) first. Circle the pairs with the same answer.")
    idx = (0, 1, 4, 5) if SIMP else range(8)
    for k, i in enumerate(idx):
        x0, y0 = MARGIN + (k % 2) * 260, y - (k // 2) * 100
        rich_line(c, x0, y0, [(f"{i + 1}.", True)], 14)
        frame(c, x0 + 24, y0, f"a.  {PAIRS_75[i][0]} = |______", size=13)
        frame(c, x0 + 24, y0 - 32, f"b.  {PAIRS_75[i][1]} = |______", size=13)
        rich_line(c, x0 + 24, y0 - 62, [("same?  yes / no", False)], 11)
    footer(c, *L12, 75)


def tri_array(c, x, y, rows, cols, groups=None, gap=16, shape="dot"):
    for i in range(rows):
        for j in range(cols):
            g = (j // groups) * 8 if groups else 0
            cx, cy = x + j * gap + g, y - i * gap
            if shape == "tri":
                p = c.beginPath()
                p.moveTo(cx - 6, cy - 5)
                p.lineTo(cx + 6, cy - 5)
                p.lineTo(cx, cy + 6)
                p.close()
                c.drawPath(p, stroke=1, fill=0)
            else:
                c.circle(cx, cy, 5)
    if groups:
        for gidx in range(cols // groups):
            gx = x + gidx * (groups * gap + 8) - 9
            c.roundRect(gx, y - (rows - 1) * gap - 9, groups * gap + 2, (rows - 1) * gap + 18, 5)


def p77(c):
    y = start(c, "Lesson 12 Problem Set", "TEKS 3.4K", "Group the rows to make an easier fact.")
    y = text(c, y, "1.", [[("Use the array to complete the equation.", False)]])
    tri_array(c, MARGIN + 30, y - 10, 3, 12, shape="tri")
    frame(c, MARGIN + 260, y - 20, "a.  3 × 12 = |______")
    tri_array(c, MARGIN + 30, y - 80, 3, 12, groups=3, shape="tri")
    eqs(c, y - 80, ["b.  (3 × 3) × 4", "= |___|  × 4", "= |______"], cols=1, gap=26, x0=MARGIN + 290, size=13)
    y -= 180
    tri_array(c, MARGIN + 30, y - 10, 3, 14)
    frame(c, MARGIN + 320, y - 20, "c.  3 × 14 = |______")
    tri_array(c, MARGIN + 30, y - 80, 3, 14, groups=2)
    eqs(c, y - 80, ["d.  (3 × 2) × 7" if SIMP else "d.  (|___| × |___|) × 7", "= |___|  × |___", "= |______"],
        cols=1, gap=26, x0=MARGIN + 320, size=13)
    footer(c, *L12, 77)


def p78(c):
    y = start(c, "Lesson 12 Problem Set", "TEKS 3.4K", "Put ( ) around the two numbers that make an easy fact.")
    y = text(c, y, "2.", [[("Place ( ) to make it true. Then solve. The first one is done for you.", False)]])
    probs = [("a.", "3 × 16 = 3 × (2 × 8)", "= (3 × 2) × 8", "= 6 × 8 = 48"),
             ("b.", "2 × 14 = 2 × (2 × 7)", "= (2 × 2) × 7", "= |___|  × 7 = |______"),
             ("c.", "3 × 12 = 3 × 3 × 4", "= 3 × 3 × 4" if not SIMP else "= (3 × 3) × 4", "= |___|  × |___|  = |______"),
             ("d.", "3 × 14 = 3 × 2 × 7", "= 3 × 2 × 7" if not SIMP else "= (3 × 2) × 7", "= |___|  × |___|  = |______"),
             ("e.", "15 × 3 = 5 × 3 × 3", "= 5 × 3 × 3", "= |___|  × |___|  = |______"),
             ("f.", "15 × 2 = 5 × 3 × 2", "= 5 × 3 × 2", "= |___|  × |___|  = |______")]
    if SIMP:
        probs = probs[:4]
    for k, (lbl, a, b, d) in enumerate(probs):
        x0, y0 = MARGIN + (k % 2) * 260, y - 10 - (k // 2) * 100
        rich_line(c, x0, y0, [(lbl + " ", True), (a, False)], 13)
        rich_line(c, x0 + 60, y0 - 24, [(b, False)], 13)
        sentence(c, x0 + 40, y0 - 48, d, size=13, blank_w=34, wide_w=50)
    y -= 10 + ((len(probs) + 1) // 2) * 100
    y = text(c, y, "3.", [[("Gianna solves ", False), ("16 × 2", True), (" by thinking ", False), ("8 × 4", True), (". Explain.", False)]])
    frame(c, MARGIN + 24, y - 10, "16 = 8 × |___|,  so 16 × 2 = 8 × |___|  × 2 = 8 × |___|  = |______", size=13)
    footer(c, *L12, 78)


def p79(c):
    y = start(c, "Lesson 12 Exit Ticket", "TEKS 3.4K", "Break a big number into two smaller factors.")
    y = text(c, y, "", [[("Find ", False), ("18 × 3", True), (". Show your work and explain your strategy.", False)]])
    if SIMP:
        eqs(c, y - 20, ["18 = 6 × 3", "18 × 3 = 6 × 3 × 3", "= 6 × (3 × 3)", "= 6 × |___", "= |______"], cols=1, gap=36)
    else:
        eqs(c, y - 20, ["18 = |___|  × |___", "18 × 3 = |___|  × |___|  × 3", "= |___|  × |___", "= |______"], cols=1, gap=40)
    footer(c, *L12, 79)


PAGES_8_12 = [p53, p55, p56, p57, p59, p61, p62, p63, p65, p66, p67, p69, p71, p72, p73, p75, p77, p78, p79]


# ================================================================ Lessons 13-23

def nines(c, x, y, extra):
    """5 dark blocks (5 × 9) and `extra` light blocks; each block is worth 9."""
    blocks(c, x, y, 5, 0)
    blocks(c, x, y - 26, 0, extra)
    rich_line(c, x + 100, y - 14, [("5 × 9 = 45", False)], 11)
    rich_line(c, x + 20 + extra * 18, y - 40, [(f"{extra} × 9", False)], 11)


def p81(c):
    y = start(c, "Lesson 13 Application Problem", "TEKS 3.4K", "5 nines + 3 nines = 8 nines.")
    wp(c, y, "", [[("5", True), (" test tubes have ", False), ("9 mL", True), (" each. ", False), ("3", True),
                   (" more test tubes have ", False), ("9 mL", True), (" each.", False)], [("How many mL in all?", False)]],
       strip(["9"] * 8, None, w=340),
       ["(5 × 9) + (|___| × |___|) = |___|  + |___|  = |______"],
       ["(5 × 9) + (3 × 9) = 45 + |___|  = |______|  mL"])
    rdw(c)
    footer(c, *L13, 81)


def p83(c):
    y = start(c, "Lesson 13 Problem Set", "TEKS 3.4K", "Each block is worth 9. Start with 5 nines = 45.")
    y = text(c, y, "1.", [[("Each block has a value of ", False), ("9", True), (". Find each row. Then add.", False)]])
    probs = [("a.", 6, 1), ("b.", 7, 2), ("c.", 8, 3), ("d.", 9, 4)]
    if SIMP:
        probs = probs[:2]
    for k, (lbl, n, e) in enumerate(probs):
        x0, y0 = MARGIN + (k % 2) * 260, y - 10 - (k // 2) * 220
        rich_line(c, x0, y0, [(f"{lbl}  {n} × 9 = ", True)], 13)
        blank(c, x0 + 90, y0, 50)
        nines(c, x0 + 10, y0 - 14, e)
        eqs(c, y0 - 80, [f"{n} × 9 = (5 + {e}) × 9" if SIMP else f"{n} × 9 = (5 + |___|) × 9",
                         f"= (5 × 9) + ({e} × 9)" if SIMP else "= (5 × 9) + (|___| × |___|)",
                         "= 45 + |______", "= |______"], cols=1, gap=26, x0=x0 + 10, size=12.5)
    footer(c, *L13, 83)


def tens_bar(c, x, y, n, w=200):
    """10 boxes of n with the last one crossed out (10 × n − 1 × n)."""
    s = w / 10
    for k in range(10):
        c.setFillColor(LIGHT if k < 9 else HexColor("#FFFFFF"))
        c.rect(x + k * s, y - 20, s, 20, stroke=1, fill=1)
    c.setFillColor(black)
    c.setFont("Sans-Bold", 10)
    c.drawCentredString(x + s / 2, y - 14, str(n))
    c.line(x + 9 * s, y - 20, x + 10 * s, y)


def p84(c):
    y = start(c, "Lesson 13 Problem Set", "TEKS 3.4K", "9 groups = 10 groups − 1 group.")
    y = text(c, y, "2.", [[("Find the value of the shaded blocks.", False)]])
    probs = [("a.", 6), ("b.", 7), ("c.", 8), ("d.", 9)]
    if SIMP:
        probs = probs[:2]
    names = {6: "sixes", 7: "sevens", 8: "eights", 9: "nines"}
    one = {6: "six", 7: "seven", 8: "eight", 9: "nine"}
    for k, (lbl, n) in enumerate(probs):
        x0, y0 = MARGIN + (k % 2) * 260, y - 10 - (k // 2) * 150
        rich_line(c, x0, y0, [(f"{lbl}  9 × {n} = ", True)], 13)
        blank(c, x0 + 80, y0, 50)
        tens_bar(c, x0 + 10, y0 - 12, n)
        rich_line(c, x0 + 10, y0 - 50, [(f"9 {names[n]} = 10 {names[n]} − 1 {one[n]}", False)], 11)
        eqs(c, y0 - 76, [f"= {10 * n} − {n}" if SIMP else f"= |___|  − {n}", "= |______"], cols=1, gap=26, x0=x0 + 10, size=12.5)
    y -= 10 + ((len(probs) + 1) // 2) * 150
    y = text(c, y, "3.", [[("Matt counts ", False), ("9", True), (" rows of ", False), ("4", True),
                          (" stamps. He thinks of 10 fours. Show his strategy.", False)]])
    if SIMP:
        tens_bar(c, MARGIN + 30, y - 6, 4)
        y -= 34
    frame(c, MARGIN + 24, y - 14, "10 × 4 = |______|      |______|  − 4 = |______|  stamps")
    footer(c, *L13, 84)


def p85(c):
    y = start(c, "Lesson 13 Problem Set", "TEKS 3.4F", "Use the number bank. Each number is used once.")
    y = text(c, y, "4.", [[("Match. Write the answer for each one.", False)]])
    rich_line(c, MARGIN + 24, y - 4, [("Number bank:  ", True), ("81   10   27   5   36   1   6   72   18   8", False)], 13)
    left = ["3 × 9", "9 × 9", "8 × 9", "9 × 4", "2 × 9"]
    right = ["45 ÷ 9", "9 ÷ 9", "90 ÷ 9", "72 ÷ 9", "54 ÷ 9"]
    if SIMP:
        left, right = left[:3], right[:3]
    for k, (a, b) in enumerate(zip(left, right)):
        yy = y - 50 - k * 56
        frame(c, MARGIN + 30, yy, f"{a} = |______", size=16)
        frame(c, MARGIN + 290, yy, f"{b} = |______", size=16)
    footer(c, *L13, 85)


def p87(c):
    y = start(c, "Lesson 13 Exit Ticket", "TEKS 3.4K", "Each block is worth 9. Start with 5 nines = 45.")
    y = text(c, y, "1.", [[("Each block is worth ", False), ("9", True), (". Find the value of the tower (6 blocks).", False)]])
    for k in range(6):
        c.setFillColor(LIGHT if k == 0 else DARK)
        c.rect(MARGIN + 40, y - 20 - k * 20, 26, 20, stroke=1, fill=1)
    c.setFillColor(black)
    eqs(c, y - 20, ["6 × 9 = (5 + 1) × 9" if SIMP else "___| × 9 = (5 + |___|) × 9",
                    "= (5 × 9) + (1 × 9)" if SIMP else "= (5 × |___|) + (|___| × |___|)",
                    "= 45 + |______", "= |______"], cols=1, gap=32, x0=MARGIN + 120)
    y -= 170
    y = text(c, y, "2.", [[("Hector solves ", False), ("9 × 8", True), (" by subtracting 1 eight from 10 eights.", False)]])
    tens_bar(c, MARGIN + 30, y - 6, 8, w=260)
    frame(c, MARGIN + 24, y - 50, "10 × 8 = |______|      |______|  − 8 = |______")
    footer(c, *L13, 87)


def p91(c):
    y = start(c, "Lesson 14 Problem Set", "TEKS 3.4K, 3.5B", "Use □ for the unknown.")
    y = text(c, y, "", [[("Write an equation with □ for each problem. Solve.", False)]])
    y = wp(c, y, "1.", [[("Mrs. Parson gives each friend ", False), ("$9", True), (". She gives ", False), ("$36", True),
                         (". How many friends?", False)]],
           strip(["$9"] * 4, None, brace="$36") if SIMP else None, ["Equation: |__________|      □ = |______"],
           ["36 ÷ 9 = □      □ = |______|  friends"])
    if not SIMP:
        y = wp(c, y, "2.", [[("Shiva pours ", False), ("27 L", True), (" equally into ", False), ("9", True),
                             (" containers. Liters in each?", False)]], None, ["Equation: |__________|      □ = |______"])
    wp(c, y, "3.", [[("Derek cuts ", False), ("7", True), (" pieces of wire. Each is ", False), ("9 m", True), (". Total length?", False)]],
       strip(["9"] * 7, None) if SIMP else None, ["Equation: |__________|      □ = |______"], ["7 × 9 = □      □ = |______|  m"])
    footer(c, *L14, 91)


def p92(c):
    y = start(c, "Lesson 14 Problem Set", "TEKS 3.4K, 3.5B", "Two steps: do Step 1, then use that answer in Step 2.")
    y = wp(c, y, "4.", [[("Aunt Deena, Uncle Chris, and ", False), ("7", True), (" friends share ", False), ("$63", True),
                         (" equally.", False)], [("How much does each person pay?", False)]],
           None, ["People: 2 + 7 = |___|      63 ÷ |___|  = □      □ = |______"])
    if not SIMP:
        y = wp(c, y, "5.", [[("Cara buys ", False), ("8", True), (" packs of ", False), ("5", True), (" beads. Each necklace uses ", False),
                             ("10", True), (" beads.", False)], [("How many necklaces?", False)]],
               None, ["8 × 5 = |______|      |______|  ÷ 10 = □      □ = |______"])
    wp(c, y, "6.", [[("A set has ", False), ("8", True), (" erasers. Damon buys ", False), ("9", True), (" sets. He has ", False),
                     ("35", True), (" left.", False)], [("How many did he give away?", False)]],
       None, ["9 × 8 = |______|      |______|  − 35 = □      □ = |______"])
    footer(c, *L14, 92)


def p93(c):
    y = start(c, "Lesson 14 Exit Ticket", "TEKS 3.4K, 3.5B", "Use □ for the unknown.")
    y = wp(c, y, "1.", [[("Mrs. Aquino pours ", False), ("36 L", True), (" equally into ", False), ("9", True),
                         (" containers. How much in each?", False)]],
           strip(["?"] * 9, None, brace="36 L", w=340) if SIMP else None, ["Equation: |__________|      □ = |______"],
           ["36 ÷ 9 = □      □ = |______|  liters"])
    wp(c, y, "2.", [[("Marlon buys ", False), ("9", True), (" packs of ", False), ("6", True), (" hot dogs. ", False), ("35", True),
                     (" are left over. How many were eaten?", False)]],
       None, ["9 × 6 = |______|      |______|  − 35 = □      □ = |______"])
    footer(c, *L14, 93)


def p95(c):
    y = start(c, "Lesson 15 Problem Set", "TEKS 3.4K", "× 1: same number.  × 0: always 0.  0 ÷ a number: 0.")
    y = text(c, y, "1.", [[("Complete.", False)]])
    q1 = ["___|  × 1 = 6", "___|  ÷ 7 = 0", "8 × |___|  = 8", "9 ÷ |___|  = 9", "0 ÷ 5 = |___", "___|  × 0 = 0",
          "4 ÷ |___|  = 1", "___|  × 1 = 3"]
    idx = (0, 1, 2, 4, 6, 7) if SIMP else range(8)
    y = eqs(c, y - 6, [f"{'abcdefgh'[k]}.  {q1[k]}" for k in idx], cols=3 if SIMP else 2, gap=30, size=12.5)
    y = text(c, y - 6, "2.", [[("Find the missing number ( ? ) in each equation.", False)]])
    mice = ["1 × ? = 3", "? ÷ 4 = 0", "1 × 6 = ?", "7 ÷ 7 = ?", "? × 1 = 9", "? ÷ 1 = 8"]
    if SIMP:
        mice = mice[:4]
    y = eqs(c, y - 6, [f"{m}     ? = |___" for m in mice], cols=2, gap=32, size=13)
    y = text(c, y - 6, "3.", [[("Let ", False), ("n", True), (" be a number. Find each product.", False)]])
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "n"] if not SIMP else ["1", "2", "3", "4", "5", "n"]
    for k, n in enumerate(nums):
        sentence(c, MARGIN + 24 + (k % 5) * 100, y - 10 - (k // 5) * 34, f"{n} × 1 = |___", size=13, blank_w=34)
    y -= 10 + ((len(nums) + 4) // 5) * 34
    frame(c, MARGIN + 24, y - 10, "Pattern: any number × 1 = |__________", size=13)
    footer(c, *L15, 95)


def p96(c):
    y = start(c, "Lesson 15 Problem Set", "TEKS 3.4K", "Any number ÷ 1 = that number. You cannot divide by 0.")
    y = text(c, y, "4.", [[("Josie says any number divided by 1 equals that number.", False)]])
    y = eqs(c, y - 6, ["a.  n ÷ 1 = |___", "b.  6 ÷ 1 = |___", "c.  |___|  × 1 = 6"][:3 if not SIMP else 2], cols=1, gap=36)
    if SIMP:
        dots(c, MARGIN + 260, y + 50, 1, 6, gap=20)
        rich_line(c, MARGIN + 260, y + 24, [("6 in 1 group", False)], 11)
    y = text(c, y - 10, "5.", [[("What would Matt tell his sister?", False)]])
    items = [("a.  0 ÷ 9 = |___", "Zero shared into 9 groups is |___|  in each group."),
             ("b.  8 ÷ 0", "Circle:  It is 0   /   You cannot divide by 0"),
             ("c.  0 ÷ 0", "Circle:  It is 0   /   You cannot divide by 0")]
    if SIMP:
        items = items[:2]
    for a, b in items:
        frame(c, MARGIN + 24, y - 10, a, size=14)
        rich_line(c, MARGIN + 200, y - 10, [(b.replace("|___|", "___"), False)], 12)
        y -= 44
    footer(c, *L15, 96)


def p97(c):
    y = start(c, "Lesson 15 Exit Ticket", "TEKS 3.4K", "× 1: same number.  × 0: always 0.  You cannot divide by 0.")
    y = text(c, y, "1.", [[("Complete.", False)]])
    y = eqs(c, y - 6, ["a.  |___|  × 1 = 5", "b.  6 × |___|  = 6", "c.  |___|  ÷ 7 = 0", "d.  5 × |___|  = 0",
                       "e.  1 = 9 ÷ |___", "f.  8 = 1 × |___"], cols=3, gap=40)
    y = text(c, y - 10, "2.", [[("Luis says ", False), ("8 ÷ 0 = 0", True), (". Is he correct?", False)]])
    rich_line(c, MARGIN + 24, y - 10, [("Circle:  ", False), ("yes  /  no", True), ("      You cannot divide by ", False)], 13)
    blank(c, MARGIN + 330, y - 10, 40)
    footer(c, *L15, 97)


def p99(c):
    y = start(c, "Lesson 16 Application Problem", "TEKS 3.4K", "9 eights + 1 eight = 10 eights.")
    wp(c, y, "", [[("9", True), (" rows of squash with ", False), ("8", True), (" plants each. ", False), ("1", True),
                   (" row of ", False), ("8", True), (" watermelon plants.", False)], [("How many plants in all?", False)]],
       strip(["8"] * 10, None, w=360),
       ["(|___| × |___|) + |___|  = |______"], ["(9 × 8) + 8 = 72 + 8 = |______|  plants"])
    rdw(c)
    footer(c, *L16, 99)


def p101(c):
    y = start(c, "Lesson 16 Problem Set", "TEKS 3.4K", "Even numbers end in 0, 2, 4, 6, or 8. Odd numbers end in 1, 3, 5, 7, or 9.")
    y = text(c, y, "1.", [[("Can every student have a partner? Put an X. Then write odd or even.", False)]])
    rows = [["Kindergarten", "45", "", "", ""], ["1st Grade", "37", "", "", ""], ["2nd Grade", "52", "", "", ""],
            ["3rd Grade", "48", "", "", ""], ["4th Grade", "61", "", "", ""], ["5th Grade", "62", "", "", ""]]
    table(c, MARGIN, y - 6, ["Grade", "Students", "All have partner", "1 left over", "Odd or Even?"], rows,
          [100, 70, 120, 100, 132], rh=32)
    if SIMP:
        rich_line(c, MARGIN, y - 260, [("Look at the ", False), ("ones", True), (" digit:  0 2 4 6 8 → even      1 3 5 7 9 → odd", False)], 12)
    footer(c, *L16, 101)


def p102(c):
    y = start(c, "Lesson 16 Problem Set", "TEKS 3.4K", "Even numbers can be split into pairs with none left over.")
    y = text(c, y, "2.", [[("Mr. Jones has ", False), ("20", True), (" desks. Each row has ", False), ("2", True),
                          (" desks. How many rows?", False)]])
    rich_line(c, MARGIN + 24, y - 6, [("a.  ", True), ("Array:", False)], 13)
    if SIMP:
        dots(c, MARGIN + 100, y - 6, 2, 10, gap=22)
    else:
        c.setStrokeColor(HexColor("#BBBBBB"))
        c.rect(MARGIN + 100, y - 70, 300, 70)
        c.setStrokeColor(black)
    y -= 100
    rich_line(c, MARGIN + 24, y, [("b.  ", True), ("Is 20 odd or even?  Circle:  ", False), ("odd  /  even", True)], 13)
    frame(c, MARGIN + 50, y - 34, "The ones digit is |___", size=13)
    y -= 80
    frame(c, MARGIN + 24, y, "c.  20 ÷ 2 = |______|  rows" if SIMP else "c.  |___|  ÷ |___|  = |______")
    footer(c, *L16, 102)


def p103(c):
    y = start(c, "Lesson 16 Problem Set", "TEKS 3.4K", "Even numbers end in 0, 2, 4, 6, or 8.")
    y = text(c, y, "3.", [[("Circle the buildings with ", False), ("even", True), (" numbers.", False)]])
    nums = ["95", "88", "352", "77", "64", "500", "48", "421"]
    for k, n in enumerate(nums):
        x0, y0 = MARGIN + 20 + (k % 4) * 125, y - 20 - (k // 4) * 90
        c.rect(x0, y0 - 60, 80, 60)
        c.line(x0, y0, x0 + 40, y0 + 22)
        c.line(x0 + 40, y0 + 22, x0 + 80, y0)
        c.setFont("Sans-Bold", 16)
        c.drawCentredString(x0 + 40, y0 - 36, n)
    y -= 210
    y = text(c, y, "4.", [[("My number is between ", False), ("26 and 39", True), (". It is a multiple of 5. It is even.", False)]])
    if SIMP:
        rich_line(c, MARGIN + 24, y - 6, [("Multiples of 5 between 26 and 39:  ", False), ("30   35", True)], 13)
        y -= 26
    frame(c, MARGIN + 24, y - 14, "My number is |______")
    footer(c, *L16, 103)


def p104(c):
    y = start(c, "Lesson 16 Problem Set", "TEKS 3.4K", "Only the ones digit tells you odd or even.")
    y = text(c, y, "5.", [[("Julia says ", False), ("958", True), (" is odd because it has two odd digits. Why is she wrong?", False)]])
    frame(c, MARGIN + 24, y - 14, "The ones digit is |___|, so 958 is |______", size=14)
    y -= 70
    if not SIMP:
        y = text(c, y, "6.", [[("Write your own mystery number riddle. Include an odd or even clue.", False)]])
        for k in range(3):
            blank(c, MARGIN + 24, y - 20 - k * 34, W - 2 * MARGIN - 48)
    footer(c, *L16, 104)


def p105(c):
    y = start(c, "Lesson 16 Exit Ticket", "TEKS 3.4K", "Even numbers end in 0, 2, 4, 6, or 8.")
    y = text(c, y, "1.", [[("The mystery number is ", False), ("even", True), (" and ", False), ("greater than 50", True),
                          (". Circle all that could be it.", False)]])
    nums = ["78", "130", "99", "56", "34", "87", "100", "222"]
    for k, n in enumerate(nums):
        c.setFont("Sans-Bold", 18)
        c.drawCentredString(MARGIN + 50 + (k % 4) * 125, y - 30 - (k // 4) * 50, n)
    y -= 130
    y = text(c, y, "2.", [[("Luis says ", False), ("621", True), (" is even because the hundreds digit is even. Is he correct?", False)]])
    frame(c, MARGIN + 24, y - 14, "The ones digit is |___|, so 621 is |______", size=14)
    rich_line(c, MARGIN + 24, y - 50, [("Circle:  Luis is  ", False), ("correct  /  not correct", True)], 13)
    footer(c, *L16, 105)


def two(c, y, num, lines, s1, s2, model=None):
    y = text(c, y, num, lines)
    if model and SIMP:
        y = model(c, y - 10) - 16
    frame(c, MARGIN + 24, y - 10, "Step 1:  " + s1, size=14)
    frame(c, MARGIN + 24, y - 46, "Step 2:  " + s2, size=14)
    return y - 90


def p107(c):
    y = start(c, "Lesson 17 Problem Set", "TEKS 3.4K, 3.5A", "Two steps: do Step 1, then use that answer in Step 2.")
    y = two(c, y, "1.", [[("Rose has ", False), ("6", True), (" pieces of yarn, each ", False), ("9 cm", True),
                         (". Sasha gives her one more.", False)], [("Now she has ", False), ("81 cm", True),
                                                                   (". How long is Sasha's piece?", False)]],
            "6 × 9 = |______", "81 − |______|  = |______|  cm", strip(["9"] * 6 + ["?"], None, brace="81", w=330))
    two(c, y, "2.", [[("Julio spends ", False), ("29", True), (" minutes on spelling, then ", False), ("7", True),
                     (" math problems at ", False), ("4", True), (" minutes each.", False)], [("How many minutes in all?", False)]],
        "7 × 4 = |______", "29 + |______|  = |______|  minutes", strip(["29"] + ["4"] * 7, None, w=330))
    footer(c, *L17, 107)


def p108(c):
    y = start(c, "Lesson 17 Problem Set", "TEKS 3.4K, 3.5A", "Two steps: do Step 1, then use that answer in Step 2.")
    y = two(c, y, "3.", [[("Pearl has ", False), ("125", True), (" stickers. She gives away ", False), ("53", True),
                         (". She puts ", False), ("9", True), (" on each page.", False)], [("How many pages?", False)]],
            "125 − 53 = |______", "______|  ÷ 9 = |______|  pages")
    if not SIMP:
        y = two(c, y, "4.", [[("A beaker had ", False), ("45 mL", True), (". Each friend pours ", False), ("8 mL", True),
                             (". Now it has ", False), ("93 mL", True), (".", False)], [("How many friends poured?", False)]],
                "93 − 45 = |______", "______|  ÷ 8 = |______|  friends")
    two(c, y, "5.", [[("4", True), (" staplers and a hole punch weigh ", False), ("55 oz", True), (". The punch weighs ", False),
                     ("19 oz", True), (".", False)], [("How much does each stapler weigh?", False)]],
        "55 − 19 = |______", "______|  ÷ 4 = |______|  oz", strip(["?"] * 4 + ["19"], None, brace="55 oz", w=300))
    footer(c, *L17, 108)


def p109(c):
    y = start(c, "Lesson 17 Exit Ticket", "TEKS 3.4K, 3.5A", "Two steps: do Step 1, then use that answer in Step 2.")
    two(c, y, "", [[("Warren swims ", False), ("45", True), (" minutes Saturday. Sunday he runs ", False), ("8", True),
                    (" miles at ", False), ("9", True), (" minutes each.", False)], [("How long does he exercise in all?", False)]],
        "8 × 9 = |______", "45 + |______|  = |______|  minutes", strip(["45"] + ["9"] * 8, None, w=340))
    footer(c, *L17, 109)


def p111(c):
    y = start(c, "Lesson 18 Application Problem", "TEKS 3.4K, 3.4A", "Two steps: subtract, then divide.")
    two(c, y, "", [[("Mia has ", False), ("152", True), (" beads. Now she has ", False), ("80", True), (". Each bracelet uses ", False),
                    ("8", True), (" beads.", False)], [("How many bracelets?", False)]],
        "152 − 80 = |______", "______|  ÷ 8 = |______|  bracelets")
    rdw(c)
    footer(c, *L18, 111)


def chart_item(c, x, y, rows, tens, ones, lines):
    disk_chart(c, x, y, rows, tens, ones, w=200, rh=16)
    eqs(c, y - 30, lines, cols=1, gap=30, x0=x + 214, size=12.5)


def p113(c):
    y = start(c, "Lesson 18 Problem Set", "TEKS 3.4K", "3 ones × 4 = 12 ones.  3 tens × 4 = 12 tens.")
    y = text(c, y, "1.", [[("Use the disks to fill in the blanks.", False)]])
    chart_item(c, MARGIN, y - 6, 4, 0, 3, ["4 × 3 ones = |___|  ones", "4 × 3 = |______"])
    y -= 110
    chart_item(c, MARGIN, y, 4, 3, 0, ["4 × 3 tens = |___|  tens", "4 × 30 = |______"])
    y -= 114
    y = text(c, y, "2.", [[("Use the chart to fill in the blanks.", False)]])
    items = [(2, 0, 4, "2 × 4 ones = |___|  ones", "2 × 4 = |______"), (2, 4, 0, "2 × 4 tens = |___|  tens", "2 × 40 = |______"),
             (3, 0, 5, "3 × 5 ones = |___|  ones", "3 × 5 = |______"), (3, 5, 0, "3 × 5 tens = |___|  tens", "3 × 50 = |______")]
    if SIMP:
        items = items[:2]
    for k, (r, t, o, a, b) in enumerate(items):
        x0, y0 = MARGIN + (k % 2) * 260, y - 6 - (k // 2) * 130
        bot = disk_chart(c, x0, y0, r, t, o, w=150, draw=True, rh=16)
        eqs(c, bot - 18, [a, b], cols=1, gap=26, x0=x0, size=11.5)
    footer(c, *L18, 113)


def p114(c):
    y = start(c, "Lesson 18 Problem Set", "TEKS 3.4K", "Multiply the basic fact. Then add a 0 for tens.")
    items = [(4, 0, 5, "e.  4 × 5 ones = |___|  ones", "4 × 5 = |______"), (4, 5, 0, "f.  4 × 5 tens = |___|  tens", "4 × 50 = |______")]
    for k, (r, t, o, a, b) in enumerate(items):
        x0 = MARGIN + k * 260
        bot = disk_chart(c, x0, y, r, t, o, w=150, rh=16) if SIMP else y
        eqs(c, bot - (18 if SIMP else 10), [a, b], cols=1, gap=26, x0=x0, size=11.5)
    y -= 170 if SIMP else 70
    y = text(c, y, "3.", [[("Fill in the blank to make the equation true.", False)]])
    q3 = ["a.  |______|  = 7 × 2", "b.  |___|  tens = 7 tens × 2", "c.  |______|  = 8 × 3", "d.  |___|  tens = 8 tens × 3",
          "e.  |______|  = 60 × 5", "f.  |______|  = 4 × 80", "g.  7 × 40 = |______", "h.  50 × 8 = |______"]
    if SIMP:
        q3 = [q3[0], q3[1], q3[6]]
    y = eqs(c, y - 6, q3, cols=2, gap=36, size=13)
    y = text(c, y - 6, "4.", [[("A bus carries ", False), ("40", True), (" passengers. How many can ", False), ("6", True),
                              (" buses carry?", False)]])
    bars(c, MARGIN + 90, y - 6, 330, [("", [("40", 1, False)] * 6)], 6, h=26, brace=("?", 0, 6))
    frame(c, MARGIN + 24, y - 84, "6 × 40 = |______|  passengers" if SIMP else "___| × |___| = |______")
    footer(c, *L18, 114)


def p115(c):
    y = start(c, "Lesson 18 Exit Ticket", "TEKS 3.4K", "Multiply the basic fact. Then add a 0 for tens.")
    y = text(c, y, "1.", [[("Use the chart to fill in the blanks.", False)]])
    if SIMP:
        disk_chart(c, MARGIN, y - 6, 6, 0, 5, w=150, rh=16)
        disk_chart(c, MARGIN + 260, y - 6, 6, 5, 0, w=150, rh=16)
        y -= 140
    eqs(c, y - 10, ["6 × 5 ones = |___|  ones", "6 × 5 tens = |___|  tens", "6 × 5 = |______", "6 × 50 = |______"], cols=2, gap=34)
    y -= 90
    y = text(c, y, "2.", [[("A small plane has ", False), ("20", True), (" rows of ", False), ("4", True), (" seats.", False)]])
    eqs(c, y - 10, ["a.  20 × 4 = |______|  seats", "b.  3 × |______|  = |______|  seats"], cols=1, gap=40)
    footer(c, *L18, 115)


def p117(c):
    y = start(c, "Lesson 19 Application Problem", "TEKS 3.4K", "30 × 4 is 10 times as much as 3 × 4.")
    y = text(c, y, "", [[("Model ", False), ("3 × 4", True), (" on a place value chart. Then use it to solve ", False),
                         ("30 × 4", True), (".", False)]])
    disk_chart(c, MARGIN + 30, y - 10, 3, 0, 4, w=200, draw=SIMP)
    eqs(c, y - 40, ["3 × 4 = |______", "30 × 4 = |______"], cols=1, gap=40, x0=MARGIN + 270)
    rdw(c)
    footer(c, *L19, 117)


def p119(c):
    y = start(c, "Lesson 19 Problem Set", "TEKS 3.4K", "Solve the ( ) first. Then × 10.")
    y = text(c, y, "1.", [[("Complete the equations. The first one is done for you.", False)]])
    items = [("a.", "(2 × 4) × 10", "= (8 ones) × 10", "= 80"), ("b.", "2 × (4 × 10)", "= 2 × (4 tens)", "= |______"),
             ("c.", "(3 × 5) × 10", "= (|___|  ones) × 10", "= |______"), ("d.", "3 × (5 × 10)", "= 3 × (|___|  tens)", "= |______")]
    for k, (lbl, a, b, d) in enumerate(items):
        x0, y0 = MARGIN + (k % 2) * 260, y - 10 - (k // 2) * 130
        rich_line(c, x0, y0, [(lbl + "  ", True), (a, True)], 14)
        frame(c, x0 + 30, y0 - 30, b, size=13)
        frame(c, x0 + 30, y0 - 60, d, size=13)
    footer(c, *L19, 119)


def p120(c):
    y = start(c, "Lesson 19 Problem Set", "TEKS 3.4K", "Group the basic fact first: (2 × 3) × 10.")
    y = text(c, y, "2.", [[("Place ( ) to find the related fact. Then solve. The first one is done for you.", False)]])
    items = [("2 × 20 = 2 × (2 × 10)", "= (2 × 2) × 10", "= 4 × 10 = 40"),
             ("2 × 30 = 2 × (3 × 10)", "= (2 × 3) × 10", "= |___|  × 10 = |______"),
             ("3 × 30 = 3 × (3 × 10)", "= 3 × 3 × 10" if not SIMP else "= (3 × 3) × 10", "= |___|  × 10 = |______"),
             ("2 × 50 = 2 × 5 × 10", "= 2 × 5 × 10" if not SIMP else "= (2 × 5) × 10", "= |___|  × 10 = |______")]
    for k, (a, b, d) in enumerate(items):
        x0, y0 = MARGIN + (k % 2) * 260, y - 10 - (k // 2) * 110
        rich_line(c, x0, y0, [(a, True)], 13)
        rich_line(c, x0 + 40, y0 - 26, [(b, False)], 13)
        frame(c, x0 + 40, y0 - 52, d, size=13)
    y -= 240
    y = text(c, y, "3.", [[("Gabriella solves ", False), ("20 × 4", True), (" by thinking ", False), ("10 × 8", True), (". Explain.", False)]])
    frame(c, MARGIN + 24, y - 10, "20 = 10 × 2,  so 20 × 4 = 10 × 2 × 4 = 10 × |___|  = |______", size=13)
    footer(c, *L19, 120)


def p121(c):
    y = start(c, "Lesson 19 Exit Ticket", "TEKS 3.4K", "Group the basic fact first.")
    y = text(c, y, "1.", [[("Place ( ) to find the related fact. Then solve.", False)]])
    for k, (a, b) in enumerate([("a.  4 × 20 = 4 × 2 × 10", "4 × 2"), ("b.  3 × 30 = 3 × 3 × 10", "3 × 3")]):
        x0 = MARGIN + k * 260
        rich_line(c, x0, y - 10, [(a, True)], 13)
        rich_line(c, x0 + 40, y - 36, [(f"= ({b}) × 10" if SIMP else "= " + a.split("= ")[1], False)], 13)
        frame(c, x0 + 40, y - 62, "= |___|  × 10 = |______", size=13)
    y -= 110
    y = text(c, y, "2.", [[("Jamila solves ", False), ("20 × 5", True), (" by thinking about ", False), ("10 tens", True), (". Explain.", False)]])
    frame(c, MARGIN + 24, y - 10, "2 × 5 = |___|, so 20 × 5 = |___|  tens = |______", size=13)
    footer(c, *L19, 121)


def p123(c):
    y = start(c, "Lesson 20 Application Problem", "TEKS 3.4K, 3.4A", "Find each person's books, then add.")
    two(c, y, "", [[("Shondra has ", False), ("3", True), (" boxes of ", False), ("4", True), (" books. Dan has ", False), ("3", True),
                    (" boxes of ", False), ("40", True), (" books.", False)], [("How many books in all?", False)]],
        "3 × 4 = |______      3 × 40 = |______", "______|  + |______|  = |______|  books")
    rdw(c)
    footer(c, *L20, 123)


def pp_item(c, x, y, a, n, filled=False, chart=True):
    rich_line(c, x, y, [(f"{n} × {a}", True)], 14)
    t, o = divmod(a, 10)
    if chart:
        disk_chart(c, x, y - 10, n, t, o, w=220, draw=SIMP or filled)
    pp(c, x + (240 if chart else 0), y - 26, a, n, filled)


def p125(c):
    y = start(c, "Lesson 20 Problem Set", "TEKS 3.4K", "Multiply the ones. Multiply the tens. Then add.")
    y = text(c, y, "1.", [[("Show each one on the chart. Record the partial products. (a) is done for you.", False)]])
    for k, (a, n, done) in enumerate([(31, 3, True), (23, 3, False), (23, 4, False)][:3 if not SIMP else 2]):
        pp_item(c, MARGIN + 10, y - 10 - k * 160, a, n, filled=done)
    footer(c, *L20, 125)


def p126(c):
    y = start(c, "Lesson 20 Problem Set", "TEKS 3.4K", "Multiply the ones. Multiply the tens. Then add.")
    probs = [("d.", 24, 4), ("e.", 25, 3), ("f.", 42, 3)][:3 if not SIMP else 2]
    for k, (lbl, a, n) in enumerate(probs):
        rich_line(c, MARGIN, y - 10 - k * 170, [(lbl, True)], 14)
        pp_item(c, MARGIN + 24, y - 10 - k * 170, a, n)
    footer(c, *L20, 126)


def p127(c):
    y = start(c, "Lesson 20 Problem Set", "TEKS 3.4K", "Break the big number into tens and ones.")
    if not SIMP:
        y = text(c, y, "2.", [[("Tom says ", False), ("3 × 6 = 18", True), (" and ", False), ("3 × 4 = 12", True),
                              (" help him find ", False), ("3 × 64", True), (". Explain.", False)]])
        dist(c, MARGIN + 24, y - 10, "3 × 60 = |___|     3 × 4 = |___|     3 × 64 = |___|  + |___|  = |______", size=12.5)
        y -= 60
    y = text(c, y, "3.", [[("Saturday: ", False), ("26", True), (" pinecones. Sunday: ", False), ("3 times as many", True),
                          (". How many in all?", False)]])
    bars(c, MARGIN + 90, y - 6, 320, [("Saturday", [("26", 1, False)]), ("Sunday", [("26", 1, False)] * 3)], 4,
         row_gap=34, h=26, brace=("?", 0, 4))
    frame(c, MARGIN + 24, y - 110, "Step 1:  3 × 26 = |______|  (Sunday)")
    frame(c, MARGIN + 24, y - 150, "Step 2:  26 + |______|  = |______|  pinecones")
    footer(c, *L20, 127)


def p129(c):
    y = start(c, "Lesson 20 Exit Ticket", "TEKS 3.4K", "Multiply the ones. Multiply the tens. Then add.")
    for k, (a, n) in enumerate([(41, 2), (35, 2)]):
        rich_line(c, MARGIN, y - 10 - k * 180, [(f"{k + 1}.", True)], 14)
        pp_item(c, MARGIN + 24, y - 10 - k * 180, a, n)
    footer(c, *L20, 129)


def p133(c):
    y = start(c, "Lesson 21 Application Problem", "TEKS 3.4K, 3.4A", "Multiply first, then subtract from the goal.")
    two(c, y, "", [[("Keshon's goal is ", False), ("200", True), (" bottles. He has ", False), ("3", True), (" boxes of ", False),
                    ("24", True), (" bottles.", False)], [("How many more does he need?", False)]],
        "3 × 24 = |______", "200 − |______|  = |______|  bottles")
    rdw(c)
    footer(c, *L21, 133)


def dots_item(c, x, y, lbl, a, n, done=False):
    t, o = divmod(a, 10)
    rich_line(c, x, y, [(f"{lbl}  {n} × {a}", True)], 14)
    disk_chart(c, x, y - 10, n, t, o, cols=("hundreds", "tens", "ones"), w=230, draw=SIMP or done)
    pp(c, x + 250, y - 26, a, n, done)


def p135(c):
    y = start(c, "Lesson 21 Problem Set", "TEKS 3.4K", "Draw dots for tens and ones. Multiply each. Add.")
    y = text(c, y, "1.", [[("Show with dots. Record the partial products. (a) is done for you.", False)]])
    probs = [("a.", 23, 2, True), ("b.", 23, 3, False), ("c.", 23, 4, False), ("d.", 23, 5, False)]
    if SIMP:
        probs = probs[:3]
    for k, (lbl, a, n, done) in enumerate(probs):
        dots_item(c, MARGIN + 10, y - 10 - k * (150 if SIMP else 128), lbl, a, n, done)
    footer(c, *L21, 135)


def p136(c):
    y = start(c, "Lesson 21 Problem Set", "TEKS 3.4K", "Draw dots for tens and ones. Multiply each. Add.")
    y = text(c, y, "2.", [[("Show with dots. Record the partial products.", False)]])
    probs = [("a.", 34, 3), ("b.", 53, 3), ("c.", 24, 6)]
    if SIMP:
        probs = [probs[0], probs[2]]
    for k, (lbl, a, n) in enumerate(probs):
        dots_item(c, MARGIN + 10, y - 10 - k * 190, lbl, a, n)
    footer(c, *L21, 136)


def p137(c):
    y = start(c, "Lesson 21 Exit Ticket", "TEKS 3.4K", "Draw disks for tens and ones. Multiply each. Add.")
    y = text(c, y, "1.", [[("Show with disks. Record the partial products.", False)]])
    for k, (lbl, a, n) in enumerate([("a.", 14, 5), ("b.", 51, 4)]):
        dots_item(c, MARGIN + 10, y - 10 - k * 190, lbl, a, n)
    footer(c, *L21, 137)


def p141(c):
    y = start(c, "Lesson 22 Problem Set", "TEKS 3.4K", "You can switch the order: 46 × 3 = 3 × 46.")
    y = text(c, y, "1.", [[("Rewrite each one with the order switched.", False)]])
    q1 = ["a.  46 × 3 = |___|  × |___", "b.  57 × 4 = |___|  × |___", "c.  63 × 5 = |___|  × |___", "d.  74 × 6 = |___|  × |___"]
    y = eqs(c, y - 6, q1[:4 if not SIMP else 2], cols=2, gap=34, size=13)
    y = text(c, y - 6, "2.", [[("Solve ", False), ("47 × 3", True), (".", False)]])
    frame(c, MARGIN + 24, y - 6, "a.  47 × 3 = 3 × |___", size=13)
    disk_chart(c, MARGIN + 24, y - 24, 3, 4, 7, cols=("hundreds", "tens", "ones"), w=260, draw=SIMP)
    pp(c, MARGIN + 320, y - 40, 47, 3)
    y -= 170
    y = text(c, y, "3.", [[("Use the area model.", False)]])
    area(c, MARGIN + 60, y - 16, 9, 50, 7, inside=SIMP)
    frame(c, MARGIN + 24, y - 100, "a.  |___|  × |___", size=13)
    dist(c, MARGIN + 24, y - 134, "b.  " + ("(9 × 50) + (9 × 7) = |___|  + |___|  = |______" if SIMP else DIST), size=12)
    footer(c, *L22, 141)


def p142(c):
    y = start(c, "Lesson 22 Problem Set", "TEKS 3.4K", "Break apart the tens and ones. Multiply each. Add.")
    y = text(c, y, "4.", [[("Solve ", False), ("5 × 64", True), (".", False)]])
    if SIMP:
        area(c, MARGIN + 60, y - 16, 5, 60, 4, inside=True)
    else:
        rich_line(c, MARGIN + 24, y - 6, [("a.  Draw an area model.", False)], 13)
        c.setStrokeColor(HexColor("#BBBBBB"))
        c.rect(MARGIN + 60, y - 90, 300, 70)
        c.setStrokeColor(black)
    dist(c, MARGIN + 24, y - 120, "b.  " + ("(5 × 60) + (5 × 4) = |___|  + |___|  = |______" if SIMP else DIST), size=12)
    y -= 170
    if not SIMP:
        y = text(c, y, "5.", [[("Use break apart and distribute to find ", False), ("53 × 4", True), (".", False)]])
        dist(c, MARGIN + 24, y - 14, DIST, size=12)
    footer(c, *L22, 142)


def p143(c):
    y = start(c, "Lesson 22 Exit Ticket", "TEKS 3.4K", "Switch the order if it helps. Break apart tens and ones.")
    y = text(c, y, "1.", [[("Solve ", False), ("62 × 3", True), (".", False)]])
    frame(c, MARGIN + 24, y - 6, "a.  62 × 3 = 3 × |___", size=13)
    disk_chart(c, MARGIN + 24, y - 24, 3, 6, 2, cols=("hundreds", "tens", "ones"), w=260, draw=SIMP)
    pp(c, MARGIN + 320, y - 40, 62, 3)
    y -= 180
    y = text(c, y, "2.", [[("Solve ", False), ("7 × 84", True), (".", False)]])
    area(c, MARGIN + 60, y - 16, 7, 80, 4, inside=SIMP)
    dist(c, MARGIN + 24, y - 100, "b.  " + ("(7 × 80) + (7 × 4) = |___|  + |___|  = |______" if SIMP else DIST), size=12)
    footer(c, *L22, 143)


def algo(c, x, y, a, n, label=None):
    if label:
        rich_line(c, x - 22, y, [(label, True)], 13)
    c.setStrokeColor(HexColor("#5577AA"))
    c.setDash(2, 2)
    c.rect(x + 18, y + 14, 16, 14)
    c.setDash()
    c.setStrokeColor(black)
    c.setFont("Sans", 18)
    c.drawRightString(x + 60, y, str(a))
    c.drawRightString(x + 60, y - 24, f"× {n}")
    c.setLineWidth(1.5)
    c.line(x, y - 30, x + 64, y - 30)
    c.setLineWidth(1)
    for k in range(3):
        c.rect(x + 2 + k * 20, y - 58, 18, 24)


def p147(c):
    y = start(c, "Lesson 23 Application Problem", "TEKS 3.4K", "Same amount in each: multiply.")
    wp(c, y, "", [[("Each of ", False), ("3", True), (" test tubes has ", False), ("42 mL", True), (". How much in all?", False)]],
       strip(["42"] * 3, None), ["___| × |___| = |______"], ["3 × 42 = |______|  mL"])
    if SIMP:
        algo(c, W - MARGIN - 120, y - 40, 42, 3)
    rdw(c)
    footer(c, *L23, 147)


def p149(c):
    y = start(c, "Lesson 23 Problem Set", "TEKS 3.4K", "Multiply the ones first. Carry the tens to the small box.")
    y = text(c, y, "1.", [[("Solve using each method.", False)]])
    for k, (lbl, a, n) in enumerate([("a.", 34, 4), ("b.", 54, 3)][:2 if not SIMP else 1]):
        x0 = MARGIN + 10 + k * 260
        rich_line(c, x0, y - 6, [(lbl, True), ("  Partial products        Algorithm", False)], 11)
        pp(c, x0, y - 30, a, n)
        algo(c, x0 + 180, y - 40, a, n)
    y -= 160
    y = text(c, y, "2.", [[("Solve. Use the standard algorithm.", False)]])
    probs = [("a.", 62, 4), ("b.", 35, 6), ("c.", 64, 6), ("d.", 85, 4), ("e.", 36, 5), ("f.", 92, 6)]
    if SIMP:
        probs = [probs[0], probs[1], probs[3]]
    for k, (lbl, a, n) in enumerate(probs):
        algo(c, MARGIN + 50 + (k % 3) * 170, y - 40 - (k // 3) * 110, a, n, lbl)
    footer(c, *L23, 149)


def p150(c):
    y = start(c, "Lesson 23 Problem Set", "TEKS 3.4K", "Multiply the ones first. Carry the tens to the small box.")
    if not SIMP:
        frame(c, MARGIN, y, "3.  The product of 7 and 86 is |______", size=13)
        frame(c, MARGIN + 270, y - 20, "4.  9 times as many as 47 is |______", size=13)
        algo(c, MARGIN + 60, y - 50, 86, 7)
        algo(c, MARGIN + 330, y - 50, 47, 9)
        y -= 130
    y = wp(c, y, "5.", [[("Eva needs ", False), ("5", True), (" pieces of wood, each ", False), ("14 cm", True), (". How many cm?", False)]],
           strip(["14"] * 5, None) if SIMP else None, ["___| × |___| = |______|  cm"], ["5 × 14 = |______|  cm"])
    algo(c, W - MARGIN - 110, y + 60, 14, 5)
    wp(c, y - 20, "6.", [[("One game costs ", False), ("$38", True), (". How much will ", False), ("4", True), (" games cost?", False)]],
       strip(["$38"] * 4, None) if SIMP else None, ["___| × |___| = |______|  dollars"], ["4 × 38 = |______|  dollars"])
    algo(c, W - MARGIN - 110, y - 50, 38, 4)
    footer(c, *L23, 150)


def p151(c):
    y = start(c, "Lesson 23 Exit Ticket", "TEKS 3.4K", "Multiply the ones first. Carry the tens to the small box.")
    y = text(c, y, "1.", [[("Solve using the standard algorithm.", False)]])
    probs = [("a.", 23, 9), ("b.", 74, 7)][:2 if not SIMP else 1]
    for k, (lbl, a, n) in enumerate(probs):
        algo(c, MARGIN + 60 + k * 220, y - 40, a, n, lbl)
    y -= 130
    wp(c, y, "2.", [[("Gerrie is ", False), ("24", True), (" years old. Her grandmother is ", False), ("3 times as old", True), (".", False)],
                    [("How old is her grandmother?", False)]],
       lambda c, y: bars(c, MARGIN + 100, y, 300, [("Gerrie", [("24", 1, False)]), ("Grandma", [("24", 1, False)] * 3)], 3,
                         row_gap=34, h=26, brace=("?", 0, 3)),
       ["___| × |___| = |______"], ["3 × 24 = |______|  years"])
    footer(c, *L23, 151)


PAGES_13_23 = [p81, p83, p84, p85, p87, p91, p92, p93, p95, p96, p97, p99, p101, p102, p103, p104, p105, p107, p108,
               p109, p111, p113, p114, p115, p117, p119, p120, p121, p123, p125, p126, p127, p129, p133, p135, p136,
               p137, p141, p142, p143, p147, p149, p150, p151]


def build():
    global SIMP
    for simp, name in ((False, "Modified"), (True, "Simplified")):
        SIMP = simp
        M.SIMP = simp
        main(f"G3_M3_L8-12_{name}.pdf", PAGES_8_12, f"Grade 3 Module 3 Lessons 8-12 – {name}")
        main(f"G3_M3_L13-23_{name}.pdf", PAGES_13_23, f"Grade 3 Module 3 Lessons 13-23 – {name}")


if __name__ == "__main__":
    build()
