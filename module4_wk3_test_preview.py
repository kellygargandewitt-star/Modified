"""Grade 3 Reading Module 4, Week 3 Assessment: preview and teaching packet (not modified).

The test is a play (drama) with 6 reading questions and a short editing passage
on quotation marks. This packet teaches every skill and question type with a NEW
practice play ("The Stuck Wagon") and a new paper, so the real test stays a true
check. Teacher pages first, then student pages.

Run: python3 module4_wk3_test_preview.py  ->  writes G3_M4_Wk3_Reading_Test_Preview.pdf
"""
import re

from reportlab.lib.colors import HexColor, black, white

from build_module2 import HELP_BG, HELP_LINE, MARGIN, W, main
from module3_test_preview import (
    CW, LEARN_BG, LEARN_LINE, TIP_BG, TIP_LINE, TRY_BG, TRY_LINE, Page, hint, page,
)
from reteach_mid_module import GREY

Page.label = "GRADE 3 READING • MODULE 4"
Page.foot = "Module 4, Week 3 Assessment Preview"
STAGE = "#1F6F78"  # colour for stage directions, so students can spot them

# ---------------------------------------------------------------- practice play
# Same parts as the test play (cast list, narrator, two scenes, stage directions,
# older siblings who won't let the youngest help, a Latin-root word, a resolution)
# but a different story, theme and root word.

CAST = [("NARRATOR", ""), ("GRANDMA ROSA", "owner of an apple orchard"), ("MIA", "the oldest sister"),
        ("LEO", "the middle brother"), ("PIP", "the youngest sister")]

SCENE_1 = [
    ("ACT 1, SCENE 1", None),
    ("Grandma Rosa’s apple orchard", None),
    (None, "(Early morning. There are apple trees, a wooden wagon full of baskets, and a dirt road "
           "that leads to town. Grandma Rosa sits on the wagon. Narrator walks onto the stage.)"),
    ("NARRATOR", "Every Saturday, Grandma Rosa sold her apples at the town market. Her three "
                 "grandchildren always came along to help."),
    ("MIA", "(lifts a basket) I am the strongest, so I will load the heavy baskets."),
    ("LEO", "I will count the apples and set the prices. I am the best at math."),
    ("PIP", "Mia, can I lift a basket too?"),
    ("MIA", "These baskets are too heavy for you, Pip. You might drop them."),
    ("PIP", "Leo, can I help you count?"),
    ("LEO", "Not today. You will mix up my numbers. Go pick some flowers."),
    ("NARRATOR", "Pip sat under a tree and sighed. Grandma Rosa noticed."),
    ("GRANDMA ROSA", "Children, the market opens at noon. If we are late, we will not sell a single "
                     "apple. Let’s go!"),
]

SCENE_2 = [
    ("ACT 1, SCENE 2", None),
    ("The muddy road to town", None),
    (None, "(Later that morning. The wagon’s back wheel is stuck deep in a mud puddle. "
           "The family stands around it.)"),
    ("NARRATOR", "It had rained all night. Halfway to town, the wagon sank into the mud and would not move."),
    ("GRANDMA ROSA", "Oh no! It is almost noon."),
    ("MIA", "Stand back. I will pull it out myself. (She pulls hard on the handle. The wagon does not move.)"),
    ("LEO", "Let me try. I will push from behind. (He pushes until his face turns red. The wagon does not move.)"),
    ("PIP", "(quietly) What if we all work together?"),
    ("MIA", "You are too little to help, Pip."),
    ("NARRATOR", "Pip did not give up. She inspected the wheel closely. Then she ran to the side of the "
                 "road and dragged back a flat wooden board."),
    ("PIP", "Put this board under the wheel. Then Mia can pull, Leo can push, and Grandma and I can "
            "lift the side."),
    ("LEO", "(scratches his head) That just might work."),
    ("NARRATOR", "On the count of three, everyone pulled, pushed, and lifted. With a loud squish, the "
                 "wagon rolled out of the mud!"),
    ("GRANDMA ROSA", "(claps) We did it, together!"),
    ("MIA", "I am sorry, Pip. We should have listened to you."),
    ("LEO", "From now on, everyone helps."),
    ("NARRATOR", "The family reached the market just in time. They sold every apple, and Pip got to "
                 "count the money."),
]


