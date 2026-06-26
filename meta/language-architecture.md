# Spanish Language Architecture

Reverse-engineering the language as a system. Not grammar rules — operating patterns.

This is the meta-system: how Spanish actually works, decomposed for a systems thinker who reverse-engineers machines before operating them.

**Design philosophy:** Spanish is a runtime. You are learning its instruction set, memory model, and execution patterns. Once you see the machine, you stop memorizing and start generating.

---

## Table of Contents

- [The Machine Model](#the-machine-model)
- [Layer 1: Sound System (I/O)](#layer-1-the-sound-system-io)
- [Layer 2: Word Formation (Data Types)](#layer-2-word-formation-data-types)
- [Layer 3: The Noun Phrase (Object Model)](#layer-3-the-noun-phrase-object-model)
- [Layer 4: The Verb Engine (CPU)](#layer-4-the-verb-engine-cpu)
- [Layer 5: Sentence Assembly (Compiler)](#layer-5-sentence-assembly-compiler)
- [Layer 6: Pronoun System (Pointers)](#layer-6-the-pronoun-system-pointers)
- [Layer 7: The Number System](#layer-7-the-number-system)
- [Layer 8: Tense Map (Timeline)](#layer-8-the-tense-map-timeline)
- [Layer 9: Connectors (Control Flow)](#layer-9-connectors-control-flow)
- [Layer 10: Repair System (Error Handling)](#layer-10-the-repair-system-error-handling)
- [Layer 11: Pattern Templates (API)](#layer-11-pattern-templates-the-api)
- [Layer 12: Word Generation (Factory Methods)](#layer-12-word-generation-factory-methods)
- [Layer 13: Mexican Spanish (Target Runtime)](#layer-13-mexican-spanish-target-runtime)
- [Layer 14: Idiomatic Structures (Design Patterns)](#layer-14-idiomatic-structures-design-patterns)
- [The Unlock Sequence](#the-unlock-sequence)

---

## The Machine Model

Spanish is a simpler, more regular machine than English. The key architectural differences:

| Property | English | Spanish | German |
|----------|---------|---------|--------|
| Phonemes | ~44 | ~22 | ~30 |
| Spelling-to-sound | chaotic | 100% predictable | mostly predictable |
| Genders | 0 | 2 | 3 |
| Cases | 0 | 0 | 4 |
| Verb conjugations | minimal | rich (but regular) | rich |
| Subject required | always | usually dropped | always |
| Word order | rigid SVO | flexible SVO | V2 rule |
| Adjective position | before noun | after noun | before noun |
| "To be" | 1 verb | 2 verbs | 1 verb |
| Double negatives | illegal | required | illegal |

**The trade:** Spanish front-loads information into the verb (who, when, mood). English front-loads it into helper words and pronouns. Once you internalize verb endings, Spanish is more compact and faster to produce.

**Your German advantage:** You already have the mental infrastructure for gender, conjugation, and formal/informal address. Spanish removes 3 things German made hard (neuter gender, 4 cases, V2 word order) and adds 1 new thing (ser vs estar). Net: easier than German.

---

## Layer 1: The Sound System (I/O)

Spanish has the most predictable sound system of any major European language. If you can read it, you can say it. Period.

### The 5 Vowels: Constants, Not Variables

| Letter | Sound | IPA | Mouth shape | Never sounds like |
|--------|-------|-----|-------------|-------------------|
| **a** | "ah" | /a/ | wide open | English "a" in "cat" or "cake" |
| **e** | "eh" | /e/ | half open | English "ee" in "see" |
| **i** | "ee" | /i/ | tight smile | English "i" in "bit" |
| **o** | "oh" | /o/ | round, forward | English "o" in "hot" |
| **u** | "oo" | /u/ | tight circle | English "u" in "but" |

**Why this matters:** English has ~15 vowel sounds for 5 letters. Spanish has 5 for 5. One letter = one sound. Always. This is the single biggest reason Spanish pronunciation is learnable: **trust the vowels.**

### Diphthongs: Two Vowels, One Syllable

When a "strong" vowel (a, e, o) meets a "weak" vowel (i, u), they blend into one syllable:

| Combination | Sound | Example | Pronunciation |
|-------------|-------|---------|---------------|
| **ia** | "yah" | grac**ia**s | GRAH-syahs |
| **ie** | "yeh" | qu**ie**ro | KYEH-roh |
| **ue** | "weh" | b**ue**no | BWEH-noh |
| **ua** | "wah" | ag**ua** | AH-gwah |
| **io** | "yoh" | camb**io** | KAHM-byoh |
| **ei/ey** | "ay" | r**ei**na | RAY-nah |
| **ai/ay** | "eye" | h**ay** | EYE |
| **oi/oy** | "oy" | h**oy** | OY |
| **au** | "ow" | **au**to | OW-toh |

**Pattern:** Weak vowel (i/u) glides into or out of a strong vowel. Two strong vowels together = two syllables (*le-er*, *ca-er*).

### Consonant Map: What to Remap

Most consonants work like English. Only remap these:

#### Context-Sensitive Consonants (The "Soft Rule")

**c** and **g** change sound based on the next vowel:

```
Before a, o, u  →  HARD sound
Before e, i      →  SOFT sound
```

| Letter | Before a/o/u | Before e/i |
|--------|-------------|------------|
| **c** | "k" → **c**asa, **c**omo | "s" → **c**ine, gra**c**ias |
| **g** | "g" → **g**ato, **g**rande | "h" → **g**ente, ele**g**ir |

**The workaround:** When Spanish needs a hard sound before e/i:
- Hard "k" before e/i → uses **qu**: **qu**iero, **qu**e
- Hard "g" before e/i → uses **gu**: **gu**erra, **gu**ía

This is a complete, predictable system, not exceptions.

#### Letters That Don't Exist in English

| Letter | Sound | How to produce it | Example |
|--------|-------|-------------------|---------|
| **ñ** | "ny" | tongue on palate, like "onion" | a**ñ**o (AH-nyoh) |
| **ll** | "y" (Mexico) | like English "yes" | ca**ll**e (KAH-yeh) |
| **rr** | rolled | tongue tip vibrates on ridge | pe**rr**o (PEH-rroh) |

#### Letters That Lie

| Letter | You expect | Actually | Example |
|--------|-----------|----------|---------|
| **h** | "h" sound | **silent** | **h**ola = OH-lah |
| **j** | "j" sound | "h" (breathy) | tra**b**a**j**o = trah-BAH-hoh |
| **v** | "v" sound | "b" (identical) | **v**ino = BEE-noh |
| **z** | "z" buzz | "s" (Latin Am) | cerve**z**a = sehr-BEH-sah |

### The 3 Stress Rules (Complete System)

These 3 rules predict the stress of **every Spanish word**:

| Rule | Condition | Stress falls on | Examples |
|------|-----------|----------------|----------|
| **1** | Ends in vowel, **n**, or **s** | second-to-last syllable | **ca**-sa, **ha**-blan, gra-**ci**-as |
| **2** | Ends in any other consonant | last syllable | ha-**blar**, es-pa-**ñol**, ciu-**dad** |
| **3** | Has written accent (á é í ó ú) | the accented syllable | ca-**fé**, lá-**piz**, te-lé-**fo**-no |

**The accent mark is an override operator.** It says "ignore rules 1-2, stress me instead."

**Accent marks also disambiguate meaning:**

| Without accent | With accent |
|---------------|-------------|
| si (if) | sí (yes) |
| tu (your) | tú (you) |
| el (the) | él (he) |
| como (like/as) | cómo (how?) |
| que (that) | qué (what?) |
| donde (where) | dónde (where?) |

**Pattern:** Question words always have accents. This is not decoration; it's data.

### The "R" Subsystem

The Spanish "r" has 2 modes:

| Position | Sound | Technique | Example |
|----------|-------|-----------|---------|
| Single **r** (middle) | tap | tongue flicks roof once (like "butter" fast) | pe**r**o (but) |
| Double **rr** | trill | tongue vibrates on ridge | pe**rr**o (dog) |
| **r** at word start | trill | same as rr | **r**ojo, **r**ápido |
| **r** after l, n, s | trill | same as rr | al**r**ededor, Is**r**ael |

**Minimal pairs that matter:** pero (but) vs perro (dog). The difference is literally life-and-death for meaning.

🇩🇪 **German speaker:** Your German "r" (uvular, throat) is wrong for Spanish. Spanish "r" is **alveolar** (tongue tip on the ridge behind upper teeth). Practice: say "butter" fast in American English. That middle "tt" sound? That's the Spanish single "r."

---

## Layer 2: Word Formation (Data Types)

Before you learn grammar, understand how Spanish *constructs* words. This lets you decode vocabulary you've never seen.

### Roots, Prefixes, Suffixes: The Assembly System

Spanish is heavily Latinate. Words are built from predictable components:

```
prefix + ROOT + suffix = word
```

**Example decomposition:**

| Word | Prefix | Root | Suffix | Meaning |
|------|--------|------|--------|---------|
| des-conocido | des- (un-) | conoc- (know) | -ido (past part.) | unknown |
| in-creíble | in- (not) | cre- (believe) | -ible (able) | incredible |
| re-comenzar | re- (again) | comenz- (begin) | -ar (infinitive) | restart |
| des-empleo | des- (un-) | emple- (employ) | -o (noun) | unemployment |

### Common Prefixes (Modifiers)

| Prefix | Meaning | Example |
|--------|---------|---------|
| **des-** | un-, reverse | deshacer (undo), descansar (rest = un-tire) |
| **re-** | again | repetir (repeat), rehacer (redo) |
| **in-/im-** | not | imposible, increíble, informal |
| **pre-** | before | preparar, prevenir |
| **sobre-** | over/above | sobrevivir (survive), sobremesa (after-dinner chat) |
| **entre-** | between | entrenar (train), entrevista (interview) |

### Common Suffixes (Type Indicators)

These tell you what *kind* of word you're looking at:

| Suffix | Makes it a... | Example |
|--------|--------------|---------|
| **-ción/-sión** | noun (action/result) | educación, decisión |
| **-dad/-tad** | noun (quality) | ciudad (city), libertad (liberty) |
| **-miento** | noun (process) | conocimiento (knowledge), sentimiento (feeling) |
| **-ero/-era** | noun (person who does) | cocinero (cook), enfermera (nurse) |
| **-ería** | noun (place of) | panadería (bakery), carnicería (butcher shop) |
| **-oso/-osa** | adjective (full of) | famoso, peligroso (dangerous) |
| **-ble** | adjective (able) | posible, increíble |
| **-mente** | adverb (-ly) | rápidamente, naturalmente |
| **-ito/-ita** | diminutive (small/cute) | cafecito (little coffee), casita (little house) |
| **-ón/-ona** | augmentative (big) | casona (big house), sillón (armchair) |
| **-azo** | augmentative/strike | golpazo (big hit), portazo (door slam) |

**Power move:** When you hear an unknown word, *decompose it*. If you hear "desconocido," break it: des- (un-) + conoc- (know) + -ido (past participle). "Unknown person." You didn't memorize it. You derived it.

### The -ería Pattern (Places)

Once you know what something is, you know where it's sold/made:

| Product | Person | Place |
|---------|--------|-------|
| pan (bread) | panadero | panad**ería** |
| carne (meat) | carnicero | carnic**ería** |
| zapato (shoe) | zapatero | zapater**ía** |
| libro (book) | librero | libr**ería** |
| café (coffee) | — | cafet**ería** |
| taco | taquero | taqu**ería** |

**System:** noun stem + -ería = the shop. noun stem + -ero/-era = the person.

---

## Layer 3: The Noun Phrase (Object Model)

Every noun in Spanish is an *object* with properties: gender, number, and determiners that must all agree. Think of it like a strongly typed language.

### Gender: A 2-Value Type System

Every Spanish noun is either masculine (M) or feminine (F). No exceptions. No neuter.

**Prediction rules (covers ~90% of nouns):**

| Ending | Gender | Accuracy | Examples |
|--------|--------|----------|----------|
| **-o** | Masculine | ~99% | libro, gato, vino |
| **-a** | Feminine | ~96% | casa, mesa, comida |
| **-ción, -sión** | Feminine | 100% | nación, decisión |
| **-dad, -tad** | Feminine | 100% | ciudad, libertad |
| **-ma** (Greek) | Masculine | 100% | problema, sistema, programa |
| **-ista** | depends on person | — | el dentista / la dentista |
| **-e** | must memorize | — | el café, la calle, la noche, el nombre |
| consonant | must memorize | — | el color, la flor, el dolor, la ciudad |

**Exceptions worth memorizing (the usual suspects):**

| Word | Expected | Actual | Why it matters |
|------|----------|--------|----------------|
| la mano | masculine (-o) | F | very common |
| el día | feminine (-a) | M | you say it daily |
| el mapa | feminine (-a) | M | Greek origin |
| el problema | feminine (-a) | M | Greek origin |
| el agua | feminine (-a) | F (but uses "el") | sound rule (el + a-) |
| la radio | masculine (-o) | F | short for radiodifusión |

### The Agreement Chain

In Spanish, determiners, nouns, and adjectives must all agree in gender AND number. It's a chain:

```
[determiner] + [noun] + [adjective]
   must agree → ← must agree
```

**Example chain:**

| M singular | F singular | M plural | F plural |
|-----------|-----------|----------|----------|
| **el** café **caliente** | **la** casa **grande** | **los** cafés **calientes** | **las** casas **grandes** |
| **un** chico **alto** | **una** chica **alta** | **unos** chicos **altos** | **unas** chicas **altas** |
| **este** libro **nuevo** | **esta** mesa **nueva** | **estos** libros **nuevos** | **estas** mesas **nuevas** |
| **mucho** tiempo | **mucha** agua | **muchos** años | **muchas** gracias |

**Your session-1 error decoded:** "muchos gracias" broke because:
- gracias ← feminine plural (from *la gracia*)
- therefore: muchas (F-pl) + gracias (F-pl) ✓
- not: muchos (M-pl) + gracias (F-pl) ✗

### Pluralization Rules

| Noun ending | Add | Example |
|-------------|-----|---------|
| vowel | **-s** | casa → casas, café → cafés |
| consonant | **-es** | ciudad → ciudades, color → colores |
| **-z** | change to **-ces** | lápiz → lápices, vez → veces |

### Demonstratives (This/That System)

Spanish has 3 distances (English has 2):

| Distance | Masculine | Feminine | Plural M | Plural F |
|----------|-----------|----------|----------|----------|
| **here** (near me) | este | esta | estos | estas |
| **there** (near you) | ese | esa | esos | esas |
| **over there** (far) | aquel | aquella | aquellos | aquellas |

**Usage:** "Quiero **este** café" (this one here), "¿Qué es **eso**?" (what's that?)

### Possessives (Before the Noun)

| Owner | Before M-sg | Before F-sg | Before plural |
|-------|-------------|-------------|---------------|
| my | **mi** | **mi** | **mis** |
| your (tú) | **tu** | **tu** | **tus** |
| his/her/your (Ud.) | **su** | **su** | **sus** |
| our | **nuestro** | **nuestra** | **nuestros/nuestras** |
| their/your (Uds.) | **su** | **su** | **sus** |

**Note:** *mi/tu/su* don't change for gender (only *nuestro* does). Simple.

**Your session-1 error decoded:** "para tu" used the possessive ("your") after a preposition. After prepositions, you need the object pronoun form: "para ti" (informal) or "para usted" (formal).

---

## Layer 4: The Verb Engine (CPU)

The verb is the CPU of every Spanish sentence. It encodes **who** is acting plus **when** plus **mood** — all in one word. Master the verb system and you have the keys to the language.

### Architecture: 3 Families, 1 Pattern

All Spanish infinitives end in **-ar**, **-er**, or **-ir**. To conjugate:

```
stem = infinitive minus ending
conjugated = stem + person/tense ending
```

| Family | % of all verbs | Infinitive | Stem |
|--------|---------------|------------|------|
| **-AR** | ~60% | hablar | habl- |
| **-ER** | ~20% | comer | com- |
| **-IR** | ~20% | vivir | viv- |

### Present Tense: The Core Matrix

**-AR endings (hablar):**

| Person | Ending | Result | Mnemonic |
|--------|--------|--------|----------|
| yo | **-o** | hablo | "oh, it's me" |
| tú | **-as** | hablas | the "s" = you |
| él/ella/Ud. | **-a** | habla | bare "a" |
| nosotros | **-amos** | hablamos | "amos" = we love to |
| ellos/Uds. | **-an** | hablan | "n" = many |

**-ER/-IR endings (comer/vivir):**

| Person | -ER | -IR | Difference |
|--------|-----|-----|------------|
| yo | com**o** | viv**o** | same |
| tú | com**es** | viv**es** | same |
| él/ella/Ud. | com**e** | viv**e** | same |
| nosotros | com**emos** | viv**imos** | **only difference** |
| ellos/Uds. | com**en** | viv**en** | same |

**The deep pattern:** -ER and -IR are nearly identical. The ONLY difference is the nosotros form (-emos vs -imos). In practice, you're learning 2 patterns, not 3.

**The yo-form pattern:** ALL regular present tense yo-forms end in **-o**. Always. Even most irregulars: hago, tengo, vengo, pongo, salgo, digo. The single exception among common verbs: soy, estoy, voy, doy, sé (and estoy/voy/doy all end in -oy).

### Stem-Changing Verbs: The Vowel Shift Pattern

These are NOT "irregular" — they follow a predictable sub-pattern. The stem vowel shifts in stressed positions:

```
Pattern: the stem vowel changes in ALL forms EXCEPT nosotros
(because nosotros stress falls on the ending, not the stem)
```

**e → ie shift:**

| Verb | yo | tú | él | nosotros | ellos |
|------|----|----|-----|----------|-------|
| qu**e**rer (want) | qu**ie**ro | qu**ie**res | qu**ie**re | qu**e**remos | qu**ie**ren |
| p**e**nsar (think) | p**ie**nso | p**ie**nsas | p**ie**nsa | p**e**nsamos | p**ie**nsan |
| ent**e**nder (understand) | ent**ie**ndo | ent**ie**ndes | ent**ie**nde | ent**e**ndemos | ent**ie**nden |

**o → ue shift:**

| Verb | yo | tú | él | nosotros | ellos |
|------|----|----|-----|----------|-------|
| p**o**der (can) | p**ue**do | p**ue**des | p**ue**de | p**o**demos | p**ue**den |
| d**o**rmir (sleep) | d**ue**rmo | d**ue**rmes | d**ue**rme | d**o**rmimos | d**ue**rmen |
| v**o**lver (return) | v**ue**lvo | v**ue**lves | v**ue**lve | v**o**lvemos | v**ue**lven |

**e → i shift (only -IR verbs):**

| Verb | yo | tú | él | nosotros | ellos |
|------|----|----|-----|----------|-------|
| p**e**dir (ask for) | p**i**do | p**i**des | p**i**de | p**e**dimos | p**i**den |
| s**e**rvir (serve) | s**i**rvo | s**i**rves | s**i**rve | s**e**rvimos | s**i**rven |

**The "boot pattern":** If you draw a box around the forms that change, it looks like a boot (or an L-shape). The nosotros form is always outside the boot.

```
  quiero    quieres
  quiere    queremos  ← safe zone (no change)
  quieren
```

### The "Yo-Go" Verbs: 1 Pattern, 6+ Verbs

These verbs add a **-g-** in the yo form only. All other forms are normal (or stem-changing):

| Infinitive | Yo form | All other forms... |
|------------|---------|-------------------|
| tener (have) | ten**go** | tienes, tiene, tenemos, tienen |
| hacer (do) | ha**go** | haces, hace, hacemos, hacen |
| poner (put) | pon**go** | pones, pone, ponemos, ponen |
| salir (leave) | sal**go** | sales, sale, salimos, salen |
| venir (come) | ven**go** | vienes, viene, venimos, vienen |
| decir (say) | di**go** | dices, dice, decimos, dicen |
| traer (bring) | trai**go** | traes, trae, traemos, traen |
| oír (hear) | oi**go** | oyes, oye, oímos, oyen |
| caer (fall) | cai**go** | caes, cae, caemos, caen |

**Pattern:** The yo form is the "weird" one. Learn that, and the rest follows the normal or stem-change pattern.

### The 5 Fully Irregular Verbs (Just Memorize)

Only these are truly unpredictable:

| Verb | yo | tú | él | nosotros | ellos |
|------|----|----|-----|----------|-------|
| **ser** (be-identity) | soy | eres | es | somos | son |
| **estar** (be-state) | estoy | estás | está | estamos | están |
| **ir** (go) | voy | vas | va | vamos | van |
| **haber** (aux.) | he | has | ha | hemos | han |
| **dar** (give) | doy | das | da | damos | dan |

**Note:** *ir* (to go) and *ser* (to be) share the SAME past tense forms. Context disambiguates. This sounds insane, but it works: "Fui al McDonald's" (I went) vs "Fui estudiante" (I was a student). The surrounding words make it obvious.

### Ser vs Estar: The Deepest Architectural Split

English has one "to be." Spanish splits it into two verbs with completely different domains. This is the most important conceptual distinction in the language.

**Mental model: SER = the blueprint. ESTAR = the current state.**

| Domain | SER | ESTAR |
|--------|-----|-------|
| **What it is** | Soy [nombre] | — |
| **What it's made of** | Es de madera (wood) | — |
| **Where it's from** | Soy de Nevada | — |
| **Essential trait** | Es inteligente | — |
| **Occupation** | Soy programador | — |
| **Time / date** | Son las tres | — |
| **Where it is** | — | Estoy en Vegas |
| **How it feels** | — | Estoy cansado |
| **Temporary state** | — | Está cerrado (closed) |
| **Result of action** | — | Está roto (broken) |
| **Ongoing action** | — | Está hablando |
| **Alive/dead** | — | Está muerto |

**The hack:** If the state can change, use estar. If it defines what the thing fundamentally IS, use ser.

**Meaning shifts with ser vs estar:**

| With SER | With ESTAR |
|----------|-----------|
| Es **aburrido** = He's boring (personality) | Está **aburrido** = He's bored (right now) |
| Es **listo** = He's clever | Está **listo** = He's ready |
| Es **malo** = He's a bad person | Está **malo** = He's sick |
| Es **rico** = He's rich | Está **rico** = It tastes delicious |
| Es **verde** = It's green (color) | Está **verde** = It's unripe |

### Reflexive Verbs: Actions on Yourself

When the subject and object are the same person, add a reflexive pronoun:

```
lavar (to wash) → lavarse (to wash oneself)
llamar (to call) → llamarse (to be called / to call oneself)
sentir (to feel) → sentirse (to feel)
```

| Person | Pronoun | Example (llamarse) |
|--------|---------|-------------------|
| yo | **me** | Me llamo [nombre] |
| tú | **te** | ¿Cómo te llamas? |
| él/ella/Ud. | **se** | Se llama María |
| nosotros | **nos** | Nos llamamos... |
| ellos/Uds. | **se** | Se llaman... |

🇩🇪 **German speaker:** Like *sich waschen*, *sich fühlen*. Same concept, different pronoun positions.

**Common reflexive verbs for daily life:**

| Infinitive | Meaning | Example |
|------------|---------|---------|
| levantarse | get up | Me levanto a las 6 |
| acostarse | go to bed | Me acuesto tarde |
| sentirse | feel | Me siento bien |
| irse | leave | Me voy |
| quedarse | stay | Me quedo aquí |
| sentarse | sit down | Siéntese (sit down, formal command) |

### The "Gustar" Construction: Backwards Verbs

"Me gusta" doesn't mean "I like." It literally means "it pleases me." The subject and object are flipped:

```
English:  I  like  coffee.
           ↓    ↓     ↓
Spanish:  Me  gusta  el café.
          (to me) (pleases) (the coffee)
```

| English | Spanish | Literally |
|---------|---------|-----------|
| I like coffee | Me gusta el café | Coffee pleases me |
| I like tacos | Me gustan los tacos | Tacos please me |
| You like music | Te gusta la música | Music pleases you |
| He likes books | Le gustan los libros | Books please him |
| We like the house | Nos gusta la casa | The house pleases us |

**Rule:** The verb agrees with the THING you like, not with you.
- 1 thing → gust**a**
- multiple things → gust**an**

**Other "backwards" verbs that work the same way:**

| Verb | Meaning | Example |
|------|---------|---------|
| encantar | love (stronger than gustar) | Me encanta la música |
| molestar | to bother | Me molesta el ruido |
| importar | to matter | No me importa |
| faltar | to lack/need | Me falta tiempo |
| doler | to hurt | Me duele la cabeza |
| parecer | to seem | Me parece bien |
| interesar | to interest | Me interesa el arte |

---

## Layer 5: Sentence Assembly (Compiler)

### The Default: SVO (Like English)

```
[Subject] + [Verb] + [Object]
   (Yo)     quiero    un café.
```

But subject is usually dropped → "Quiero un café."

### Question Formation: 3 Methods

**Method 1: Intonation only (most common in speech)**
```
Tienes leche.  →  ¿Tienes leche?  (just raise pitch at end)
```

**Method 2: Inversion (more formal)**
```
¿Tienes tú leche?  (verb before subject)
```

**Method 3: Question word at front**
```
¿Qué quieres?     ¿Dónde está?     ¿Cuánto cuesta?
```

### Negation: "No" Before the Verb. Done.

```
Quiero café.     →  No quiero café.
Entiendo.        →  No entiendo.
Hay leche.       →  No hay leche.
```

### Double Negatives: Required (Not Wrong!)

In English, "I don't have nothing" is wrong. In Spanish, it's mandatory:

| English | Spanish | Literally |
|---------|---------|-----------|
| I don't have anything | No tengo **nada** | I don't have nothing |
| I don't see anyone | No veo a **nadie** | I don't see nobody |
| I never go | No voy **nunca** | I don't go never |
| I don't want any | No quiero **ninguno** | I don't want none |

**Or put the negative word first (then drop "no"):**
- **Nada** tengo = I have nothing
- **Nunca** voy = I never go
- **Nadie** viene = Nobody comes

### Adjective Placement: After the Noun (Usually)

```
English:  the big house       the red car        the cold coffee
Spanish:  la casa grande      el coche rojo      el café frío
```

**Exceptions (before noun):**
- Numbers: **dos** cafés
- Quantity: **mucho** tiempo, **poco** dinero
- Possessives: **mi** casa, **tu** café
- Demonstratives: **este** libro, **esa** mesa
- bueno/malo (often): **buen** día, **mal** tiempo (note: shortened forms)
- grande (meaning "great" not "big"): un **gran** hombre (a great man) vs un hombre **grande** (a big man)

### Word Order for Emphasis

Spanish uses word order to emphasize. Moving something to the front = spotlight:

```
Normal:    Quiero café.         (I want coffee)
Emphatic:  Café es lo que quiero.  (Coffee is what I want)
Emphatic:  Yo no hablo inglés.    (I don't speak English — emphasis on "I")
```

---

## Layer 6: The Pronoun System (Pointers)

This is where most learners get confused. Spanish has **4 sets** of pronouns for different grammatical roles. Think of them as pointer types.

### The 4 Pronoun Sets

| Role | yo form | tú form | él/ella/Ud. | nosotros | ellos/Uds. |
|------|---------|---------|------------|----------|------------|
| **Subject** (who acts) | yo | tú | él/ella/usted | nosotros | ellos/ustedes |
| **Direct object** (receives action) | me | te | lo/la | nos | los/las |
| **Indirect object** (to/for whom) | me | te | le | nos | les |
| **After preposition** | mí | ti | él/ella/usted | nosotros | ellos/ustedes |

**Your session-1 error decoded (final explanation):**
- "para tu" used the **possessive** (tu = your) where you needed the **prepositional** form (ti = you)
- After *para*, *sin*, *de*, *con*, etc. → use prepositional pronouns
- para **mí**, para **ti**, para **usted**

### Where Object Pronouns Go

**Before conjugated verbs:**
```
Lo quiero.        (I want it)
La veo.           (I see her)
Me gusta.         (It pleases me / I like it)
Te ayudo.         (I help you)
```

**Attached to infinitives (either position OK):**
```
Quiero verlo.     OR   Lo quiero ver.     (I want to see it)
Voy a comprarlo.  OR   Lo voy a comprar.  (I'm going to buy it)
```

**Attached to commands:**
```
Dígame.           (Tell me)
Quédese.          (Stay / Keep it)
Siéntese.         (Sit down)
```

### Direct vs Indirect Object (When It Matters)

**Direct object** = what receives the action directly
```
Veo a María.   →   La veo.       (I see her)
Quiero café.   →   Lo quiero.    (I want it)
```

**Indirect object** = who benefits/receives the result
```
Doy el café a María.  →  Le doy el café.  (I give her the coffee)
Digo la verdad a ti.   →  Te digo la verdad. (I tell you the truth)
```

**The "double object" stack:** When you have both, indirect goes first:
```
Se lo doy.    (I give it to him/her)
Me lo da.     (He gives it to me)
Te las traigo. (I bring them to you)
```

**Note:** *le/les* becomes **se** when followed by lo/la/los/las. This is just a sound rule (le lo → se lo).

### The "Personal A"

When a person is the direct object of a verb, add "a" before them:

```
Veo la casa.      (I see the house — no "a" needed)
Veo a María.      (I see María — "a" required because person)
Busco a mi padre.  (I'm looking for my father)
Ayudo a los niños. (I help the children)
```

**This doesn't translate to anything in English.** It's a marker that says "the next word is a person being acted on, not the subject."

---

## Layer 7: The Number System

You struggled with "Son tres dólares con cincuenta" in session 1. Here's the complete system.

### 0-15: Just Memorize (Unique Words)

| # | Spanish | # | Spanish |
|---|---------|---|---------|
| 0 | cero | 8 | ocho |
| 1 | uno | 9 | nueve |
| 2 | dos | 10 | diez |
| 3 | tres | 11 | once |
| 4 | cuatro | 12 | doce |
| 5 | cinco | 13 | trece |
| 6 | seis | 14 | catorce |
| 7 | siete | 15 | quince |

### 16-19: "dieci" + unit

| # | Spanish | Pattern |
|---|---------|---------|
| 16 | dieciséis | dieci + seis |
| 17 | diecisiete | dieci + siete |
| 18 | dieciocho | dieci + ocho |
| 19 | diecinueve | dieci + nueve |

### 20-29: "veinti" + unit

| # | Spanish | Pattern |
|---|---------|---------|
| 20 | veinte | |
| 21 | veintiuno | veinti + uno |
| 22 | veintidós | veinti + dos |
| 25 | veinticinco | veinti + cinco |

### 30-99: tens + "y" + unit

| # | Spanish | Pattern |
|---|---------|---------|
| 30 | treinta | |
| 31 | treinta y uno | 30 + y + 1 |
| 40 | cuarenta | |
| 42 | cuarenta y dos | 40 + y + 2 |
| 50 | cincuenta | |
| 55 | cincuenta y cinco | 50 + y + 5 |
| 60 | sesenta | |
| 70 | setenta | |
| 80 | ochenta | |
| 90 | noventa | |

### 100+

| # | Spanish |
|---|---------|
| 100 | cien (exactly) / ciento (100+) |
| 101 | ciento uno |
| 200 | doscientos |
| 500 | quinientos |
| 1,000 | mil |
| 1,000,000 | un millón |

### Money Pattern (What You Heard in Session 1)

```
Son [dollars] dólares con [cents].

Son tres dólares con cincuenta.  = $3.50
Son cinco con veinticinco.       = $5.25
Son diez.                        = $10.00
```

**"con"** = "with" (dollars WITH fifty cents)

**Shortcut in fast speech:** They often drop "dólares":
- "Son tres cincuenta" = $3.50

### Telling Time

```
¿Qué hora es?  = What time is it?

Es la una.              = It's 1:00 (singular!)
Son las dos.            = It's 2:00
Son las tres y media.   = It's 3:30
Son las cuatro y cuarto. = It's 4:15
Son las cinco menos diez. = It's 4:50 (5 minus 10)
```

**Pattern:** "Son las [number]" for 2-12. "Es la una" for 1:00 only.

---

## Layer 8: The Tense Map (Timeline)

You only need present tense now. But understanding the full map helps you see where you're going. Spanish has fewer tenses than you think — many are hacks built from pieces you already know.

### The Timeline

```
←── PAST ──────────────── PRESENT ──────────────── FUTURE ──→

 Preterite          Present              Near Future
 (completed)       (now/habit)          (voy a + inf)

 Imperfect                               Simple Future
 (ongoing/habitual                      (will)
  in past)
                                         Conditional
 Present Perfect                        (would)
 (have done)
```

### The 3 Tenses You Actually Need First

**1. Present (Layer 4 — you're learning this now)**
```
Hablo español.          I speak Spanish.
Quiero café.            I want coffee.
```

**2. Near Future (FREE — already know ir)**
```
Voy a + infinitive

Voy a hablar.           I'm going to speak.
Voy a practicar.        I'm going to practice.
Vamos a comer.          We're going to eat.
```

**3. Recent Past (FREE — already know "acabo de")**
```
Acabo de + infinitive = I just [did something]

Acabo de comer.         I just ate.
Acabo de llegar.        I just arrived.
```

### The Next 2 Tenses (Month 2)

**4. Preterite (completed past actions):**

-AR verbs: habl**é**, habl**aste**, habl**ó**, habl**amos**, habl**aron**
-ER/-IR verbs: com**í**, com**iste**, com**ió**, com**imos**, com**ieron**

```
Hablé con mi papá.     I spoke with my dad.
Comí tacos.             I ate tacos.
Fui al McDonald's.      I went to McDonald's.
```

**5. Imperfect (ongoing/habitual past):**

-AR verbs: habl**aba**, habl**abas**, habl**aba**, habl**ábamos**, habl**aban**
-ER/-IR verbs: com**ía**, com**ías**, com**ía**, com**íamos**, com**ían**

```
Hablaba español de niño.    I used to speak Spanish as a kid.
Siempre comía tacos.        I always ate tacos.
Vivía en California.        I lived in (was living in) California.
```

**Preterite vs Imperfect (the key distinction):**

| Preterite | Imperfect |
|-----------|-----------|
| Completed action | Ongoing/habitual |
| "I ate" (done) | "I was eating" / "I used to eat" |
| "I spoke" (once) | "I always spoke" |
| Specific time | Background/context |

### The "Have Done" Hack (Present Perfect)

```
haber (present) + past participle

He hablado.     I have spoken.
Has comido.     You have eaten.
Ha ido.         He has gone.
Hemos visto.    We have seen.
```

**Past participles:** -AR → -ado (hablado), -ER/-IR → -ido (comido, vivido)

**Irregulars:** hecho (done), dicho (said), visto (seen), escrito (written), abierto (opened), vuelto (returned), puesto (put), roto (broken), muerto (dead)

---

## Layer 9: Connectors (Control Flow)

These are the words that turn isolated sentences into flowing conversation. They're the cheapest upgrade to sounding fluent.

### Tier 1: Essential (Learn Now)

| Spanish | English | Function | Example |
|---------|---------|----------|---------|
| **y** | and | join | Quiero café **y** pan |
| **o** | or | choice | ¿Café **o** agua? |
| **pero** | but | contrast | Entiendo **pero** no mucho |
| **porque** | because | reason | Hablo español **porque** quiero |
| **también** | also | add | **También** quiero agua |
| **no** | not | negate | **No** entiendo |

### Tier 2: Flow (Week 2-3)

| Spanish | English | Function | Example |
|---------|---------|----------|---------|
| **entonces** | so/then | consequence | **Entonces**, vamos |
| **cuando** | when | time | **Cuando** tengo tiempo |
| **si** | if | condition | **Si** puedes, ayúdame |
| **como** | like/as | comparison | **Como** en México |
| **que** | that | subordinate | Creo **que** sí |
| **ya** | already/now | timing | **Ya** voy (I'm coming) |
| **todavía** | still/yet | ongoing | **Todavía** no (not yet) |

### Tier 3: Conversational Lubricant (Week 3-4)

These don't translate well. They're conversational filler that makes you sound *human*:

| Spanish | Function | When to use |
|---------|----------|-------------|
| **bueno** | well... | starting a new thought |
| **pues** | well/so | transitioning, softening |
| **a ver** | let's see | thinking out loud |
| **es que** | the thing is | explaining/justifying |
| **o sea** | I mean | clarifying what you said |
| **la verdad** | honestly | emphasizing |
| **mira/mire** | look/listen | getting attention |
| **fíjate** | imagine/check it out | surprise, emphasis |
| **la neta** | the truth (Mexico slang) | real talk |

### Tier 4: Sophistication (Month 2+)

| Spanish | English | Example |
|---------|---------|---------|
| **aunque** | although/even though | Aunque no hablo bien... |
| **sin embargo** | however | Sin embargo, entiendo. |
| **por eso** | that's why | Por eso estudio. |
| **en cambio** | on the other hand | Ella habla bien; yo, en cambio... |
| **mientras** | while | Mientras como, hablo. |
| **además** | besides/also | Además, me gusta. |
| **por lo menos** | at least | Por lo menos entiendo un poco. |

---

## Layer 10: The Repair System (Error Handling)

These keep you IN the conversation when your production engine fails. They are your most important phrases for real-world deployment.

### Tier 1: Emergency (Memorize Cold)

| Situation | Say this | Pronunciation |
|-----------|----------|---------------|
| Didn't understand | **No entendí** | noh en-ten-DEE |
| Too fast | **Más despacio, por favor** | mahs des-PAH-syoh |
| Repeat? | **¿Puede repetir?** | PWEH-deh reh-peh-TEER |
| How do you say...? | **¿Cómo se dice...?** | KOH-moh seh DEE-seh |
| What does X mean? | **¿Qué significa...?** | keh seeg-NEE-fee-kah |
| One second | **Un momento** | oon moh-MEN-toh |
| I'm learning | **Estoy aprendiendo español** | es-TOY ah-pren-dee-EN-doh |
| I don't know (word) | **No sé la palabra** | noh seh lah pah-LAH-brah |

### Tier 2: Recovery (Week 2)

| Situation | Say this |
|-----------|----------|
| Wrong word | **Quiero decir...** (I mean...) |
| Forgot mid-sentence | **¿Cómo es?** (How is it? / What's the word?) |
| Need simpler words | **¿Puede decirlo más simple?** |
| Misunderstood | **¿Eso quiere decir que...?** (Does that mean...?) |
| Confirming | **¿Así está bien?** (Is that right?) |

### Tier 3: Social Recovery

| Situation | Say this |
|-----------|----------|
| Apologizing for level | **Perdón, mi español no es muy bueno todavía** |
| Thanking patience | **Gracias por su paciencia** |
| Self-deprecating humor | **Estoy aprendiendo, poco a poco** |
| Switching to English | **¿Habla inglés?** (only as last resort!) |

**Anti-pattern:** Don't switch to English unless you absolutely must. Staying in Spanish, even badly, builds the neural pathways you need.

---

## Layer 11: Pattern Templates (The API)

These are sentence-generation templates. Master the template, swap the parts, produce hundreds of sentences.

### Core Templates (Week 1)

**WANT:** `Quiero + [noun / infinitive]`
```
Quiero un café.           Quiero ir.
Quiero agua.              Quiero hablar.
Quiero la cuenta.         Quiero aprender.
```

**NEED:** `Necesito + [noun / infinitive]`
```
Necesito ayuda.           Necesito descansar.
Necesito cambio.          Necesito practicar.
Necesito tiempo.          Necesito hablar con usted.
```

**HAVE TO:** `Tengo que + [infinitive]`
```
Tengo que ir.             Tengo que trabajar.
Tengo que pagar.          Tengo que practicar.
```

**GOING TO:** `Voy a + [infinitive]`
```
Voy a comer.              Voy a pagar.
Voy a hablar español.     Voy a practicar.
```

**CAN/COULD:** `Puedo + [infinitive]` / `¿Puede + [infinitive]?`
```
Puedo ayudar.             ¿Puede repetir?
Puedo pagar con tarjeta.  ¿Puede hablar más despacio?
No puedo ir.              ¿Puede ayudarme?
```

### Question Templates (Week 1-2)

**HAVE?** `¿Tiene(s) + [noun]?`
```
¿Tiene leche?      ¿Tiene cambio?      ¿Tiene tiempo?
```

**WHERE?** `¿Dónde está + [noun]?`
```
¿Dónde está el baño?    ¿Dónde está la tienda?
```

**HOW MUCH?** `¿Cuánto cuesta + [noun]?` / `¿Cuánto es?`
```
¿Cuánto cuesta el café?    ¿Cuánto es en total?
```

**IS THERE?** `¿Hay + [noun]?`
```
¿Hay café?     ¿Hay un baño?     ¿Hay alguien aquí?
```

**WHAT?** `¿Qué + [verb]?`
```
¿Qué quieres?     ¿Qué es eso?     ¿Qué hora es?
```

### Expressive Templates (Week 2-3)

**LIKE:** `Me gusta + [noun / infinitive]`
```
Me gusta el café.         Me gusta hablar español.
Me gusta esta música.     No me gusta el frío.
```

**FEEL:** `Me siento + [adjective]` / `Estoy + [adjective]`
```
Me siento bien.           Estoy cansado.
Me siento nervioso.       Estoy contento.
```

**THINK:** `Creo que + [sentence]`
```
Creo que sí.              Creo que es bueno.
Creo que entiendo.        No creo que sea difícil.
```

**BECAUSE:** `[sentence] + porque + [reason]`
```
Estudio español porque mi papá es mexicano.
Quiero aprender porque vivo en Vegas.
No puedo ir porque estoy trabajando.
```

### Politeness Upgrades (Any Time)

| Direct | Polite | Extra polite |
|--------|--------|-------------|
| Quiero café | Quisiera café | Me gustaría un café, por favor |
| Dime | ¿Puede decirme...? | ¿Sería tan amable de decirme...? |
| Dame agua | ¿Me da agua? | ¿Me podría dar agua, por favor? |

---

## Layer 12: Word Generation (Factory Methods)

These rules let you *manufacture* vocabulary on the fly. You won't know every word, but you can often build the one you need.

### English → Spanish Cognate Rules

Thousands of English words have Spanish cognates. These patterns let you guess correctly ~80% of the time:

| English ending | Spanish ending | Examples |
|---------------|---------------|----------|
| **-tion** | **-ción** | nation → nación, education → educación |
| **-sion** | **-sión** | decision → decisión, vision → visión |
| **-ty** | **-dad** | university → universidad, city → ciudad |
| **-ous** | **-oso** | famous → famoso, nervous → nervioso |
| **-ble** | **-ble** | possible → posible, terrible → terrible |
| **-ment** | **-mento** / **-miento** | moment → momento, sentiment → sentimiento |
| **-al** | **-al** | normal → normal, animal → animal |
| **-ent/-ant** | **-ente/-ante** | intelligent → inteligente, important → importante |
| **-ly** | **-mente** | rapidly → rápidamente, normally → normalmente |
| **-ist** | **-ista** | artist → artista, dentist → dentista |
| **-ism** | **-ismo** | capitalism → capitalismo |
| **-ence/-ance** | **-encia/-ancia** | experience → experiencia, importance → importancia |
| **-ic** | **-ico** | music → música, public → público |

**Warning: False cognates exist.** The most dangerous:

| English word | Spanish look-alike | Actually means |
|-------------|-------------------|----------------|
| embarrassed | embarazada | **pregnant** |
| exit | éxito | **success** |
| actual | actual | **current** |
| sensible | sensible | **sensitive** |
| large | largo | **long** |
| carpet | carpeta | **folder** |
| fabric | fábrica | **factory** |

### Verb-to-Noun Patterns

| Verb | Noun form | Pattern |
|------|-----------|---------|
| trabajar (work) | trabajo (work/job) | drop -ar, use -o |
| ayudar (help) | ayuda (help) | drop -ar, use -a |
| cambiar (change) | cambio (change) | drop -ar, use -o |
| cocinar (cook) | cocina (kitchen) | drop -ar, use -a |
| bailar (dance) | baile (dance) | drop -ar, use -e |

### The Diminutive System (-ito/-ita)

Adding -ito/-ita makes things smaller, cuter, or softer. Mexicans use this **constantly**:

| Base | Diminutive | Effect |
|------|-----------|--------|
| café | cafe**cito** | little coffee (affectionate) |
| momento | moment**ito** | just a moment (softer) |
| poco | poqu**ito** | a tiny bit |
| ahora | ahor**ita** | right now / in a sec |
| casa | cas**ita** | little house (cozy) |
| hermano | herman**ito** | little brother / bro |

**The vibe:** Using diminutives makes you sound warm, Mexican, and fluent. Say "un cafecito" instead of "un café" and you'll get smiles.

### The Augmentative System (-ón/-ote/-azo)

Makes things bigger or more intense:

| Base | Augmentative | Effect |
|------|-------------|--------|
| grande | grand**ote** | huge |
| golpe (hit) | golp**azo** | big hit |
| amigo | amig**ote** | buddy (rough affection) |
| puerta (door) | port**azo** | door slam |

---

## Layer 13: Mexican Spanish (Target Runtime)

Your target dialect is Mexican Spanish (the McDonald's crew, your father, the neighbors). It differs from Spain/Argentine/Caribbean Spanish in specific ways.

### Pronunciation

| Feature | Mexico | Spain | Argentina |
|---------|--------|-------|-----------|
| **c** before e/i | "s" | "th" | "s" |
| **z** | "s" | "th" | "s" |
| **ll** | "y" | "y" / "ly" | "sh" |
| **s** at end | pronounced | often dropped | pronounced |
| general speed | moderate | fast | moderate |

### Vocabulary (Mexico vs Spain)

| Meaning | Mexico | Spain |
|---------|--------|-------|
| car | **carro** / coche | coche |
| computer | **computadora** | ordenador |
| apartment | **departamento** | piso |
| cool | **padre** / chido | guay / mola |
| bus | **camión** | autobús |
| cellphone | **celular** | móvil |
| to drive | **manejar** | conducir |
| money | **lana** (slang) | pasta (slang) |
| dude | **güey** | tío |
| angry | **enojado** | enfadado |

### Mexican Slang You'll Hear

| Slang | Meaning | Context |
|-------|---------|---------|
| **güey** (wey) | dude, bro | among friends only |
| **¿qué onda?** | what's up? | casual greeting |
| **chido** / **padre** | cool, awesome | "¡Qué padre!" |
| **no manches** | no way / come on | surprise, disbelief |
| **ándale** | come on / that's right | agreement, encouragement |
| **neta** | truth, for real | "¿Neta?" = Really? |
| **fresa** | snob/preppy | adjective, sometimes noun |
| **ahorita** | right now (or... later) | time is flexible |
| **mande** | pardon? / yes? | polite "what?" (Mexico only) |
| **órale** | wow / let's go / right on | all-purpose affirmative |

**Important:** "Mande" instead of "¿qué?" is uniquely Mexican and considered more polite. Use it with the McDonald's crew and they'll know you've been learning from Mexicans, not textbooks.

### The "Usted" Default

In Mexico (unlike Spain), **usted** is used more broadly:
- Always with strangers and service workers
- Often with elders, even if you know them
- Shows respect, never stiff

Your McDonald's strategy: **Start with usted. Always.** They may switch you to tú. Let them lead that transition.

---

## Layer 14: Idiomatic Structures (Design Patterns)

These are constructions that don't translate word-for-word. They're the "design patterns" of Spanish — recurring structures that native speakers use constantly.

### "Tener" Expressions (Have → Feel)

Spanish uses "have" where English uses "be" for physical/emotional states:

| Spanish | Literal | Actual meaning |
|---------|---------|---------------|
| Tengo hambre | I have hunger | I'm hungry |
| Tengo sed | I have thirst | I'm thirsty |
| Tengo frío | I have cold | I'm cold |
| Tengo calor | I have heat | I'm hot |
| Tengo sueño | I have sleep | I'm sleepy |
| Tengo miedo | I have fear | I'm scared |
| Tengo prisa | I have hurry | I'm in a rush |
| Tengo razón | I have reason | I'm right |
| Tengo [X] años | I have [X] years | I'm [X] years old |
| Tengo ganas de... | I have desire of... | I feel like [doing]... |

**Pattern:** Physical/emotional states use *tener* + noun (not *ser/estar* + adjective). This is NOT irregular — it's a systematic design choice.

### "Hacer" + Weather

| Spanish | Literal | Meaning |
|---------|---------|---------|
| Hace frío | It makes cold | It's cold (weather) |
| Hace calor | It makes heat | It's hot |
| Hace sol | It makes sun | It's sunny |
| Hace viento | It makes wind | It's windy |
| Hace buen tiempo | It makes good time | Nice weather |

**Note:** "Llueve" (it rains) and "nieva" (it snows) are standalone verbs, not hacer constructions.

### "Hay" (There Is / There Are)

One word covers both singular and plural:

```
Hay un café.         There is a café.
Hay muchos cafés.    There are many cafés.
¿Hay leche?          Is there milk?
No hay problema.     There's no problem. / No worries.
```

**"Hay que" + infinitive = "one must" / "you gotta":**
```
Hay que practicar.   You gotta practice.
Hay que comer.       You need to eat.
```

### "Acabar de" (Just Did)

```
Acabo de comer.      I just ate.
Acaba de llegar.     He/she just arrived.
Acabamos de hablar.  We just spoke.
```

### "Llevar" + Time (Duration)

```
Llevo dos meses estudiando.  I've been studying for 2 months.
Lleva una hora esperando.    He/she has been waiting for an hour.
```

### "Quedar" (Remainder/Agreement)

```
¿Cuánto queda?              How much is left?
Nos quedan dos días.         We have 2 days left.
¿Quedamos a las tres?       Shall we meet at 3?
Me queda bien.               It fits me well.
```

---

## The Unlock Sequence

This is the master order. Each layer builds on the previous. Don't skip ahead.

### Phase 1: Survival (Week 1-2)
- Sound system (5 vowels, 3 stress rules, consonant remapping)
- Repair phrases (Layer 10, Tier 1) — deploy immediately
- Pattern templates (Layer 11, Core) — Quiero, Necesito, Tengo que
- Numbers 0-20 + money pattern
- Present tense: ser, estar, tener, ir, querer (5 verbs)
- Gender basics (-o = M, -a = F)
- Greetings + polite phrases

### Phase 2: Expansion (Week 3-4)
- Present tense: all regular -AR verbs + poder, hacer
- Near future (voy a + infinitive)
- Stem-change pattern (e→ie, o→ue)
- Connectors Tier 1-2 (y, pero, porque, entonces, cuando)
- Numbers 20-100 + time
- Reflexive verbs (me llamo, me siento)
- Question words + question templates
- Negation + double negatives

### Phase 3: Depth (Week 5-6)
- Yo-go verbs (6+ verbs, 1 pattern)
- Gustar construction + other "backwards" verbs
- Object pronouns (direct + indirect, placement)
- Preterite tense basics
- Connectors Tier 3 (bueno, pues, es que, o sea)
- Tener expressions (tengo hambre, tengo frío, etc.)
- Diminutives (-ito/-ita)
- Mexican slang basics (güey, órale, ándale)

### Phase 4: Flow (Week 7-8)
- Imperfect tense (background/habitual past)
- Present perfect (he hablado, he comido)
- Preterite vs imperfect distinction
- Complex connectors (aunque, sin embargo, por eso)
- Idiomatic structures (acabar de, llevar + time, hay que)
- Word generation via cognate rules
- Subjunctive exposure (recognition only)
- Full conversational flow with fillers

### Phase 5: Mastery (Month 3+)
- Subjunctive production (basic triggers)
- Conditional (would)
- Commands (all forms)
- Complex relative clauses
- Register switching (tú vs usted fluently)
- Humor, wordplay, cultural references
- Speed and natural rhythm

---

*This document is the map, not the territory. It evolves. When a pattern clicks or a confusion persists, update this architecture.*

*When in doubt: produce first, analyze second. The machine reveals itself through use.*

*Last Updated: February 20, 2026*
