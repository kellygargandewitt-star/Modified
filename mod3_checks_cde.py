"""Grade 3 Module 3 Topic C, D, E TEKS Progress Checks: COMPUTER HELPER + SIMPLIFIED (test_builder.py).

Run: python3 mod3_checks_cde.py
  -> G3_M3_TopicC_Check_{Helper,Simplified}.pdf, ..._TopicD_..., ..._TopicE_...
"""
from test_builder import *  # noqa: F401,F403
from test_builder import T


def box_sym(n="☐"):
    return n


# ================================================================ TOPIC C

def skip_list(c, y, nums, circled, counts=()):
    bw, x0 = 44, MARGIN + 10
    for k, n in enumerate(nums):
        x = x0 + k * bw + bw / 2
        c.setFont("Sans-Bold", 17)
        c.drawCentredString(x, y, str(n))
        if n == circled:
            c.circle(x, y + 6, 19)
        if k < len(counts):
            c.setFont("Sans", 11)
            c.drawCentredString(x, y - 30, counts[k])
    return y - 50


def c1(c):
    y = start(c)
    y = qtext(c, y, 1, [[("Julie counts by ", False), ("6s", True), (". She circles ", False), ("60", True), (".", False)]],
              [[("Julie skip-counted. She circled her answer.", False)],
               [("Which number sentence finds the answer she circled?", False)]])
    counts = ["1", "2", "3", "4", "5", "___", "___", "___", "___", "___"] if T.simp else ["1", "2", "3"]
    y = skip_list(c, y - 20, [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66], 60, counts)
    y = do_this(c, y - 30, [("60 = ", False), ("___", True), (" sixes.   ", False), ("___", True), (" × 6 = 60", False)])
    pick(c, y, "Which one finds 60?",
         [("A", "6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6"), ("B", "6 × 10")],
         [(None, "10 × 10 × 10 × 10 × 10 × 10 ="), (None, "6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 ="),
          (None, "6 × 10 ="), (None, "60 ÷ 3 =")], size2=19)
    foot(c, 1)


def c2(c):
    y = start(c)
    y = qtext(c, y, 2, [[("☐ ÷ 7 = 9", True)]], [[("What number goes in the box?", False)], [("☐ ÷ 7 = 9", True)]])
    y = strips(c, MARGIN, y - 10, [("", ["9"] * 7, "none")], 60, total="☐", label_w=40)
    labels = ["0", "9", "18", "27", "36", "45", "54", "___"] if T.simp else ["0", "9", "18", "", "", "", "", ""]
    y = jump_line(c, MARGIN + 40, y - 50, labels, 60, "+ 9")
    y = do_this(c, y - 10, [("☐ ÷ 7 = 9  means  ", False), ("☐ = 7 × 9", True)])
    pick(c, y, "What number goes in the box?", [("A", "63"), ("B", "56")],
         [(None, "63"), (None, "56"), (None, "16"), (None, "2")])
    foot(c, 2)


def pizza(c, x, y, r=26, label=None):
    c.setFillColor(HexColor("#F6D9A6"))
    c.circle(x, y, r, stroke=1, fill=1)
    c.setFillColor(black)
    for dx, dy in ((1, 0), (0, 1), (0.707, 0.707), (0.707, -0.707)):
        c.line(x - r * dx, y - r * dy, x + r * dx, y + r * dy)
    if label:
        c.setFont("Sans-Bold", 14)
        c.drawCentredString(x, y - r - 18, label)


def c3(c):
    y = start(c)
    y = qtext(c, y, 3, [[("6", True), (" pizzas.  ", False), ("8", True), (" slices each.", False)]],
              [[("Jacob buys ", False), ("6 pizzas", True), (". Each pizza has ", False), ("8 slices", True), (".", False)],
               [("Which number sentence finds the total slices?", False)]])
    for k in range(6):
        pizza(c, MARGIN + 60 + k * 82, y - 40, label="8" if T.simp else None)
    y = do_this(c, y - 120, [("6", True), (" groups of ", False), ("8", True), (" slices", False)])
    pick(c, y, "Which one finds all the slices?", [("A", "6 + 8 = 14"), ("B", "6 × 8 = 48")],
         [(None, "6 + 8 = 14"), (None, "6 × 8 = 48"), (None, "8 + 8 + 8 + 8 + 8 = 40"), (None, "6 + 6 + 6 + 6 + 6 + 6 = 36")])
    foot(c, 3)


