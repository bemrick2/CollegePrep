// Original practice-question fixtures for demo mode.
//
// Every item here was written for this app. None is copied or adapted from a
// released ACT or SAT form. Items follow the style of the current tests
// (ACT enhanced 2025: English, Math, Reading, optional Science; digital SAT:
// Reading and Writing, Math) and each has exactly one correct answer.
//
// English items show the underlined portion in [brackets].

import type { Choice, ExamFamily, Skill, Strategy, TrapType } from '../types'

export interface FixtureQuestion {
  id: string
  exam_family: ExamFamily
  /** ACT: 'english' | 'math' | 'reading' | 'science'; SAT: 'reading_writing' | 'math' */
  section: string
  difficulty: 1 | 2 | 3 | 4 | 5
  stem: string
  passage?: string
  choices: Choice[]
  answer_format: 'choice' | 'numeric'
  accepted_answers: string[]
  expected_time_seconds: number
  primary_skill_key: string
  hints: string[]
  teaching_explanation: string
  strategy_explanation: string
  remember: string
  distractors: { choice: string; rationale: string; trap: string | null }[]
  strategies: { strategy_key: string; role: 'primary' | 'secondary'; is_fastest: boolean; explanation: string }[]
}

// ---------------------------------------------------------------------------
// Taxonomy
// ---------------------------------------------------------------------------

function skill(exam_family: ExamFamily, section: string, domain: string | null, skill_key: string, name: string): Skill {
  return { id: `sk-${skill_key}`, exam_family, section, domain, skill_key, name }
}

export const SKILLS: Skill[] = [
  // ACT English
  skill('act', 'english', 'conventions_of_standard_english', 'act_punctuation', 'Punctuation'),
  skill('act', 'english', 'conventions_of_standard_english', 'act_sentence_structure', 'Sentence Structure'),
  skill('act', 'english', 'conventions_of_standard_english', 'act_usage', 'Usage and Agreement'),
  skill('act', 'english', 'production_of_writing', 'act_rhetorical_skills', 'Rhetorical Skills'),
  // ACT Math
  skill('act', 'math', 'preparing_for_higher_math', 'act_algebra_linear', 'Linear Equations and Systems'),
  skill('act', 'math', 'preparing_for_higher_math', 'act_functions', 'Functions'),
  skill('act', 'math', 'preparing_for_higher_math', 'act_geometry', 'Geometry and Trigonometry'),
  skill('act', 'math', 'preparing_for_higher_math', 'act_statistics_probability', 'Statistics and Probability'),
  skill('act', 'math', 'integrating_essential_skills', 'act_number_quantity', 'Number, Ratio, and Percent'),
  // ACT Reading
  skill('act', 'reading', 'key_ideas_and_details', 'act_main_idea', 'Main Idea and Details'),
  skill('act', 'reading', 'key_ideas_and_details', 'act_inference', 'Inference'),
  skill('act', 'reading', 'craft_and_structure', 'act_vocabulary_in_context', 'Vocabulary in Context'),
  skill('act', 'reading', 'craft_and_structure', 'act_author_purpose', "Author's Purpose and Technique"),
  // ACT Science
  skill('act', 'science', 'interpretation_of_data', 'act_data_interpretation', 'Data Interpretation'),
  skill('act', 'science', 'scientific_investigation', 'act_experiment_design', 'Experimental Design'),
  skill('act', 'science', 'evaluation_of_models', 'act_conflicting_viewpoints', 'Conflicting Viewpoints'),
  // SAT Reading and Writing
  skill('sat', 'reading_writing', 'craft_and_structure', 'sat_craft_structure', 'Craft and Structure'),
  skill('sat', 'reading_writing', 'information_and_ideas', 'sat_information_ideas', 'Information and Ideas'),
  skill('sat', 'reading_writing', 'standard_english_conventions', 'sat_standard_english', 'Standard English Conventions'),
  skill('sat', 'reading_writing', 'expression_of_ideas', 'sat_expression_of_ideas', 'Expression of Ideas'),
  // SAT Math
  skill('sat', 'math', 'algebra', 'sat_algebra', 'Algebra'),
  skill('sat', 'math', 'advanced_math', 'sat_advanced_math', 'Advanced Math'),
  skill('sat', 'math', 'problem_solving_data_analysis', 'sat_problem_solving_data', 'Problem-Solving and Data Analysis'),
  skill('sat', 'math', 'geometry_trigonometry', 'sat_geometry_trig', 'Geometry and Trigonometry'),
]

export const STRATEGIES: Strategy[] = [
  { strategy_key: 'backsolve', name: 'Backsolve', description: 'Test the answer choices in the problem, starting with a middle value, until one works.' },
  { strategy_key: 'plug_in_numbers', name: 'Plug In Numbers', description: 'Replace variables with simple numbers so an abstract question becomes arithmetic.' },
  { strategy_key: 'predict_then_match', name: 'Predict, Then Match', description: 'Form your own answer before reading the choices, then pick the closest match.' },
  { strategy_key: 'process_of_elimination', name: 'Process of Elimination', description: 'Cross out choices with a clear flaw; the survivor is your answer.' },
  { strategy_key: 'read_question_first', name: 'Read the Question First', description: 'Know exactly what is being asked before diving into the passage or data.' },
  { strategy_key: 'concise_is_correct', name: 'Concise Is Correct', description: 'When choices are all grammatical, the shortest clear one is usually best.' },
  { strategy_key: 'find_the_trend', name: 'Find the Trend', description: 'Describe how one variable changes as another changes before answering.' },
  { strategy_key: 'translate_to_algebra', name: 'Translate to Algebra', description: 'Turn the words into an equation one phrase at a time, then solve.' },
  { strategy_key: 'locate_evidence', name: 'Locate the Evidence', description: 'Go back to the exact lines or table row that answer the question.' },
  { strategy_key: 'draw_it_out', name: 'Draw It Out', description: 'Sketch the figure or situation and label what you know.' },
]

export const TRAPS: TrapType[] = [
  { trap_key: 'partial_answer', name: 'Partial Answer', description: 'A value from a middle step, not the quantity the question asks for.' },
  { trap_key: 'wrong_quantity', name: 'Wrong Quantity', description: 'A correct calculation of something other than what was asked.' },
  { trap_key: 'sign_error', name: 'Sign Error', description: 'The result of dropping or flipping a negative sign.' },
  { trap_key: 'extreme_language', name: 'Extreme Language', description: 'Words like always, only, or never that go further than the text supports.' },
  { trap_key: 'true_but_irrelevant', name: 'True but Irrelevant', description: 'An accurate statement that does not answer the question asked.' },
  { trap_key: 'out_of_scope', name: 'Out of Scope', description: 'A claim the passage never makes or supports.' },
  { trap_key: 'wordy_redundant', name: 'Wordy or Redundant', description: 'Grammatical, but repeats an idea or uses more words than needed.' },
  { trap_key: 'misread_graph', name: 'Misread Data', description: 'Reading the wrong row, column, or axis of a table or graph.' },
  { trap_key: 'overextend_trend', name: 'Overextended Trend', description: 'Assuming a pattern keeps going the same way beyond the data.' },
  { trap_key: 'comma_splice', name: 'Comma Splice', description: 'Two complete sentences joined with only a comma (or nothing at all).' },
  { trap_key: 'wrong_transition', name: 'Wrong Transition', description: 'A transition word whose logic does not match the relationship between ideas.' },
  { trap_key: 'misplaced_modifier', name: 'Misplaced Modifier', description: 'An introductory phrase that ends up describing the wrong noun.' },
  { trap_key: 'nearest_noun_agreement', name: 'Nearest-Noun Agreement', description: 'Matching the verb to a nearby noun instead of the true subject.' },
  { trap_key: 'familiar_meaning', name: 'Familiar Meaning', description: "A word's most common meaning, which does not fit this context." },
]

// ---------------------------------------------------------------------------
// Shared passages
// ---------------------------------------------------------------------------

/** Show only underline number `n` in brackets; other underline markers become plain text. */
function underline(template: string, n: number): string {
  return template.replace(/\{\{(\d+)\|([^}]*)\}\}/g, (_m, k: string, text: string) =>
    Number(k) === n ? `[${text}]` : text,
  )
}

const EN_GARDEN =
  "When the empty lot on Fifth Street finally became a community garden, nobody expected the tomatoes to be the stars. {{1|The neighbors, who had argued for months about what to plant,}} agreed at last on a simple plan: each family would tend one raised bed. By July, the beds were {{2|overflowing, the tomato vines}} had climbed past the fences. Mrs. Okafor, whose porch faced the garden, began leaving baskets of extra tomatoes on the library steps. Soon the library started a recipe exchange, and the garden became the place where neighbors who had never spoken to one another {{3|traded}} advice about compost and salsa."

const EN_MONARCH =
  "Every September, students at Lakeview Middle School join a science project that stretches across a continent. {{1|Using tiny adhesive tags, the students mark monarch butterflies}} before the insects begin their long migration south to Mexico. Each tag carries a unique code, and anyone who later finds a tagged butterfly can report that code online. {{2|However,}} scientists can map the routes the monarchs traveled. Reports from volunteers across North America {{3|has revealed}} that some monarchs fly up to 3,000 miles to reach their winter home. {{4|The students find this fact to be extremely amazing and very surprising to them.}}"

const EN_SEEDS =
  "[1] Over a decade ago, a small public library began lending something unusual: seeds. [2] Patrons could check out packets of three kinds of {{1|seeds: bean,}} squash, and pepper. [3] They planted the seeds at home and later returned seeds saved from their own harvests. [4] The idea spread quickly, and today hundreds of libraries host similar collections. [5] Librarians say the programs teach patrons about local plant varieties, many of which are not sold in stores. [6] Because returned seeds come from plants that thrived in local soil, each new generation of the collection is a little better suited to the region's climate."

const RD_WATCH =
  "Grandpa Teo kept his watch repair shop open long after anyone in town wore a watch that needed winding. The bell above the door rang perhaps twice a week, usually for a battery or a broken strap. Still, every morning at seven he unlocked the door, wiped the glass counter, and laid out his tools in the same order: tweezers, loupe, the tiny screwdrivers with their worn red handles.\n\nThe summer I turned fourteen, I asked him why he bothered. He didn't answer right away. He lifted a pocket watch from the drawer, its case dented, its hands frozen at 4:10. 'Mrs. Albrecht brought this in eleven years ago,' he said. 'It was her husband's. She said she would come back for it when she was ready.' He set it gently on the felt. 'Somebody has to be here when she is.'"

const RD_HEAT =
  "On a summer afternoon, the center of a large city can be several degrees warmer than the farmland around it. Scientists call this an urban heat island. Dark surfaces such as asphalt and rooftops absorb sunlight during the day and release that heat slowly after sunset, so cities often stay warm well into the night. Buildings also block breezes that might otherwise carry heat away.\n\nSome cities are experimenting with remedies. Light-colored 'cool roofs' reflect more sunlight than dark shingles do, and street trees shade pavement while releasing water vapor that cools the surrounding air. These measures are not cures; a city of concrete will never be as cool as a meadow. But researchers note that even modest reductions in nighttime temperatures can matter, because people's bodies recover from daytime heat during the cooler hours of the night."

const RD_JAZZ =
  "Many people assume that improvisation in jazz means playing whatever comes to mind. Musicians tend to describe it differently. Before a solo, a player has usually spent years absorbing scales, chord patterns, and the phrases of earlier artists, sometimes copying recordings note for note. The solo itself may be invented in the moment, but it is built from that stored vocabulary, much as a fluent speaker invents new sentences from familiar words.\n\nThis is why two performances of the same tune by the same musician can sound strikingly different and yet unmistakably hers. The freedom listeners hear is real, but it rests on a discipline they do not hear: the hours of practice that make spontaneous choices possible."

const SCI_LIGHT =
  "Students grew bean seedlings under lamps of five different light intensities. All seedlings received the same amount of water and were kept at 22°C. After 14 days, the students measured the average height of the seedlings in each group.\n\nTable 1\nLight intensity (lux) | Average height (cm)\n1,000 | 4.2\n2,000 | 7.9\n4,000 | 12.6\n8,000 | 14.1\n16,000 | 14.3"

const SCI_PENDULUM =
  "A student studied the period of a pendulum (the time for one complete back-and-forth swing). In each trial, the student released the bob, timed 10 complete swings with a stopwatch, and divided by 10.\n\nExperiment 1: Bob mass 50 g, release angle 10°; string length varied.\nLength (cm) | Period (s)\n25 | 1.0\n50 | 1.4\n100 | 2.0\n\nExperiment 2: String length 100 cm, release angle 10°; bob mass varied.\nMass (g) | Period (s)\n50 | 2.0\n100 | 2.0\n200 | 2.0"

const SCI_ALGAE =
  "Each late summer, Lake Marlow develops large algae blooms that turn the water green. Two students explain the cause.\n\nStudent 1: The blooms are caused mainly by fertilizer runoff from nearby farms. Fertilizer adds phosphorus to the water, and algae growth in the lake is limited by the amount of phosphorus available. Blooms should be largest after heavy rains, which wash fertilizer into the lake.\n\nStudent 2: The blooms are caused mainly by rising water temperature. Warm, still water allows algae near the surface to multiply quickly whether or not extra phosphorus is present. Blooms should be largest during long stretches of hot, calm weather, even with no rain."

const NO_CHANGE = 'NO CHANGE'

// ---------------------------------------------------------------------------
// Questions
// ---------------------------------------------------------------------------

