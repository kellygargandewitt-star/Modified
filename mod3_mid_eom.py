"""Grade 3 Module 3 Mid-Module and End-of-Module Assessments: HELPER + SIMPLIFIED (test_builder.py).

Paper tests, so the HELPER keeps the book's answer letters (A-D, F-J); SIMPLIFIED keeps the
book letters of the 2 choices it shows. Written-answer questions get partly filled frames.

Run: python3 mod3_mid_eom.py
  -> G3_M3_MidModule_{Helper,Simplified}.pdf, G3_M3_EndOfModule_{Helper,Simplified}.pdf
"""
from test_builder import *  # noqa: F401,F403
from test_builder import T


def answer_box(c, x, y, text, w=300, size=22):
    c.setLineWidth(2)
    c.rect(x, y - 30, w, 50)
    c.setLineWidth(1)
    fill(c, x + 16, y - 12, text, size=size, bw=80)
    return y - 50


def work_box(c, x, y, w, h, label):
    c.setStrokeColor(SOFT)
    c.setDash(4, 3)
    c.rect(x, y - h, w, h)
    c.setDash()
    c.setStrokeColor(black)
    c.setFont("Sans", 11)
    c.drawString(x + 6, y - 14, label)


# ================================================================ MID-MODULE

def bee(c, x, y, label=None):
    c.setFillColor(HexColor("#FBE7A1"))
    c.ellipse(x - 30, y - 16, x + 30, y + 16, stroke=1, fill=1)
    c.setFillColor(black)
    c.setLineWidth(2.5)
    for k in range(6):
        sx = x - 20 + k * 8
        c.line(sx, y - 12, sx, y + 12)
    c.setLineWidth(1)
    if label:
        c.setFont("Sans-Bold", 14)
        c.drawCentredString(x, y - 34, label)


def m1(c):
    y = start(c)
    y = qtext(c, y, 1, [[("6", True), (" dolls.  ", False), ("6", True), (" stripes on each.", False)]],
              [[("Fabrizio and ", False), ("5", True), (" other children each have a bee doll.", False)],
               [("Each doll has ", False), ("6", True), (" stripes. How many stripes in all?", False)],
               [("Write an equation with a box. Solve.", False)]])
    for k in range(6):
        bee(c, MARGIN + 60 + k * 82, y - 24, label="6" if T.simp else None)
    y -= 80
    if T.simp:
        y = jump_line(c, MARGIN + 40, y - 40, ["0", "6", "12", "18", "24", "30", "___"], 70, "+ 6")
        y = do_this(c, y - 10, [("6", True), (" groups of ", False), ("6", True), (".", False)])
        y = lines(c, MARGIN + 40, y, ["6 × 6 = ☐", "☐ = ___"], size=22, gap=48)
    else:
        y = do_this(c, y - 10, [("1 + 5 = ", False), ("6", True), (" dolls.  Each doll has ", False), ("6", True), (" stripes.", False)])
        y = lines(c, MARGIN + 40, y, ["Equation:   ___ × ___ = ☐", "☐ = ___ stripes"], size=20, gap=48)
        work_box(c, MARGIN, y, W - 2 * MARGIN, 120, "Work space")
    foot(c, 1)


def m2(c):
    y = start(c)
    y = qtext(c, y, 2, [[("Write ", False), ("2", True), (" equations for the array.", False)]],
              [[("Use the array to write ", False), ("two", True), (" different multiplication equations.", False)]])
    x0, s = MARGIN + 80, 38
    for r in range(4):
        for k in range(8):
            c.rect(x0 + k * s, y - 20 - (r + 1) * s, s, s)
    if T.simp:
        c.setFont("Sans-Bold", 16)
        c.drawCentredString(x0 + 4 * s, y - 10, "8 in each row")
        c.drawRightString(x0 - 10, y - 20 - 2 * s - 6, "4 rows")
    y = do_this(c, y - 20 - 4 * s - 30, [("Count the rows. Count the squares in a row.", False)] if not T.simp
                else [("Count by 8s:  8, 16, 24, ", False), ("___", True)])
    if T.simp:
        lines(c, MARGIN + 40, y, ["___ = 4 × 8", "___ = 8 × 4"], size=24, gap=56)
    else:
        lines(c, MARGIN + 40, y, ["Rows: ___     In each row: ___", "___ = ___ × ___", "___ = ___ × ___"], size=20, gap=52)
    foot(c, 2)


