// "Little League Champs": data for the text-only fluency kit.
// Level 3 is the original article. " / " marks a short pause and " // " the end of a sentence
// (shown only on the phrase-cued page; the plain page strips them, so both pages are the same text).
const STORY = {
  title: 'Little League Champs',

  l1: {
    title: 'The Big Win',
    paras: [
      'The Tigers had a big game. If they won, they would be the champs!',
      'Casey was the Tigers’ pitcher. At the start, the Hawks did not get a hit. The Tigers got 3 runs. The Hawks had 0.',
      'Then Casey had a bad inning. The Hawks hit the ball far. It was a home run! Now it was 3 to 3.',
      'The two teams got more runs. Then it was 6 to 6. It was the last inning.',
      'Tyler got up to bat. Coach Martin said, “You can do it!” Tyler swung. Miss! He swung again. Miss!',
      'Tyler was upset. If he did not get a hit, the Tigers might not win.',
      'Then Tyler hit the ball. Smack! It went up, up, and out of the park. A home run!',
      'The Tigers won, 7 to 6! Casey’s gran said, “It was the best win yet!”',
      '“Will you win next year?” “You bet we will!” said the kids.',
    ],
    questions: [
      'Who won the big game?',
      'What was the score at the end?',
      'What happened in Casey’s bad inning?',
      'How did Tyler feel when he missed the ball?',
      'What did Tyler do to win the game?',
    ],
  },

  l2: {
    title: 'Little League Champs',
    chunk: ['Tra|vis|town', 'Har|ris|burg', 'Sat|ur|day', 'in|nings', 'ner|vous'],
    paras: [
      'The Travistown Tigers won the Little League big game last Saturday. They beat the Harrisburg Hawks. The final score was 7 to 6.',
      '“I have never seen a game like it!” said Martha Nessbaum. She is the grandma of Casey Nessbaum, the Tigers’ pitcher.',
      'The players told us about the win.',
      '“At first I thought it would be an easy win,” said Casey. “The Hawks did not get a hit for two innings. We were ahead 3 to 0. Then, in the fourth inning, I threw some bad pitches. I walked two players. Then the Hawks hit a home run. It was 3 to 3.”',
      'Tyler Martin made the winning run. “The game was close until the end,” he said. “In the last inning, the score was tied, and we had two outs. It was my turn to bat. Coach Martin gave me some tips. Then I ran out to home plate. I was so nervous! I missed the first two pitches. I knew if I struck out, we might not win.”',
      'Then Tyler hit a home run! The Tigers won!',
      '“I am so proud of all the players,” said Coach Eric Daly.',
      'Will the Tigers win again next year? “You bet we will!” they said.',
    ],
  },

  l3: {
    title: 'Little League Champs',
    pageBreak: 4,
    paras: [
      'The Travistown Tigers / became Little League regional champions / this past Saturday. // They won their final game / in a showdown / against the Harrisburg Hawks / with a final score of 7-6. //',
      '“I’ve never seen anything like it. // It was a one-in-a-million finish!” / said Martha Nessbaum, / proud grandmother / of Tigers’ pitcher, / Casey Nessbaum. //',
      'When asked to describe the win, / Tigers teammates / had the following to say: //',
      '“At first / I thought it’d be an easy win,” / said Casey Nessbaum. // “I’d pitched two no-hit innings. // We were ahead / three to zero. // But I couldn’t keep it up. // In the fourth inning / I threw some pitches / that should’ve been strikes. // I walked two players. // Then the Hawks hit a home run / and we were tied / three to three.” //',
      'Second baseman Tyler Martin / made the winning run. // When asked about it / he said, / “We’d been neck and neck / for the second half of the game. // In the bottom of the ninth / we were tied / with two outs. // There weren’t any players on base. // It was my turn to hit. // Coach Martin was beside me / in the dugout. // He gave me some pointers. // Then I ran out to home plate. // The whole team / was depending on me. // Boy, / was I nervous! // Maybe that’s why / my first two swings / were strikes. // I knew / if I struck out, / there was a chance / we wouldn’t win.” // Tyler Martin’s next swing / was the home run / that brought the Tigers to victory. //',
      'Coach Eric Daly said, / “I couldn’t be happier. // I’m so proud / of all the players.” //',
      'When asked / if they’d return / to win next year’s championship, / Tigers players said, / “You bet we will!” //',
    ],
  },

  questions: [
    'Who won the championship, and what was the final score?',
    'Why did Casey think it would be an easy win? What changed in the fourth inning?',
    'What does “neck and neck” mean? Which words help you figure it out?',
    'How did Tyler feel when he was at bat? Find two clues in the text.',
    'Why do you think the writer included quotes from the players and the coach?',
  ],

  wordBox: [
    ['inning', 'One part of a baseball game. A game has 9 innings.'],
    ['pitcher', 'The player who throws the ball to the batter.'],
    ['strike', 'A pitch the batter misses. Three strikes and you are out.'],
    ['walked', 'The batter gets to go to first base after 4 bad pitches.'],
    ['no-hit innings', 'Innings when the other team got no hits.'],
    ['home run', 'A hit that lets the batter run all the way around the bases.'],
    ['dugout', 'The bench where the team sits.'],
    ['bottom of the ninth', 'The second half of the last inning.'],
    ['neck and neck', 'Very close. Almost tied.'],
    ['one-in-a-million', 'Very rare and special.'],
    ['You bet!', 'Yes, for sure!'],
  ],

  warm: {
    steps: [
      ['Short vowel<br>words',      ['win', 'bat', 'hit']],
      ['More short<br>vowels',      ['ran', 'got', 'big', 'up']],
      ['Blends',                    ['last', 'swung', 'best', 'plan']],
      ['Digraphs<br>th • ch • tch', ['then', 'that', 'with', 'pitch']],
      ['Endings',                   ['walked', 'pitched', 'players', 'swings']],
      ['Chunk it!',                 ['in|ning', 'pitch|er', 'Sat|ur|day', 'ner|vous']],
      ['Power<br>words',            ['re|gion|al', 'vic|to|ry', 'de|pend|ing']],
    ],
    phrases: [
      ['run', 'home run', 'hit a home run', 'Then the Hawks', 'hit a home run.'],
      ['ninth', 'the ninth', 'bottom of the ninth', 'In the bottom of the ninth', 'we were tied.'],
      ['proud', 'so proud', 'I am so proud', 'I am so proud', 'of all the players.'],
    ],
    tap: 'b-a-t → bat',
    chunk: 'in • ning',
  },

  power: [
    ['regional', 're • gion • al', 'Having to do with one area, or part of a state.', '“…became Little League regional champions…”'],
    ['champions', 'cham • pi • ons', 'The winners of a contest.', '“…regional champions this past Saturday.”'],
    ['showdown', 'show • down', 'The big, final contest that decides who wins.', '“They won their final game in a showdown…”'],
    ['describe', 'de • scribe', 'To tell what something was like.', '“When asked to describe the win…”'],
    ['teammates', 'team • mates', 'People who play on the same team.', '“…Tigers teammates had the following to say.”'],
    ['depending', 'de • pend • ing', 'Counting on someone.', '“The whole team was depending on me.”'],
    ['nervous', 'ner • vous', 'Worried or scared about what will happen.', '“Boy, was I nervous!”'],
    ['victory', 'vic • to • ry', 'A win.', '“…the home run that brought the Tigers to victory.”'],
  ],

  home: {
    intro: 'This week we are reading <b>Little League Champs</b>, a news article about a baseball team that wins a big game.',
    cvcEx: 'bat',
    boxName: 'Baseball Words & Sayings',
    bonus: 'Read the plain ★★★ article out loud like a sports reporter on the news!',
  },
};
