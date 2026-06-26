# The Logic Codex — The Rules Under the Argument, Made Simple

> The discourse codex teaches you to win the room. This one teaches you to be right. It is the formal
> backbone under every move in [discourse-codex.md](discourse-codex.md): the missing warrant you learn
> to spot is a hidden premise, the fallacy you learn to name is an invalid form, the term you learn to
> pin is a predicate with a fixed meaning. This is introductory first-order logic stripped down to what
> you actually use in an argument.
>
> Written in plain language, in our own words (CC BY-SA 4.0). It teaches the ideas; it copies no text.
> Examples are original. Where a term is standard, it is named so you can look it up.

---

## Part 0 — The one question logic answers

All of logic is built to answer a single question about an argument: **if the premises are true, does
the conclusion have to be true?** If yes, the argument is **valid**. If no, it is **invalid**. That is
the whole game.

The trap, and the most useful distinction you will ever learn, is that **validity is not truth**. They
come apart in both directions:

- An argument can be **valid but have a false conclusion**, if a premise is false. "All birds can fly.
  A penguin is a bird. So a penguin can fly." The form is perfect. The first premise is false, so the
  conclusion is wrong. Valid, not sound.
- An argument can be **invalid but have a true conclusion**, by luck. "The sky is blue. So grass is
  green." True conclusion, no connection. Invalid.

So there are two separate jobs, and most bad arguments fail by blurring them:

1. **Validity** — does the conclusion follow from the premises? (the *form*)
2. **Soundness** — is it valid *and* are the premises actually true? (form *plus* facts)

When you argue, you attack one or the other on purpose. Either "your logic does not connect" (validity)
or "your premise is false" (soundness). Naming which one you are attacking is half of arguing well.

---

## Part 1 — A claim has a shape

The first drill, the thing that is hard at first and then makes everything else easy: **separate what a
claim says from the shape it has**. A claim is not a blob. It is a structure you can see.

The simplest claim, an **atomic sentence**, is a predicate applied to names:

- `Tall(socrates)` — "Socrates is tall." One name, one property.
- `LeftOf(a, b)` — "a is to the left of b." Two names, a relation.
- `Between(a, b, c)` — "a is between b and c." Three names.

The **predicate** is the property or relation word (`Tall`, `LeftOf`, `Between`). The **arity** is how
many names it needs: one for a property, two or three for a relation. That is it. Every claim, no
matter how tangled the English, is some arrangement of names and predicates joined by a few connectors.

Why this matters off the page: the moment you can see the shape, you can see where an argument cheats.
Two people using `Fair` as if it were one predicate when they each mean something different is not a
disagreement about facts. It is two different predicates wearing the same word. (That is "pin the term"
in the discourse codex, seen from underneath.)

---

## Part 2 — The three connectives (and, or, not)

Complex claims are built from atomic ones with a tiny set of connectors. Three to start, and they are
exactly as simple as they look, with one catch each.

- **Not** (negation). Flips true to false. "It is not raining." Catch: in English we often negate the
  wrong part. "Not all cats are black" does **not** mean "all cats are not black." Scope matters; see
  Part 4.
- **And** (conjunction). True only when **both** parts are true. "It is cold and dark." Catch: a claim
  with "and" makes you responsible for defending *both* halves. Concede one and the conjunction falls.
- **Or** (disjunction). True when **at least one** part is true. Logic's "or" is **inclusive**: "or
  both" is allowed unless stated otherwise. Catch: everyday "or" often means "one or the other but not
  both." When precision matters, say which you mean.

The honest way to define each is a **truth table**: list every combination of true/false for the parts
and state the result. You rarely draw one out loud, but knowing they exist is what lets you answer "is
that always true, or only sometimes?" instantly.

---

## Part 3 — The conditional (if-then), where most errors live

`If P then Q`. P is the **antecedent**, Q the **consequent**. This one connector causes more bad
reasoning than all the others combined, so it earns its own part.

The single fact to burn in: **`If P then Q` only promises that whenever P holds, Q holds.** It says
nothing about what happens when P is false, and nothing about whether Q can happen on its own. From
that, the two valid moves and the two famous fallacies fall out:

**The two valid moves:**
- **Modus ponens** (affirm the antecedent): If P then Q. P is true. Therefore Q. Solid.
- **Modus tollens** (deny the consequent): If P then Q. Q is false. Therefore P is false. Solid, and
  the more powerful of the two, because it reasons backward.

**The two fallacies that feel valid and are not:**
- **Affirming the consequent:** If P then Q. Q is true. Therefore P. **Invalid.** "If it rained, the
  street is wet. The street is wet. So it rained." No: a burst pipe also wets the street. Q has other
  causes.
- **Denying the antecedent:** If P then Q. P is false. Therefore Q is false. **Invalid.** "If it
  rained, the street is wet. It did not rain. So the street is dry." No again, same pipe.

Two more pieces of English that trip everyone:
- **"P only if Q"** means `If P then Q`, **not** `If Q then P`. "You pass only if you study" does not
  promise that studying makes you pass.
- **"P if and only if Q"** (biconditional) means it works **both** directions: P guarantees Q and Q
  guarantees P. This is the strong claim; people assert it when they have only earned the one-way
  version.

If you learn one thing from this codex, learn the conditional. Most "you're not following the logic"
moments are one of these four shapes.

---

## Part 4 — Quantifiers (all, some, none, scope)

Now claims about **how many**. Two quantifiers do almost all the work:

- **Universal** ("all", "every", "each"): a claim about every case. `All A are B`.
- **Existential** ("some", "at least one", "there is"): a claim about at least one case. `Some A are B`.

The fundamentals you actually need:

- **"Some" means at least one, maybe all.** Logic's "some" does not imply "not all." If I say "some
  students passed," I have not denied that all did. Everyday speech implies otherwise; do not import
  that implication into an argument.
- **Negation flips the quantifier and the scope.** The opposite of "all A are B" is **"some A is not
  B"** (one counterexample is enough). The opposite of "some A is B" is **"no A is B."** This is the
  move that wins arguments: to refute "all," you do not need to prove "none," you need **one
  counterexample**.
- **"Any" is ambiguous in English** and means "all" or "some" depending on the sentence. "Anyone can
  do it" = all. "If anyone objects, stop" = some. Pin it before you argue it.