def stage(text):
    """Colour every (stage direction) so it stands out from the spoken words."""
    return re.sub(r"(\([^)]*\))", rf'<font color="{STAGE}">\1</font>', text)


def script(p, lines, size=12.5):
    for who, text in lines:
        if text is None:
            p.para(who, size + 1, bold=True)
            p.gap(2)
        elif who is None:
            p.para(stage(text), size, x=MARGIN + 16, w=CW - 16)
            p.gap(8)
        else:
            p.para(f"<b>{who}:</b> " + stage(text), size, leading=size * 1.45)
            p.gap(5)


def scene_check(p, n):
    p.box(f"Scene {n} check", "Who is in this scene? ______________________________<br/>"
          "What is happening (the problem)? ___________________________________", TRY_BG, TRY_LINE,
          size=11.5, pad=9)


# ---------------------------------------------------------------- teacher pages

@page("How to Use This Preview", name=False, teacher=True)
def t_overview(p):
    """Purpose, the test at a glance, how to preview it, and a 3-day plan."""
    p.title("Module 4, Week 3 Assessment Preview: Teacher Guide",
            "Tools to <b>preview</b> the test and <b>teach</b> the skills it checks. This is not a modified "
            "test. Students practice every question type with a new play (“The Stuck Wagon”) and a new "
            "paper, so the real test stays a true check of what they know.")
    p.para("<b>What is on the test</b>", 13)
    p.gap(4)
    p.table([
        ["Part", "What students do", "Items"],
        ["Reading: a play (drama), 2 scenes", "Narrator’s role, how the scenes connect, Choose two characters, "
         "Latin root <b>vis</b>, theme", "1–5"],
        ["Reading: written answer", "Tell the <b>resolution</b> of the play with details from the play", "6"],
        ["Writing: editing", "A short paper with dialogue. Choose the correct way to punctuate quotations", "W1–W3"],
    ], [150, 300, CW - 450])
    p.gap(12)
    p.box("How to preview the real test",
          "Before test day, show students the real booklet with the questions covered. Point out: the cast "
          "list (Characters), ACT 1, SCENE 1 and SCENE 2, the words in parentheses (stage directions), the "
          "character names in capital letters before each line, “Choose two answers,” the lines for the "
          "written answer, and the numbered sentences in Beth’s paper.", HELP_BG, HELP_LINE, size=11.5)


@page("Preview Plan", name=False, teacher=True)
def t_plan(p):
    """3-day plan and IEP supports."""
    p.title("3-Day Preview Plan", "About 30 minutes a day. Student page numbers are at the bottom of each page.")
    p.table([
        ["Day", "Teach (I do → we do → you do)", "Student pages"],
        ["1", "Test Plan, Question Decoder, Parts of a Play. Read “The Stuck Wagon” as readers’ theater: "
         "assign parts, and have everyone act out the stage directions.", "1–5"],
        ["2", "Plot and characters, theme, Latin roots. Practice questions 1–6 and 8 together, then "
         "with partners. Ask every time: “Prove it. Which line?”", "6–7, 9–11"],
        ["3", "Write the resolution answer (Q7) with ACE. Quotation mark rules and the practice paper. "
         "Hand out bookmarks.", "8, 11, 12–15"],
    ], [40, 354, CW - 394])
    p.gap(14)
    p.box("Make every lesson stick", "• <b>Act it out:</b> readers’ theater turns stage directions and dialogue "
          "into something students can see and do.<br/>"
          "• <b>Think aloud</b> as you answer. Students need to hear <i>how</i> a reader rules out wrong answers.<br/>"
          "• <b>“Prove it”</b> is the routine for every answer: students point to the line in the play.<br/>"
          "• Keep the strategy pages out on test day if your classroom test allows it.",
          LEARN_BG, LEARN_LINE, size=11.5)
    p.gap(14)
    p.box("Students with IEPs or 504 plans",
          "Readers’ theater is great practice for students with dyslexia or reading-fluency goals: give them "
          "a short part (Pip or Grandma Rosa) to rehearse ahead of time. Use each student’s usual supports "
          "while you teach (reading aloud, a line tracker, highlighting names, breaks between scenes, a scribe "
          "for the written answer). During the test, use only the supports listed in the student’s plan.",
          TIP_BG, TIP_LINE, size=11)