def m3(c):
    y = start(c)
    y = qtext(c, y, 3, [[("Show ", False), ("5 × 6", True), (". What is the product?", False)]],
              [[("Show ", False), ("5 × 6", True), (" with a number line, an array, or equal groups.", False)],
               [("What is the product?", False)]])
    if T.simp:
        dot_groups(c, MARGIN + 30, y - 10, 5, 6, r=6, gap=15, group_gap=30)
        rich_line(c, MARGIN + 30, y - 66, [("5", True), (" groups of ", False), ("6", True)], 15)
        y = jump_line(c, MARGIN + 40, y - 140, ["0", "6", "12", "18", "24", "___"], 85, "+ 6")
    else:
        for k in range(5):
            c.setStrokeColor(SOFT)
            c.circle(MARGIN + 60 + k * 100, y - 40, 38)
        c.setStrokeColor(black)
        rich_line(c, MARGIN + 30, y - 100, [("Draw ", False), ("6", True), (" dots in each circle.", False)], 14)
        y = jump_line(c, MARGIN + 40, y - 170, ["0", "", "", "", "", ""], 85, "+ ?")
    y = do_this(c, y - 10, [("5", True), (" jumps of ", False), ("6", True), (" or ", False), ("5", True), (" groups of ", False),
                            ("6", True), (".", False)])
    answer_box(c, MARGIN + 40, y - 10, "5 × 6 = ___")
    foot(c, 3)


def m4(c):
    y = start(c)
    y = qtext(c, y, 4, [[("Find the pattern. Finish the table.", False)]],
              [[("Zara uses tickets to play games.", False)],
               [("Explain the pattern. Then complete the table.", False)]])
    y = table(c, MARGIN + 30, y - 4, ["Tickets", "Games"], [(14, 2), (21, 3), (28, 4), (35, 5), ("___", 6)], cw=110, rh=32,
              arrows="+ 7")
    y = do_this(c, y - 36, [("1 game = ", False), ("7", True), (" tickets.  ", False), ("6 × 7 = ___", True)] if T.simp
                else [("How many more tickets each time?  ", False), ("___", True)])
    lines(c, MARGIN + 30, y, (["Each game uses 7 tickets.", "Tickets = 7 × games.", "6 games:  6 × 7 = ___ tickets"] if T.simp
                              else ["Each game uses ___ tickets.", "Tickets = ___ × games.", "6 games:  6 × ___ = ___ tickets"]),
          size=18, gap=42)
    foot(c, 4)


def m5(c):
    y = start(c)
    y = qtext(c, y, 5, [[("Ivan: ", False), ("2", True), (" apples.  Jayla: ", False), ("2 × 4", True), (".", False)]],
              [[("Ivan picks ", False), ("2", True), (" apples. ", False), ("2 × 4", True), (" shows Jayla's apples.", False)],
               [("Which is true?", False)]])
    y = strips(c, MARGIN, y - 6, [("Ivan", ["2"], "none"), ("Jayla", ["2", "2", "2", "2"], "none")], 80)
    y = do_this(c, y, [("Jayla has ", False), ("4", True), (" boxes of Ivan's ", False), ("2", True), (".", False)])
    pick(c, y, "Which is true?", [("A", "Jayla picks 4 times as many apples as Ivan."), ("C", "Jayla picks 4 more apples than Ivan.")],
         [("A", "Jayla picks 4 times as many apples as Ivan."), ("B", "Ivan picks 4 times as many apples as Jayla."),
          ("C", "Jayla picks 4 more apples than Ivan."), ("D", "Ivan picks 4 more apples than Jayla.")], size2=16, size4=14)
    foot(c, 5)