# ================================================================ TOPIC D

def d1(c):
    y = start(c)
    y = qtext(c, y, 1, [[("28 + (14 ÷ 7)", True)]], [[("What is the value of ", False), ("28 + (14 ÷ 7)", True), ("?", False)]])
    rich_line(c, MARGIN + 20, y - 4, [("14 in groups of 7:", False)], 14)
    dot_groups(c, MARGIN + 200, y - 4, 2, 7, r=6, gap=15)
    y -= 80
    y = do_this(c, y, [("Do the ", False), ("( )", True), (" first.", False)])
    lines(c, MARGIN + 30, y, ["Step 1:   14 ÷ 7 = 2" if T.simp else "Step 1:   14 ÷ 7 = ___",
                              "Step 2:   28 + ___ = ___"])
    pick(c, y - 100, "What is the value?", [("A", "42"), ("B", "30")], [(None, "42"), (None, "30"), (None, "6"), (None, "2")])
    foot(c, 1)


def diamond(c, x, y, s=4):
    p = c.beginPath()
    p.moveTo(x, y + s)
    p.lineTo(x + s, y)
    p.lineTo(x, y - s)
    p.lineTo(x - s, y)
    p.close()
    c.drawPath(p, stroke=1, fill=0)


def d_array(c, x, y, rows, cols, g=11):
    for r in range(rows):
        for k in range(cols):
            diamond(c, x + k * g, y - r * g)


def d_groups(c, x, y):
    for g in range(6):
        gx = x + g * 46
        c.setStrokeColor(SOFT)
        c.rect(gx - 7, y - 29, 36, 36)
        c.setStrokeColor(black)
        d_array(c, gx + 1, y, 3, 3)


def d_skip(c, x, y, size=16):
    nums = [3, 21, 39, 57, 75, 93]
    for k, n in enumerate(nums):
        c.setFont("Sans-Bold", size)
        c.drawCentredString(x + k * 42, y - 5, str(n))
        if n == 57:
            c.circle(x + k * 42, y, 16)


def d2(c):
    y = start(c)
    y = qtext(c, y, 2, [[("3 × 18 = 54", True), (". Which one is ", False), ("NOT", True), (" right?", False)]],
              [[("Gianna shows ways to solve ", False), ("3 × 18 = ?", True)],
               [("Which one is ", False), ("NOT", True), (" a correct way?", False)]])
    y = do_this(c, y - 6, [("3 × 18 = ", False), ("54", True), (".  The right ways show 3 eighteens or 54.", False)])
    if T.simp:
        opts = [("A", lambda x, yy: d_array(c, x, yy + 12, 3, 18), "3 rows of 18"),
                ("B", lambda x, yy: d_skip(c, x + 10, yy), "")]
        h = 80
    else:
        opts = [("1st", lambda x, yy: d_array(c, x, yy + 12, 3, 18), "3 rows of 18"),
                ("2nd", lambda x, yy: d_skip(c, x + 10, yy), ""),
                ("3rd", lambda x, yy: rich_line(c, x, yy - 6, [("54 ÷ 3 = 18", True)], 17), ""),
                ("4th", lambda x, yy: d_groups(c, x, yy + 12), "6 groups of 9")]
        h = 64
    for k, (lab, draw, note) in enumerate(opts):
        top = y - k * (h + 10)
        c.setStrokeColor(SOFT)
        c.roundRect(MARGIN + 20, top - h, W - 2 * MARGIN - 40, h, 8)
        c.setStrokeColor(black)
        if len(lab) == 1:
            c.circle(MARGIN + 46, top - h / 2, 12)
        c.setFont("Sans-Bold", 13 if len(lab) == 1 else 11)
        c.drawCentredString(MARGIN + 46, top - h / 2 - 4.5, lab)
        draw(MARGIN + 80, top - h / 2)
        if note:
            c.setFont("Sans", 11)
            c.drawRightString(W - MARGIN - 30, top - h / 2 - 4, note)
    foot(c, 2)