@page("Test Map", name=False, teacher=True)
def t_map(p):
    """Each test item mapped to its skill, the strategy, and the practice item."""
    p.title("Test Map: Item → Skill → Strategy",
            "Teach the skill with the practice item. Do not preview the real items’ answers.")
    p.table([
        ["Test item", "Skill", "What students should do", "Practice"],
        ["1", "Parts of a play: narrator", "The narrator talks to the <b>audience</b> to explain what is "
         "happening. The narrator is not part of the action.", "Q1"],
        ["2", "How scenes connect", "Write one line about what happens in each scene. Then ask: Where is the "
         "<b>problem</b>? Where is it <b>solved</b>?", "Q2"],
        ["3", "Character actions (Choose two)", "Find each character’s lines. Who says “no” to the brother? "
         "Circle <b>two</b>.", "Q3"],
        ["4", "Latin root <b>vis</b>", "vis/vid = <b>see</b>. Use the root plus the sentence clues.", "Q4"],
        ["5", "Theme", "What lesson does the ending teach everyone? Cross out answers with <b>never</b> or "
         "<b>always</b> and answers the play does not show.", "Q5"],
        ["6", "Resolution (written)", "Resolution = how the problem is solved at the end. ACE with a detail "
         "from the last scene.", "Q7"],
        ["—", "Stage directions, character change", "Extra skills students need to understand the play.", "Q6, Q8"],
        ["W1", "Quotation: asked/said first", "Comma after <i>asked</i>, quotation marks, capital first "
         "word, ? inside the quotation marks.", "W1"],
        ["W2", "Quotation: said last", "Comma goes <b>inside</b> the closing quotation mark.", "W2"],
        ["W3", "Quotation: ! or ?", "Quotation marks go around the spoken words only. ! stays inside.", "W3"],
    ], [58, 128, CW - 58 - 128 - 58, 58], size=10)


@page("Answer Key", name=False, teacher=True)
def t_key(p):
    """Answer key for the practice items with think-aloud notes."""
    p.title("Answer Key: Practice Items", "Why the right answer is right, and how to rule out the others.")
    p.table([
        ["Q", "Answer", "Think aloud"],
        ["1", "B", "The narrator tells the audience what is happening (“It had rained all night…”). "
         "The narrator never pulls the wagon or talks to the family."],
        ["2", "C", "Scene 1 introduces the family and their plan to go to market. Scene 2 has the stuck "
         "wagon and how they fix it. A, B, D do not match what happens."],
        ["3", "B, C", "Mia: “too heavy for you.” Leo: “Not today.” Grandma never says no to Pip."],
        ["4", "A", "spect = look. Pip <b>looked carefully</b> at the wheel, then found a board."],
        ["5", "B", "The wagon moves only when everyone helps. A and C use “always” or “most” and are not "
         "shown. D is about one detail, not a lesson."],
        ["6", "B", "Words in parentheses are stage directions: they tell what a character <b>does</b>."],
        ["7", "Model", "<b>A:</b> The resolution is that the family works together and gets the wagon out of "
         "the mud. <b>C:</b> The narrator says, “On the count of three, everyone pulled, pushed, and lifted,” "
         "and the wagon “rolled out of the mud.” <b>E:</b> This shows the problem was solved because they "
         "used Pip’s idea and worked together, and they got to the market in time."],
        ["8", "D", "Beginning: “You are too little to help.” End: “We should have listened to you.”"],
        ["W1", "B", "Mr. Lopez asked, “What should we name him?”"],
        ["W2", "C", "“Let’s call him Peanut,” Ava said."],
        ["W3", "A", "“Wow, that is a great name!” said Mr. Lopez."],
        ["W4", "D", "Sentence 7 is already correct: comma inside the quotation marks, then the speaker."],
    ], [32, 62, CW - 94], size=10.5)


# ---------------------------------------------------------------- student pages