def m6(c):
    y = start(c)
    y = qtext(c, y, 6, [[("8", True), (" jumping jacks each lap.  ", False), ("7", True), (" laps.", False)]],
              [[("Mr. Perez does ", False), ("8", True), (" jumping jacks after each lap.", False)],
               [("How many after ", False), ("7", True), (" laps? Draw a model. Solve.", False)]])
    parts = ["8"] * 7 if T.simp else [""] * 7
    y = strips(c, MARGIN, y - 6, [("Laps", parts, "none")], 60, total="?", label_w=60)
    labels = ["0", "8", "16", "24", "32", "40", "48", "___"] if T.simp else ["0", "8", "", "", "", "", "", ""]
    y = jump_line(c, MARGIN + 40, y - 40, labels, 62, "+ 8")
    y = do_this(c, y - 10, [("7", True), (" groups of ", False), ("8", True), (".", False)] if T.simp
                else [("Write ", False), ("8", True), (" in each lap box.", False)])
    answer_box(c, MARGIN + 40, y - 10, "7 × 8 = ___" if T.simp else "___ × ___ = ___", w=360)
    foot(c, 6)


# ================================================================ END-OF-MODULE

FACTS = ["2 × 1 = ___", "4 ÷ 2 = ___", "___ = 10 ÷ 5", "3 × 3 = ___", "2 × ___ = 4",
         "___ × 6 = 12", "100 ÷ 10 = ___", "8 × ___ = 24", "___ = 9 × 3", "___ = 30 ÷ 10",
         "5 × 3 = ___", "8 ÷ 2 = ___", "___ × 3 = 12", "___ = 16 ÷ 4", "6 × 4 = ___",
         "9 × 4 = ___", "10 × ___ = 100", "40 ÷ 8 = ___", "___ = 3 × 5", "___ × 4 = 20",
         "7 × ___ = 35", "___ = 54 ÷ 9", "___ × 6 = 36", "8 × 6 = ___", "24 ÷ 4 = ___",
         "9 × 6 = ___", "___ = 49 ÷ 7", "8 × ___ = 56", "___ = 6 × 7", "21 ÷ 3 = ___",
         "7 × 7 = ___", "___ × 9 = 63", "___ = 64 ÷ 8", "6 × ___ = 48", "___ = 4 × 8",
         "24 ÷ 3 = ___", "81 ÷ 9 = ___", "63 ÷ 7 = ___", "8 × 9 = ___", "9 × ___ = 81"]


