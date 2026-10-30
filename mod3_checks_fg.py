"""Grade 3 Module 3 Topic F and G TEKS Progress Checks: COMPUTER HELPER + SIMPLIFIED (test_builder.py).

Run: python3 mod3_checks_fg.py  ->  G3_M3_TopicF_Check_{Helper,Simplified}.pdf, G3_M3_TopicG_Check_...
"""
from test_builder import *  # noqa: F401,F403
from test_builder import T


# ================================================================ TOPIC F

FISH = [("8 × 1 = ?", ("8", "1")), ("? ÷ 4 = 0", ("4", "0")), ("1 × ? = 2", ("2", "1")), ("? × 1 = 7", ("1", "7")),
        ("3 ÷ 3 = ?", ("3", "1")), ("? ÷ 9 = 1", ("9", "1")), ("5 ÷ 1 = ?", ("1", "5")), ("? × 1 = 6", ("6", "1"))]


def rules(c, y):
    c.setStrokeColor(SOFT)
    c.roundRect(MARGIN, y - 66, W - 2 * MARGIN, 76, 8)
    c.setStrokeColor(black)
    for k, (rule, ex) in enumerate((("× 1  →  same number", "4 × 1 = 4"), ("÷ 1  →  same number", "9 ÷ 1 = 9"),
                                    ("same ÷ same  →  1", "6 ÷ 6 = 1"), ("0 ÷ number  →  0", "0 ÷ 5 = 0"))):
        x, yy = MARGIN + 14 + (k % 2) * 262, y - 10 - (k // 2) * 34
        rich_line(c, x, yy, [(rule, True), ("    " + ex, False)], 13)
    return y - 104


def f1(c):
    y = start(c)
    y = qtext(c, y, 1, [[("Circle the answer for each one.", False)]],
              [[("Match each answer to its number sentence.", False)]])
    if not T.simp:
        rich_line(c, MARGIN, y, [("Answers:  ", True), ("6    8    9    7    0    5    2    1", False)], 16)
        y -= 30
    y = rules(c, y)
    for k, (eq, opts) in enumerate(FISH):
        yy = y - k * 46
        c.setStrokeColor(SOFT)
        c.roundRect(MARGIN + 20, yy - 16, W - 2 * MARGIN - 40, 40, 8)
        c.setStrokeColor(black)
        rich_line(c, MARGIN + 40, yy, [(eq, True)], 19)
        if T.simp:
            for j, o in enumerate(opts):
                c.setFont("Sans-Bold", 19)
                c.drawCentredString(W - MARGIN - 150 + j * 70, yy, o)
        else:
            fill(c, W - MARGIN - 200, yy, "? = ___", size=18, bw=60)
    foot(c, 1)


def num_card(c, x, y, n):
    s = str(n)
    c.setFont("Sans-Bold", 26)
    w = c.stringWidth(s, "Sans-Bold", 26)
    c.drawString(x, y, s)
    dw = c.stringWidth(s[-1], "Sans-Bold", 26)
    c.rect(x + w - dw - 3, y - 6, dw + 6, 30)


def f2(c):
    y = start(c)
    y = qtext(c, y, 2, [[("Which number is ", False), ("odd", True), ("?", False)]])
    y = even_odd(c, MARGIN + 30, y - 6)
    nums = [407, 130] if T.simp else [407, 130, 368, 594]
    for k, n in enumerate(nums):
        num_card(c, MARGIN + 40 + k * 125, y - 30, n)
    rich_line(c, MARGIN + 40, y - 60, [("The box shows the ones digit.", False)], 12)
    y = do_this(c, y - 100, [("Look at the ", False), ("ones", True), (" digit only.", False)])
    pick(c, y, "Which number is odd?", [("A", "407"), ("B", "130")],
         [(None, "407"), (None, "130"), (None, "368"), (None, "594")])
    foot(c, 2)


def f3(c):
    y = start(c)
    y = qtext(c, y, 3, [[("7", True), (" bracelets with ", False), ("6", True), (" beads.  ", False),
                         ("3", True), (" necklaces with ", False), ("9", True), (" beads.", False)],
                        [("How many beads in all?", False)]],
              [[("Sarah makes ", False), ("7", True), (" bracelets with ", False), ("6", True), (" beads each.", False)],
               [("Then ", False), ("3", True), (" necklaces with ", False), ("9", True), (" beads each.", False)],
               [("How many beads altogether?", False)]])
    x = MARGIN
    end = strip(c, x, y - 4, "Bracelets", ["6"] * 7, 40, h=32, size=15, label_w=90)
    rich_line(c, end + 10, y - 26, [("7 × 6 = 42" if T.simp else "7 × 6 = ___", True)], 15)
    end = strip(c, x, y - 50, "Necklaces", ["9"] * 3, 40, h=32, size=15, label_w=90)
    rich_line(c, end + 10, y - 72, [("3 × 9 = ___", True)], 15)
    y = do_this(c, y - 120, [("Find both. Then ", False), ("add", True), (":  42 + ___ = ___" if T.simp else ":  ___ + ___ = ___", True)])
    pick(c, y, "Which one finds all the beads?", [("A", "7 × 6 = 42"), ("B", "(7 × 6) + (3 × 9) = 69")],
         [(None, "7 + 6 + 3 + 9 = 25"), (None, "7 × 6 = 42"), (None, "3 × 9 = 27"), (None, "(7 × 6) + (3 × 9) = 69")], size2=20)
    foot(c, 3)


def f4(c):
    y = start(c)
    y = qtext(c, y, 4, [[("Who is correct?", False)]],
              [[("Hanna's brother and sister helped with homework.", False)], [("Who is correct?", False)]])
    for k in range(7):
        c.setStrokeColor(SOFT)
        c.circle(MARGIN + 60 + k * 40, y - 14, 15)
    c.setStrokeColor(black)
    rich_line(c, MARGIN + 350, y - 19, [("7 groups of 0 = ___", True)], 14)
    dot_groups(c, MARGIN + 54, y - 56, 1, 8, r=5)
    rich_line(c, MARGIN + 350, y - 66, [("1 group of 8 = ___", True)], 14)
    y = do_this(c, y - 120, [("Empty groups make ", False), ("0", True), (".  1 group of 8 is ", False), ("8", True), (".", False)])
    two = [("A", [("Brother:  ", True), ("7 × 0 = 7    1 × 8 = 1", False)]),
           ("B", [("Sister:  ", True), ("7 × 0 = 0    1 × 8 = 8", False)])]
    if T.simp:
        pick(c, y, "Who is correct?", two, [], size2=19)
    else:
        rich_line(c, MARGIN, y, [("Who is correct?", True)], 15)
        choice_y = y - 20
        for k, (lab, txt) in enumerate(two):
            top = choice_y - k * 50
            c.setStrokeColor(SOFT)
            c.roundRect(MARGIN + 20, top - 40, W - 2 * MARGIN - 40, 40, 8)
            c.setStrokeColor(black)
            rich_line(c, MARGIN + 40, top - 26, txt, 16)
        rich_line(c, MARGIN, choice_y - 120, [("On the computer: ", True), ("pick the correct person from the drop-down list.", False)], 13)
    foot(c, 4)


def f5(c):
    y = start(c)
    y = qtext(c, y, 5, [[("Is ", False), ("370", True), (" even or odd?", False)]],
              [[("Which is true about ", False), ("370", True), ("?", False)]])
    y = place_chart(c, MARGIN + 30, y - 4, ["Hundreds", "Tens", "Ones"], "370", shade=(2,))
    y = even_odd(c, MARGIN + 30, y - 20)
    y = do_this(c, y - 10, [("The ", False), ("ones", True), (" digit is ___.  Is it even or odd?", False)])
    pick(c, y, "Which is true?", [("A", "Odd, because the 0 in the ones place is odd."),
                                  ("B", "Even, because it can be divided by 2 evenly.")],
         [(None, "It is odd, because the 0 in the ones place is odd."),
          (None, "It is odd, because the digit in the hundreds place is odd."),
          (None, "It is even, because it can be divided by 2 evenly."),
          (None, "It is even, because the digit in the tens place is even.")], size2=16, size4=13)
    foot(c, 5)


# ================================================================ TOPIC G

def to_chart(c, x, y, tens_dots, ones_dots, w=200, h=80, per=3):
    """Tens/ones chart; *_dots = (rows, cols)."""
    c.setLineWidth(1.5)
    c.line(x, y - 18, x + w, y - 18)
    c.line(x + w / 2, y, x + w / 2, y - h)
    c.setLineWidth(1)
    c.setFont("Sans-Bold", 13)
    c.drawCentredString(x + w / 4, y - 13, "tens")
    c.drawCentredString(x + 3 * w / 4, y - 13, "ones")
    for (rows, cols), cx in ((tens_dots, x + w / 4), (ones_dots, x + 3 * w / 4)):
        for r in range(rows):
            for k in range(cols):
                c.setFillColor(INK)
                c.circle(cx - (cols - 1) * 6 + k * 12, y - 32 - r * 12, 4, stroke=0, fill=1)
        c.setFillColor(black)


def g1(c):
    y = start(c)
    y = qtext(c, y, 1, [[("2 × 3 ones = ___ ones", True)]],
              [[("Which chart shows ", False), ("2 × 3 ones = ___ ones", True), ("?", False)]])
    dot_groups(c, MARGIN + 60, y - 10, 2, 3, r=6, gap=15)
    rich_line(c, MARGIN + 200, y - 15, [("2 groups of 3 ones", True)], 15)
    y = do_this(c, y - 70, [("2 × 3 = ___.  The dots go in the ", False), ("ones", True), (" side.", False)])
    rich_line(c, MARGIN, y, [("Which chart shows it?", True)], 17 if T.simp else 15)
    if T.simp:
        opts = [("A", (0, 0), (2, 3)), ("B", (2, 3), (0, 0))]
    else:
        opts = [("1st", (0, 0), (2, 4)), ("2nd", (0, 0), (2, 3)), ("3rd", (2, 3), (0, 0)), ("4th", (0, 0), (3, 5))]
    for k, (lab, td, od) in enumerate(opts):
        x0, y0 = MARGIN + 20 + (k % 2) * 262, y - 30 - (k // 2) * 130
        c.setStrokeColor(SOFT)
        c.roundRect(x0, y0 - 110, 240, 120, 8)
        c.setStrokeColor(black)
        if len(lab) == 1:
            c.circle(x0 + 18, y0 - 8, 11)
        c.setFont("Sans-Bold", 13 if len(lab) == 1 else 11)
        c.drawCentredString(x0 + 18, y0 - 12.5, lab)
        to_chart(c, x0 + 30, y0 - 18, td, od)
    if not T.simp:
        rich_line(c, MARGIN, y - 300, [("On the computer, the charts are in this order: 1st, 2nd, 3rd, 4th.", False)], 12)
    foot(c, 1)


def g2(c):
    y = start(c)
    y = qtext(c, y, 2, [[("20", True), (" ones  × 10  =  ", False), ("20", True), (" tens", False)]],
              [[("Which ones match this place value chart?", False)], [("Pick ", False), ("2", True), (".", False)]])
    to_chart(c, MARGIN + 40, y, (0, 0), (4, 5), w=200, h=90)
    rich_line(c, MARGIN + 260, y - 50, [("× 10  →", True)], 16)
    to_chart(c, MARGIN + 340, y, (4, 5), (0, 0), w=180, h=90)
    y = do_this(c, y - 110, [("4 × 5 = ", False), ("20", True), (" ones.  Then ", False), ("× 10", True), (".", False)])
    if T.simp:
        yes_no(c, y, "Does it match?  Circle yes or no.", ["(4 × 5) × 10", "(4 × 5) × 100", "(20 ones) × 10"])
    else:
        yes_no(c, y, "Does it match?  On the computer, check the 2 yes answers.",
               ["(4 × 5) × 10", "(4 × 5) × 100", "(200 ones) × 10", "(20 ones) × 10", "(20 + 20) × 10"], size=16)
    foot(c, 2)


def g3(c):
    y = start(c)
    y = qtext(c, y, 3, [[("8", True), (" games.  ", False), ("$20", True), (" each.", False)]],
              [[("A team played ", False), ("8", True), (" tournaments. Each one cost ", False), ("$20", True), (".", False)],
               [("How much did the team pay in all?", False)]])
    y = strips(c, MARGIN, y - 6, [("", ["$20"] * 8, "none")], 56, total="?", label_w=40)
    y = do_this(c, y, [("$20 = 2 tens.   8 × 2 tens = ", False), ("16" if T.simp else "___", True), (" tens = $___", True)])
    pick(c, y, "How much in all?", [("A", "$160"), ("B", "$28")], [(None, "$160"), (None, "$28"), (None, "$16"), (None, "$100")])
    foot(c, 3)


def g4(c):
    y = start(c)
    y = qtext(c, y, 4, [[("1 set = ", False), ("16", True), (" plates + ", False), ("16", True), (" bowls + ", False), ("8", True),
                         (" mugs.  ", False), ("8", True), (" sets?", False)]],
              [[("Andres buys ", False), ("8", True), (" sets of dishes.", False)],
               [("Each set has ", False), ("16", True), (" plates, ", False), ("16", True), (" bowls, and ", False), ("8", True),
                (" mugs.", False)], [("How many dishes altogether?", False)]])
    y = strips(c, MARGIN, y - 6, [("1 set", ["16 plates", "16 bowls", "8 mugs"], "none")], 130, h=34, size=14,
               total="40" if T.simp else "?", label_w=60)
    y = do_this(c, y, [("1 set = 40 = 4 tens.   8 × 4 tens = ", False), ("___", True), (" tens", False)])
    pick(c, y, "How many dishes in all?", [("A", "40"), ("B", "320")], [(None, "48"), (None, "40"), (None, "256"), (None, "320")])
    foot(c, 4)


def g5(c):
    y = start(c)
    y = qtext(c, y, 5, [[("22 × 4", True)]], [[("Find the product: ", False), ("22 × 4", True)]])
    x0, top = MARGIN + 80, y - 30
    c.setFillColor(GREY)
    c.rect(x0, top - 80, 300, 80, stroke=1, fill=1)
    c.setFillColor(white)
    c.rect(x0 + 300, top - 80, 60, 80, stroke=1, fill=1)
    c.setFillColor(black)
    c.setFont("Sans-Bold", 18)
    c.drawCentredString(x0 + 150, top + 8, "20")
    c.drawCentredString(x0 + 330, top + 8, "2")
    c.drawRightString(x0 - 10, top - 46, "4")
    c.setFont("Sans-Bold", 16)
    c.drawCentredString(x0 + 150, top - 46, "20 × 4")
    c.drawCentredString(x0 + 330, top - 46, "2 × 4")
    y = do_this(c, top - 120, [("Break ", False), ("22", True), (" into ", False), ("20", True), (" and ", False), ("2", True), (".", False)])
    y = lines(c, MARGIN + 40, y, ["20 × 4 = 80" if T.simp else "20 × 4 = ___", "2 × 4 = ___",
                                 ("80" if T.simp else "___") + " + ___ = ___"], gap=44)
    c.setLineWidth(2)
    c.rect(MARGIN + 40, y - 30, 300, 50)
    c.setLineWidth(1)
    fill(c, MARGIN + 60, y - 12, "22 × 4 = ___", size=22, bw=80)
    if not T.simp:
        rich_line(c, MARGIN + 40, y - 60, [("On the computer: ", True), ("type your answer in the box.", False)], 13)
    foot(c, 5)


def g6(c):
    y = start(c)
    y = qtext(c, y, 6, [[("$18", True), (" for each dog.  ", False), ("6", True), (" dogs?", False)]],
              [[("Alex earns ", False), ("$18", True), (" for each dog he walks.", False)],
               [("He walks ", False), ("6", True), (" dogs. How much does he earn?", False)]])
    vals = ["18", "36", "54", "72", "90" if T.simp else "?", "?"]
    x0, cw, rh = MARGIN + 110, 64, 34
    for r, (head, row) in enumerate((("Dogs", [str(k) for k in range(1, 7)]), ("$ Earned", vals))):
        yy = y - 10 - r * rh
        c.setFillColor(GREY)
        c.rect(x0 - 100, yy - rh, 100, rh, stroke=1, fill=1)
        c.setFillColor(black)
        c.setFont("Sans-Bold", 13)
        c.drawCentredString(x0 - 50, yy - rh + 12, head)
        for k, v in enumerate(row):
            c.rect(x0 + k * cw, yy - rh, cw, rh)
            c.setFont("Sans-Bold", 17)
            c.drawCentredString(x0 + k * cw + cw / 2, yy - rh + 11, v)
    for k in range(5):
        xm = x0 + k * cw + cw
        c.arc(xm - 24, y - 10 - 2 * rh - 30, xm + 24, y - 10 - 2 * rh + 6, 180, 180)
        c.setFont("Sans-Bold", 10)
        c.drawCentredString(xm, y - 10 - 2 * rh - 40, "+18")
    y = do_this(c, y - 150, [("Add ", False), ("18", True), (" each time:  " + ("90 + 18 = ___" if T.simp else "72 + 18 = ___,  ___ + 18 = ___"), True)])
    pick(c, y, "How much does Alex earn?", [("A", "$90"), ("B", "$108")],
         [(None, "$24"), (None, "$72"), (None, "$90"), (None, "$108")])
    foot(c, 6)


if __name__ == "__main__":
    build(("Topic F Progress Check", "Module 3, Topic F:", "G3_M3_TopicF_Check"), [f1, f2, f3, f4, f5])
    build(("Topic G Progress Check", "Module 3, Topic G:", "G3_M3_TopicG_Check"), [g1, g2, g3, g4, g5, g6])