@page("My Test Plan")
def s_plan(p):
    """Student test map and the 6-step plan for reading a play."""
    p.title("My Test Plan for a Play", "Read these steps out loud with your teacher. Use them on test day.")
    p.box("What is on my test?",
          "☐ <b>Reading:</b> a play with 2 scenes. Questions 1–5 and a written answer, question 6.<br/>"
          "☐ <b>Writing:</b> a short paper with talking (dialogue). I fix the quotation marks. Questions 1–3.",
          LEARN_BG, LEARN_LINE, size=12.5)
    p.gap(14)
    steps = [
        ("PEEK", "Look at the title and the <b>Characters</b> list. Who is in the play? Who is the narrator?"),
        ("PREVIEW", "Read the questions first (not the answers). Now you know what to look for."),
        ("SCENE BY SCENE", "Read one scene. Stop. Who is there? What is the problem? Then read the next scene."),
        ("UNDERLINE", "Underline the key words in the question: <b>Scene 1</b>, <b>Scene 2</b>, <b>two</b>, "
                      "<b>theme</b>, <b>resolution</b>."),
        ("PROVE IT", "Go back to the play. Find the character’s name and read their words."),
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
        ["How is the <b>narrator</b> different from the other characters?", "What is the narrator’s job?",
         "Every NARRATOR line. Who is the narrator talking to?"],
        ["How are <b>Scene 1</b> and <b>Scene 2</b> connected?", "What does each scene do in the story?",
         "My scene check boxes. Where is the problem? Where is it solved?"],
        ["Which characters will not let…? <b>Choose two</b> answers.", "Which two characters said no?",
         "The lines with those characters’ names. Circle <b>two</b> letters."],
        ["Think about the <b>Latin root</b> ___.", "Use the root to find the meaning.",
         "My Latin Roots chart (page 7) and the sentence"],
        ["What is the <b>theme</b> of the play?", "What lesson does the play teach everyone?",
         "How the problem is solved at the end"],
        ["What is the <b>resolution</b> of the play?", "How is the problem solved at the end?",
         "The last scene. Use ACE and a detail from the play."],
        ["What is the correct way to write sentence __?", "Which choice has the right punctuation?",
         "My Quotation Mark Rules (page 12)"],
    ], [180, 160, CW - 340], size=10.5)
    p.gap(14)
    p.box("Big words for plays", "<b>problem</b> = what goes wrong   •   <b>resolution</b> = how the problem "
          "is solved at the end<br/><b>theme</b> = the lesson the story teaches everyone   •   <b>audience</b> = "
          "the people watching the play", HELP_BG, HELP_LINE, size=12)


@page("Lesson: Parts of a Play")
def s_parts(p):
    """Cast list, narrator, acts and scenes, stage directions, dialogue."""
    p.title("Lesson: Parts of a Play", "A play is a story written to be acted out on a stage.")
    p.table([
        ["Part", "What it is", "Example from “The Stuck Wagon”"],
        ["Characters (cast)", "A list of everyone in the play, at the top", "MIA, the oldest sister"],
        ["Narrator", "A storyteller who talks to the <b>audience</b>. Explains what is happening. "
         "Is <b>not</b> part of the action.", "NARRATOR: It had rained all night."],
        ["Act and scene", "Parts of a play, like chapters in a book. A new scene can mean a new <b>time</b> "
         "or <b>place</b>.", "ACT 1, SCENE 2<br/>The muddy road to town"],
        ["Setting", "Where and when the scene happens", "Early morning, Grandma Rosa’s orchard"],
        ["Stage directions", "Words in <b>(parentheses)</b>. They tell what characters <b>do</b> or how they "
         "feel. Actors do not say them out loud.", f'<font color="{STAGE}">(scratches his head)</font>'],
        ["Dialogue", "The words characters say. The speaker’s name comes first, then a colon (:).",
         "PIP: What if we all work together?"],
    ], [110, 230, CW - 340], size=11, valign="MIDDLE")
    p.gap(14)
    p.box("How to read a play", "1. Read the <b>name</b> first. That is who is talking.<br/>"
          "2. Read the words after the colon. Do <b>not</b> read the name as part of the sentence.<br/>"
          "3. When you see <b>( )</b>, picture it or act it out.<br/>"
          "4. At each new <b>SCENE</b>, ask: Where are we now? What time is it?", LEARN_BG, LEARN_LINE)
    p.gap(12)
    p.para("<b>Try it:</b> Circle the cast list. Box each SCENE. Highlight every narrator line in the play.", 12.5)