def d3(c):
    y = start(c)
    y = qtext(c, y, 3, [[("48", True), (" bars.  ", False), ("6", True), (" in each bag.", False)]],
              [[("Megan has ", False), ("48", True), (" granola bars. She puts ", False), ("6", True), (" in each bag.", False)],
               [("How many bags can she fill?", False)]])
    if T.simp:
        dot_groups(c, MARGIN + 20, y - 10, 8, 6, r=5, gap=13, group_gap=22)
    else:
        for r in range(6):
            for k in range(8):
                c.setFillColor(INK)
                c.circle(MARGIN + 60 + k * 26, y - 10 - r * 18, 6, stroke=0, fill=1)
        c.setFillColor(black)
    y = do_this(c, y - (70 if T.simp else 130), [("Count the bags of 6:  ", False), ("48 ÷ 6 = ___", True)] if T.simp
                else [("Circle groups of 6. Count the groups.  ", False), ("48 ÷ 6 = ___", True)])
    pick(c, y, "How many bags?", [("A", "8 bags"), ("B", "42 bags")], [(None, "8"), (None, "42"), (None, "54"), (None, "288")])
    foot(c, 3)


def d4(c):
    y = start(c)
    y = qtext(c, y, 4, [[("18", True), (" in each row.  ", False), ("3", True), (" rows.", False)]],
              [[("Each quilt row has ", False), ("18", True), (" diamonds.", False)],
               [("How many diamonds in ", False), ("3", True), (" rows?", False)]])
    d_array(c, MARGIN + 60, y - 6, 1, 18, g=16)
    rich_line(c, MARGIN + 60 + 18 * 16, y - 11, [("= 18", True)], 14)
    y = strips(c, MARGIN, y - 40, [("3 rows", ["18", "18", "18"], "none")], 120, total="?", label_w=80)
    y = do_this(c, y, [("18 + 18 + 18", True), ("  or  ", False), ("3 × 18", True)])
    lines(c, MARGIN + 30, y, ["18 + 18 = 36      36 + 18 = ___" if T.simp else "18 + 18 = ___      ___ + 18 = ___"])
    pick(c, y - 50, "How many diamonds?", [("A", "36"), ("B", "54")], [(None, "18"), (None, "21"), (None, "36"), (None, "54")])
    foot(c, 4)


def d5(c):
    y = start(c)
    y = qtext(c, y, 5, [[("☐ ÷ 6 = 8", True)]], [[("What number goes in the box?", False)], [("☐ ÷ 6 = 8", True)]])
    y = strips(c, MARGIN, y - 10, [("", ["8"] * 6, "none")], 70, total="☐", label_w=40)
    labels = ["0", "8", "16", "24", "32", "40", "___"] if T.simp else ["0", "8", "16", "", "", "", ""]
    y = jump_line(c, MARGIN + 40, y - 50, labels, 70, "+ 8")
    y = do_this(c, y - 10, [("☐ ÷ 6 = 8  means  ", False), ("☐ = 6 × 8", True)])
    pick(c, y, "What number goes in the box?", [("A", "54"), ("B", "48")],
         [(None, "54"), (None, "14"), (None, "48"), (None, "2")])
    foot(c, 5)


# ================================================================ TOPIC E

def e1(c):
    y = start(c)
    y = qtext(c, y, 1, [[("9 × 6 = 54", True), (". Which ones are also ", False), ("54", True), ("?", False)]],
              [[("Which ones are equal to ", False), ("9 × 6", True), ("?", False)], [("Pick ", False), ("3", True), (".", False)]])
    x0, g = MARGIN + 60, 14
    for r in range(9):
        for k in range(6):
            c.setFillColor(INK if r < 5 else HexColor("#8A8A8A"))
            c.circle(x0 + k * g, y - 6 - r * g, 4.5, stroke=0, fill=1)
    c.setFillColor(black)
    c.setDash(3, 3)
    c.line(x0 - 12, y - 6 - 4.5 * g, x0 + 6 * g, y - 6 - 4.5 * g)
    c.setDash()
    rich_line(c, x0 + 100, y - 30, [("5 × 6 = 30", True)], 15)
    rich_line(c, x0 + 100, y - 100, [("4 × 6 = 24", True)], 15)
    rich_line(c, x0 + 260, y - 64, [("30 + 24 = 54", True)], 15)
    y = do_this(c, y - 168, [("Find ", False), ("54", True), (" each way.", False)])
    if T.simp:
        yes_no(c, y, "Is it 54?  Circle yes or no.", ["6 × 9", "(5 × 6) + (4 × 6)", "54", "63"])
    else:
        yes_no(c, y, "Is it 54?  On the computer, check the 3 yes answers.",
               ["6 × 9", "(8 × 6) + 9", "(5 × 6) + (4 × 6)", "54", "63"], size=16)
    foot(c, 1)