const ACT_ENGLISH: FixtureQuestion[] = [
  {
    id: 'act-english-01',
    exam_family: 'act',
    section: 'english',
    difficulty: 1,
    passage: underline(EN_GARDEN, 3),
    stem: 'Which choice is best for the bracketed portion?',
    choices: [
      { key: 'A', text: NO_CHANGE },
      { key: 'B', text: 'trades' },
      { key: 'C', text: 'trading' },
      { key: 'D', text: 'has traded' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 30,
    primary_skill_key: 'act_usage',
    hints: [
      'Find the subject of the verb. Who is doing the trading?',
      'Check that the verb matches both the subject (singular or plural) and the past-tense story.',
    ],
    teaching_explanation:
      "The subject is 'neighbors,' which is plural, and the passage tells its story in the past tense ('became,' 'began'). 'Traded' works with a plural subject and keeps the tense consistent, so no change is needed.",
    strategy_explanation:
      "Strip the sentence down to 'neighbors ... traded advice.' If it sounds right in its simplest form, keep it.",
    remember: 'Strip the sentence to subject plus verb, then listen.',
    distractors: [
      { choice: 'B', rationale: "'Trades' is singular and present tense; 'neighbors' is plural and the story is in the past.", trap: null },
      { choice: 'C', rationale: "'Trading' is not a complete verb on its own, so the clause has no main verb.", trap: null },
      { choice: 'D', rationale: "'Has traded' is singular, which does not match the plural subject 'neighbors.'", trap: null },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'Eliminate every choice that is singular or not a full verb; only NO CHANGE survives.' },
    ],
  },
  {
    id: 'act-english-02',
    exam_family: 'act',
    section: 'english',
    difficulty: 2,
    passage: underline(EN_GARDEN, 2),
    stem: 'Which choice is best for the bracketed portion?',
    choices: [
      { key: 'A', text: NO_CHANGE },
      { key: 'B', text: 'overflowing; the tomato vines' },
      { key: 'C', text: 'overflowing the tomato vines' },
      { key: 'D', text: 'overflowing, and, the tomato vines' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 36,
    primary_skill_key: 'act_sentence_structure',
    hints: [
      'Cover the bracketed punctuation. Could each side stand alone as a sentence?',
      'Two complete sentences need more than a comma between them.',
    ],
    teaching_explanation:
      "'By July, the beds were overflowing' and 'the tomato vines had climbed past the fences' are both independent clauses. A semicolon is one correct way to join two independent clauses; a comma alone is not.",
    strategy_explanation:
      'When choices differ only in punctuation between two clauses, test whether both sides are complete sentences. If so, look for a period, semicolon, or comma plus FANBOYS conjunction.',
    remember: 'Complete + complete needs a semicolon, period, or comma plus and/but/so.',
    distractors: [
      { choice: 'A', rationale: 'A comma alone between two complete sentences creates a comma splice.', trap: 'comma_splice' },
      { choice: 'C', rationale: 'With no punctuation at all, the two sentences run together (a fused sentence).', trap: 'comma_splice' },
      { choice: 'D', rationale: "The comma after 'and' is misplaced; it interrupts the conjunction from the clause it introduces.", trap: null },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'Spot that both sides are complete sentences, then eliminate the comma-only and no-punctuation choices.' },
    ],
  },
  {
    id: 'act-english-03',
    exam_family: 'act',
    section: 'english',
    difficulty: 2,
    passage: underline(EN_MONARCH, 4),
    stem: 'Which choice is best for the bracketed portion?',
    choices: [
      { key: 'A', text: NO_CHANGE },
      { key: 'B', text: 'The students find this fact amazing.' },
      { key: 'C', text: 'The students, amazed, find this fact amazing.' },
      { key: 'D', text: 'This is a fact that the students find to be amazing and surprising.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 30,
    primary_skill_key: 'act_rhetorical_skills',
    hints: [
      'All four choices say roughly the same thing. Which says it most directly?',
      "Look for words that repeat an idea already expressed ('amazing' and 'surprising,' 'to them').",
    ],
    teaching_explanation:
      "Choice B communicates the full idea with no repeated words. 'Extremely amazing,' 'very surprising,' and 'to them' add length without adding meaning, since 'the students find' already tells us whose reaction it is.",
    strategy_explanation:
      'When every option is grammatical and means the same thing, choose the shortest one that keeps the meaning.',
    remember: 'Same meaning, fewer words: concise wins.',
    distractors: [
      { choice: 'A', rationale: "'To them' repeats 'the students,' and 'amazing' and 'surprising' overlap in meaning.", trap: 'wordy_redundant' },
      { choice: 'C', rationale: "'Amazed' and 'amazing' say the same thing twice.", trap: 'wordy_redundant' },
      { choice: 'D', rationale: "'This is a fact that ... find to be' is a roundabout way of saying the same thing.", trap: 'wordy_redundant' },
    ],
    strategies: [
      { strategy_key: 'concise_is_correct', role: 'primary', is_fastest: true, explanation: 'B is the shortest choice and loses no meaning.' },
    ],
  },
  {
    id: 'act-english-04',
    exam_family: 'act',
    section: 'english',
    difficulty: 3,
    passage: EN_GARDEN.replace(/\{\{\d+\|([^}]*)\}\}/g, '$1'),
    stem:
      "The writer is considering adding the following sentence right after the sentence about Mrs. Okafor's baskets:\n\n'Tomatoes are botanically classified as fruits, not vegetables.'\n\nShould the writer make this addition?",
    choices: [
      { key: 'A', text: 'Yes, because it provides interesting scientific background about the garden’s most successful crop.' },
      { key: 'B', text: 'Yes, because it explains why the tomatoes grew better than the other plants.' },
      { key: 'C', text: 'No, because it distracts from the paragraph’s focus on how the garden brought neighbors together.' },
      { key: 'D', text: 'No, because it contradicts the earlier claim that the tomatoes were the stars of the garden.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 40,
    primary_skill_key: 'act_rhetorical_skills',
    hints: [
      'In one phrase, what is this paragraph about?',
      'Does the new sentence move that main point forward?',
    ],
    teaching_explanation:
      'The paragraph traces how the garden connected neighbors: shared beds, baskets of produce, a recipe exchange. A botany fact about tomatoes may be true, but it does not advance that story, so it should be left out.',
    strategy_explanation:
      "Decide yes or no first by asking 'Does this fit the paragraph’s focus?' Then pick the choice with the matching reason.",
    remember: 'True is not enough; the sentence must serve the paragraph’s focus.',
    distractors: [
      { choice: 'A', rationale: 'The fact is accurate and mildly interesting, but it pulls attention away from the neighbors.', trap: 'true_but_irrelevant' },
      { choice: 'B', rationale: 'Being classified as a fruit says nothing about why the plants grew well.', trap: 'out_of_scope' },
      { choice: 'D', rationale: 'Calling tomatoes fruits does not contradict anything; the reason given is false.', trap: null },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Predict "No, it is off topic," then match to C.' },
      { strategy_key: 'process_of_elimination', role: 'secondary', is_fastest: false, explanation: 'Check each reason against the passage; B and D make claims the text does not support.' },
    ],
  },
  {
    id: 'act-english-05',
    exam_family: 'act',
    section: 'english',
    difficulty: 3,
    passage: underline(EN_GARDEN, 1),
    stem: 'Which choice is best for the bracketed portion?',
    choices: [
      { key: 'A', text: NO_CHANGE },
      { key: 'B', text: 'The neighbors who had argued for months about what to plant,' },
      { key: 'C', text: 'The neighbors, who had argued for months, about what to plant' },
      { key: 'D', text: 'The neighbors, who had argued for months about what to plant' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 36,
    primary_skill_key: 'act_punctuation',
    hints: [
      'Try reading the sentence without the who-clause. Does the sentence still make sense?',
      'Extra information set off from the sentence needs a matching pair of commas.',
    ],
    teaching_explanation:
      "'Who had argued for months about what to plant' is extra information about the neighbors, so it is set off by a pair of commas, one before and one after. Removing it leaves 'The neighbors agreed at last on a simple plan,' a complete sentence.",
    strategy_explanation:
      'For a clause in the middle of a sentence, check for comma pairs: two commas or none. One lonely comma is almost always wrong.',
    remember: 'Extra info in the middle? Commas come in pairs.',
    distractors: [
      { choice: 'B', rationale: "With only a closing comma, a single comma now separates the subject 'neighbors' from its verb 'agreed.'", trap: null },
      { choice: 'C', rationale: "The second comma splits 'argued for months' from 'about what to plant,' which belong together.", trap: null },
      { choice: 'D', rationale: 'The opening comma has no partner, so the extra information is never closed off.', trap: null },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'Remove any choice with an unpaired comma; only A has a complete pair around the full clause.' },
    ],
  },
  {
    id: 'act-english-06',
    exam_family: 'act',
    section: 'english',
    difficulty: 3,
    passage: underline(EN_MONARCH, 2),
    stem: 'Which choice is best for the bracketed portion?',
    choices: [
      { key: 'A', text: NO_CHANGE },
      { key: 'B', text: 'Using these reports,' },
      { key: 'C', text: 'Nevertheless,' },
      { key: 'D', text: 'In contrast,' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 36,
    primary_skill_key: 'act_rhetorical_skills',
    hints: [
      'How is the sentence about mapping routes related to the sentence before it: contrast, or cause and effect?',
      'What makes it possible for scientists to map the routes?',
    ],
    teaching_explanation:
      "The previous sentence explains that people report tag codes online; the next explains that scientists map routes. The reports make the mapping possible, so the connection is one of building on, not contrast. 'Using these reports' states that link directly.",
    strategy_explanation:
      'Cover the transition, decide the relationship between the two sentences in your own words, then pick the choice that matches.',
    remember: 'Name the relationship first, then choose the transition.',
    distractors: [
      { choice: 'A', rationale: "'However' signals contrast, but the second sentence follows from the first.", trap: 'wrong_transition' },
      { choice: 'C', rationale: "'Nevertheless' means 'in spite of that,' but nothing here is being overcome.", trap: 'wrong_transition' },
      { choice: 'D', rationale: "'In contrast' sets up an opposing idea that never appears.", trap: 'wrong_transition' },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Predict "because of these reports," then match it to B.' },
    ],
  },
  {
    id: 'act-english-07',
    exam_family: 'act',
    section: 'english',
    difficulty: 3,
    passage: underline(EN_SEEDS, 1),
    stem: 'Which choice is best for the bracketed portion?',
    choices: [
      { key: 'A', text: NO_CHANGE },
      { key: 'B', text: 'seeds; bean,' },
      { key: 'C', text: 'seeds, such as: bean,' },
      { key: 'D', text: 'seeds bean,' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 36,
    primary_skill_key: 'act_punctuation',
    hints: [
      'Is the part before the punctuation a complete sentence?',
      'What punctuation mark introduces a list after a complete sentence?',
    ],
    teaching_explanation:
      "'Patrons could check out packets of three kinds of seeds' is a complete sentence, and what follows names those three kinds. A colon is the right mark to introduce a list or explanation after a complete sentence.",
    strategy_explanation:
      'Colon test: the part before it must be a complete sentence, and the part after must explain or list. Both are true here.',
    remember: 'Complete sentence + list or explanation = colon.',
    distractors: [
      { choice: 'B', rationale: "A semicolon must join two complete sentences, but 'bean, squash, and pepper' is not a sentence.", trap: null },
      { choice: 'C', rationale: "A colon should not follow 'such as,' because 'such as' already introduces the examples.", trap: null },
      { choice: 'D', rationale: "With no punctuation, 'seeds bean' runs the general word into the list.", trap: null },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'Apply the colon and semicolon tests to each option; only A passes.' },
    ],
  },
  {
    id: 'act-english-08',
    exam_family: 'act',
    section: 'english',
    difficulty: 4,
    passage: underline(EN_MONARCH, 1),
    stem: 'Which choice is best for the bracketed portion?',
    choices: [
      { key: 'A', text: NO_CHANGE },
      { key: 'B', text: 'Using tiny adhesive tags, monarch butterflies are marked by the students' },
      { key: 'C', text: 'Monarch butterflies, using tiny adhesive tags, are marked by the students' },
      { key: 'D', text: 'Using tiny adhesive tags, monarch butterflies get marked' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 40,
    primary_skill_key: 'act_sentence_structure',
    hints: [
      "Who is actually using the tags?",
      'An opening phrase describes whatever noun comes right after the comma.',
    ],
    teaching_explanation:
      "The phrase 'Using tiny adhesive tags' must be followed by the people who use them: the students. In A, 'the students' comes right after the comma, so the modifier is correctly placed.",
    strategy_explanation:
      'When a sentence starts with an -ing phrase, check the first noun after the comma. It must be the one doing the action.',
    remember: 'The opening phrase describes the very next noun.',
    distractors: [
      { choice: 'B', rationale: 'This says the butterflies are using the tags, which makes no sense.', trap: 'misplaced_modifier' },
      { choice: 'C', rationale: "Placing 'using tiny adhesive tags' right after 'monarch butterflies' again makes the butterflies the tag-users.", trap: 'misplaced_modifier' },
      { choice: 'D', rationale: 'The butterflies still appear to be using the tags, and the students disappear from the sentence.', trap: 'misplaced_modifier' },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'Ask "who is using the tags?" for each choice; B, C, and D all answer "the butterflies."' },
    ],
  },
  {
    id: 'act-english-09',
    exam_family: 'act',
    section: 'english',
    difficulty: 4,
    passage: underline(EN_MONARCH, 3),
    stem: 'Which choice is best for the bracketed portion?',
    choices: [
      { key: 'A', text: NO_CHANGE },
      { key: 'B', text: 'have revealed' },
      { key: 'C', text: 'having revealed' },
      { key: 'D', text: 'reveals' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 40,
    primary_skill_key: 'act_usage',
    hints: [
      "Cross out the prepositional phrases ('from volunteers,' 'across North America'). What is left as the subject?",
      'Is that subject singular or plural?',
    ],
    teaching_explanation:
      "The subject is 'Reports,' which is plural. The phrases 'from volunteers' and 'across North America' sit between the subject and the verb but do not change it, so the plural verb 'have revealed' is correct.",
    strategy_explanation:
      'Cross out prepositional phrases between the subject and verb, then match the verb to what remains.',
    remember: 'Cross out the prepositional phrase to find the real subject.',
    distractors: [
      { choice: 'A', rationale: "'Has revealed' is singular; it agrees with the nearby 'North America' instead of the subject 'Reports.'", trap: 'nearest_noun_agreement' },
      { choice: 'C', rationale: "'Having revealed' cannot serve as the main verb, so the sentence becomes a fragment.", trap: null },
      { choice: 'D', rationale: "'Reveals' is singular and does not match the plural subject 'Reports.'", trap: 'nearest_noun_agreement' },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'Once you know the subject is plural, cross off the two singular verbs and the -ing form.' },
    ],
  },
  {
    id: 'act-english-10',
    exam_family: 'act',
    section: 'english',
    difficulty: 5,
    passage: EN_SEEDS.replace(/\{\{\d+\|([^}]*)\}\}/g, '$1'),
    stem:
      "The writer wants to add the following sentence to the paragraph:\n\n'That way, the collection restocks itself each season without the library buying new packets.'\n\nThe sentence would most logically be placed after:",
    choices: [
      { key: 'A', text: 'Sentence 1.' },
      { key: 'B', text: 'Sentence 2.' },
      { key: 'C', text: 'Sentence 3.' },
      { key: 'D', text: 'Sentence 5.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 50,
    primary_skill_key: 'act_rhetorical_skills',
    hints: [
      "What does 'That way' need to point back to?",
      'Which sentence describes the action that would let the collection restock itself?',
    ],
    teaching_explanation:
      "'That way' must refer to a method described in the sentence just before it. Sentence 3 explains that patrons return seeds saved from their harvests, which is exactly how the collection restocks itself without new purchases.",
    strategy_explanation:
      "Use the new sentence's opening words as a clue. 'That way' points back to a process, so find the sentence that describes one.",
    remember: 'Pointer words like "that way" reveal what must come right before.',
    distractors: [
      { choice: 'A', rationale: 'Sentence 1 only introduces the idea of lending seeds; nothing yet explains how the collection is replenished.', trap: null },
      { choice: 'B', rationale: "Sentence 2 lists the kinds of seeds, so 'that way' would have no process to refer to.", trap: null },
      { choice: 'D', rationale: "Sentence 5 is about what patrons learn, not about how seeds come back to the library.", trap: 'true_but_irrelevant' },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: "Look for the sentence describing seeds being returned, then confirm 'That way' reads smoothly after it." },
      { strategy_key: 'process_of_elimination', role: 'secondary', is_fastest: false, explanation: 'Read the new sentence after each option and drop any spot where "that way" has nothing to point to.' },
    ],
  },
]

const ACT_MATH: FixtureQuestion[] = [
  {
    id: 'act-math-01',
    exam_family: 'act',
    section: 'math',
    difficulty: 1,
    stem: 'A recipe uses 3 cups of flour for every 2 cups of sugar. How many cups of flour are needed to go with 8 cups of sugar?',
    choices: [
      { key: 'A', text: '10' },
      { key: 'B', text: '11' },
      { key: 'C', text: '12' },
      { key: 'D', text: '16' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 45,
    primary_skill_key: 'act_number_quantity',
    hints: ['How many times larger is 8 cups of sugar than 2 cups?', 'Scale the flour by that same factor.'],
    teaching_explanation:
      'A ratio stays the same when both parts are multiplied by the same number. Going from 2 cups to 8 cups of sugar multiplies by 4, so the flour is 3 × 4 = 12 cups.',
    strategy_explanation: 'Find the scale factor (8 ÷ 2 = 4) and apply it to the other quantity.',
    remember: 'Ratios scale by multiplying, never by adding.',
    distractors: [
      { choice: 'A', rationale: 'Adding 2 to 8 ignores the ratio; ratios scale by multiplication.', trap: null },
      { choice: 'B', rationale: 'Adding 3 to 8 treats the ratio as a difference instead of a multiple.', trap: null },
      { choice: 'D', rationale: '16 is 8 × 2, which multiplies the sugar by its own ratio part instead of finding the flour.', trap: 'wrong_quantity' },
    ],
    strategies: [
      { strategy_key: 'translate_to_algebra', role: 'primary', is_fastest: true, explanation: 'Set up 3/2 = x/8 and solve: x = 12.' },
    ],
  },
  {
    id: 'act-math-02',
    exam_family: 'act',
    section: 'math',
    difficulty: 2,
    stem: 'If 4x − 7 = 2x + 9, what is the value of x?',
    choices: [
      { key: 'A', text: '1' },
      { key: 'B', text: '4' },
      { key: 'C', text: '8' },
      { key: 'D', text: '16' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 50,
    primary_skill_key: 'act_algebra_linear',
    hints: ['Get all the x terms on one side and the numbers on the other.', 'Do not forget the final division.'],
    teaching_explanation:
      'Subtract 2x from both sides to get 2x − 7 = 9, then add 7 to get 2x = 16. Dividing by 2 gives x = 8. Check: 4(8) − 7 = 25 and 2(8) + 9 = 25.',
    strategy_explanation: 'Solve directly in three short steps, then plug your answer back in to confirm both sides match.',
    remember: 'Finish the last step: 2x = 16 means x = 8.',
    distractors: [
      { choice: 'A', rationale: 'This comes from subtracting 7 from 9 instead of adding, giving 2x = 2.', trap: 'sign_error' },
      { choice: 'B', rationale: 'This divides 16 by 4 instead of by the coefficient 2.', trap: null },
      { choice: 'D', rationale: '16 is the value of 2x, not x. The final division by 2 was skipped.', trap: 'partial_answer' },
    ],
    strategies: [
      { strategy_key: 'translate_to_algebra', role: 'primary', is_fastest: true, explanation: 'Collect like terms and solve: 2x = 16, so x = 8.' },
      { strategy_key: 'backsolve', role: 'secondary', is_fastest: false, explanation: 'Plug in C: 4(8) − 7 = 25 and 2(8) + 9 = 25. It works.' },
    ],
  },
  {
    id: 'act-math-03',
    exam_family: 'act',
    section: 'math',
    difficulty: 2,
    stem: 'A rectangle has a perimeter of 30 inches and a length of 9 inches. What is the area of the rectangle, in square inches?',
    choices: [
      { key: 'A', text: '6' },
      { key: 'B', text: '54' },
      { key: 'C', text: '108' },
      { key: 'D', text: '270' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 55,
    primary_skill_key: 'act_geometry',
    hints: ['Perimeter counts each side once: 2 lengths plus 2 widths.', 'Find the width first, then multiply.'],
    teaching_explanation:
      'Perimeter = 2(length) + 2(width), so 30 = 18 + 2w and w = 6. Area = length × width = 9 × 6 = 54 square inches.',
    strategy_explanation: 'Sketch the rectangle, label 9 on two sides, and split the remaining 12 inches between the other two sides.',
    remember: 'Perimeter goes around; area fills in. Find the missing side first.',
    distractors: [
      { choice: 'A', rationale: '6 is the width, a middle step, not the area.', trap: 'partial_answer' },
      { choice: 'C', rationale: 'This uses 12 as the width, forgetting that the 12 leftover inches cover two sides.', trap: null },
      { choice: 'D', rationale: 'This multiplies the length by the perimeter, which is not a meaningful measurement.', trap: 'wrong_quantity' },
    ],
    strategies: [
      { strategy_key: 'draw_it_out', role: 'primary', is_fastest: true, explanation: 'Label the sketch: 9 + 9 = 18, leaving 12 for two widths, so each is 6.' },
    ],
  },
  {
    id: 'act-math-04',
    exam_family: 'act',
    section: 'math',
    difficulty: 3,
    stem: 'If f(x) = 2x² − 3x + 1, what is the value of f(−2)?',
    choices: [
      { key: 'A', text: '3' },
      { key: 'B', text: '−1' },
      { key: 'C', text: '15' },
      { key: 'D', text: '23' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 60,
    primary_skill_key: 'act_functions',
    hints: ['Substitute (−2) for every x, keeping the parentheses.', 'Square first, then multiply by 2.'],
    teaching_explanation:
      'f(−2) = 2(−2)² − 3(−2) + 1 = 2(4) + 6 + 1 = 15. Squaring −2 gives positive 4, and −3 times −2 gives positive 6.',
    strategy_explanation: 'Write the substitution with parentheses around −2 before simplifying. Most errors come from skipping that step.',
    remember: 'Parentheses around negatives protect your signs.',
    distractors: [
      { choice: 'A', rationale: 'This treats −3(−2) as −6, giving 8 − 6 + 1. A negative times a negative is positive.', trap: 'sign_error' },
      { choice: 'B', rationale: 'This treats (−2)² as −4, giving −8 + 6 + 1.', trap: 'sign_error' },
      { choice: 'D', rationale: 'This squares 2x as a whole, (2 · −2)² = 16, instead of squaring only x.', trap: null },
    ],
    strategies: [
      { strategy_key: 'plug_in_numbers', role: 'primary', is_fastest: true, explanation: 'Substitute −2 carefully with parentheses and evaluate term by term.' },
    ],
  },
  {
    id: 'act-math-05',
    exam_family: 'act',
    section: 'math',
    difficulty: 3,
    stem:
      'Five students scored 82, 90, 75, 90, and 88 on a quiz. A sixth student takes the quiz, and the mean of all six scores is then exactly 86. What did the sixth student score?',
    choices: [
      { key: 'A', text: '85' },
      { key: 'B', text: '86' },
      { key: 'C', text: '91' },
      { key: 'D', text: '90' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 60,
    primary_skill_key: 'act_statistics_probability',
    hints: ['Mean × number of values = total.', 'What must all six scores add up to?'],
    teaching_explanation:
      'The first five scores total 425. For six scores to average 86, they must total 6 × 86 = 516. The sixth score is 516 − 425 = 91.',
    strategy_explanation: 'Work with totals, not averages: needed total minus current total gives the missing value.',
    remember: 'Averages hide totals. Convert to sums to find a missing value.',
    distractors: [
      { choice: 'A', rationale: '85 is the mean of the first five scores, not the sixth score.', trap: 'partial_answer' },
      { choice: 'B', rationale: 'Adding a score equal to the new mean would only work if the old mean were already 86.', trap: null },
      { choice: 'D', rationale: '90 is the mode of the original scores, which does not answer the question.', trap: 'wrong_quantity' },
    ],
    strategies: [
      { strategy_key: 'translate_to_algebra', role: 'primary', is_fastest: true, explanation: '(425 + x) / 6 = 86, so x = 516 − 425 = 91.' },
      { strategy_key: 'backsolve', role: 'secondary', is_fastest: false, explanation: 'Add each choice to 425 and check whether the sum is 516.' },
    ],
  },
  {
    id: 'act-math-06',
    exam_family: 'act',
    section: 'math',
    difficulty: 3,
    stem:
      'A jacket is priced at $80. It is discounted by 25%, and then a 5% sales tax is applied to the discounted price. What is the total cost of the jacket, in dollars?',
    choices: [],
    answer_format: 'numeric',
    accepted_answers: ['63', '63.00', '$63', '$63.00'],
    expected_time_seconds: 60,
    primary_skill_key: 'act_number_quantity',
    hints: ['Apply the discount first, then apply the tax to that new price.', 'A 25% discount leaves 75% of the price.'],
    teaching_explanation:
      'After a 25% discount, the price is 0.75 × 80 = $60. A 5% tax on $60 adds $3, so the total is 1.05 × 60 = $63.',
    strategy_explanation: 'Use multipliers: 80 × 0.75 × 1.05 = 63. One line, no separate subtraction or addition steps.',
    remember: 'Percent changes chain by multiplying: 0.75 then 1.05.',
    distractors: [],
    strategies: [
      { strategy_key: 'translate_to_algebra', role: 'primary', is_fastest: true, explanation: 'Translate each percent change into a multiplier and multiply them together.' },
    ],
  },
  {
    id: 'act-math-07',
    exam_family: 'act',
    section: 'math',
    difficulty: 3,
    stem: 'If 2x + y = 11 and x − y = 1, what is the value of x + y?',
    choices: [
      { key: 'A', text: '4' },
      { key: 'B', text: '3' },
      { key: 'C', text: '7' },
      { key: 'D', text: '12' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 60,
    primary_skill_key: 'act_algebra_linear',
    hints: ['Notice the y terms have opposite signs. What happens if you add the equations?', 'Read the question again: it asks for x + y.'],
    teaching_explanation:
      'Adding the equations cancels y: 3x = 12, so x = 4. Then 4 − y = 1 gives y = 3. The question asks for x + y = 7.',
    strategy_explanation: 'Use elimination when coefficients are already opposites, and underline what the question asks for so you finish the job.',
    remember: 'Solve for x and y, then answer the question actually asked.',
    distractors: [
      { choice: 'A', rationale: '4 is the value of x alone.', trap: 'partial_answer' },
      { choice: 'B', rationale: '3 is the value of y alone.', trap: 'partial_answer' },
      { choice: 'D', rationale: '12 is 3x, the result right after adding the equations.', trap: 'partial_answer' },
    ],
    strategies: [
      { strategy_key: 'read_question_first', role: 'primary', is_fastest: true, explanation: 'Knowing the target is x + y keeps you from stopping at x = 4.' },
      { strategy_key: 'translate_to_algebra', role: 'secondary', is_fastest: false, explanation: 'Add the equations to eliminate y, then substitute.' },
    ],
  },
  {
    id: 'act-math-08',
    exam_family: 'act',
    section: 'math',
    difficulty: 3,
    stem: 'In the standard (x, y) coordinate plane, a circle has equation (x − 3)² + (y + 2)² = 49. What are the center and radius of the circle?',
    choices: [
      { key: 'A', text: 'Center (3, −2), radius 7' },
      { key: 'B', text: 'Center (−3, 2), radius 7' },
      { key: 'C', text: 'Center (3, −2), radius 49' },
      { key: 'D', text: 'Center (−3, 2), radius 49' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 50,
    primary_skill_key: 'act_geometry',
    hints: ['Compare to the form (x − h)² + (y − k)² = r².', 'What number squared gives 49?'],
    teaching_explanation:
      'In (x − h)² + (y − k)² = r², the center is (h, k) and the radius is r. Here x − 3 gives h = 3, and y + 2 = y − (−2) gives k = −2. Since r² = 49, r = 7.',
    strategy_explanation: 'Flip the signs inside the parentheses for the center, and take the square root of the right side for the radius.',
    remember: 'Center: flip the signs. Radius: square root the constant.',
    distractors: [
      { choice: 'B', rationale: 'The signs were not flipped; the center coordinates are the opposites of the numbers shown.', trap: 'sign_error' },
      { choice: 'C', rationale: '49 is r², not r.', trap: 'wrong_quantity' },
      { choice: 'D', rationale: 'Both the center signs and the radius are off.', trap: 'sign_error' },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'First eliminate radius 49, then choose the center with flipped signs.' },
    ],
  },
  {
    id: 'act-math-09',
    exam_family: 'act',
    section: 'math',
    difficulty: 4,
    stem: 'The function g is defined by g(x) = |x − 4| − 3. For how many integer values of x is g(x) < 0?',
    choices: [
      { key: 'A', text: '3' },
      { key: 'B', text: '5' },
      { key: 'C', text: '6' },
      { key: 'D', text: '7' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 75,
    primary_skill_key: 'act_functions',
    hints: ['Rewrite g(x) < 0 as |x − 4| < 3.', 'Which numbers are less than 3 units away from 4? Be careful with the endpoints.'],
    teaching_explanation:
      'g(x) < 0 means |x − 4| < 3, so −3 < x − 4 < 3, or 1 < x < 7. The integers strictly between 1 and 7 are 2, 3, 4, 5, and 6: five values. At x = 1 and x = 7, g(x) = 0, which is not less than 0.',
    strategy_explanation: 'Think of |x − 4| < 3 as "within 3 of 4," list the integers, and check the endpoints.',
    remember: 'Strict inequality: the endpoints do not count.',
    distractors: [
      { choice: 'A', rationale: 'This counts too few values, perhaps solving only one side of the absolute value.', trap: 'partial_answer' },
      { choice: 'C', rationale: 'This includes one endpoint, where g(x) equals 0 rather than being less than 0.', trap: null },
      { choice: 'D', rationale: 'This includes both endpoints, 1 and 7, where g(x) = 0.', trap: null },
    ],
    strategies: [
      { strategy_key: 'plug_in_numbers', role: 'primary', is_fastest: true, explanation: 'Test integers near 4 (1 through 7) and count where g(x) is negative.' },
      { strategy_key: 'translate_to_algebra', role: 'secondary', is_fastest: false, explanation: 'Solve the compound inequality 1 < x < 7.' },
    ],
  },
  {
    id: 'act-math-10',
    exam_family: 'act',
    section: 'math',
    difficulty: 4,
    stem:
      'A bag holds 4 red, 5 blue, and 3 green marbles. Two marbles are drawn at random, one after the other, without replacement. What is the probability that both marbles are blue? Enter your answer as a fraction in lowest terms or a decimal.',
    choices: [],
    answer_format: 'numeric',
    accepted_answers: ['5/33', '0.1515', '.1515', '0.1516', '.1516', '0.152', '.152'],
    expected_time_seconds: 75,
    primary_skill_key: 'act_statistics_probability',
    hints: ['How many marbles are there in total?', 'After one blue marble is removed, how many blue and how many total remain?'],
    teaching_explanation:
      'There are 12 marbles. The first draw is blue with probability 5/12. Then 4 blue remain out of 11, so the second is blue with probability 4/11. Multiply: (5/12)(4/11) = 20/132 = 5/33.',
    strategy_explanation: 'For "and" events without replacement, multiply the probabilities, reducing both the favorable count and the total by one for the second draw.',
    remember: 'Without replacement: both the top and bottom drop by one.',
    distractors: [],
    strategies: [
      { strategy_key: 'translate_to_algebra', role: 'primary', is_fastest: true, explanation: 'Write P = (5/12)(4/11) and simplify.' },
    ],
  },
  {
    id: 'act-math-11',
    exam_family: 'act',
    section: 'math',
    difficulty: 4,
    stem: 'In right triangle ABC, angle C is the right angle and sin A = 5/13. What is tan B?',
    choices: [
      { key: 'A', text: '5/12' },
      { key: 'B', text: '12/13' },
      { key: 'C', text: '12/5' },
      { key: 'D', text: '13/12' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 75,
    primary_skill_key: 'act_geometry',
    hints: ['Draw the triangle and label the side opposite A as 5 and the hypotenuse as 13.', 'Use the Pythagorean theorem for the third side, then look from angle B.'],
    teaching_explanation:
      'sin A = opposite/hypotenuse, so BC = 5 and AB = 13. Then AC = √(13² − 5²) = 12. From angle B, the opposite side is AC = 12 and the adjacent side is BC = 5, so tan B = 12/5.',
    strategy_explanation: 'Sketch and label the 5-12-13 triangle, then switch your viewpoint to angle B before applying SOH-CAH-TOA.',
    remember: "Opposite and adjacent depend on which angle you're standing at.",
    distractors: [
      { choice: 'A', rationale: '5/12 is tan A. The opposite and adjacent sides swap when you move to angle B.', trap: 'wrong_quantity' },
      { choice: 'B', rationale: '12/13 is sin B (or cos A), not tan B.', trap: 'wrong_quantity' },
      { choice: 'D', rationale: 'This divides the hypotenuse by a leg, which is not a tangent ratio.', trap: null },
    ],
    strategies: [
      { strategy_key: 'draw_it_out', role: 'primary', is_fastest: true, explanation: 'A quick labeled sketch makes the opposite and adjacent sides for B obvious.' },
    ],
  },
  {
    id: 'act-math-12',
    exam_family: 'act',
    section: 'math',
    difficulty: 5,
    stem: 'For what positive value of k does the system of equations y = x² + k and y = 4x have exactly one real solution?',
    choices: [
      { key: 'A', text: '2' },
      { key: 'B', text: '4' },
      { key: 'C', text: '8' },
      { key: 'D', text: '16' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 90,
    primary_skill_key: 'act_functions',
    hints: ['Set the two expressions for y equal and move everything to one side.', 'A quadratic has exactly one real solution when its discriminant equals zero.'],
    teaching_explanation:
      'Setting x² + k = 4x gives x² − 4x + k = 0. Exactly one solution means the discriminant b² − 4ac = 0: (−4)² − 4(1)(k) = 16 − 4k = 0, so k = 4. Check: x² − 4x + 4 = (x − 2)², which has the single solution x = 2.',
    strategy_explanation: 'Combine into one quadratic and set the discriminant to zero. Or backsolve: only k = 4 makes a perfect square.',
    remember: 'Exactly one solution means the discriminant equals zero.',
    distractors: [
      { choice: 'A', rationale: '2 is the x-value where the line and parabola touch, not k.', trap: 'partial_answer' },
      { choice: 'C', rationale: 'With k = 8, the discriminant is 16 − 32 < 0, so there are no real solutions.', trap: null },
      { choice: 'D', rationale: 'This drops the 4 in 4ac, solving 16 − k = 0.', trap: null },
    ],
    strategies: [
      { strategy_key: 'translate_to_algebra', role: 'primary', is_fastest: true, explanation: 'Write x² − 4x + k = 0 and solve 16 − 4k = 0.' },
      { strategy_key: 'backsolve', role: 'secondary', is_fastest: false, explanation: 'Test each k to see which makes x² − 4x + k a perfect square.' },
    ],
  },
]

const ACT_READING: FixtureQuestion[] = [
  {
    id: 'act-reading-01',
    exam_family: 'act',
    section: 'reading',
    difficulty: 1,
    passage: RD_WATCH,
    stem: "According to the passage, how often did customers typically come into Grandpa Teo's shop?",
    choices: [
      { key: 'A', text: 'Several times a day' },
      { key: 'B', text: 'About twice a week' },
      { key: 'C', text: 'About once a month' },
      { key: 'D', text: 'Only during the summer' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 40,
    primary_skill_key: 'act_main_idea',
    hints: ['Look for a sentence about the bell above the door.'],
    teaching_explanation: "The passage says 'The bell above the door rang perhaps twice a week.' The bell signals a customer arriving, so customers came about twice a week.",
    strategy_explanation: 'This is a detail question. Find the exact sentence rather than relying on memory.',
    remember: 'Detail questions: go back and point to the line.',
    distractors: [
      { choice: 'A', rationale: 'The passage stresses how rarely customers came, not how often.', trap: 'out_of_scope' },
      { choice: 'C', rationale: 'The passage gives a frequency of twice a week, not once a month.', trap: null },
      { choice: 'D', rationale: "Summer is mentioned only as when the narrator turned fourteen, not as the shop's season.", trap: null },
    ],
    strategies: [
      { strategy_key: 'locate_evidence', role: 'primary', is_fastest: true, explanation: "Scan for 'bell' and read that sentence." },
    ],
  },
  {
    id: 'act-reading-02',
    exam_family: 'act',
    section: 'reading',
    difficulty: 3,
    passage: RD_WATCH,
    stem: 'It can most reasonably be inferred that Grandpa Teo keeps his shop open mainly because he:',
    choices: [
      { key: 'A', text: 'expects business to improve as wind-up watches come back into fashion.' },
      { key: 'B', text: 'feels responsible to people who have trusted him with meaningful objects.' },
      { key: 'C', text: 'wants to teach the narrator how to repair watches.' },
      { key: 'D', text: 'has nowhere else to spend his time.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 50,
    primary_skill_key: 'act_inference',
    hints: ["Reread Grandpa Teo's answer at the end of the passage.", "What does 'Somebody has to be here when she is' suggest about his reasons?"],
    teaching_explanation:
      "When asked why he bothers, Grandpa Teo shows the watch Mrs. Albrecht left with him eleven years ago and says, 'Somebody has to be here when she is.' This shows a sense of duty to a customer and the sentimental object she trusted him with.",
    strategy_explanation: "Predict the answer from his own words before reading the choices: he stays open for people like Mrs. Albrecht.",
    remember: 'A good inference stays one small step from the text.',
    distractors: [
      { choice: 'A', rationale: 'Nothing in the passage suggests he expects wind-up watches to return.', trap: 'out_of_scope' },
      { choice: 'C', rationale: 'The narrator is present, but the passage never mentions teaching repairs.', trap: 'out_of_scope' },
      { choice: 'D', rationale: 'This is unsupported and ignores the reason he actually gives.', trap: 'extreme_language' },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Use his final line to predict "duty to Mrs. Albrecht," then match to B.' },
    ],
  },
  {
    id: 'act-reading-03',
    exam_family: 'act',
    section: 'reading',
    difficulty: 4,
    passage: RD_WATCH,
    stem: "The detail that the pocket watch's hands are 'frozen at 4:10' mainly serves to:",
    choices: [
      { key: 'A', text: 'suggest that the watch, like Grandpa Teo, has been waiting unchanged for its owner.' },
      { key: 'B', text: 'indicate the exact time of day Mrs. Albrecht visited the shop.' },
      { key: 'C', text: 'show that Grandpa Teo lacks the skill to repair the watch.' },
      { key: 'D', text: 'explain why the shop opens at seven each morning.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 55,
    primary_skill_key: 'act_author_purpose',
    hints: ['Think about what a stopped watch might symbolize in a story about waiting.', 'Does the passage say anything about whether Teo tried to fix it?'],
    teaching_explanation:
      'A watch whose hands never move suggests time standing still. That image echoes the story: the watch has sat unchanged for eleven years, and Grandpa Teo keeps waiting for Mrs. Albrecht to return.',
    strategy_explanation: 'For "mainly serves to" questions, connect the detail to the passage’s central idea rather than reading it literally.',
    remember: 'Ask how a detail connects to the big idea.',
    distractors: [
      { choice: 'B', rationale: 'The passage never links 4:10 to the time of her visit; this reads the detail too literally.', trap: 'out_of_scope' },
      { choice: 'C', rationale: 'Nothing suggests he cannot fix it; he is keeping it until she is ready.', trap: 'out_of_scope' },
      { choice: 'D', rationale: 'The opening time is unrelated to the stopped watch.', trap: 'true_but_irrelevant' },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Predict "it shows time standing still while he waits," then match to A.' },
      { strategy_key: 'process_of_elimination', role: 'secondary', is_fastest: false, explanation: 'Cross out choices that make claims the passage never supports.' },
    ],
  },
  {
    id: 'act-reading-04',
    exam_family: 'act',
    section: 'reading',
    difficulty: 2,
    passage: RD_HEAT,
    stem: 'The main purpose of the passage is to:',
    choices: [
      { key: 'A', text: 'explain what causes urban heat islands and describe some ways cities are responding.' },
      { key: 'B', text: 'argue that every city should replace all dark roofs with cool roofs.' },
      { key: 'C', text: 'compare the climates of several major cities around the world.' },
      { key: 'D', text: 'prove that street trees are more effective than cool roofs.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 45,
    primary_skill_key: 'act_main_idea',
    hints: ['What does the first paragraph do? What does the second paragraph do?'],
    teaching_explanation:
      'The first paragraph explains causes of urban heat islands (dark surfaces, blocked breezes). The second describes remedies like cool roofs and street trees. Choice A covers both paragraphs.',
    strategy_explanation: 'Summarize each paragraph in a few words, then choose the answer that covers all of them.',
    remember: 'The main purpose must cover the whole passage, not one part.',
    distractors: [
      { choice: 'B', rationale: "'Every' and 'all' go far beyond the passage, which describes remedies without demanding them.", trap: 'extreme_language' },
      { choice: 'C', rationale: 'The passage does not compare specific cities.', trap: 'out_of_scope' },
      { choice: 'D', rationale: 'The passage never ranks trees against cool roofs.', trap: 'extreme_language' },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Predict "causes, then solutions," and match to A.' },
    ],
  },
  {
    id: 'act-reading-05',
    exam_family: 'act',
    section: 'reading',
    difficulty: 3,
    passage: RD_HEAT,
    stem: "As it is used in the passage, the word 'modest' most nearly means:",
    choices: [
      { key: 'A', text: 'humble.' },
      { key: 'B', text: 'shy.' },
      { key: 'C', text: 'small.' },
      { key: 'D', text: 'old-fashioned.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 40,
    primary_skill_key: 'act_vocabulary_in_context',
    hints: ["Cover the word and reread: 'even ___ reductions in nighttime temperatures can matter.'", 'What kind of word would fit with "even"?'],
    teaching_explanation:
      "The sentence says that 'even modest reductions' can matter, meaning that even small decreases in temperature are helpful. 'Modest' here describes size, not personality.",
    strategy_explanation: 'Replace the word with a blank, predict your own word, then pick the choice closest to your prediction.',
    remember: 'Vocab in context: predict a replacement before reading the choices.',
    distractors: [
      { choice: 'A', rationale: "'Humble' is a common meaning of 'modest' for people, but temperature reductions cannot be humble.", trap: 'familiar_meaning' },
      { choice: 'B', rationale: "'Shy' describes a personality, which does not fit a temperature change.", trap: 'familiar_meaning' },
      { choice: 'D', rationale: 'Nothing about the reductions relates to being outdated.', trap: null },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Predict "small" from "even ___ reductions," then match.' },
    ],
  },
  {
    id: 'act-reading-06',
    exam_family: 'act',
    section: 'reading',
    difficulty: 4,
    passage: RD_HEAT,
    stem: 'Based on the passage, the author would most likely agree that cool roofs and street trees:',
    choices: [
      { key: 'A', text: 'can eliminate the temperature difference between cities and nearby farmland.' },
      { key: 'B', text: 'are worthwhile even though they cannot fully solve the problem.' },
      { key: 'C', text: 'are too expensive for most cities to adopt.' },
      { key: 'D', text: 'have no effect on temperatures after sunset.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 55,
    primary_skill_key: 'act_inference',
    hints: ["Find the sentence that begins 'These measures are not cures.'", 'What does the author say right after that?'],
    teaching_explanation:
      "The author states that the measures 'are not cures' but adds that 'even modest reductions in nighttime temperatures can matter.' Together, those lines show the author sees them as helpful but limited.",
    strategy_explanation: "Look for contrast words like 'but' near the topic; the author's real view often follows them.",
    remember: "After 'but,' you usually find the author's real opinion.",
    distractors: [
      { choice: 'A', rationale: "The author says a city 'will never be as cool as a meadow,' so the gap is not eliminated.", trap: 'extreme_language' },
      { choice: 'C', rationale: 'Cost is never discussed in the passage.', trap: 'out_of_scope' },
      { choice: 'D', rationale: 'The author specifically mentions reductions in nighttime temperatures.', trap: null },
    ],
    strategies: [
      { strategy_key: 'locate_evidence', role: 'primary', is_fastest: true, explanation: "Go to 'These measures are not cures ... But ...' and read both halves." },
    ],
  },
  {
    id: 'act-reading-07',
    exam_family: 'act',
    section: 'reading',
    difficulty: 3,
    passage: RD_JAZZ,
    stem: "The author compares a jazz soloist to 'a fluent speaker' primarily to:",
    choices: [
      { key: 'A', text: 'show that improvised solos are built from a learned set of musical elements.' },
      { key: 'B', text: 'suggest that jazz musicians are also skilled public speakers.' },
      { key: 'C', text: 'argue that learning jazz is harder than learning a language.' },
      { key: 'D', text: 'explain why jazz solos tend to be short.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 50,
    primary_skill_key: 'act_author_purpose',
    hints: ['What does a fluent speaker use to make new sentences?', 'What is the matching idea for a musician?'],
    teaching_explanation:
      'A fluent speaker creates new sentences from words they already know. Likewise, a soloist invents new music from stored scales, patterns, and phrases. The comparison shows that improvisation relies on a learned vocabulary.',
    strategy_explanation: 'For a comparison, ask what the two things have in common in the passage, and pick the choice that names it.',
    remember: 'An analogy highlights what two things share.',
    distractors: [
      { choice: 'B', rationale: 'The comparison is about how both create new material, not about musicians giving speeches.', trap: 'out_of_scope' },
      { choice: 'C', rationale: 'The author never ranks jazz and language by difficulty.', trap: 'out_of_scope' },
      { choice: 'D', rationale: 'Solo length is never discussed.', trap: 'out_of_scope' },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Predict "both build new things from familiar pieces," then match to A.' },
    ],
  },
  {
    id: 'act-reading-08',
    exam_family: 'act',
    section: 'reading',
    difficulty: 5,
    passage: RD_JAZZ,
    stem: 'Which statement best describes how the author presents the relationship between freedom and discipline in the last paragraph?',
    choices: [
      { key: 'A', text: "A musician's freedom shrinks as practice increases, since practiced phrases crowd out new ideas." },
      { key: 'B', text: 'Freedom and discipline are separate parts of jazz that do not affect each other.' },
      { key: 'C', text: "The discipline of practice is what makes a musician's freedom possible." },
      { key: 'D', text: 'Listeners care more about a musician’s discipline than about freedom.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 60,
    primary_skill_key: 'act_main_idea',
    hints: ["Reread the final sentence. What does the word 'rests on' tell you?", 'Does the author see practice as a limit on freedom, or as its foundation?'],
    teaching_explanation:
      "The final sentence says freedom 'rests on a discipline they do not hear: the hours of practice that make spontaneous choices possible.' Practice is described as the foundation for freedom, not its opposite.",
    strategy_explanation: "Focus on the relationship words in the key sentence ('rests on,' 'make ... possible') and match the choice that keeps the same direction.",
    remember: 'Track relationship words: "rests on" means one supports the other.',
    distractors: [
      { choice: 'A', rationale: 'This reverses the relationship. The author says practice enables freedom rather than limiting it.', trap: null },
      { choice: 'B', rationale: "The author explicitly connects them with 'rests on.'", trap: null },
      { choice: 'D', rationale: "The author says listeners do not even hear the discipline, so they cannot be said to value it more.", trap: 'out_of_scope' },
    ],
    strategies: [
      { strategy_key: 'locate_evidence', role: 'primary', is_fastest: true, explanation: 'Reread the last sentence and match its cause-and-effect direction.' },
      { strategy_key: 'process_of_elimination', role: 'secondary', is_fastest: false, explanation: 'Remove choices that reverse or disconnect the relationship.' },
    ],
  },
]

const ACT_SCIENCE: FixtureQuestion[] = [
  {
    id: 'act-science-01',
    exam_family: 'act',
    section: 'science',
    difficulty: 1,
    passage: SCI_LIGHT,
    stem: 'According to Table 1, what was the average height of the seedlings grown at 4,000 lux?',
    choices: [
      { key: 'A', text: '4.2 cm' },
      { key: 'B', text: '7.9 cm' },
      { key: 'C', text: '12.6 cm' },
      { key: 'D', text: '14.1 cm' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 30,
    primary_skill_key: 'act_data_interpretation',
    hints: ['Find 4,000 in the light intensity column, then read across.'],
    teaching_explanation: 'In Table 1, the row for 4,000 lux shows an average height of 12.6 cm.',
    strategy_explanation: 'Put your finger on the correct row before reading across. Most errors come from sliding to a neighboring row.',
    remember: 'Find the row first, then read across carefully.',
    distractors: [
      { choice: 'A', rationale: '4.2 cm is the height at 1,000 lux.', trap: 'misread_graph' },
      { choice: 'B', rationale: '7.9 cm is the height at 2,000 lux.', trap: 'misread_graph' },
      { choice: 'D', rationale: '14.1 cm is the height at 8,000 lux.', trap: 'misread_graph' },
    ],
    strategies: [
      { strategy_key: 'locate_evidence', role: 'primary', is_fastest: true, explanation: 'Go straight to the 4,000 lux row.' },
    ],
  },
  {
    id: 'act-science-02',
    exam_family: 'act',
    section: 'science',
    difficulty: 2,
    passage: SCI_LIGHT,
    stem: 'Based on Table 1, as light intensity increased from 1,000 lux to 16,000 lux, the average seedling height:',
    choices: [
      { key: 'A', text: 'increased only.' },
      { key: 'B', text: 'decreased only.' },
      { key: 'C', text: 'increased, then decreased.' },
      { key: 'D', text: 'remained the same.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 35,
    primary_skill_key: 'act_data_interpretation',
    hints: ['Compare each height to the one above it.', 'Even a small rise still counts as an increase.'],
    teaching_explanation:
      'The heights go 4.2, 7.9, 12.6, 14.1, 14.3. Each value is larger than the one before, so the height increased only, even though the increases became much smaller at high intensities.',
    strategy_explanation: 'Check each step in the column for a change in direction. If there is none, the trend is "increased only."',
    remember: 'Slowing growth is still growth.',
    distractors: [
      { choice: 'B', rationale: 'Every height is larger than the one before it.', trap: 'misread_graph' },
      { choice: 'C', rationale: 'The increase slows from 14.1 to 14.3 cm, but it never turns into a decrease.', trap: 'misread_graph' },
      { choice: 'D', rationale: 'The height changes from 4.2 cm to 14.3 cm.', trap: null },
    ],
    strategies: [
      { strategy_key: 'find_the_trend', role: 'primary', is_fastest: true, explanation: 'Scan the height column top to bottom and note the direction of each change.' },
    ],
  },
  {
    id: 'act-science-03',
    exam_family: 'act',
    section: 'science',
    difficulty: 4,
    passage: SCI_LIGHT,
    stem: 'If seedlings had been grown at 32,000 lux under the same conditions, their average height after 14 days would most likely have been closest to:',
    choices: [
      { key: 'A', text: '7 cm' },
      { key: 'B', text: '14 cm' },
      { key: 'C', text: '20 cm' },
      { key: 'D', text: '28 cm' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 55,
    primary_skill_key: 'act_data_interpretation',
    hints: ['How much did the height change from 8,000 lux to 16,000 lux?', 'What does a very small change between the last two rows suggest about the next one?'],
    teaching_explanation:
      'Doubling the light from 8,000 to 16,000 lux raised the height by only 0.2 cm, so growth had nearly leveled off. Another doubling would most likely produce a height still close to 14 cm.',
    strategy_explanation: 'When extrapolating, follow the most recent part of the trend, not the steep early part.',
    remember: 'Extend the trend where the data ends, not where it started.',
    distractors: [
      { choice: 'A', rationale: 'Nothing in the data suggests height would drop sharply at higher light.', trap: null },
      { choice: 'C', rationale: 'This assumes the earlier, faster growth would resume, ignoring the plateau.', trap: 'overextend_trend' },
      { choice: 'D', rationale: 'This doubles the height along with the light, but the data stopped following that pattern long before 16,000 lux.', trap: 'overextend_trend' },
    ],
    strategies: [
      { strategy_key: 'find_the_trend', role: 'primary', is_fastest: true, explanation: 'Notice the leveling off at the bottom of the table and extend it.' },
    ],
  },
  {
    id: 'act-science-04',
    exam_family: 'act',
    section: 'science',
    difficulty: 3,
    passage: SCI_PENDULUM,
    stem: 'In Experiment 2, which two variables were held constant?',
    choices: [
      { key: 'A', text: 'String length and release angle' },
      { key: 'B', text: 'Bob mass and string length' },
      { key: 'C', text: 'Bob mass and release angle' },
      { key: 'D', text: 'Period and bob mass' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 40,
    primary_skill_key: 'act_experiment_design',
    hints: ['Read the description line for Experiment 2.', 'Which variable did the student change on purpose?'],
    teaching_explanation:
      'Experiment 2 lists string length (100 cm) and release angle (10°) as fixed, while bob mass was varied. Holding the other variables constant lets the student test the effect of mass alone.',
    strategy_explanation: 'Identify the one variable that changes in the table; the controlled variables are the ones listed as fixed.',
    remember: 'Change one thing; hold everything else steady.',
    distractors: [
      { choice: 'B', rationale: 'Bob mass was the variable that changed in Experiment 2.', trap: 'misread_graph' },
      { choice: 'C', rationale: 'Bob mass was varied, not held constant.', trap: 'misread_graph' },
      { choice: 'D', rationale: 'Period is the measured result, and bob mass was varied.', trap: 'wrong_quantity' },
    ],
    strategies: [
      { strategy_key: 'read_question_first', role: 'primary', is_fastest: true, explanation: 'Know you need the constants, then go straight to the Experiment 2 description.' },
    ],
  },
  {
    id: 'act-science-05',
    exam_family: 'act',
    section: 'science',
    difficulty: 3,
    passage: SCI_PENDULUM,
    stem: 'Why did the student most likely time 10 complete swings and divide by 10, rather than timing a single swing?',
    choices: [
      { key: 'A', text: 'To reduce the effect of reaction-time error when starting and stopping the stopwatch' },
      { key: 'B', text: 'To make the pendulum swing faster' },
      { key: 'C', text: 'To change the period of the pendulum' },
      { key: 'D', text: 'To keep the release angle the same in each trial' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 45,
    primary_skill_key: 'act_experiment_design',
    hints: ['A single swing lasts only a second or two. How accurately can a person start and stop a stopwatch?'],
    teaching_explanation:
      'Human reaction time adds a small, roughly fixed error to each timing. Spreading that error across 10 swings makes it about one-tenth as large per swing, so the calculated period is more accurate.',
    strategy_explanation: 'For "why did they do it this way" questions, think about which source of error the method reduces.',
    remember: 'Timing many cycles shrinks the error per cycle.',
    distractors: [
      { choice: 'B', rationale: 'Timing more swings does not change how fast the pendulum moves.', trap: null },
      { choice: 'C', rationale: 'The period depends on the pendulum itself, not on how it is timed.', trap: null },
      { choice: 'D', rationale: 'The release angle is controlled by how the bob is released, not by how many swings are timed.', trap: 'true_but_irrelevant' },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'B, C, and D claim timing changes the pendulum itself, which it cannot.' },
    ],
  },
  {
    id: 'act-science-06',
    exam_family: 'act',
    section: 'science',
    difficulty: 4,
    passage: SCI_PENDULUM,
    stem: 'Based on Experiments 1 and 2, a pendulum with a 200 g bob and a 50 cm string, released at 10°, would have a period closest to:',
    choices: [
      { key: 'A', text: '1.0 s' },
      { key: 'B', text: '1.4 s' },
      { key: 'C', text: '2.0 s' },
      { key: 'D', text: '2.8 s' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 55,
    primary_skill_key: 'act_data_interpretation',
    hints: ['What did Experiment 2 show about the effect of bob mass on period?', 'Then use Experiment 1 to look up a 50 cm string.'],
    teaching_explanation:
      'Experiment 2 shows that changing the mass from 50 g to 200 g did not change the period. So only length matters here, and Experiment 1 shows a 50 cm pendulum has a period of 1.4 s.',
    strategy_explanation: 'Use one experiment to rule out an irrelevant variable, then read the answer from the other.',
    remember: 'If a variable changes nothing, ignore it.',
    distractors: [
      { choice: 'A', rationale: '1.0 s is the period for a 25 cm string.', trap: 'misread_graph' },
      { choice: 'C', rationale: '2.0 s is the period for a 100 cm string, the length used in Experiment 2.', trap: 'misread_graph' },
      { choice: 'D', rationale: 'This assumes a heavier bob lengthens the period, but Experiment 2 shows mass has no effect.', trap: 'overextend_trend' },
    ],
    strategies: [
      { strategy_key: 'find_the_trend', role: 'primary', is_fastest: true, explanation: 'Notice the flat period column in Experiment 2, then read the 50 cm row in Experiment 1.' },
    ],
  },
  {
    id: 'act-science-07',
    exam_family: 'act',
    section: 'science',
    difficulty: 3,
    passage: SCI_ALGAE,
    stem: "Which of the following observations would most strongly support Student 2's explanation over Student 1's?",
    choices: [
      { key: 'A', text: 'A large bloom formed during a hot, calm, dry week when no runoff entered the lake.' },
      { key: 'B', text: 'Phosphorus levels in the lake rose sharply after a heavy rainstorm.' },
      { key: 'C', text: 'Farms near the lake used more fertilizer this year than last year.' },
      { key: 'D', text: 'Algae need sunlight to grow.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 50,
    primary_skill_key: 'act_conflicting_viewpoints',
    hints: ['What does Student 2 predict that Student 1 does not?', 'Which choice matches a situation with heat but no extra fertilizer?'],
    teaching_explanation:
      "Student 2 predicts large blooms during hot, calm weather even without rain. A bloom with no runoff (so no new fertilizer) but warm, still water fits Student 2's explanation and goes against Student 1's.",
    strategy_explanation: 'Summarize each student in one line, then pick the observation that only one of them predicts.',
    remember: 'Support for one view should be something only that view predicts.',
    distractors: [
      { choice: 'B', rationale: "Rising phosphorus after rain fits Student 1's explanation, not Student 2's.", trap: null },
      { choice: 'C', rationale: "More fertilizer use supports Student 1's runoff explanation.", trap: null },
      { choice: 'D', rationale: 'Both students could accept this; it does not distinguish between them.', trap: 'true_but_irrelevant' },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Predict "a bloom in hot weather without runoff," then match to A.' },
    ],
  },
  {
    id: 'act-science-08',
    exam_family: 'act',
    section: 'science',
    difficulty: 5,
    passage: SCI_ALGAE,
    stem:
      'Researchers sealed off one section of Lake Marlow, added phosphorus to it, and kept its water cool. No bloom formed in that section. How does this result relate to the students’ explanations?',
    choices: [
      { key: 'A', text: "It weakens Student 1's explanation but is consistent with Student 2's." },
      { key: 'B', text: "It weakens Student 2's explanation but is consistent with Student 1's." },
      { key: 'C', text: 'It is consistent with both explanations.' },
      { key: 'D', text: 'It weakens both explanations.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 70,
    primary_skill_key: 'act_conflicting_viewpoints',
    hints: ['According to Student 1, what should happen when phosphorus is added?', 'According to Student 2, what should happen when the water stays cool?'],
    teaching_explanation:
      "Student 1 says phosphorus limits algae growth, so adding phosphorus should cause a bloom. It did not, which weakens Student 1. Student 2 says warm water drives blooms, so cool water should prevent one, exactly as observed.",
    strategy_explanation: 'Test the result against each student separately: did that student predict a bloom here or not?',
    remember: "Check the result against each viewpoint's prediction, one at a time.",
    distractors: [
      { choice: 'B', rationale: 'This reverses the logic. Student 2 predicted no bloom in cool water, which is what happened.', trap: null },
      { choice: 'C', rationale: 'Student 1 predicted a bloom after phosphorus was added, but none formed.', trap: null },
      { choice: 'D', rationale: "The result matches Student 2's prediction, so it does not weaken that view.", trap: null },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'Decide whether each student is weakened, then eliminate choices that disagree.' },
    ],
  },
]

const SAT_RW: FixtureQuestion[] = [
  {
    id: 'sat-rw-01',
    exam_family: 'sat',
    section: 'reading_writing',
    difficulty: 1,
    passage:
      'When the town of Millbrook painted protected bike lanes along Harbor Avenue, some business owners worried that losing dozens of street parking spaces would drive their regular customers away to the mall across town. Instead, a survey conducted one year later found that the number of cyclists using the avenue ______ by nearly 30 percent, and most shop owners reported steady or rising sales.',
    stem: 'Which choice completes the text so that it conforms to the conventions of Standard English?',
    choices: [
      { key: 'A', text: 'have increased' },
      { key: 'B', text: 'had increased' },
      { key: 'C', text: 'increasing' },
      { key: 'D', text: 'to increase' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 55,
    primary_skill_key: 'sat_standard_english',
    hints: ["What is the subject of the verb: 'the number' or 'cyclists'?", 'The clause needs a complete verb.'],
    teaching_explanation:
      "The subject is 'the number,' which is singular, and the survey happened in the past. 'Had increased' is a complete verb that works with a singular subject and fits the past-tense context.",
    strategy_explanation: "Cross out 'of cyclists using the avenue' to find the subject, then eliminate any choice that is plural or not a full verb.",
    remember: "'The number of ...' is singular.",
    distractors: [
      { choice: 'A', rationale: "'Have increased' is plural; it agrees with 'cyclists' instead of the subject 'the number.'", trap: 'nearest_noun_agreement' },
      { choice: 'C', rationale: "'Increasing' is not a complete verb, so the clause has no main verb.", trap: null },
      { choice: 'D', rationale: "'To increase' is not a main verb, leaving the clause incomplete.", trap: null },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'Eliminate the non-verbs and the plural verb.' },
    ],
  },
  {
    id: 'sat-rw-02',
    exam_family: 'sat',
    section: 'reading_writing',
    difficulty: 2,
    passage:
      'Marine biologist Lena Ortiz spent three seasons recording the songs of humpback whales off the coast of Hawaii, often listening for hours from a small boat. She found that the songs were not fixed: each year, the whales ______ their melodies, adding new phrases and dropping old ones, so that the song heard in one season was noticeably different from the song heard two seasons later.',
    stem: 'Which choice completes the text with the most logical and precise word or phrase?',
    choices: [
      { key: 'A', text: 'abandoned' },
      { key: 'B', text: 'revised' },
      { key: 'C', text: 'memorized' },
      { key: 'D', text: 'silenced' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 60,
    primary_skill_key: 'sat_craft_structure',
    hints: ["Look at the words right after the blank: 'adding new phrases and dropping old ones.'", 'Which word means changing something while keeping some of it?'],
    teaching_explanation:
      "The text says the whales were 'adding new phrases and dropping old ones.' That describes changing a song piece by piece, which is what 'revised' means.",
    strategy_explanation: 'Use the explanation after the colon and blank as your clue, predict "changed," and match.',
    remember: 'The clue to a blank is usually in the same sentence.',
    distractors: [
      { choice: 'A', rationale: "'Abandoned' means giving up entirely, but the whales kept singing and kept some phrases.", trap: 'extreme_language' },
      { choice: 'C', rationale: "'Memorized' suggests keeping the song the same, which contradicts the changes described.", trap: null },
      { choice: 'D', rationale: "'Silenced' means stopped, but the whales went on singing new versions.", trap: null },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Predict "changed" from the context, then pick the closest word.' },
    ],
  },
  {
    id: 'sat-rw-03',
    exam_family: 'sat',
    section: 'reading_writing',
    difficulty: 2,
    passage:
      "Honeybees share the location of food through a movement known as the 'waggle dance.' When a forager returns to the hive, she walks in a figure-eight pattern, and the angle of the straight 'waggle' part of the dance indicates the direction of the food relative to the sun. ______ the length of time the bee spends waggling signals distance: longer waggles point to flowers farther away.",
    stem: 'Which choice completes the text with the most logical transition?',
    choices: [
      { key: 'A', text: 'However,' },
      { key: 'B', text: 'Additionally,' },
      { key: 'C', text: 'For instance,' },
      { key: 'D', text: 'As a result,' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 55,
    primary_skill_key: 'sat_expression_of_ideas',
    hints: ['The earlier sentence describes how the dance signals direction. What does the next sentence describe?', 'Is the new information a contrast, an example, a result, or another piece of the same idea?'],
    teaching_explanation:
      "The text first explains how the dance shows direction, then explains how it shows distance. These are two separate pieces of information the dance carries, so 'Additionally' correctly signals that one more point is being added.",
    strategy_explanation: 'Name the relationship between the two sentences before looking at the choices. Here it is "and also."',
    remember: 'Pick the transition after naming the relationship.',
    distractors: [
      { choice: 'A', rationale: 'Distance does not contrast with direction; both are things the dance communicates.', trap: 'wrong_transition' },
      { choice: 'C', rationale: 'Distance is not an example of direction; it is a separate piece of information.', trap: 'wrong_transition' },
      { choice: 'D', rationale: 'The length of the waggle is not caused by the angle of the dance.', trap: 'wrong_transition' },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Predict "also," then match to Additionally.' },
    ],
  },
  {
    id: 'sat-rw-04',
    exam_family: 'sat',
    section: 'reading_writing',
    difficulty: 3,
    passage:
      'For many years, historians assumed that the great medieval trade fairs of Champagne, in northern France, faded because new sea routes made long overland journeys less necessary. One economic historian’s analysis of tax and trade records tells a different story. The records show that the fairs began to decline before the sea routes were widely used, and that the decline matched a period when regional rulers raised taxes on visiting merchants and offered them less protection.',
    stem: 'Which choice best states the main idea of the text?',
    choices: [
      { key: 'A', text: 'An analysis of historical records challenges a long-standing explanation for why the Champagne fairs declined.' },
      { key: 'B', text: 'New sea routes were the main reason merchants stopped traveling to the Champagne fairs.' },
      { key: 'C', text: 'Medieval rulers always protected the merchants who traveled to regional fairs.' },
      { key: 'D', text: 'Tax records are the only reliable source of information about medieval trade.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 70,
    primary_skill_key: 'sat_information_ideas',
    hints: ["Notice the phrase 'tells a different story.' Different from what?"],
    teaching_explanation:
      'The text sets up an older explanation (sea routes) and then presents new evidence that the decline began earlier and matched political changes. The main idea is that this evidence challenges the traditional explanation.',
    strategy_explanation: 'Texts that start with "for many years, people assumed" usually go on to challenge that assumption. Look for the choice that captures the challenge.',
    remember: '"For years, people thought..." signals a challenge is coming.',
    distractors: [
      { choice: 'B', rationale: 'This is the older view that the text questions, not the main idea.', trap: null },
      { choice: 'C', rationale: "'Always' contradicts the text, which says rulers offered merchants less protection.", trap: 'extreme_language' },
      { choice: 'D', rationale: "'Only reliable source' goes far beyond anything the text claims.", trap: 'extreme_language' },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Predict "new evidence challenges the old explanation," then match to A.' },
    ],
  },
  {
    id: 'sat-rw-05',
    exam_family: 'sat',
    section: 'reading_writing',
    difficulty: 3,
    passage:
      "Stretching along the Pacific coast of South America, Chile's Atacama Desert receives so little rain that scientists use parts of it to test equipment designed for Mars. The air is so dry that wooden structures left there decay very slowly. The desert is one of the driest places on ______ some of its weather stations have gone years without recording any measurable rainfall.",
    stem: 'Which choice completes the text so that it conforms to the conventions of Standard English?',
    choices: [
      { key: 'A', text: 'Earth; ' },
      { key: 'B', text: 'Earth, ' },
      { key: 'C', text: 'Earth ' },
      { key: 'D', text: 'Earth, and, ' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 60,
    primary_skill_key: 'sat_standard_english',
    hints: ['Is there a complete sentence on each side of the blank?', 'Which punctuation can join two complete sentences on its own?'],
    teaching_explanation:
      "'The desert is one of the driest places on Earth' and 'some of its weather stations have gone years without recording any measurable rainfall' are both independent clauses. A semicolon correctly joins two independent clauses.",
    strategy_explanation: 'Check both sides of the blank for complete sentences; if both are complete, choose a semicolon, period, or comma plus conjunction.',
    remember: 'Two full sentences can share a semicolon, never just a comma.',
    distractors: [
      { choice: 'B', rationale: 'A comma alone between two independent clauses is a comma splice.', trap: 'comma_splice' },
      { choice: 'C', rationale: 'With no punctuation, the two clauses run together into a fused sentence.', trap: 'comma_splice' },
      { choice: 'D', rationale: "The comma after 'and' is incorrect; it separates the conjunction from the clause it introduces.", trap: null },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'Identify two complete clauses, then eliminate the comma-only and no-punctuation options.' },
    ],
  },
  {
    id: 'sat-rw-06',
    exam_family: 'sat',
    section: 'reading_writing',
    difficulty: 3,
    passage:
      'A student is researching how library use changed in her city. She finds the following visit counts.\n\nBranch | 2022 visits | 2024 visits\nCentral | 120,000 | 108,000\nEastside | 45,000 | 61,000\nRiverside | 38,000 | 52,000\n\nThe student claims that while visits to the large Central branch fell between 2022 and 2024, visits to the two smaller branches grew.',
    stem: 'Which choice most effectively uses data from the table to support the student’s claim?',
    choices: [
      { key: 'A', text: 'Central had 108,000 visits in 2024, more than any other branch that year.' },
      { key: 'B', text: "Central's visits fell from 120,000 to 108,000, while Eastside's rose from 45,000 to 61,000 and Riverside's rose from 38,000 to 52,000." },
      { key: 'C', text: 'Eastside had 45,000 visits in 2022.' },
      { key: 'D', text: 'Riverside had fewer visits than Eastside in both 2022 and 2024.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 70,
    primary_skill_key: 'sat_information_ideas',
    hints: ['The claim has two parts. What are they?', 'Which choice addresses both parts with numbers from both years?'],
    teaching_explanation:
      "The claim says Central's visits fell and the smaller branches' visits grew. Only B gives the change over time for all three branches, showing the decline at Central and the increases at Eastside and Riverside.",
    strategy_explanation: 'Break the claim into parts and check off each part against every choice. The right answer covers all of them.',
    remember: 'Support every part of the claim, not just one.',
    distractors: [
      { choice: 'A', rationale: 'Accurate, but it shows Central is the largest, not that its visits fell.', trap: 'true_but_irrelevant' },
      { choice: 'C', rationale: 'A single year cannot show growth over time.', trap: 'partial_answer' },
      { choice: 'D', rationale: 'Accurate, but comparing two branches to each other does not address change over time.', trap: 'true_but_irrelevant' },
    ],
    strategies: [
      { strategy_key: 'read_question_first', role: 'primary', is_fastest: true, explanation: 'Identify the two-part claim first, then look for the one choice that addresses both parts.' },
    ],
  },
  {
    id: 'sat-rw-07',
    exam_family: 'sat',
    section: 'reading_writing',
    difficulty: 4,
    passage:
      "The following text is from a novel. In the opening chapter, the narrator describes the family farm in loving detail: the creak of the porch swing, the smell of cut hay drying in the sun, the rows of corn stretching all the way to the tree line, and the old dog asleep in the shade of the barn. Only on the chapter's final page does the narrator mention that the farm was sold decades ago and that she has not seen it since she was a child.",
    stem: 'Which choice best describes the function of the final sentence in the overall structure of the text?',
    choices: [
      { key: 'A', text: 'It reveals information that recasts the earlier description as a memory rather than a present scene.' },
      { key: 'B', text: "It shows that the narrator's earlier description of the farm was deliberately inaccurate." },
      { key: 'C', text: 'It introduces a new character who will narrate the rest of the novel.' },
      { key: 'D', text: 'It summarizes the sensory details listed earlier in the text.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 80,
    primary_skill_key: 'sat_craft_structure',
    hints: ['How does your understanding of the farm description change after you read the last sentence?'],
    teaching_explanation:
      'The vivid details seem at first to describe a place the narrator is in now. The final sentence reveals the farm was sold long ago, so the reader realizes the description is a memory. That is a shift in how the earlier details are understood.',
    strategy_explanation: 'For function questions, ask what a sentence does to the rest of the text, not just what it says.',
    remember: 'Function questions ask what a sentence does, not what it says.',
    distractors: [
      { choice: 'B', rationale: 'Nothing suggests the description was false; it is remembered, not invented.', trap: 'out_of_scope' },
      { choice: 'C', rationale: 'The same narrator is speaking throughout; no new character is introduced.', trap: null },
      { choice: 'D', rationale: 'The final sentence adds new information rather than repeating the earlier details.', trap: null },
    ],
    strategies: [
      { strategy_key: 'predict_then_match', role: 'primary', is_fastest: true, explanation: 'Predict "it reveals a twist that changes how we read the description," then match to A.' },
    ],
  },
  {
    id: 'sat-rw-08',
    exam_family: 'sat',
    section: 'reading_writing',
    difficulty: 4,
    passage:
      'While researching a topic, a student has taken the following notes:\n\n• The axolotl is a salamander native to lakes near Mexico City.\n• Unlike most salamanders, axolotls usually keep their gills and remain aquatic as adults.\n• Axolotls can regrow lost limbs as well as parts of the heart and spinal cord.\n• Scientists study axolotls to learn how tissue regeneration might be encouraged in other animals.',
    stem: 'The student wants to emphasize why scientists are interested in axolotls. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
    choices: [
      { key: 'A', text: 'Axolotls, salamanders native to lakes near Mexico City, usually remain aquatic as adults.' },
      { key: 'B', text: 'Because axolotls can regrow limbs and even parts of the heart and spinal cord, scientists study them to learn how regeneration might be encouraged in other animals.' },
      { key: 'C', text: 'Unlike most salamanders, axolotls usually keep their gills as adults.' },
      { key: 'D', text: 'Axolotls live in lakes near Mexico City, where they are one of many salamander species.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 75,
    primary_skill_key: 'sat_expression_of_ideas',
    hints: ['Focus on the goal in the question, not on which choice sounds most interesting.', 'Which note mentions scientists?'],
    teaching_explanation:
      "The goal is to emphasize why scientists are interested. Choice B connects axolotls' regeneration ability to the reason scientists study them, using the two notes that address that goal.",
    strategy_explanation: 'Read the goal first, then eliminate any choice that does not directly accomplish it, no matter how accurate.',
    remember: 'Rhetorical synthesis: the goal decides, not the facts.',
    distractors: [
      { choice: 'A', rationale: 'Accurate, but it says nothing about why scientists study axolotls.', trap: 'true_but_irrelevant' },
      { choice: 'C', rationale: 'Accurate, but it describes their gills, not scientific interest.', trap: 'true_but_irrelevant' },
      { choice: 'D', rationale: "The notes do not mention 'many salamander species' in those lakes, and the choice ignores the goal.", trap: 'out_of_scope' },
    ],
    strategies: [
      { strategy_key: 'read_question_first', role: 'primary', is_fastest: true, explanation: 'Read the goal before the notes, then go straight to the choice that mentions scientists and why.' },
    ],
  },
  {
    id: 'sat-rw-09',
    exam_family: 'sat',
    section: 'reading_writing',
    difficulty: 5,
    passage:
      "Ecologists studying a grassland noticed that a certain wildflower produced far more seedlings in plots where ants were present than in plots where ants had been kept out. The flower's seeds carry a small fatty attachment that ants carry back to their nests and eat; the ants then discard the seeds themselves in nutrient-rich waste piles, where seedlings grow well. The researchers also observed that ants never visited the flowers' blossoms and did not pollinate them. Taken together, these findings suggest that the ants' benefit to the wildflower ______",
    stem: 'Which choice most logically completes the text?',
    choices: [
      { key: 'A', text: 'results from the ants pollinating the flowers while collecting seeds.' },
      { key: 'B', text: 'comes from where the ants deposit the seeds rather than from any role in pollination.' },
      { key: 'C', text: 'depends on the ants eating the seeds themselves.' },
      { key: 'D', text: 'is probably outweighed by the harm ants cause by carrying seeds away from the parent plant.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 90,
    primary_skill_key: 'sat_information_ideas',
    hints: ['List what the ants do and do not do according to the text.', 'Where do the seedlings that benefit from ants actually grow?'],
    teaching_explanation:
      'The ants eat only the fatty attachment, discard the seeds in nutrient-rich piles where seedlings thrive, and never pollinate the flowers. So the benefit must come from where the ants place the seeds, not from pollination.',
    strategy_explanation: 'For logical-completion items, build the conclusion from each sentence in turn and reject any choice that contradicts even one sentence.',
    remember: 'A logical completion must agree with every sentence in the text.',
    distractors: [
      { choice: 'A', rationale: 'The text states directly that ants did not pollinate the flowers.', trap: null },
      { choice: 'C', rationale: 'The ants eat the fatty attachment, not the seeds; they discard the seeds.', trap: null },
      { choice: 'D', rationale: 'The data show more seedlings where ants are present, so there is no evidence of net harm.', trap: 'out_of_scope' },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'Each wrong choice contradicts a specific sentence; cross them out one by one.' },
      { strategy_key: 'predict_then_match', role: 'secondary', is_fastest: false, explanation: 'Predict "the benefit is seed placement, not pollination," then match.' },
    ],
  },
  {
    id: 'sat-rw-10',
    exam_family: 'sat',
    section: 'reading_writing',
    difficulty: 3,
    passage:
      "Each spring, a high school cross-country team from Colorado travels to a regional race held at sea level. Coaches have long believed that training at high elevation, where the air holds less oxygen, helps runners perform better when they race at lower elevations. This year's results seemed to support that belief. Having trained for months in the thin mountain air, ______",
    stem: 'Which choice completes the text so that it conforms to the conventions of Standard English?',
    choices: [
      { key: 'A', text: 'the race was completed easily by the team.' },
      { key: 'B', text: 'the team completed the race with energy to spare.' },
      { key: 'C', text: "the team's victory came easily." },
      { key: 'D', text: 'energy was left to spare by the team.' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 60,
    primary_skill_key: 'sat_standard_english',
    hints: ['Who trained for months in the mountain air?', 'That noun needs to come right after the comma.'],
    teaching_explanation:
      "The introductory phrase 'Having trained for months in the thin mountain air' describes whoever did the training: the team. In B, 'the team' comes immediately after the comma, so the modifier is attached to the right noun.",
    strategy_explanation: 'With an opening modifier, check only the first noun after the comma. Eliminate every choice where it is not the one doing the action.',
    remember: 'Opening phrase? The very next noun must be the doer.',
    distractors: [
      { choice: 'A', rationale: 'This says the race trained for months, which is illogical.', trap: 'misplaced_modifier' },
      { choice: 'C', rationale: "The noun after the comma is 'victory,' so the victory appears to have done the training.", trap: 'misplaced_modifier' },
      { choice: 'D', rationale: "This makes 'energy' the thing that trained for months.", trap: 'misplaced_modifier' },
    ],
    strategies: [
      { strategy_key: 'process_of_elimination', role: 'primary', is_fastest: true, explanation: 'Look at the first noun in each choice; only B starts with the team.' },
    ],
  },
]

const SAT_MATH: FixtureQuestion[] = [
  {
    id: 'sat-math-01',
    exam_family: 'sat',
    section: 'math',
    difficulty: 1,
    stem: 'If 3x + 5 = 20, what is the value of 6x + 10?',
    choices: [
      { key: 'A', text: '15' },
      { key: 'B', text: '30' },
      { key: 'C', text: '40' },
      { key: 'D', text: '45' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 60,
    primary_skill_key: 'sat_algebra',
    hints: ['How is 6x + 10 related to 3x + 5?'],
    teaching_explanation:
      '6x + 10 is exactly 2(3x + 5). Since 3x + 5 = 20, 6x + 10 = 2 × 20 = 40. Solving for x first (x = 5) gives the same result: 6(5) + 10 = 40.',
    strategy_explanation: 'Look for a multiple of the given expression before solving for x. Doubling both sides takes one step.',
    remember: 'Before solving, check whether the target is a multiple of what you know.',
    distractors: [
      { choice: 'A', rationale: '15 is the value of 3x, a middle step.', trap: 'partial_answer' },
      { choice: 'B', rationale: '30 is the value of 6x; the +10 was left off.', trap: 'partial_answer' },
      { choice: 'D', rationale: 'This doubles only the 20 and then adds 5, mixing up the two expressions.', trap: null },
    ],
    strategies: [
      { strategy_key: 'translate_to_algebra', role: 'primary', is_fastest: true, explanation: 'Notice 6x + 10 = 2(3x + 5) = 40.' },
    ],
  },
  {
    id: 'sat-math-02',
    exam_family: 'sat',
    section: 'math',
    difficulty: 2,
    stem: 'A store sold 240 shirts in May and 300 shirts in June. By what percent did the number of shirts sold increase from May to June?',
    choices: [
      { key: 'A', text: '20%' },
      { key: 'B', text: '25%' },
      { key: 'C', text: '60%' },
      { key: 'D', text: '125%' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 75,
    primary_skill_key: 'sat_problem_solving_data',
    hints: ['Percent change = (new − old) ÷ old.', 'Which month is the starting point?'],
    teaching_explanation:
      'The increase is 300 − 240 = 60 shirts. Percent change compares the increase to the original amount: 60 ÷ 240 = 0.25, or 25%.',
    strategy_explanation: 'Always divide the change by the original (starting) value.',
    remember: 'Percent change: divide by where you started.',
    distractors: [
      { choice: 'A', rationale: 'This divides by the new value: 60 ÷ 300 = 20%.', trap: 'wrong_quantity' },
      { choice: 'C', rationale: '60 is the number of extra shirts, not a percent.', trap: 'partial_answer' },
      { choice: 'D', rationale: "125% is June's sales as a percent of May's, not the increase.", trap: 'wrong_quantity' },
    ],
    strategies: [
      { strategy_key: 'translate_to_algebra', role: 'primary', is_fastest: true, explanation: '(300 − 240) / 240 = 0.25.' },
    ],
  },
  {
    id: 'sat-math-03',
    exam_family: 'sat',
    section: 'math',
    difficulty: 2,
    stem:
      'A phone plan charges a monthly fee of $15 plus $0.10 for each text message sent. If a customer’s bill for one month was $27.50, how many text messages did the customer send that month?',
    choices: [],
    answer_format: 'numeric',
    accepted_answers: ['125'],
    expected_time_seconds: 75,
    primary_skill_key: 'sat_algebra',
    hints: ['Write an equation with t for the number of texts.', 'Subtract the fixed fee first.'],
    teaching_explanation:
      'The bill is 15 + 0.10t = 27.50. Subtracting 15 gives 0.10t = 12.50, so t = 125 text messages.',
    strategy_explanation: 'Remove the fixed part, then divide by the per-unit rate.',
    remember: 'Total = fixed fee + rate × units.',
    distractors: [],
    strategies: [
      { strategy_key: 'translate_to_algebra', role: 'primary', is_fastest: true, explanation: 'Write 15 + 0.10t = 27.50 and solve.' },
    ],
  },
  {
    id: 'sat-math-04',
    exam_family: 'sat',
    section: 'math',
    difficulty: 3,
    stem: 'The expression (x + 3)(x − 5) is equivalent to x² + bx + c, where b and c are constants. What is the value of b + c?',
    choices: [
      { key: 'A', text: '−17' },
      { key: 'B', text: '−13' },
      { key: 'C', text: '13' },
      { key: 'D', text: '−15' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 85,
    primary_skill_key: 'sat_advanced_math',
    hints: ['Multiply out using FOIL.', 'Combine the two x terms carefully, watching the signs.'],
    teaching_explanation:
      '(x + 3)(x − 5) = x² − 5x + 3x − 15 = x² − 2x − 15. So b = −2 and c = −15, and b + c = −17.',
    strategy_explanation: 'Expand, read off b and c, and add. Or plug in x = 1: (4)(−4) = −16 = 1 + b + c, so b + c = −17.',
    remember: 'Plug in x = 1 to get 1 + b + c instantly.',
    distractors: [
      { choice: 'B', rationale: 'This uses b = +2 instead of −2.', trap: 'sign_error' },
      { choice: 'C', rationale: 'This uses c = +15 instead of −15.', trap: 'sign_error' },
      { choice: 'D', rationale: '−15 is c alone; b was not added.', trap: 'partial_answer' },
    ],
    strategies: [
      { strategy_key: 'plug_in_numbers', role: 'primary', is_fastest: true, explanation: 'At x = 1, the expression equals 1 + b + c, and (1 + 3)(1 − 5) = −16, so b + c = −17.' },
      { strategy_key: 'translate_to_algebra', role: 'secondary', is_fastest: false, explanation: 'Expand fully and add the coefficients.' },
    ],
  },
  {
    id: 'sat-math-05',
    exam_family: 'sat',
    section: 'math',
    difficulty: 3,
    stem: 'A right circular cylinder has a radius of 3 centimeters and a height of 10 centimeters. What is the volume of the cylinder, in cubic centimeters?',
    choices: [
      { key: 'A', text: '30π' },
      { key: 'B', text: '60π' },
      { key: 'C', text: '90π' },
      { key: 'D', text: '180π' },
    ],
    answer_format: 'choice',
    accepted_answers: ['C'],
    expected_time_seconds: 70,
    primary_skill_key: 'sat_geometry_trig',
    hints: ['Volume of a cylinder = area of the circular base × height.'],
    teaching_explanation: 'V = πr²h = π(3²)(10) = π(9)(10) = 90π cubic centimeters.',
    strategy_explanation: 'The SAT reference sheet lists V = πr²h. Square the radius before multiplying.',
    remember: 'Cylinder volume: base area (πr²) times height.',
    distractors: [
      { choice: 'A', rationale: 'This uses πrh, forgetting to square the radius.', trap: null },
      { choice: 'B', rationale: '60π is 2πrh, the curved surface area, not the volume.', trap: 'wrong_quantity' },
      { choice: 'D', rationale: '180π is double the correct volume; the base area πr² should not be multiplied by 2.', trap: null },
    ],
    strategies: [
      { strategy_key: 'translate_to_algebra', role: 'primary', is_fastest: true, explanation: 'Substitute directly into V = πr²h.' },
    ],
  },
  {
    id: 'sat-math-06',
    exam_family: 'sat',
    section: 'math',
    difficulty: 3,
    stem:
      'A teacher modeled the relationship between hours spent studying and test scores with the equation y = 2.5x + 40, where y is the predicted test score and x is the number of hours spent studying. What is the best interpretation of 2.5 in this context?',
    choices: [
      { key: 'A', text: 'The predicted score for a student who does not study' },
      { key: 'B', text: 'The predicted increase in score for each additional hour of study' },
      { key: 'C', text: 'The number of hours a student must study to pass' },
      { key: 'D', text: 'The highest score a student can earn' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 60,
    primary_skill_key: 'sat_problem_solving_data',
    hints: ['In y = mx + b, what does m represent?', 'What happens to y when x goes up by 1?'],
    teaching_explanation:
      '2.5 is the slope. Each time x (hours) increases by 1, the predicted score y increases by 2.5 points. The 40 is the y-intercept, the predicted score with 0 hours of study.',
    strategy_explanation: 'For "interpret the number" questions, label the slope as "per one unit of x" and the intercept as "when x is 0."',
    remember: 'Slope = change in y per one unit of x.',
    distractors: [
      { choice: 'A', rationale: 'That describes the y-intercept, 40, not 2.5.', trap: 'wrong_quantity' },
      { choice: 'C', rationale: 'The equation says nothing about a passing score.', trap: 'out_of_scope' },
      { choice: 'D', rationale: 'A linear model has no maximum; 2.5 is a rate, not a score.', trap: null },
    ],
    strategies: [
      { strategy_key: 'plug_in_numbers', role: 'primary', is_fastest: true, explanation: 'Compare x = 1 and x = 2: y goes from 42.5 to 45, an increase of 2.5.' },
    ],
  },
  {
    id: 'sat-math-07',
    exam_family: 'sat',
    section: 'math',
    difficulty: 4,
    stem: 'The function f is defined by f(x) = 3x² − 12x + 7. What is the minimum value of f(x)?',
    choices: [],
    answer_format: 'numeric',
    accepted_answers: ['-5', '−5'],
    expected_time_seconds: 100,
    primary_skill_key: 'sat_advanced_math',
    hints: ['The minimum of an upward-opening parabola occurs at its vertex.', 'The vertex x-coordinate is −b / (2a).'],
    teaching_explanation:
      'Because a = 3 > 0, the parabola opens upward and its minimum is at the vertex. The vertex is at x = −(−12) / (2 · 3) = 2, and f(2) = 3(4) − 24 + 7 = −5.',
    strategy_explanation: 'Find x = −b/(2a), then substitute it back in. The question asks for the minimum value (the y-value), not where it occurs.',
    remember: 'Minimum value is the y-coordinate of the vertex.',
    distractors: [],
    strategies: [
      { strategy_key: 'translate_to_algebra', role: 'primary', is_fastest: true, explanation: 'Use x = −b/(2a) = 2, then evaluate f(2) = −5.' },
      { strategy_key: 'read_question_first', role: 'secondary', is_fastest: false, explanation: 'Notice the question asks for the minimum value, so do not stop at x = 2.' },
    ],
  },
  {
    id: 'sat-math-08',
    exam_family: 'sat',
    section: 'math',
    difficulty: 3,
    stem: 'A line in the xy-plane passes through the points (2, 5) and (6, 13). Which equation represents the line?',
    choices: [
      { key: 'A', text: 'y = 2x + 1' },
      { key: 'B', text: 'y = 2x + 5' },
      { key: 'C', text: 'y = (1/2)x + 4' },
      { key: 'D', text: 'y = 2x − 1' },
    ],
    answer_format: 'choice',
    accepted_answers: ['A'],
    expected_time_seconds: 80,
    primary_skill_key: 'sat_algebra',
    hints: ['Slope = (change in y) ÷ (change in x).', 'Use one point to find the y-intercept.'],
    teaching_explanation:
      'Slope = (13 − 5) / (6 − 2) = 8 / 4 = 2. Using (2, 5): 5 = 2(2) + b, so b = 1. The line is y = 2x + 1. Check with (6, 13): 2(6) + 1 = 13.',
    strategy_explanation: 'Plug one given point into each choice; only one equation passes through both points.',
    remember: 'Check both points in your equation.',
    distractors: [
      { choice: 'B', rationale: "This uses the first point's y-value, 5, as the y-intercept.", trap: 'wrong_quantity' },
      { choice: 'C', rationale: 'This computes slope as run over rise, (6 − 2)/(13 − 5), flipping the fraction.', trap: null },
      { choice: 'D', rationale: 'This has the wrong sign on the y-intercept.', trap: 'sign_error' },
    ],
    strategies: [
      { strategy_key: 'backsolve', role: 'primary', is_fastest: true, explanation: 'Test (2, 5) in each choice: only A and C pass. Then test (6, 13): only A works.' },
      { strategy_key: 'translate_to_algebra', role: 'secondary', is_fastest: false, explanation: 'Compute the slope, then the intercept.' },
    ],
  },
  {
    id: 'sat-math-09',
    exam_family: 'sat',
    section: 'math',
    difficulty: 4,
    stem: 'Points A and B lie on a circle with center O and radius 6. Central angle AOB measures 120°. What is the length of the minor arc AB?',
    choices: [
      { key: 'A', text: '2π' },
      { key: 'B', text: '4π' },
      { key: 'C', text: '12π' },
      { key: 'D', text: '8π' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 90,
    primary_skill_key: 'sat_geometry_trig',
    hints: ['What fraction of the full circle is 120°?', 'Arc length is that fraction of the circumference.'],
    teaching_explanation:
      'The circumference is 2π(6) = 12π. An angle of 120° is 120/360 = 1/3 of the circle, so the minor arc length is (1/3)(12π) = 4π.',
    strategy_explanation: 'Arc length = (angle/360) × 2πr. Make sure you use circumference, not area.',
    remember: 'Arc length uses circumference; sector area uses πr².',
    distractors: [
      { choice: 'A', rationale: 'This takes 1/3 of πr (6π) instead of 1/3 of the circumference 2πr.', trap: null },
      { choice: 'C', rationale: '12π is both the full circumference and the sector area, not the arc length.', trap: 'wrong_quantity' },
      { choice: 'D', rationale: '8π is the major arc (240°), not the minor arc.', trap: 'wrong_quantity' },
    ],
    strategies: [
      { strategy_key: 'draw_it_out', role: 'primary', is_fastest: true, explanation: 'Sketch the circle and see that 120° is one-third of the way around.' },
    ],
  },
  {
    id: 'sat-math-10',
    exam_family: 'sat',
    section: 'math',
    difficulty: 5,
    stem:
      'A colony of bacteria starts with 500 cells and triples in size every 4 hours. Which expression gives the number of cells in the colony after t days?',
    choices: [
      { key: 'A', text: '500(3)^(t/4)' },
      { key: 'B', text: '500(3)^(6t)' },
      { key: 'C', text: '500(3)^(4t)' },
      { key: 'D', text: '500(3)^(t/6)' },
    ],
    answer_format: 'choice',
    accepted_answers: ['B'],
    expected_time_seconds: 110,
    primary_skill_key: 'sat_advanced_math',
    hints: ['Notice that t is measured in days, but tripling happens every 4 hours.', 'How many 4-hour periods are in one day?'],
    teaching_explanation:
      'There are 24 ÷ 4 = 6 tripling periods in each day, so in t days the colony triples 6t times. The number of cells is 500 · 3^(6t). Check: after 1 day, 500 · 3⁶ = 364,500, which matches tripling six times.',
    strategy_explanation: 'Plug in t = 1 day and count: the colony should triple 6 times. Only 3^(6t) gives exponent 6.',
    remember: 'Exponent = number of growth periods, in the units of t.',
    distractors: [
      { choice: 'A', rationale: 'This would be correct if t were in hours, but t is in days.', trap: 'wrong_quantity' },
      { choice: 'C', rationale: 'This uses 4 tripling periods per day instead of 6.', trap: null },
      { choice: 'D', rationale: 'This divides by 6 instead of multiplying, so the colony would triple only once every 6 days.', trap: null },
    ],
    strategies: [
      { strategy_key: 'plug_in_numbers', role: 'primary', is_fastest: true, explanation: 'Set t = 1; one day has six 4-hour periods, so the exponent must be 6.' },
    ],
  },
]

export const QUESTIONS: FixtureQuestion[] = [...ACT_ENGLISH, ...ACT_MATH, ...ACT_READING, ...ACT_SCIENCE, ...SAT_RW, ...SAT_MATH]