@page("Practice Play")
def s_play_1(p):
    """Practice play, cast list and Scene 1."""
    p.para("Read the play. Stop after each scene and fill in the box.", 12, bold=True)
    p.gap(4)
    p.para("The Stuck Wagon", 20, bold=True, align=1)
    p.gap(4)
    p.para("<b>Characters</b>", 12.5)
    for who, desc in CAST:
        p.para(who + (f", {desc}" if desc else ""), 12, x=MARGIN + 16, w=CW - 16)
    p.gap(8)
    script(p, SCENE_1, size=12)
    scene_check(p, 1)


@page("Practice Play")
def s_play_2(p):
    """Practice play, Scene 2."""
    script(p, SCENE_2, size=12)
    scene_check(p, 2)


@page("Lesson: Plot and Characters")
def s_plot(p):
    """How scenes connect, what characters say and do, character change."""
    p.title("Lesson: Plot and Characters")
    p.box("How do the scenes connect?", "Each scene has a job. Write one line for each scene, then ask:<br/>"
          "• Which scene <b>introduces</b> the characters?<br/>"
          "• Where does the <b>problem</b> happen?   • Where is the problem <b>solved</b>?",
          LEARN_BG, LEARN_LINE)
    p.gap(10)
    c = p.c
    bw = (CW - 3 * 14) / 4
    for k, (label, cue) in enumerate([("Scene 1", "Who? What plan?"), ("Problem", "What goes wrong?"),
                                      ("Try, try again", "What do they try?"), ("Resolution", "How is it solved?")]):
        x = MARGIN + k * (bw + 14)
        c.setStrokeColor(HELP_LINE)
        c.roundRect(x, p.y - 100, bw, 100, 6)
        c.setStrokeColor(black)
        c.setFont("Sans-Bold", 12)
        c.drawCentredString(x + bw / 2, p.y - 18, label)
        c.setFont("Sans", 9.5)
        c.setFillColor(GREY)
        c.drawCentredString(x + bw / 2, p.y - 32, cue)
        c.setFillColor(black)
        if k < 3:
            c.setFont("Sans-Bold", 16)
            c.drawCentredString(x + bw + 7, p.y - 55, "→")
    p.y -= 110
    p.box("What characters say and do", "To learn about a character, read their <b>words</b> (dialogue) "
          "and their <b>actions</b> (stage directions).<br/>"
          "<b>Choose two:</b> find each character’s name in the play. Write <b>yes</b> or <b>no</b> next to "
          "each choice. Circle the two yeses.", LEARN_BG, LEARN_LINE)
    p.gap(10)
    p.para("<b>Try it:</b> Who would <b>not</b> let Pip help? Find the proof.", 12.5)
    p.gap(6)
    p.table([["Character", "Said no to Pip?", "Proof (their words)"]] +
            [[n, "yes   no", ""] for n in ("Mia", "Leo", "Grandma Rosa")], [120, 110, CW - 230], size=12)
    p.gap(6)
    p.box("How does a character change?", "Compare what the character says at the <b>beginning</b> with what "
          "they say at the <b>end</b>. Mia at the beginning: “too heavy for you.” Mia at the end: ________",
          LEARN_BG, LEARN_LINE)