def facts_page(part):
    def draw(c):
        y = start(c)
        if part == 0:
            y = qtext(c, y, 1, [[("Solve. Use the chart on the next page if you need it.", False)]],
                      [[("Solve as many as you can.", False)], [("Use the chart on the next page if you need it.", False)]])
        if T.simp:
            items, cols, size, gap = FACTS[part * 20:(part + 1) * 20], 2, 20, 54
        else:
            items, cols, size, gap = FACTS, 3, 15, 37
        cw = (W - 2 * MARGIN) / cols
        for k, f in enumerate(items):
            fill(c, MARGIN + 10 + (k % cols) * cw, y - 20 - (k // cols) * gap, f, size=size, bw=46)
        foot(c, "1" if part == 0 else "1 (cont.)")
    return draw


def chart_page(c):
    y = start(c)
    rich_line(c, MARGIN, y, [("Multiplication Chart", True)], 18)
    cs, x0, top = 44, MARGIN + 20, y - 24
    for r in range(11):
        for k in range(11):
            head = r == 0 or k == 0
            c.setFillColor(GREY if head else white)
            c.rect(x0 + k * cs, top - (r + 1) * cs, cs, cs, stroke=1, fill=1)
            c.setFillColor(black)
            val = "×" if r == k == 0 else str(k if r == 0 else r if k == 0 else r * k)
            c.setFont("Sans-Bold" if head else "Sans", 15)
            c.drawCentredString(x0 + k * cs + cs / 2, top - (r + 1) * cs + 15, val)
    foot(c, "Chart")


def person(c, x, y, label):
    c.setFillColor(HexColor("#BFD8F2"))
    c.circle(x, y, 11, stroke=1, fill=1)
    c.roundRect(x - 15, y - 48, 30, 34, 8, stroke=1, fill=1)
    c.setFillColor(black)
    c.setFont("Sans-Bold", 14)
    c.drawCentredString(x, y - 70, label)


def e2(c):
    y = start(c)
    y = qtext(c, y, 2, [[("Korina + ", False), ("3", True), (" friends.  Each pays ", False), ("$6", True), (".", False)]],
              [[("Aunt Korina and ", False), ("3", True), (" friends share a cab.", False)],
               [("Each pays ", False), ("$6", True), (". How much did the cab cost?", False)],
               [("Write an equation with ? or a box. Solve.", False)]])
    for k, name in enumerate(["Korina", "friend", "friend", "friend"]):
        person(c, MARGIN + 80 + k * 110, y - 20, "$6" if T.simp else "")
        c.setFont("Sans", 10)
        c.drawCentredString(MARGIN + 80 + k * 110, y + 0, name)
    y -= 130
    y = do_this(c, y, [("Korina + 3 friends = ", False), ("4" if T.simp else "___", True), (" people.", False)])
    lines(c, MARGIN + 40, y, (["4 × 6 = ☐", "☐ = $___"] if T.simp else ["___ × ___ = ☐", "☐ = $___"]), size=22, gap=50)
    foot(c, 2)


def e3(c):
    y = start(c)
    y = qtext(c, y, 3, [[("Sale price = original ", False), ("÷ 3", True), (".  ", False), ("$24", True), (" on sale?", False)]],
              [[("Compare the original prices to the sale prices.", False)],
               [("What is the sale price for ", False), ("$24", True), ("?", False)],
               [("Explain with words and equations.", False)]])
    rows = [("$12", "$4"), ("$21", "$7"), ("$27", "$9"), ("$3", "$1"), ("$24", "?")]
    tx, cw, rh = MARGIN + 30, 110, 32
    y2 = table(c, tx, y - 4, ["Original", "Sale"], rows, cw=cw, rh=rh)
    for i in range(5):
        yy = y - 4 - (i + 2) * rh + 10
        rich_line(c, tx + 2 * cw + 12, yy, [("÷ 3" if (T.simp or i == 0) else "÷ ___", True)], 14)
        if T.simp and i < 4:
            rich_line(c, tx + 2 * cw + 70, yy, [(f"{rows[i][0][1:]} ÷ 3 = {rows[i][1][1:]}", False)], 13)
    y = do_this(c, y2 - 30, [("Check one row:  12 ÷ ", False), ("___", True), (" = 4", False)])
    lines(c, MARGIN + 30, y, (["24 ÷ 3 = ___", "The sale price is $___."] if T.simp else
                              ["Each sale price is the original price ÷ ___.", "24 ÷ ___ = ___", "The sale price is $___."]),
          size=18, gap=44)
    foot(c, 3)


def e4(c):
    y = start(c)
    y = qtext(c, y, 4, [[("Shirt ", False), ("$28", True), (".  Pants cost ", False), ("twice as much", True), (".", False)],
                        [("How much in all?", False)]],
              [[("Riley buys a shirt for ", False), ("$28", True), (".", False)],
               [("The pants cost ", False), ("twice as much", True), (". How much in all?", False)]])
    y = strips(c, MARGIN, y - 6, [("Shirt", ["28"], "none"), ("Pants", ["28", "28"], "none")], 110, total="?")
    y = do_this(c, y, [("Twice", True), (" = 2 times.  Find the pants. Then add.", False)])
    lines(c, MARGIN + 30, y, (["Step 1  Pants:  28 + 28 = 56", "Step 2  All:  28 + 56 = ___", "Riley spent $___."] if T.simp else
                              ["Step 1  Pants:  ___ + ___ = ___", "Step 2  All:  ___ + ___ = ___", "Riley spent $___."]),
          size=18, gap=46)
    foot(c, 4)


def e5(c):
    y = start(c)
    y = qtext(c, y, 5, [[("Ling: ", False), ("15", True), (" pounds.  Bailey: ", False), ("3 × 15", True), (".", False)]],
              [[("Mrs. Ling's class collects ", False), ("15", True), (" pounds of cans.", False)],
               [("3 × 15", True), (" shows Mrs. Bailey's class. Which is true?", False)]])
    y = strips(c, MARGIN, y - 6, [("Ling", ["15"], "none"), ("Bailey", ["15", "15", "15"], "none")], 90)
    y = do_this(c, y, [("Bailey has ", False), ("3", True), (" boxes of Ling's ", False), ("15", True), (".", False)])
    pick(c, y, "Which is true?",
         [("A", "Ling's class has 3 times as many as Bailey's."), ("B", "Bailey's class has 3 times as many as Ling's.")],
         [("A", "Mrs. Ling's class collects 3 times as many pounds of cans as Mrs. Bailey's class."),
          ("B", "Mrs. Bailey's class collects 3 times as many pounds of cans as Mrs. Ling's class."),
          ("C", "Mrs. Bailey's class collects 3 more pounds of cans than Mrs. Ling's class."),
          ("D", "Mrs. Ling's class collects 3 more pounds of cans than Mrs. Bailey's class.")], size2=16, size4=10.5)
    foot(c, 5)


def e6(c):
    y = start(c)
    y = qtext(c, y, 6, [[("6", True), (" cookies in each box.  ", False), ("57", True), (" boxes.", False)]],
              [[("A baker packs ", False), ("6", True), (" cookies in each box.", False)],
               [("How many cookies in ", False), ("57", True), (" boxes?", False)]])
    x0, top = MARGIN + 80, y - 30
    c.setFillColor(GREY)
    c.rect(x0, top - 70, 300, 70, stroke=1, fill=1)
    c.setFillColor(white)
    c.rect(x0 + 300, top - 70, 70, 70, stroke=1, fill=1)
    c.setFillColor(black)
    c.setFont("Sans-Bold", 18)
    c.drawCentredString(x0 + 150, top + 8, "50")
    c.drawCentredString(x0 + 335, top + 8, "7")
    c.drawRightString(x0 - 10, top - 42, "6")
    c.setFont("Sans-Bold", 16)
    c.drawCentredString(x0 + 150, top - 42, "50 × 6")
    c.drawCentredString(x0 + 335, top - 42, "7 × 6")
    y = do_this(c, top - 100, [("Break ", False), ("57", True), (" into ", False), ("50", True), (" and ", False), ("7", True), (".", False)])
    y = lines(c, MARGIN + 40, y, ["50 × 6 = 300" if T.simp else "50 × 6 = ___", "7 × 6 = ___",
                                 ("300" if T.simp else "___") + " + ___ = ___"], size=17, gap=36)
    pick(c, y - 6, "How many cookies?", [("F", "72"), ("G", "342")], [("F", "72"), ("G", "342"), ("H", "348"), ("J", "3,042")])
    foot(c, 6)


def e7(c):
    y = start(c)
    y = qtext(c, y, 7, [[("Show ", False), ("2 × 8 = 8 × 2", True), (".", False)]],
              [[("Show ", False), ("2 × 8 = 8 × 2", True), (".", False)],
               [("Use skip-counting, equal groups, or a number line.", False)]])
    if T.simp:
        rich_line(c, MARGIN + 20, y - 4, [("2", True), (" groups of ", False), ("8", True)], 15)
        dot_groups(c, MARGIN + 30, y - 30, 2, 8, r=5, gap=13)
        rich_line(c, MARGIN + 20, y - 110, [("8", True), (" groups of ", False), ("2", True)], 15)
        dot_groups(c, MARGIN + 30, y - 136, 8, 2, r=5, gap=13, group_gap=20)
        y -= 180
    else:
        work_box(c, MARGIN, y - 4, 250, 150, "Draw 2 groups of 8")
        work_box(c, MARGIN + 272, y - 4, 250, 150, "Draw 8 groups of 2")
        y -= 175
    y = do_this(c, y, [("Count both. Are they the same?", False)])
    lines(c, MARGIN + 30, y, ["2 × 8 = ___", "8 × 2 = ___", "Same?   yes  /  no"], size=20, gap=44)
    foot(c, 7)


def heart(c, x, y, s=12):
    c.setFillColor(HexColor("#F4B6B0"))
    p = c.beginPath()
    p.moveTo(x, y - s)
    p.curveTo(x - 1.6 * s, y, x - 0.9 * s, y + 1.1 * s, x, y + 0.4 * s)
    p.curveTo(x + 0.9 * s, y + 1.1 * s, x + 1.6 * s, y, x, y - s)
    c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(black)


def e8(c):
    y = start(c)
    y = qtext(c, y, 8, [[("2", True), (" rows of ", False), ("5", True), (" hearts.", False)]],
              [[("The model shows two number sentences. Which two?", False)]])
    for r in range(2):
        for k in range(5):
            heart(c, MARGIN + 80 + k * 50, y - 14 - r * 40)
    for k in range(5):
        c.setStrokeColor(SOFT)
        c.setDash(3, 3)
        c.roundRect(MARGIN + 62 + k * 50, y - 72, 36, 78, 10)
    c.setDash()
    c.setStrokeColor(black)
    rich_line(c, MARGIN + 340, y - 30, [("5", True), (" groups of ", False), ("2", True)], 15)
    y = do_this(c, y - 100, [("5 groups of 2 = ", False), ("5 × 2", True), (" = 2 + 2 + 2 + 2 + 2", False)])
    pick(c, y, "Which two number sentences?", [("A", "5 × 5 = ___      5 + 5 = ___"), ("C", "5 × 2 = ___      2 + 2 + 2 + 2 + 2 = ___")],
         [("A", "5 × 5 = ___      5 + 5 = ___"), ("B", "5 + 5 + 5 + 5 + 5 = ___      5 + 2 = ___"),
          ("C", "5 × 2 = ___      2 + 2 + 2 + 2 + 2 = ___"), ("D", "2 × 5 = ___      2 × 2 × 2 × 2 × 2 = ___")], size2=16)
    foot(c, 8)


def e9(c):
    y = start(c)
    y = qtext(c, y, 9, [[("Is ", False), ("438", True), (" even or odd?", False)]], [[("Which is true about ", False), ("438", True), ("?", False)]])
    y = place_chart(c, MARGIN + 30, y - 4, ["Hundreds", "Tens", "Ones"], "438", shade=(2,))
    y = even_odd(c, MARGIN + 30, y - 20)
    y = do_this(c, y - 10, [("The ", False), ("ones", True), (" digit is ___.  Is it even or odd?", False)])
    pick(c, y, "Which is true?", [("F", "Odd, because the ones digit is odd."), ("J", "Even, because it can be divided by 2 evenly.")],
         [("F", "It is odd because the digit in the ones place is odd."),
          ("G", "It is even because the digit in the hundreds place is even."),
          ("H", "It is odd because it can be divided by 3 evenly."),
          ("J", "It is even because it can be divided by 2 evenly.")], size2=16, size4=13)
    foot(c, 9)


def e10(c):
    y = start(c)
    y = qtext(c, y, 10, [[("Which number is ", False), ("even", True), ("?", False)]])
    y = even_odd(c, MARGIN + 30, y - 6)
    nums = [621, 750] if T.simp else [249, 543, 621, 750]
    for k, n in enumerate(nums):
        s = str(n)
        c.setFont("Sans-Bold", 26)
        x = MARGIN + 40 + k * 125
        w = c.stringWidth(s, "Sans-Bold", 26)
        dw = c.stringWidth(s[-1], "Sans-Bold", 26)
        c.drawString(x, y - 30, s)
        c.rect(x + w - dw - 3, y - 36, dw + 6, 30)
    y = do_this(c, y - 80, [("Look at the ", False), ("ones", True), (" digit only.", False)])
    pick(c, y, "Which number is even?", [("C", "621"), ("D", "750")], [("A", "249"), ("B", "543"), ("C", "621"), ("D", "750")])
    foot(c, 10)


def e11(c):
    y = start(c)
    y = qtext(c, y, 11, [[("☐ ÷ 8 = 8", True)]], [[("What number goes in the box?   ", False), ("☐ ÷ 8 = 8", True)]])
    y = strips(c, MARGIN, y - 10, [("", ["8"] * 8, "none")], 56, total="☐", label_w=40)
    labels = ["0", "8", "16", "24", "32", "40", "48", "56", "___"] if T.simp else ["0", "8", "16", "", "", "", "", "", ""]
    y = jump_line(c, MARGIN + 30, y - 40, labels, 56, "+ 8", size=15)
    y = do_this(c, y - 10, [("☐ ÷ 8 = 8  means  ", False), ("☐ = 8 × 8", True)])
    pick(c, y, "What number goes in the box?", [("F", "64"), ("G", "16")], [("F", "64"), ("G", "16"), ("H", "1"), ("J", "0")])
    foot(c, 11)


def e12(c):
    y = start(c)
    y = qtext(c, y, 12, [[("Look at ", False), ("24,485", True), (".", False)]], [[("Which is true about ", False), ("24,485", True), ("?", False)]])
    y = place_chart(c, MARGIN + 10, y - 4, ["Ten Thousands", "Thousands", "Hundreds", "Tens", "Ones"], "24485", cw=102,
                    values=["10,000", "1,000", "100", "10", "1"])
    y = do_this(c, y - 6, [("Find the digit. Read its place. Then multiply.", False)])
    pick(c, y, "Which is true?",
         [("C", "4 in the hundreds place, so 4 × 100 = 400."), ("D", "4 in the thousands place, so 4 × 1,000 = 40,000.")],
         [("A", "There is a 2 in the tens place, so 2 times 10 equals 20."),
          ("B", "There is a 2 in the thousands place, so 2 times 1,000 equals 2,000."),
          ("C", "There is a 4 in the hundreds place, so 4 times 100 equals 400."),
          ("D", "There is a 4 in the thousands place, so 4 times 1,000 equals 40,000.")], size2=16, size4=12.5)
    foot(c, 12)


if __name__ == "__main__":
    build(("Mid-Module Assessment", "Module 3:", "G3_M3_MidModule"), [m1, m2, m3, m4, m5, m6], paper=True)
    T.title, T.foot, T.paper = "End-of-Module Assessment", "Module 3:", True
    from build_module2 import main
    for simp, suffix in ((False, "Helper"), (True, "Simplified")):
        T.simp = simp
        q1 = [facts_page(0)] + ([facts_page(1)] if simp else [])
        main(f"G3_M3_EndOfModule_{suffix}.pdf", q1 + [chart_page, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12],
             f"Grade 3 Module 3 End-of-Module Assessment – {suffix}")