def e2(c):
    y = start(c)
    y = qtext(c, y, 2, [[("Each movie costs ", False), ("$6", True), (". She spends ", False), ("$54", True), (".", False)]],
              [[("Each movie costs ", False), ("$6", True), (". Emma spends ", False), ("$54", True), (".", False)],
               [("Which one shows how many movies?", False)]])
    parts = ["$6"] * 9 if T.simp else ["$6", "$6", "$6", "...", "", "", "", "", ""]
    y = strips(c, MARGIN, y - 10, [("", parts, "none")], 52, total="$54", label_w=40)
    y = do_this(c, y, [("Check:  6 × 8 = ___     6 × 9 = ___", True)])
    pick(c, y, "How many movies?", [("A", "6 × ? = 54      ? = 8"), ("B", "54 ÷ 6 = ?      ? = 9")],
         [(None, "6 × ? = 54      ? = 8"), (None, "54 + 6 = ?      ? = 60"), (None, "54 − 6 = ?      ? = 48"),
          (None, "54 ÷ 6 = ?      ? = 9")], size2=20)
    foot(c, 2)


def e3(c):
    y = start(c)
    y = qtext(c, y, 3, [[("72", True), (" books.  ", False), ("8", True), (" on each shelf.", False)]],
              [[("Martin puts ", False), ("72", True), (" books on shelves, ", False), ("8", True), (" on each shelf.", False)],
               [("How many shelves?", False)]])
    labels = [str(8 * k) for k in range(10)] if T.simp else ["0", "8", "16", "", "", "", "", "", "", "72"]
    y = jump_line(c, MARGIN + 30, y - 60, labels, 50, "+ 8", size=15)
    y = do_this(c, y - 10, [("Count the jumps of 8 to 72:  ", False), ("72 ÷ 8 = ___", True)])
    pick(c, y, "How many shelves?", [("A", "9 shelves"), ("B", "10 shelves")],
         [(None, "80"), (None, "64"), (None, "9"), (None, "10")])
    foot(c, 3)


def e4(c):
    y = start(c)
    y = qtext(c, y, 4, [[("Each delivery has ", False), ("9", True), (" bags.  ", False), ("8", True), (" deliveries?", False)]],
              [[("The table shows bags of chips for each number of deliveries.", False)],
               [("Al's Market gets ", False), ("8", True), (" deliveries. How many bags?", False)]], )
    rows = [(2, 18), (3, 27), (4, 36), (5, 45)] + ([(6, 54), (7, 63), (8, "___")] if T.simp else [(6, "___"), (7, "___"), (8, "___")])
    y = table(c, MARGIN + 30, y - 4, ["Deliveries", "Bags"], rows, cw=110, rh=26, arrows="+ 9")
    y = do_this(c, y - 40, [("1 delivery = ", False), ("9", True), (" bags.   ", False), ("8 × 9 = ___", True)])
    pick(c, y, "How many bags?", [("A", "63"), ("B", "72")], [(None, "144"), (None, "72"), (None, "63"), (None, "54")])
    foot(c, 4)


if __name__ == "__main__":
    build(("Topic C Progress Check", "Module 3, Topic C:", "G3_M3_TopicC_Check"), [c1, c2, c3])
    build(("Topic D Progress Check", "Module 3, Topic D:", "G3_M3_TopicD_Check"), [d1, d2, d3, d4, d5])
    build(("Topic E Progress Check", "Module 3, Topic E:", "G3_M3_TopicE_Check"), [e1, e2, e3, e4])