@page("Lesson: Theme and Roots")
def s_theme(p):
    """Theme vs topic, wrong-answer traps, and Latin roots."""
    p.title("Lesson: Theme and Latin Roots")
    p.box("Theme", "The <b>theme</b> is the lesson a story teaches <b>everyone</b>, not just the characters. "
          "Write it as a sentence, not one word.<br/><br/>"
          "<b>Find it:</b> Look at the ending. What did the characters learn? How was the problem solved?<br/>"
          "<b>Cross out</b> answers that:<br/>"
          "  ✗ use <b>never</b>, <b>always</b>, or <b>most</b> (too big)<br/>"
          "  ✗ are about one small part instead of the whole play<br/>"
          "  ✗ are the opposite of what happens in the play", LEARN_BG, LEARN_LINE)
    p.gap(10)
    p.para("<b>Try it:</b> Finish the sentence with the theme of “The Stuck Wagon.”", 12.5)
    p.gap(4)
    p.para("The play teaches that _________________________________________________", 12.5)
    p.lines(1)
    p.gap(14)
    p.para("<b>My Latin Roots chart</b>  A <b>root</b> is the main part of a word. Many English words come "
           "from Latin.", 12.5)
    p.gap(6)
    p.table([
        ["Root", "Means", "Words", "Your turn"],
        ["vis / vid", "see", "<b>vis</b>ion, tele<b>vis</b>ion, <b>vid</b>eo", "visible = ________"],
        ["spect", "look", "in<b>spect</b>, <b>spect</b>ator", "spectacles = ________"],
        ["aud", "hear", "<b>aud</b>ience, <b>aud</b>io", "audible = ________"],
        ["port", "carry", "<b>port</b>able, trans<b>port</b>", "porter = ________"],
        ["dict", "say", "<b>dict</b>ionary, pre<b>dict</b>", "dictate = ________"],
    ], [80, 60, 180, CW - 320], size=11, valign="MIDDLE")
    p.gap(10)
    p.box(None, "<b>Root strategy:</b> 1. Find the root. 2. Say what it means. 3. Read the sentence: "
          "which answer has that meaning <b>and</b> fits the sentence?", TIP_BG, TIP_LINE, size=11.5)


@page("Lesson: Writing About the Resolution")
def s_resolution(p):
    """ACE for the written resolution answer, with a model on a different story."""
    p.title("Lesson: Writing About the Resolution")
    p.box("Resolution", "The <b>resolution</b> is how the problem is solved at the <b>end</b> of the story. "
          "To find it, ask: What was the problem? How did it get fixed? How does the story end?",
          LEARN_BG, LEARN_LINE)
    p.gap(10)
    p.box("Write it with ACE",
          "<b>A</b> = <b>Answer</b> in a full sentence: “The resolution is…”<br/>"
          "<b>C</b> = <b>Cite</b> a detail: “In Scene __, [character] says, ‘…’” or “The narrator says…”<br/>"
          "<b>E</b> = <b>Explain</b>: “This shows the problem is solved because…”", TRY_BG, TRY_LINE)
    p.gap(14)
    p.para("<b>Model (we do together).</b> Story: Kai’s dog, Max, runs away during a storm. Kai and his dad "
           "search the park. At the end, Max is found hiding under the slide, and Kai hugs him.", 12.5)
    p.gap(6)
    p.para("<b>A:</b> The resolution is that Kai finds his dog, Max. <b>C:</b> At the end, the story says "
           "Max was “hiding under the slide, and Kai hugs him.” <b>E:</b> This shows the problem is solved "
           "because Max is not lost anymore and is safe with Kai.", 12, x=MARGIN + 20, w=CW - 20,
           color=HexColor("#204A80"))
    p.gap(14)
    p.box("Check my answer", "☐ I started with “The resolution is…”<br/>"
          "☐ I used a detail from the <b>end</b> of the play (with quotation marks if I copied words).<br/>"
          "☐ I explained how the problem got solved.<br/>"
          "☐ Capital letters, end marks, and spelling.", LEARN_BG, LEARN_LINE, size=12)


def qpage(fn):
    return page("Practice Questions")(fn)


@qpage
def s_q1(p):
    """Practice questions 1-3."""
    p.para("Use “The Stuck Wagon.” <b>Prove it:</b> find the line that shows each answer.", 12)
    p.gap(12)
    p.question(1, "How is the narrator different from the other characters?")
    p.choices(["The narrator helps pull the wagon out of the mud.",
               "The narrator tells the audience what is happening.",
               "The narrator argues with Mia and Leo.",
               "The narrator sells apples at the market."])
    p.question(2, "How are Scene 1 and Scene 2 connected?")
    p.choices(["Scene 1 tells about the market, and Scene 2 tells how apples grow.",
               "Scene 1 happens at night, and Scene 2 happens the next week.",
               "Scene 1 introduces the family and their plan, and Scene 2 shows a problem and how it is solved.",
               "Scene 1 solves the problem, and Scene 2 shows how the problem started."])
    p.question(3, "Which characters will not let Pip help? Choose <b>two</b> answers.")
    p.choices(["Narrator", "Mia", "Leo", "Grandma Rosa", "Pip"], square=True)
    hint(p, "Find each name in the play. Who tells Pip “no”?")


