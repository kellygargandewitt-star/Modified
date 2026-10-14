"""Grade 3 Reading Module 3 Assessment: preview and teaching packet (not modified).

Teaches the skills and question types on the Module 3 Assessment (STAAR-style)
with a NEW practice article and letter, so students learn how to take the test
without seeing the real answers. Teacher pages first, then student pages.

Run: python3 module3_test_preview.py  ->  writes G3_M3_Reading_Test_Preview.pdf
"""
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import Paragraph, Table, TableStyle

from build_module2 import DARK, H, HELP_BG, HELP_LINE, LIGHT, MARGIN, W, main
from reteach_mid_module import GREY, LEARN_BG, LEARN_LINE

registerFontFamily("Sans", normal="Sans", bold="Sans-Bold", italic="Sans", boldItalic="Sans-Bold")

TIP_BG = HexColor("#FFF6D6")
TIP_LINE = HexColor("#C8961E")
TRY_BG = HexColor("#F4EEFB")
TRY_LINE = HexColor("#7A4FB0")
CW = W - 2 * MARGIN
BOTTOM = 72
FOOT = "Module 3 Assessment Preview"


# ---------------------------------------------------------------- layout helpers

def style(size=12, leading=None, bold=False, color=black, align=0):
    return ParagraphStyle("s", fontName="Sans-Bold" if bold else "Sans", fontSize=size,
                          leading=leading or size * 1.4, textColor=color, alignment=align)


