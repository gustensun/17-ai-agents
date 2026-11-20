# Matching the owner's voice

Read this when the owner supplied writing samples or a brand voice document, or asked for a piece in their own voice.

## Where the voice comes from

Use the first source that exists:

1. The samples the owner gave during setup, in `my-business/voice-samples.txt`.
2. The owner's own messages in the conversation. How they phrase requests is how they talk.
3. The Voice card in `my-business/BRAIN.md`, or a brand voice document.
4. The default voice at the end of this file.

Published copy that someone else wrote, or that was written with AI, is a weak sample. Prefer text the owner typed or said themselves: posts, emails, DMs, transcripts of them speaking.

## Build the profile

Put the samples in one text file and run:

```
python3 skills/anti-ai-slop-writing/scripts/slop_scan.py --profile my-business/voice-samples.txt
```

It prints sentence-length numbers, contraction and first-person rates, punctuation habits, recurring words and common sentence openers. With under 300 words of samples the numbers are rough, so lean on reading the samples.

Then write a profile of about eight lines and keep it in the Voice card:

- Sentence length: typical length, and how far the short and long ones spread.
- Paragraphs: how many sentences, and whether one-line paragraphs appear.
- Person: I, we, you, and how often.
- Contractions and casual qualifiers they use.
- Punctuation habits: parentheses, questions, exclamation marks, colons.
- Recurring words, product names and terms. Use these exact words and don't swap in synonyms.
- How they open a piece and how they stop.
- What never appears in their writing.

## Apply it

- Draft to the profile, then scan with `--voice my-business/voice-samples.txt`. The output puts the draft's numbers next to the owner's so you can see the large gaps.
- Close the gaps by changing how the sentences are built. Sprinkling in the owner's favorite words to hit a count makes it worse.
- A REVIEW pattern that appears at least twice in the samples is downgraded to INFO and marked as the owner's habit. Keep it at about the rate the owner uses it.
- Dashes are still removed from delivered copy even when the samples contain them, unless the owner asks to keep them.
- Voice never overrides truth. If the samples exaggerate, the new piece still claims only what the evidence supports.
- When writing for a brand with several authors, profile the brand's best-performing pieces and say so in the profile.
- When writing for a client, use the client's samples from `my-business/clients/<client>/`.

## Default voice when there are no samples

- Plain and confident. Says the thing once.
- Specific: prefers the number, the name and the example to the category.
- Warm without performing closeness. Speaks to one reader as a capable adult.
- Uses contractions and first person where the format allows.
- Has opinions and gives the reason for each.
- Comfortable leaving a point open when it really is open.