@qpage
def s_q2(p):
    """Practice questions 4-6."""
    p.question(4, "Read the sentence from Act 1, Scene 2.")
    p.quote("Pip did not give up. She <b>inspected</b> the wheel closely.")
    p.para("Think about the Latin root <b>spect</b>. What is the meaning of <b>inspected</b> above?", 13,
           x=MARGIN + 40, w=CW - 40)
    p.gap(8)
    p.choices(["looked at carefully", "fixed quickly", "pushed hard", "forgot about"])
    p.question(5, "What is the theme of the play?")
    p.choices(["Grown-ups are always right.", "Working together can solve big problems.",
               "Being the strongest is what matters most.", "Mud makes roads dangerous."])
    p.question(6, "Read the line from Act 1, Scene 2.")
    p.quote(stage("LEO: (scratches his head) That just might work."))
    p.para("What do the words in parentheses tell the reader?", 13, x=MARGIN + 40, w=CW - 40)
    p.gap(8)
    p.choices(["what Leo says out loud", "what Leo does", "where the scene takes place",
               "what the narrator thinks"])


@qpage
def s_q3(p):
    """Practice questions 7-8."""
    p.question(7, "What is the resolution of the play? Use details from the play to support your answer. "
                  "Use ACE.")
    p.lines(6)
    p.gap(20)
    p.question(8, "How does Mia change from the beginning to the end of the play?")
    p.choices(["At first she is happy, and at the end she is angry.",
               "At first she wants to sell apples, and at the end she wants to go home.",
               "At first she helps Pip, and at the end she will not help Pip.",
               "At first she says Pip is too little to help, and at the end she says sorry for not listening."])
    p.gap(6)
    p.box("Check my work", "☐ I answered every question.<br/>"
          "☐ I found the line in the play that proves each answer.<br/>"
          "☐ I circled <b>two</b> letters for “Choose two.”<br/>"
          "☐ My written answer starts with “The resolution is…” and uses a detail.<br/>"
          "☐ I went back to every question with a star ★.", LEARN_BG, LEARN_LINE, size=12)


@page("Lesson: Quotation Marks")
def s_quotes(p):
    """Rules for punctuating dialogue."""
    p.title("Lesson: Quotation Mark Rules", "Quotation marks “ ” go around the exact words someone says.")
    rules = [
        ("Capital letter", "The first spoken word starts with a capital letter.",
         "She asked, “<b>W</b>here is my hat?”"),
        ("Speaker first", "Put a comma after <i>said</i> or <i>asked</i>, before the first quotation mark.",
         "Dad said<b>,</b> “Time for dinner.”"),
        ("Speaker last", "Put a comma <b>inside</b> the closing quotation mark.",
         "“Time for dinner<b>,</b>” Dad said."),
        ("? and !", "Question marks and exclamation points go <b>inside</b>. No comma needed.",
         "“Watch out<b>!</b>” yelled Max."),
        ("Only the spoken words", "<i>said Max</i> or <i>I said</i> stays <b>outside</b> the quotation marks.",
         "“I love pizza<b>!</b>” said Max.   ✗ “I love pizza! said Max.”"),
    ]
    p.table([["Rule", "What to do", "Example"]] + [[a, b, cc] for a, b, cc in rules],
            [120, 210, CW - 330], size=11.5, valign="MIDDLE")
    p.gap(12)
    p.box(None, "<b>Hug the words!</b> The quotation marks hug the spoken words, and the punctuation that "
          "goes with them (, ? !) stays inside the hug.", TIP_BG, TIP_LINE, size=12.5)
    p.gap(14)
    p.para("<b>Try it:</b> Fix each sentence. Add quotation marks, commas, and capitals.", 12.5)
    p.gap(4)
    for t in ("1.  I am hungry said Leo.", "2.  Mom asked are you ready?", "3.  Look at that rainbow! yelled Pip.",
              "4.  Ava said my dog is brown."):
        p.gap(6)
        p.para(t, 13)
        p.lines(1, gap=22)