class Page:
    """Draws one page top to bottom; y moves down as things are added."""
    counts = {True: 0, False: 0}

    def __init__(self, c, title, name=True, teacher=False):
        Page.counts[teacher] += 1
        self.c = c
        self.no = ("T" if teacher else "") + str(Page.counts[teacher])
        top = H - 40
        c.setFillColor(DARK)
        c.rect(MARGIN, top - 22, 250, 22, stroke=0, fill=1)
        c.setFillColor(LIGHT)
        c.rect(MARGIN + 252, top - 22, CW - 252, 22, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Sans-Bold", 10)
        c.drawString(MARGIN + 8, top - 15, "GRADE 3 READING • MODULE 3")
        c.setFillColor(black)
        c.setFont("Sans-Bold", 9.5)
        c.drawRightString(W - MARGIN - 8, top - 15, ("TEACHER • " if teacher else "") + title)
        self.y = top - 34
        if name:
            c.setFont("Sans", 12)
            c.drawString(MARGIN, self.y - 14, "Name")
            c.line(MARGIN + 42, self.y - 16, MARGIN + 300, self.y - 16)
            c.drawString(MARGIN + 330, self.y - 14, "Date")
            c.line(MARGIN + 365, self.y - 16, W - MARGIN, self.y - 16)
            self.y -= 34

    def gap(self, n=10):
        self.y -= n

    def check(self):
        if self.y < BOTTOM:
            print(f"  ! page {self.no} overflows by {BOTTOM - self.y:.0f}pt")

    def para(self, html, size=12, x=MARGIN, w=CW, **kw):
        p = Paragraph(html, style(size, **kw))
        _, h = p.wrap(w, 2000)
        p.drawOn(self.c, x, self.y - h)
        self.y -= h
        self.check()
        return h

    def title(self, text, sub=None):
        self.para(text, 20, bold=True)
        if sub:
            self.gap(4)
            self.para(sub, 12, color=GREY)
        self.gap(10)

    def box(self, label, html, bg=HELP_BG, edge=HELP_LINE, size=12, x=MARGIN, w=CW, pad=12):
        p = Paragraph(html, style(size))
        _, h = p.wrap(w - 2 * pad, 2000)
        bh = h + pad * 2 + (20 if label else 0)
        c = self.c
        c.setFillColor(bg)
        c.setStrokeColor(edge)
        c.setLineWidth(1.5)
        c.roundRect(x, self.y - bh, w, bh, 8, stroke=1, fill=1)
        if label:
            c.setFillColor(edge)
            c.setFont("Sans-Bold", 12)
            c.drawString(x + pad, self.y - pad - 10, label)
        p.drawOn(c, x + pad, self.y - bh + pad)
        c.setFillColor(black)
        c.setStrokeColor(black)
        c.setLineWidth(1)
        self.y -= bh
        self.check()
        return bh

    def table(self, rows, widths, size=10.5, head=LIGHT, valign="TOP"):
        cells = [[Paragraph(str(t), style(size, bold=(r == 0))) for t in row] for r, row in enumerate(rows)]
        t = Table(cells, colWidths=widths)
        t.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.75, GREY),
            ("BACKGROUND", (0, 0), (-1, 0), head),
            ("VALIGN", (0, 0), (-1, -1), valign),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        _, h = t.wrap(CW, 2000)
        t.drawOn(self.c, MARGIN, self.y - h)
        self.y -= h
        self.check()

    def question(self, n, html, size=13):
        c = self.c
        c.setFillColor(DARK)
        c.roundRect(MARGIN, self.y - 22, 30, 22, 4, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Sans-Bold", 12)
        c.drawCentredString(MARGIN + 15, self.y - 16, str(n))
        c.setFillColor(black)
        self.para(html, size, x=MARGIN + 40, w=CW - 40)
        self.gap(8)

    def quote(self, html, size=12.5):
        self.para(html, size, x=MARGIN + 70, w=CW - 100)
        self.gap(6)

    def choices(self, items, size=12.5, square=False, letters="ABCDE"):
        c = self.c
        for k, text in enumerate(items):
            x = MARGIN + 52
            c.setLineWidth(1.2)
            if square:
                c.rect(x - 9, self.y - 15, 18, 18)
            else:
                c.circle(x, self.y - 6, 9)
            c.setFont("Sans-Bold", 10)
            c.drawCentredString(x, self.y - 10, letters[k])
            c.setLineWidth(1)
            self.para(text, size, x=MARGIN + 72, w=CW - 72)
            self.gap(7)
        self.gap(4)

    def lines(self, n, gap=28, x=MARGIN, w=CW):
        for _ in range(n):
            self.y -= gap
            self.c.setStrokeColor(GREY)
            self.c.line(x, self.y, x + w, self.y)
        self.c.setStrokeColor(black)
        self.check()

    def footer(self):
        c = self.c
        c.setStrokeColor(LIGHT)
        c.setLineWidth(3)
        c.line(MARGIN, 62, W - MARGIN, 62)
        c.setLineWidth(1)
        c.setStrokeColor(black)
        c.setFont("Sans-Bold", 9)
        c.drawString(MARGIN, 44, FOOT)
        c.setFont("Sans-Bold", 14)
        c.drawCentredString(W / 2, 22, f"Page {self.no}")


def page(title, name=True, teacher=False):
    """Decorator: wraps a page function so it gets a fresh Page and a footer."""
    def wrap(fn):
        def draw(c):
            p = Page(c, title, name, teacher)
            fn(p)
            p.footer()
        draw.__doc__ = fn.__doc__
        return draw
    return wrap


def hint(p, html):
    p.box(None, "<b>Hint:</b> " + html, TIP_BG, TIP_LINE, size=11.5, x=MARGIN + 40, w=CW - 40, pad=8)
    p.gap(12)


# ---------------------------------------------------------------- practice texts
# New texts that use the same skills as the real test (headings, bold words,
# a sequence paragraph, a person-word with -er, im-, -er meaning "more",
# multiple-meaning words) so students practice without seeing test answers.

BEES_A = [
    (None, "Have you ever seen a bee buzzing from flower to flower? That bee is not just "
           "playing. It is working hard! Honeybees live and work together in a home called a "
           "<b>hive</b>. One hive can have thousands of bees."),
    ("Jobs in the Hive", "Every bee in a hive has a job. The <b>queen bee</b> lays all of the eggs. "
           "<b>Worker bees</b> clean the hive, feed the baby bees, and guard the door. Some worker "
           "bees are <b>foragers</b>. Foragers are bees that fly out of the hive to find food in flowers."),
    ("How Bees Make Honey", "Bees follow steps to make honey. First, a forager sips a sweet juice "
           "called <b>nectar</b> from a flower. Next, she carries the nectar back to the hive. Then, "
           "other worker bees put the nectar into tiny wax rooms called cells. Finally, the bees fan "
           "their wings to dry the nectar until it turns into thick, sticky honey."),
]
BEES_B = [
    (None, "It may seem impossible, but one bee makes only a tiny bit of honey in her whole "
           "life. It is less than one spoonful! That is why a hive needs so many bees working together."),
    ("Bees Help Us", "Bees help people and plants, too. When a bee visits a flower, yellow dust "
           "called <b>pollen</b> sticks to her body. She carries the pollen to the next flower. "
           "This helps plants make fruits and seeds. Without bees, we would have fewer apples, "
           "berries, and pumpkins."),
    (None, "Beekeepers are people who take care of bees. They build safe boxes for hives and "
           "check that the bees are healthy. You can help bees, too! Plant flowers in your yard, "
           "and the bees in your neighborhood will be happier."),
]


def passage(p, paras, start, note=True):
    """Numbered paragraphs with headings, plus a 'stop and jot' box beside each one."""
    tw = 352 if note else CW - 28
    for k, (heading, text) in enumerate(paras):
        if heading:
            p.gap(4)
            p.para(heading, 14, bold=True, x=MARGIN + 28, w=tw)
            p.gap(4)
        top = p.y
        h = p.para(text, 13.5, x=MARGIN + 28, w=tw, leading=21)
        p.c.setFont("Sans-Bold", 11)
        p.c.drawString(MARGIN, top - 13, str(start + k))
        if note:
            bx = MARGIN + 28 + tw + 12
            p.c.setStrokeColor(LEARN_LINE)
            p.c.setDash(3, 2)
            p.c.roundRect(bx, top - h - 2, W - MARGIN - bx, h + 2, 6)
            p.c.setDash()
            p.c.setStrokeColor(black)
            p.c.setFont("Sans", 8)
            p.c.setFillColor(GREY)
            p.c.drawString(bx + 6, top - 12, f"¶{start + k}  2–3 words or a sketch")
            p.c.setFillColor(black)
        p.gap(12)


# ---------------------------------------------------------------- teacher pages

@page("How to Use This Preview", name=False, teacher=True)
def t_overview(p):
    """Purpose, the test at a glance, and a 5-day preview plan."""
    p.title("Module 3 Assessment Preview: Teacher Guide",
            "Tools to <b>preview</b> the test and <b>teach</b> the skills it checks. This is not a "
            "modified test. Students practice every question type with a new article (“Busy "
            "Honeybees”) and a new letter, so the real test stays a true check of what they know.")
    p.para("<b>What is on the test</b>", 13)
    p.gap(4)
    p.table([
        ["Part", "What students do", "Items"],
        ["Reading: article 1 (informational, 8 ¶)", "7 questions: headings, multiple-meaning word, "
         "short written answer (bold words), sequence, Part A/Part B central idea, prefix <b>im-</b>, "
         "central idea of the article", "1–7"],
        ["Reading: article 2 (informational, 10 ¶)", "6 questions: author’s purpose, Select TWO, "
         "context clues, signal words, multiple-meaning word, suffix <b>-er</b>", "8–13"],
        ["Reading: essay", "Informational essay that explains, with evidence from article 2", "14"],
        ["Writing: revising and editing", "A letter with numbered sentences. Commas in a series (write "
         "and choose), verb tense, abstract nouns, word choice", "W1–W6"],
    ], [150, 300, CW - 450])
    p.gap(14)
    p.box("How to preview the real test",
          "Show students the real test booklet (or project one page at a time) <b>before</b> test day, with the "
          "questions covered or only the first lines showing. Point out: the numbered paragraphs, the headings, "
          "the sentences shown in the middle of the page, “Select TWO,” Part A and Part B, the lined pages and "
          "planning page for the essay, and the numbered sentences in the letter. Knowing what the pages look "
          "like lowers stress, and students can spend their energy on reading.", HELP_BG, HELP_LINE, size=11.5)


@page("Preview Plan", name=False, teacher=True)
def t_plan(p):
    """5-day preview plan, teaching routines, and IEP supports."""
    p.title("5-Day Preview Plan", "About 30 minutes a day. Student page numbers are at the bottom of each page.")
    p.gap(4)
    p.table([
        ["Day", "Teach (I do → we do → you do)", "Student pages"],
        ["1", "Tour the test (cover the answers). Teach the Test Plan and Question Decoder. "
         "Model reading “Busy Honeybees” with stop-and-jot boxes.", "1–5"],
        ["2", "Text features (headings, bold) and the short written answer with ACE. "
         "Text structure and author’s purpose.", "6–7"],
        ["3", "Central idea (paragraph and whole article), Part A/Part B, Select TWO. "
         "Word detective: multiple-meaning words, prefixes, suffixes, context clues.", "8–10"],
        ["4", "Practice questions 1–12 together, then partners. Always ask: “Prove it. Which paragraph?”",
         "11–15"],
        ["5", "Plan and write the model essay together. Editing rules and the practice letter. "
         "Hand out bookmarks.", "16–21"],
    ], [40, 354, CW - 394])
    p.gap(14)
    p.box("Make every lesson stick", "• <b>Say it, show it, do it:</b> read each strategy aloud, point to it "
          "on the page, then have students do it with a pencil.<br/>"
          "• <b>Think aloud</b> as you answer. Students need to hear <i>how</i> a reader rules out wrong answers.<br/>"
          "• <b>“Prove it”</b> is the routine for every answer: students write the paragraph number next to their choice.<br/>"
          "• Keep the strategy pages out on test day if your classroom test allows it.",
          LEARN_BG, LEARN_LINE, size=11)
    p.gap(10)
    p.box("Students with IEPs or 504 plans",
          "Use these same pages and give each student’s usual supports while you teach, so test day feels "
          "familiar: reading aloud, chunking a passage into stop-and-jot parts, a reading guide or line "
          "tracker, highlighter for key words in the question, short movement breaks after each passage, "
          "and a scribe or speech-to-text for the essay. During the test, use only the supports listed in "
          "the student’s plan.", TIP_BG, TIP_LINE, size=11)


@page("Test Map", name=False, teacher=True)
def t_map(p):
    """Each test item mapped to its skill, the strategy, and the practice item."""
    p.title("Test Map: Item → Skill → Strategy",
            "Teach the skill with the practice item. Do not preview the real items’ answers.")
    p.table([
        ["Test item", "Skill", "What students should do", "Practice"],
        ["1", "Text features: headings", "A heading tells what <b>that part</b> is mostly about.", "Q1"],
        ["2, 12", "Multiple-meaning words", "Try each meaning in the sentence. Keep the one that makes sense.", "Q2, Q11"],
        ["3", "Short answer: why bold?", "ACE: bold marks <b>important words</b> the author explains. "
         "Cite the sentence that tells the meaning.", "Q3"],
        ["4, 11", "Text structure: sequence", "Signal words (first, next, then, finally) show <b>steps in order</b>.", "Q4"],
        ["5", "Part A/B: central idea of a paragraph", "Answer A, then find the sentence that proves A.", "Q5"],
        ["6", "Prefix <b>im-</b>", "im- = <b>not</b>. Cover the prefix, define the base word, add “not.”", "Q6"],
        ["7", "Central idea of the article", "The umbrella answer covers <b>every</b> part, not one detail.", "Q7"],
        ["8", "Author’s purpose", "Inform: to <b>explain</b> or teach. Look at what the whole article does.", "Q8"],
        ["9", "Select TWO details", "Find the idea first. Check each choice: Does it prove the idea? Circle two.", "Q9"],
        ["10", "Context clues + -er", "Read the sentences around the word. -er on an action word = a person who.", "Q10"],
        ["13", "Suffix <b>-er</b>", "-er on a describing word = <b>more</b> (cleaner = more clean).", "Q12"],
        ["14", "Informational essay", "Plan: central idea + 2–3 ways, each with evidence. Use the planner.", "pp. 16–17"],
        ["W1, W5", "Commas in a series", "Put a comma after each item in a list of three or more, before <i>and/or</i>.", "p. 18"],
        ["W2, W4", "Verb tense", "Find the time clue: last week → past (-ed), tomorrow → will.", "p. 18"],
        ["W3, W6", "Abstract nouns", "A feeling or idea you cannot touch: courage, joy, fear.", "p. 18"],
    ], [58, 128, CW - 58 - 128 - 58, 58], size=9.5)


@page("Answer Key", name=False, teacher=True)
def t_key(p):
    """Answer key for the practice items with think-aloud notes."""
    p.title("Answer Key: Practice Items", "Why the right answer is right, and how to rule out the others.")
    p.table([
        ["Q", "Answer", "Think aloud"],
        ["1", "C", "The heading sits above ¶3, and ¶3 is all about the steps for honey."],
        ["2", "C", "“The bees fan their wings.” Bees cannot be a sports fan. They move air with their wings."],
        ["3", "Model", "The author uses bold for <i>foragers</i> because it is an important word. Right after it, "
         "the author explains: “Foragers are bees that fly out of the hive to find food in flowers.” "
         "Bold tells the reader to stop and learn the word."],
        ["4", "B", "First, next, then, finally = steps in order. A, C, D are true but not in ¶3."],
        ["5", "A: B    B: C", "¶5 is about how bees help. The sentence that proves it: “This helps plants make "
         "fruits and seeds.”"],
        ["6", "D", "im- = not. possible = can happen. impossible = <b>cannot</b> happen."],
        ["7", "D", "A, B, C are each one small part (raindrops). D covers the whole article (umbrella)."],
        ["8", "B", "The article teaches facts about bees. It does not tell a story or ask you to buy anything."],
        ["9", "A, D", "Clean, feed, guard, sip, carry, fan = hard work. B and C are true but do not show work. "
         "E is not in the article."],
        ["10", "A", "“…are people who take care of bees.” The text tells the meaning. keep + -er = someone who keeps."],
        ["11", "B", "“Tiny wax rooms called cells” = small rooms in the hive."],
        ["12", "C", "happy + -er = happier = <b>more</b> happy."],
        ["W1", "Rewrite", "“We packed sandwiches, apples, and juice for our garden work day.”"],
        ["W2", "A", "<i>Yesterday</i> is the time clue: past tense = <b>visited</b>."],
        ["W3", "B", "<i>joy</i> is a feeling you cannot touch (an abstract noun) and fits the sentence."],
        ["W4", "D", "<i>Next Saturday</i> is the future. <b>will plant</b> is already correct."],
        ["W5", "C", "Comma after each item before <i>and</i>: tulips, daisies, and sunflowers."],
        ["W6", "A", "<i>pride</i> is the feeling Grandpa has. The other choices are things you can touch."],
    ], [32, 66, CW - 98], size=10)


# ---------------------------------------------------------------- student pages

@page("My Test Plan")
def s_plan(p):
    """Student test map and the 6-step reading plan."""
    p.title("My Reading Test Plan", "Read these steps out loud with your teacher. Use them on every passage.")
    p.box("What is on my test?",
          "☐ <b>Reading:</b> 2 articles that teach facts. Questions 1–13.<br/>"
          "☐ <b>Essay:</b> I write to <b>explain</b> using facts from article 2. Question 14.<br/>"
          "☐ <b>Writing:</b> a letter. I find and fix mistakes. Questions W1–W6.",
          LEARN_BG, LEARN_LINE, size=12.5)
    p.gap(14)
    steps = [
        ("PEEK", "Look at the title, the <b>headings</b>, and the <b>bold words</b>. They tell what you will learn."),
        ("PREVIEW", "Read the questions first (not the answers). Now you know what to look for."),
        ("CHUNK", "Read one paragraph. Stop. Write 2–3 words or draw a sketch about it. Then read the next one."),
        ("UNDERLINE", "Underline the key words in the question: paragraph numbers, <b>TWO</b>, <b>NOT</b>, "
                      "<b>best</b>, <b>mostly</b>."),
        ("PROVE IT", "Go back to the paragraph. Find the answer in the words. Write the ¶ number next to your answer."),
        ("CROSS OUT", "Put an ✗ on answers that are wrong. Choose the <b>best</b> answer that is left."),
    ]
    for k, (word, text) in enumerate(steps):
        c, y = p.c, p.y
        c.setFillColor(HELP_LINE)
        c.circle(MARGIN + 16, y - 16, 16, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Sans-Bold", 16)
        c.drawCentredString(MARGIN + 16, y - 22, str(k + 1))
        c.setFillColor(black)
        p.para(f"<b>{word}</b>", 15, x=MARGIN + 44, w=CW - 44)
        p.gap(2)
        p.para(text, 12.5, x=MARGIN + 44, w=CW - 44)
        p.gap(11)
    p.box(None, "<b>Take your time.</b> Careful readers beat fast readers. If a question is hard, "
          "make your best choice, put a star ★ by it, and come back later.", TIP_BG, TIP_LINE, size=12.5)


@page("Question Decoder")
def s_decoder(p):
    """What each question stem on this test is really asking."""
    p.title("Question Decoder", "Test questions use special words. Here is what they really mean.")
    p.table([
        ["When the question says…", "It is really asking…", "Where I look"],
        ["What do the <b>headings</b> tell the reader?", "What is each part mostly about?",
         "The words under each heading"],
        ["Why does the author use <b>bold</b>…?", "Why are these words special?",
         "The sentence after the bold word. It often tells what the word means."],
        ["Which <b>meaning</b> of the word ___ is used?", "Which meaning fits this sentence?",
         "The sentence in the box. Try each meaning in it."],
        ["Think about the <b>prefix</b> im-<br/>Think about the <b>suffix</b> -er",
         "Use the word parts to find the meaning.", "My Word Parts chart (page 10)"],
        ["What is the <b>meaning</b> of ___ as it is used above?", "Use clues to figure out the word.",
         "The words before and after it"],
        ["Why does the author use <b>sequence</b>…?<br/>…the words <b>first, next, finally</b>?",
         "Why does the author tell things in order?", "The steps in that paragraph"],
        ["What is the <b>central idea</b>…?", "What is it <b>mostly</b> about?",
         "Paragraph question: that paragraph. Article question: the whole article."],
        ["Which sentence <b>best supports</b> the answer to Part A?", "Which sentence proves my Part A answer?",
         "The paragraph from Part A"],
        ["<b>Why did the author write</b> the article?", "What is the author’s purpose?",
         "What the whole article does: teach, tell a story, or try to convince"],
        ["Which details support…? <b>Select TWO</b>.", "Which two facts prove the idea?",
         "Circle <b>two</b> letters. Not one. Not three."],
    ], [180, 160, CW - 340], size=10.5)


@page("Question Types")
def s_types(p):
    """What each kind of question looks like and how to mark it."""
    p.title("What the Questions Look Like", "Know how to mark each kind before test day.")
    cards = [
        ("Choose ONE", "Four answers: A, B, C, D. Only one is best.",
         "Cross out wrong ones ✗. Circle <b>one</b> letter."),
        ("Select TWO", "Five answers: A–E. Two are right.",
         "Check every choice. Circle <b>two</b> letters."),
        ("Part A and Part B", "Two questions that go together.",
         "Answer Part A. Then pick the sentence in Part B that <b>proves</b> Part A."),
        ("Read the sentence", "A sentence from the article is shown in the middle of the page.",
         "Read the sentence. Find it in the article and read the sentences around it."),
        ("Write on the lines", "A question with lines to write on.",
         "Use <b>ACE</b>: Answer, Cite (“The text says…”), Explain (“This shows…”)."),
        ("Essay", "A big question and pages to plan and write.",
         "Plan first. Central idea + 2–3 reasons with facts + closing."),
        ("Revising and editing", "A letter with numbered sentences (1), (2), (3)…",
         "Go to the sentence number. Read it with each choice. Pick the one that sounds and looks right."),
        ("Choose the word", "A box of choices sits in the middle of a sentence.",
         "Read the sentence with each word in the blank. Choose the one that fits."),
    ]
    col_w = (CW - 14) / 2
    for r in range(4):
        top = p.y
        hs = []
        for k in range(2):
            name, looks, job = cards[2 * r + k]
            p.y = top
            hs.append(p.box(name, f"<b>Looks like:</b> {looks}<br/><b>My job:</b> {job}", HELP_BG, HELP_LINE,
                            size=11, x=MARGIN + k * (col_w + 14), w=col_w))
        p.y = top - max(hs) - 12


@page("Practice Article")
def s_bees_1(p):
    """Practice article, paragraphs 1-3."""
    p.para("<b>Read the article. Stop after each paragraph and jot in the box.</b>", 12)
    p.gap(10)
    p.para("Busy Honeybees", 20, bold=True, align=1)
    p.gap(10)
    passage(p, BEES_A, 1)
    p.box(None, "<b>PEEK check:</b> What do the headings tell you this article will teach? "
          "Is it a story, or does it teach facts?", TIP_BG, TIP_LINE, size=11.5)


@page("Practice Article")
def s_bees_2(p):
    """Practice article, paragraphs 4-6, with fact box."""
    passage(p, BEES_B, 4)
    p.box("Stop and think", "In your own words, what is this <b>whole</b> article mostly about?",
          TRY_BG, TRY_LINE, size=12)
    p.lines(2)


@page("Lesson: Text Features")
def s_features(p):
    """Headings and bold words, plus the ACE short answer."""
    p.title("Lesson: Headings and Bold Words")
    p.box("Headings", "A <b>heading</b> is a small title above a part of an article. It tells what "
          "<b>that part</b> is mostly about.<br/><br/>"
          "<b>Example:</b> The heading <i>Jobs in the Hive</i> is above ¶2. ¶2 tells the jobs of the queen and "
          "the worker bees.", LEARN_BG, LEARN_LINE)
    p.gap(10)
    p.box("Bold words", "Authors use <b>bold</b> type for <b>important words</b>. Bold means: "
          "“Stop! Learn this word.” The author usually tells what the word means in the same sentence "
          "or the next one.<br/><br/>"
          "<b>Example:</b> “…a sweet juice called <b>nectar</b>.” The bold word is nectar. The clue "
          "tells me nectar is a sweet juice.", LEARN_BG, LEARN_LINE)
    p.gap(10)
    p.box("Writing a short answer: ACE",
          "<b>A</b> = <b>Answer</b> the question in a full sentence. Use words from the question.<br/>"
          "<b>C</b> = <b>Cite</b> evidence: “In paragraph __, the text says, ‘…’”<br/>"
          "<b>E</b> = <b>Explain</b> how your evidence proves your answer: “This shows…”",
          TRY_BG, TRY_LINE)
    p.gap(14)
    p.para("<b>Model (we do together):</b> Why does the author use bold for the word <i>hive</i> in ¶1?", 12.5)
    p.gap(6)
    p.para("<b>A:</b> The author uses bold for <i>hive</i> because it is an important word to know. "
           "<b>C:</b> In paragraph 1, the text says that bees “live and work together in a home called a "
           "<b>hive</b>.” <b>E:</b> This shows that a hive is a bee’s home, and the bold helps me notice and "
           "learn the word.", 12, x=MARGIN + 20, w=CW - 20, color=HexColor("#204A80"))


@page("Lesson: Structure and Purpose")
def s_structure(p):
    """Sequence structure, signal words, and author's purpose."""
    p.title("Lesson: How and Why Authors Write")
    p.box("Sequence structure", "When an author tells things <b>in order</b>, the structure is "
          "<b>sequence</b>. Look for signal words:<br/>"
          "<b>first   →   next   →   then   →   after that   →   finally</b><br/><br/>"
          "<b>Why does an author use sequence?</b> To show the <b>steps</b> someone takes, in order.", LEARN_BG, LEARN_LINE)
    p.gap(12)
    p.para("<b>Try it:</b> Reread ¶3 of “Busy Honeybees.” Box the signal words. Then write the steps.", 12.5)
    p.gap(10)
    c = p.c
    bw = (CW - 3 * 12) / 4
    for k, word in enumerate(["First", "Next", "Then", "Finally"]):
        x = MARGIN + k * (bw + 12)
        c.setStrokeColor(HELP_LINE)
        c.roundRect(x, p.y - 92, bw, 92, 6)
        c.setStrokeColor(black)
        c.setFont("Sans-Bold", 12)
        c.drawCentredString(x + bw / 2, p.y - 18, word)
        if k < 3:
            c.setFont("Sans-Bold", 16)
            c.drawCentredString(x + bw + 6, p.y - 50, "→")
    p.y -= 106
    p.box("Author’s purpose: Why did the author write it?",
          "<b>To inform / explain</b> = teach facts about a topic. (Articles like the ones on your test!)<br/>"
          "<b>To entertain</b> = tell a story.<br/>"
          "<b>To persuade</b> = try to get you to think or do something.<br/><br/>"
          "<b>Tip:</b> Think about the <b>whole</b> article. Wrong answers often talk about only one paragraph. "
          "Be careful with choices that start “to tell people to…”. That is persuading, not explaining.",
          LEARN_BG, LEARN_LINE)
    p.gap(12)
    p.para("<b>Try it:</b> Why did the author write “Busy Honeybees”? Finish the sentence.", 12.5)
    p.gap(4)
    p.para("The author wrote the article to __________________________________________", 12.5)
    p.gap(4)
    p.lines(1)


@page("Lesson: Central Idea")
def s_central(p):
    """Central idea umbrella, Part A/B, and Select TWO."""
    p.title("Lesson: Central Idea")
    p.box("The umbrella test", "The <b>central idea</b> is what the text is <b>mostly</b> about. "
          "It is like an umbrella: it covers <b>every</b> part.<br/>"
          "A <b>detail</b> is like one raindrop: it is true, but it is only one small part.<br/><br/>"
          "• Central idea of a <b>paragraph</b>: what do <b>all</b> the sentences in that paragraph talk about?<br/>"
          "• Central idea of the <b>article</b>: what do <b>all</b> the headings and parts talk about?",
          LEARN_BG, LEARN_LINE)
    p.gap(10)
    p.para("<b>Try it:</b> Sort these for “Busy Honeybees.” Write <b>U</b> for umbrella or <b>R</b> for raindrop.", 12.5)
    p.gap(8)
    for t in ("Bees fan their wings.", "Honeybees work together in many ways that help the hive and help us.",
              "Beekeepers build boxes for hives.", "The queen bee lays the eggs."):
        p.para("_____   " + t, 12.5, x=MARGIN + 20, w=CW - 20)
        p.gap(6)


@page("Lesson: Proving Answers")
def s_prove(p):
    """Part A/B and Select TWO."""
    p.title("Lesson: Part A, Part B, and Select TWO")
    p.box("Part A and Part B", "<b>Part A</b> asks a question. <b>Part B</b> asks which sentence "
          "<b>proves</b> your Part A answer.<br/>"
          "<b>Check:</b> Read your Part A answer, then say “because…” and read your Part B sentence. "
          "Do they match? If not, fix one of them.", LEARN_BG, LEARN_LINE)
    p.gap(10)
    p.box("Select TWO", "1. Read the idea in the question.  2. Read each choice and ask: "
          "<b>Does this prove the idea?</b>  Write yes or no next to it.<br/>"
          "3. Circle the <b>two</b> yeses. A choice can be true and still not prove the idea!",
          LEARN_BG, LEARN_LINE)
    p.gap(14)
    p.para("<b>Try it together:</b> Idea: <i>Worker bees have many jobs.</i> Write yes or no. Circle TWO.", 12.5)
    p.gap(8)
    for k, t in enumerate(("Worker bees clean the hive.", "The hive can have thousands of bees.",
                           "Worker bees guard the door.", "Pollen is yellow dust.")):
        p.para(f"_____   <b>{'ABCD'[k]}</b>   {t}", 12.5, x=MARGIN + 20, w=CW - 20)
        p.gap(8)
    p.gap(8)
    p.para("<b>Check it:</b> Say the idea + “because” + your two choices. Do they prove it?", 12.5)
    p.gap(14)
    p.para("<b>Try Part A/B together:</b> Part A: What is ¶2 mostly about? <i>Every bee in a hive has a job.</i>  "
           "Part B: Which sentence proves it? Underline it in ¶2 on page 4.", 12.5)


@page("Lesson: Word Detective")
def s_words(p):
    """Multiple-meaning words, context clues, prefixes and suffixes."""
    p.para("Lesson: Word Detective", 20, bold=True)
    p.gap(8)
    p.box("Multiple-meaning words", "Some words have more than one meaning. "
          "<b>Try each meaning in the sentence.</b> Keep the one that makes sense.<br/><br/>"
          "<b>guard</b>  “Worker bees guard the door.”<br/>"
          "  ✗ a person whose job is to keep a place safe (a noun, not an action here)<br/>"
          "  ✓ to watch and protect something", LEARN_BG, LEARN_LINE, size=11, pad=9)
    p.gap(8)
    p.box("Context clues", "Read the sentence <b>before</b>, the sentence <b>with</b> the word, and the "
          "sentence <b>after</b>. Authors often tell you the meaning with words like <i>is, are, called, "
          "means, which,</i> or <i>who</i>.<br/>"
          "Example: “Some worker bees are <b>foragers</b>. Foragers <b>are</b> bees that fly out…”",
          LEARN_BG, LEARN_LINE, size=11, pad=9)
    p.gap(10)
    p.para("<b>My Word Parts chart</b>  (Cover the prefix or suffix. Read the base word. Put it back together.)", 12.5)
    p.gap(6)
    p.table([
        ["Word part", "Means", "Example", "Your turn"],
        ["im-  (prefix)", "not", "im + polite = <b>impolite</b> = not polite", "imperfect = _________"],
        ["un-  (prefix)", "not", "un + happy = <b>unhappy</b> = not happy", "unsafe = _________"],
        ["re-  (prefix)", "again", "re + read = <b>reread</b> = read again", "refill = _________"],
        ["-er  on an action word", "a person who", "teach + er = <b>teacher</b> = a person who teaches",
         "farmer = _________"],
        ["-er  on a describing word", "more", "tall + er = <b>taller</b> = more tall",
         "colder = _________"],
    ], [118, 78, 175, CW - 371], size=10, valign="MIDDLE")
    p.gap(8)
    p.box(None, "<b>Watch out for -er!</b> Action word (teach, farm, keep) → a <b>person</b> who. "
          "Describing word (tall, cold, clean) → <b>more</b>.", TIP_BG, TIP_LINE, size=11, pad=8)


def qpage(fn):
    return page("Practice Questions")(fn)


@qpage
def s_q1(p):
    """Practice questions 1-3."""
    p.para("Use “Busy Honeybees.” <b>Prove it:</b> write the ¶ number next to each answer.", 12)
    p.gap(12)
    p.question(1, "What does the heading <b>How Bees Make Honey</b> tell the reader?")
    p.choices(["what the title of the article is", "how many bees live in a hive",
               "what that part of the article is mostly about", "which words in the article are hardest"])
    p.question(2, "Read the sentence from paragraph 3.")
    p.quote("Finally, the bees <b>fan</b> their wings to dry the nectar until it turns into thick, sticky honey.")
    p.para("Which meaning of the word <b>fan</b> is used above?", 13, x=MARGIN + 40, w=CW - 40)
    p.gap(8)
    p.choices(["a person who loves a sports team", "a machine that blows air",
               "to move air by waving something", "a folded paper you hold"])
    p.question(3, "In paragraph 2, the author uses bold type for the word <b>foragers</b>. Why does the author "
                  "use bold for this word? Support your answer with evidence. Use ACE.")
    p.lines(4)


@qpage
def s_q2(p):
    """Practice questions 4-5."""
    p.question(4, "Why does the author use sequence structure in paragraph 3?")
    p.choices(["to tell what the queen bee does", "to show the steps bees take to make honey",
               "to explain why bees are important", "to show where bees find flowers"])
    p.gap(6)
    p.question(5, "This question has two parts. First, answer Part A. Then, answer Part B.")
    p.para("<b>Part A</b>   What is the central idea of paragraph 5?", 13, x=MARGIN + 40, w=CW - 40)
    p.gap(8)
    p.choices(["Bees have yellow dust on them.", "Bees help plants make fruits and seeds.",
               "People like to eat apples and berries.", "Bees fly from the hive to many flowers."])
    p.para("<b>Part B</b>   Which sentence from the article <b>best supports</b> the answer to Part A?",
           13, x=MARGIN + 40, w=CW - 40)
    p.gap(8)
    p.choices(["“When a bee visits a flower, yellow dust called pollen sticks to her body.”",
               "“She carries the pollen to the next flower.”",
               "“This helps plants make fruits and seeds.”",
               "“Beekeepers are people who take care of bees.”"])
    hint(p, "Read your Part A answer, say “because,” then read your Part B sentence. Do they match?")


@qpage
def s_q3(p):
    """Practice questions 6-8."""
    p.question(6, "Read the sentence from paragraph 4.")
    p.quote("It may seem <b>impossible</b>, but one bee makes only a tiny bit of honey in her whole life.")
    p.para("Think about the prefix <b>im-</b>. What is the meaning of <b>impossible</b>?", 13,
           x=MARGIN + 40, w=CW - 40)
    p.gap(8)
    p.choices(["very easy", "very funny", "able to happen", "not able to happen"])
    p.question(7, "What is the central idea of the article?")
    p.choices(["Bees live in hives.", "Bees fan their wings to make honey.", "Beekeepers keep bees safe.",
               "Honeybees work hard in many ways that help the hive and help people."])
    p.question(8, "Why did the author write the article?")
    p.choices(["to tell people to buy honey", "to teach facts about honeybees",
               "to tell a funny story about a bee", "to show how to build a beehive"])


@qpage
def s_q4(p):
    """Practice questions 9-10."""
    p.question(9, "Which details support the idea that bees are hard workers? <b>Select TWO</b> correct answers.")
    p.choices(["Worker bees clean, feed baby bees, and guard the door.", "Bees live in a hive.",
               "Pollen is yellow dust.", "Bees fan their wings to dry the nectar.",
               "Bees sleep all winter."], square=True)
    hint(p, "Write yes or no next to each choice first. Then circle the two yeses.")
    p.question(10, "Read the sentence from paragraph 6.")
    p.quote("<b>Beekeepers</b> are people who take care of bees.")
    p.para("What is the meaning of <b>beekeepers</b> as it is used above?", 13, x=MARGIN + 40, w=CW - 40)
    p.gap(8)
    p.choices(["people who look after bees", "people who are afraid of bees",
               "bees that make honey", "boxes where bees live"])


@qpage
def s_q5(p):
    """Practice questions 11-12 and a check-my-work list."""
    p.question(11, "Read the words from paragraph 3.")
    p.quote("…tiny wax rooms called <b>cells</b>.")
    p.para("Which meaning of the word <b>cells</b> is used above?", 13, x=MARGIN + 40, w=CW - 40)
    p.gap(8)
    p.choices(["phones you carry", "small rooms in a beehive", "rooms in a jail", "tiny parts of the body"])
    p.question(12, "Read the sentence from paragraph 6.")
    p.quote("Plant flowers in your yard, and the bees in your neighborhood will be <b>happier</b>.")
    p.para("Think about the suffix <b>-er</b>. What is the meaning of <b>happier</b> as it is used above?", 13,
           x=MARGIN + 40, w=CW - 40)
    p.gap(8)
    p.choices(["not happy", "a person who is happy", "more happy", "happy again"])
    p.gap(6)
    p.box("Check my work", "☐ I answered every question.<br/>"
          "☐ I wrote a ¶ number next to my answers to prove them.<br/>"
          "☐ I circled <b>two</b> letters for Select TWO.<br/>"
          "☐ My Part B sentence proves my Part A answer.<br/>"
          "☐ I went back to every question with a star ★.", LEARN_BG, LEARN_LINE, size=12)


@page("Lesson: Informational Essay")
def s_essay_teach(p):
    """How to plan an explaining essay, with a model."""
    p.title("Lesson: Writing an Essay That Explains",
            "On the test you will explain how a person’s work helps something, using facts from the article.")
    p.table([
        ["Part", "What I write", "Sentence starters"],
        ["Introduction", "Hook + <b>central idea</b> (the answer to the prompt in one sentence)",
         "Did you know…?   ___ helps ___ in many ways."],
        ["Body 1", "First way + evidence from the article + explain", "One way ___ is…   The article says…"],
        ["Body 2", "Second way + evidence + explain", "Another way ___ is…   In paragraph __, …"],
        ["Body 3", "Third way + evidence + explain", "Also, …   This shows that…"],
        ["Conclusion", "Say the central idea again in new words", "As you can see, …   That is why…"],
    ], [90, 210, CW - 300], size=10)
    p.gap(6)
    p.para("<b>Model prompt:</b> Explain how bees help people and plants.", 13)
    p.gap(6)
    p.box("Model essay (read it together and label each part)",
          "Did you know that a tiny bee can do a big job? Bees help people and plants in many important ways.<br/><br/>"
          "One way bees help is by moving pollen. In paragraph 5, the article says that a bee “carries the pollen "
          "to the next flower.” This helps plants make fruits and seeds.<br/><br/>"
          "Another way bees help is by making honey. In paragraph 3, the article explains that bees dry nectar "
          "“until it turns into thick, sticky honey.” People can enjoy that honey.<br/><br/>"
          "Bees also help us have food to eat. The article says that without bees, “we would have fewer apples, "
          "berries, and pumpkins.” This shows that many foods depend on bees.<br/><br/>"
          "As you can see, bees are small, but they help people and plants every day. That is why we should "
          "plant flowers and take care of bees.", HELP_BG, HELP_LINE, size=11)
    p.gap(6)
    p.box(None, "<b>Before you write:</b> Plan on the planning page.  <b>After you write:</b> Reread. "
          "Capital letters? End marks? Did I use facts from the article?", TIP_BG, TIP_LINE, size=11, pad=8)


@page("Essay Planner")
def s_planner(p):
    """Graphic organizer for an explaining essay."""
    p.title("My Essay Planner", "Prompt: Explain how ______________________________ helps ______________________.")
    rows = [("Central idea", "_____ helps _____ in many ways."), ("Way 1", "Evidence (¶ __):"),
            ("Way 2", "Evidence (¶ __):"), ("Way 3", "Evidence (¶ __):"), ("Closing", "As you can see,")]
    c = p.c
    for label, cue in rows:
        bh = 92 if label.startswith("Way") else 64
        c.setStrokeColor(HELP_LINE)
        c.setLineWidth(1.5)
        c.roundRect(MARGIN, p.y - bh, CW, bh, 8)
        c.setLineWidth(1)
        c.setFillColor(HELP_LINE)
        c.setFont("Sans-Bold", 12)
        c.drawString(MARGIN + 12, p.y - 20, label)
        c.setFillColor(GREY)
        c.setFont("Sans", 10.5)
        c.drawString(MARGIN + 120, p.y - 20, cue)
        c.setFillColor(black)
        c.setStrokeColor(LIGHT)
        for ly in range(int(p.y - 44), int(p.y - bh), -26):
            c.line(MARGIN + 12, ly, W - MARGIN - 12, ly)
        c.setStrokeColor(black)
        p.y -= bh + 12
    p.check()
    p.box("Check my essay", "☐ I wrote my central idea.   ☐ I gave 2–3 ways.   ☐ I used facts from the article "
          "and said the ¶ number.   ☐ I wrote a closing.   ☐ Capitals, end marks, spelling.",
          LEARN_BG, LEARN_LINE, size=11.5)


@page("Lesson: Editing Rules")
def s_editing(p):
    """Commas in a series, verb tense, abstract nouns."""
    p.para("Lesson: Editing Rules for the Writing Test", 20, bold=True)
    p.gap(8)
    p.box("Commas in a series", "When you list <b>three or more</b> things, put a comma after each one "
          "before <i>and</i> or <i>or</i>.<br/>"
          "✗  I like red blue and green.<br/>"
          "✓  I like red<b>,</b> blue<b>,</b> and green.<br/>"
          "<b>Trick:</b> Say the list out loud. Put a comma where you take a small breath.", LEARN_BG, LEARN_LINE)
    p.gap(8)
    p.box("Verb tense: find the time clue", "Look for a word that tells <b>when</b>.<br/>"
          "<b>Past</b> (already happened): yesterday, last week, ago → add <b>-ed</b>: walk → walk<b>ed</b><br/>"
          "<b>Present</b> (happens now or always): today, every day → walk / walks<br/>"
          "<b>Future</b> (will happen): tomorrow, next week, soon → <b>will</b> walk<br/>"
          "<b>Remember:</b> “No change is needed” is sometimes the right answer!", LEARN_BG, LEARN_LINE)
    p.gap(8)
    p.box("Abstract nouns", "A <b>concrete noun</b> is something you can see or touch: beach, water, dog.<br/>"
          "An <b>abstract noun</b> is a feeling or idea you <b>cannot</b> touch: courage, happiness, fear, "
          "pride, joy, kindness, friendship.<br/>"
          "<b>Clue:</b> Many abstract nouns end in <b>-ness</b>, <b>-ship</b>, or <b>-dom</b>.", LEARN_BG, LEARN_LINE)
    p.gap(2)
    p.para("<b>Try it:</b> Sort the words. Write each one in the right column.", 12.5)
    p.gap(4)
    p.para("<b>kindness    rock    joy    pencil    bravery    tree    love    shoe</b>", 12.5, align=1)
    p.gap(8)
    p.table([["Concrete (I can touch it)", "Abstract (a feeling or idea)"]] + [["&nbsp;", ""]] * 4,
            [CW / 2, CW / 2], size=12)


@page("Practice: Revising and Editing")
def s_letter(p):
    """Practice letter with numbered sentences (same format as the writing test)."""
    p.para("Jada wrote a letter to her grandpa. Read the letter and look for changes she should make. "
           "Then answer the questions.", 12)
    p.gap(4)
    p.para("My Garden", 15, bold=True, align=1)
    p.gap(2)
    p.box(None, "(1) Dear Grandpa,<br/><br/>"
          "(2) I hope you are doing well. (3) My class is growing a garden at school. (4) We packed "
          "sandwiches apples and juice for our garden work day. (5) Yesterday, my class visit a big flower "
          "farm. (6) The farmer showed us how to plant seeds. (7) I was a little nervous, but I was brave "
          "and tried it.<br/><br/>"
          "(8) Next Saturday, Mom and I will plant flowers at home. (9) We will plant tulips daisies and "
          "sunflowers. (10) Planting with you last spring filled me with _______.<br/><br/>"
          "(11) Love,<br/>(12) Jada", HELP_BG, HELP_LINE, size=12.5)
    p.gap(12)
    p.question("W1", "Sentence 4 needs to be revised. Rewrite sentence 4 using commas.", size=12)
    p.lines(2, gap=22)
    p.gap(6)
    p.question("W2", "What change should be made in sentence 5?", size=12)
    p.choices(["Change visit to visited.", "Change visit to visiting.", "Change visit to will visit.",
               "No change is needed."], size=12)


@page("Practice: Revising and Editing")
def s_letter_2(p):
    """Practice letter questions W3-W6."""
    p.question("W3", "Jada wants to add an abstract noun. Which word best completes the sentence?", size=12)
    p.para("I was a little nervous, but I felt _______ when I planted my first seed.", 12.5,
           x=MARGIN + 40, w=CW - 40)
    p.gap(8)
    p.choices(["dirt", "joy", "shovel", "flower"], size=12)
    p.question("W4", "What change should be made in sentence 8?", size=12)
    p.choices(["Change will plant to planted.", "Change will plant to planting.", "Change will plant to plants.",
               "No change is needed."], size=12)
    p.question("W5", "What is the correct way to write sentence 9?", size=12)
    p.choices(["We will plant tulips daisies, and sunflowers.", "We will plant tulips, daisies and, sunflowers.",
               "We will plant tulips, daisies, and sunflowers.", "No change is needed."], size=12)
    p.question("W6", "Which word would be best to put in the blank at the end of sentence 10?", size=12)
    p.choices(["pride", "seeds", "dirt", "spring"], size=12)
    p.box("How I answer editing questions", "1. Find the sentence <b>number</b> in the letter.  "
          "2. Read the whole sentence.  3. Read it again with <b>each</b> choice.  "
          "4. Use the rules: commas in a list, time clue for tense, feeling word for abstract noun.",
          LEARN_BG, LEARN_LINE, size=11, pad=9)


@page("Test Day Bookmarks", name=False)
def s_bookmarks(p):
    """Three cut-out bookmarks with the test plan."""
    p.para("Cut out a bookmark. Keep it next to you while you practice.", 12, color=GREY)
    p.gap(10)
    bw = (CW - 2 * 16) / 3
    bh = 560
    c = p.c
    text = ("<b>MY TEST PLAN</b><br/><br/>"
            "<b>1 PEEK</b><br/>title, headings, bold words<br/><br/>"
            "<b>2 PREVIEW</b><br/>read the questions first<br/><br/>"
            "<b>3 CHUNK</b><br/>read one ¶, stop, jot<br/><br/>"
            "<b>4 UNDERLINE</b><br/>TWO, NOT, best, mostly, ¶ #<br/><br/>"
            "<b>5 PROVE IT</b><br/>go back, write the ¶ #<br/><br/>"
            "<b>6 CROSS OUT</b><br/>✗ wrong answers, pick the best<br/><br/>"
            "<b>Write: ACE</b><br/>Answer • Cite • Explain<br/><br/>"
            "<b>Word parts</b><br/>im-/un- = not<br/>-er = person who OR more<br/><br/>"
            "<b>Editing</b><br/>list → commas<br/>time clue → tense<br/>feeling → abstract noun")
    for k in range(3):
        x = MARGIN + k * (bw + 16)
        c.setDash(4, 3)
        c.rect(x, p.y - bh, bw, bh)
        c.setDash()
        c.setFillColor(HELP_BG)
        c.rect(x + 6, p.y - bh + 6, bw - 12, bh - 12, stroke=0, fill=1)
        c.setFillColor(black)
        para = Paragraph(text, style(11, leading=14.5, align=1))
        _, h = para.wrap(bw - 24, bh)
        para.drawOn(c, x + 12, p.y - 18 - h)
    p.y -= bh
    p.check()


PAGES = [t_overview, t_plan, t_map, t_key, s_plan, s_decoder, s_types, s_bees_1, s_bees_2, s_features,
         s_structure, s_central, s_prove, s_words, s_q1, s_q2, s_q3, s_q4, s_q5, s_essay_teach, s_planner, s_editing,
         s_letter, s_letter_2, s_bookmarks]

if __name__ == "__main__":
    main("G3_M3_Reading_Test_Preview.pdf", PAGES, "Grade 3 Module 3 Assessment Preview")