- **Order of quantifiers changes the meaning.** "Everyone loves someone" and "someone is loved by
  everyone" are different claims. The second is much stronger. Mixing them up is a classic slip in
  political and ethical arguments ("everyone has a right to a job" vs "there is one job everyone has a
  right to").

The practical upshot, again from underneath the discourse codex: the fastest refutation in any room is
the **counterexample**, and it is just the negation of a universal claim. Someone says "X always
fails." You produce one case where it did not. The universal is dead.

---

## Part 5 — Telling valid from invalid (the counterexample method)

You do not need formal proof to check most arguments. You need one tool: **try to build a case where
every premise is true and the conclusion is false.** If you can, the argument is invalid, and that case
is your refutation. If you genuinely cannot, no matter how you try, that is strong evidence it is valid.

Three labels worth knowing for single claims:
- **Tautology:** true in every case ("it is raining or it is not raining"). Says nothing about the
  world, but can never be wrong.
- **Contradiction:** false in every case ("it is raining and it is not raining"). If someone's position
  implies one, they have already lost.
- **Contingent:** true in some cases, false in others. Almost every real claim is here, which is why
  almost every real claim needs evidence, not just logic.

The sharp move in live argument: when a position sounds airtight, look for the hidden case it forgot.
That hidden case is a counterexample, and producing it is more devastating than any amount of
disagreement, because it works *on the other person's own terms*.

---

## Part 6 — Translation (English to form), the real skill

Everything above is easy once the claim is in clean form. The hard, trainable skill is **getting it
into clean form** from messy English. Watch words:

- **"Only", "only if", "none but"** reverse or restrict. "Only members vote" = "if you vote, you are a
  member," not the other way.
- **"Unless"** means "if not." "I will go unless it rains" = "if it does not rain, I will go."
- **"All... are not"** is ambiguous and usually means "not all." Rewrite it.
- **"A few", "most", "many"** are not "some" or "all"; they are vaguer quantifiers that hide how much
  you are claiming. Decide what you actually mean.
- **Pronouns and "it"** hide which name a predicate attaches to. Name the name.

The drill is simple and brutal: take a real sentence from an argument, write what it actually claims in
the names-and-predicates-and-connectives form, and watch what falls out. Half the time the hidden
premise or the overreach appears the moment the English is gone.

---

## Part 7 — What a proof is, without the notation

A **formal proof** sounds intimidating and is not. It is a chain of steps from premises to conclusion
where **every single step is licensed by a rule you already trust** (like modus ponens). Nothing is
asserted; everything is earned from what came before. The point of the formal version is to remove
judgment entirely, so that a step is either legal or it is not.

You will rarely write a full formal proof in a conversation. What transfers is the **stance**: a
conclusion is only as good as the chain that reaches it, and a chain is only as strong as its weakest
licensed step. When you argue, you are building an informal version of this. Naming your steps ("here
is the premise, here is the rule, here is what follows") is what makes an argument feel inevitable
instead of merely loud.

---

## Part 8 — The seam: how this powers the discourse codex

This is not a separate subject. It is the floor the discourse codex stands on. The map:

- **"Find the missing warrant"** (discourse Domain 3) = find the **hidden premise** an argument needs
  to be valid but never stated. Formal logic shows you exactly which premise is missing, because
  without it the chain does not connect.
- **"Name the fallacy"** (discourse Domain 5) = recognize an **invalid form**. Affirming the
  consequent, denying the antecedent, and the quantifier slips above are the most common ones in real
  rooms. You name them faster because you have seen their shape.
- **"Pin the term"** (discourse Domain 3) = fix the **predicate's meaning** so both people are using
  one predicate, not two wearing the same word.
- **"The counterexample"** (the sharpest refutation) = the **negation of a universal**, produced as a
  single case. Parts 4 and 5 are where it comes from.
- **Validity vs soundness** (Part 0) = the choice, every time, of whether you are attacking the
  **connection** or the **facts**. Saying which one out loud is a composure move and a clarity move at
  once.

The discourse codex tells you *when* to reach for these while a mind is coming at you. This codex tells
you *what they are* and *why they hold*, so that when you reach, the thing is actually there.

---

## How to drill it the Velocidad way

Comprehension here is worthless and production is everything, same as the rest of the engine. Reading
these rules will let you nod. It will not let you spot the fallacy in real time. The flywheel:

- **Deploy:** take a real argument (an op-ed, a claim in a meeting, your own position) and do two
  things out loud: (1) translate the key claim into names/predicates/connectives, (2) decide valid or
  invalid, and if invalid, name the counterexample or the fallacy.
- **Capture friction:** the moment you grope, that is the card. The friction types specific to logic:
  - *Form-blind:* could not see the shape of the claim under the English.
  - *Conditional slip:* affirmed the consequent or denied the antecedent without noticing.
  - *Quantifier slip:* read "some" as "not all," or swapped quantifier order.
  - *Validity/soundness blur:* attacked the facts when the form was the problem, or the reverse.
  - *Missed counterexample:* accepted a universal claim you could have killed with one case.
- **Distill:** turn each into a one-line rule you can recall ("only if reverses the arrow"; "to kill
  'all', find one").
- **Drill (SRS):** cards that show an argument and ask "valid or invalid, and why." Not definitions.
  *Judgments under time.*
- **Redeploy:** next real argument, reach for the move you drilled.

The target: collapse the gap between **recognizing** that an argument is bad and **producing**, on
demand, exactly why. Logic is what makes the "why" precise instead of a feeling.

---

*Original plain-language reconstruction of standard introductory logic (CC BY-SA 4.0). The concepts —
validity and soundness, the connectives, the conditional and its fallacies, quantifiers and the
counterexample method — are common to any first-order logic course; the wording and examples here are
original.*