@page("Practice: Editing")
def s_paper(p):
    """Practice paper with dialogue errors (same format as the writing test)."""
    p.para("Sam wrote a paper about the new class pet. Read Sam’s paper and look for changes he should "
           "make. Then answer the questions.", 12)
    p.gap(6)
    p.para("Our Class Pet", 15, bold=True, align=1)
    p.gap(4)
    p.box(None, "(1) Yesterday our teacher, Mr. Lopez, brought a hamster to class. (2) Everyone crowded "
          "around the cage. (3) Mr. Lopez asked what should we name him?<br/><br/>"
          "(4) “Let’s call him Peanut” Ava said.<br/><br/>"
          "(5) Wow, that is a great name! said Mr. Lopez. (6) We all cheered. (7) “I will help feed him,” "
          "said Leo. (8) Now Peanut is the best part of my day.", HELP_BG, HELP_LINE, size=12.5)
    p.gap(12)
    p.question("W1", "What is the correct way to write sentence 3?", size=12)
    p.choices(["Mr. Lopez asked, “what should we name him?”", "Mr. Lopez asked, “What should we name him?”",
               "Mr. Lopez asked, “What should we name him”?", "No change is needed."], size=12)
    p.question("W2", "What is the correct way to write sentence 4?", size=12)
    p.choices(["“Let’s call him Peanut” Ava, said.", "“Let’s call him Peanut” Ava said,",
               "“Let’s call him Peanut,” Ava said.", "No change is needed."], size=12)


@page("Practice: Editing")
def s_paper_2(p):
    """Practice paper questions W3-W4."""
    p.question("W3", "What is the correct way to write sentence 5?", size=12)
    p.choices(["“Wow, that is a great name!” said Mr. Lopez.", "“Wow, that is a great name! said Mr. Lopez.”",
               "“Wow, that is a great name! said” Mr. Lopez.", "No change is needed."], size=12)
    p.question("W4", "What is the correct way to write sentence 7?", size=12)
    p.choices(["“I will help feed him” said Leo.", "“I will help feed him, said Leo.”",
               "“I will help feed him,” said, Leo.", "No change is needed."], size=12)
    p.gap(6)
    p.box("How I answer editing questions", "1. Find the sentence <b>number</b> in the paper.<br/>"
          "2. Point to the <b>spoken words</b>. Do the quotation marks hug only those words?<br/>"
          "3. Check: capital first word? Comma or ? ! <b>inside</b> the hug? Comma after <i>said</i> or "
          "<i>asked</i> when the speaker comes first?<br/>"
          "4. If the sentence already follows every rule, choose <b>No change is needed</b>.",
          LEARN_BG, LEARN_LINE, size=12)


@page("Test Day Bookmarks", name=False)
def s_bookmarks(p):
    """Three cut-out bookmarks with the test plan."""
    from module3_test_preview import Paragraph, style
    p.para("Cut out a bookmark. Keep it next to you while you practice.", 12, color=GREY)
    p.gap(10)
    bw = (CW - 2 * 16) / 3
    bh = 560
    c = p.c
    text = ("<b>MY PLAY PLAN</b><br/><br/>"
            "<b>1 PEEK</b><br/>title, Characters list<br/><br/>"
            "<b>2 PREVIEW</b><br/>read the questions first<br/><br/>"
            "<b>3 SCENE BY SCENE</b><br/>who? what problem?<br/><br/>"
            "<b>4 UNDERLINE</b><br/>Scene 1, Scene 2, two, theme<br/><br/>"
            "<b>5 PROVE IT</b><br/>find the name, read the line<br/><br/>"
            "<b>6 CROSS OUT</b><br/>✗ wrong answers, pick the best<br/><br/>"
            "<b>Words to know</b><br/>narrator = talks to audience<br/>( ) = what they do<br/>"
            "resolution = how it’s solved<br/>theme = lesson for all<br/><br/>"
            "<b>Roots</b><br/>vis = see • spect = look<br/><br/>"
            "<b>Quotes</b><br/>Hug the words!<br/>, ? ! go inside “ ”")
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


PAGES = [t_overview, t_plan, t_map, t_key, s_plan, s_decoder, s_parts, s_play_1, s_play_2, s_plot, s_theme,
         s_resolution, s_q1, s_q2, s_q3, s_quotes, s_paper, s_paper_2, s_bookmarks]

if __name__ == "__main__":
    main("G3_M4_Wk3_Reading_Test_Preview.pdf", PAGES, "Grade 3 Module 4 Week 3 Assessment Preview")
