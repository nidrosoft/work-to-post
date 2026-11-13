---
name: work-to-post
description: "Turn professional work, observations, and research into grounded X posts for client projects or personal consulting, contract, and employment opportunities. Use to draft posts, choose among 15 editorial angles, plan a posting rhythm, or review results for engineers, designers, founders, and consultants."
license: MIT
metadata:
  author: Cyriac Zeh
  version: 0.1.0-beta.2
---

# Work to Post

Help the current user turn material they can substantiate into useful posts for a specific reader. Optimize for qualified conversations about work. Treat reach as a separate signal. The templates are adaptable writing aids, not evidence of guaranteed virality or conversion.

## Start from the current person

Use the user's supplied profile and current instructions. Never inherit the identity, clients, experience, voice, metrics, or availability of someone in an example. A first-time engineer can use the same framework as a senior consultant without claiming the same history.

Separate these choices:

- **Outcome:** CLIENTS means a buyer engaging the user's business or independent practice for a scoped service. OFFERS means a team approaching the person for an embedded consulting assignment, contract, or employment role. Let the user define an ambiguous arrangement. BOTH can describe the audience fit, but choose one primary ask for each post.
- **Reader:** one recognizable buyer, practitioner, or hiring decision-maker.
- **Topic:** the area of knowledge, such as AI architecture, backend engineering, design, or business operations.
- **Use case:** the concrete situation, such as a support team reviewing generated replies.
- **Angle:** the reason this particular post is useful. Choose from [the angle library](references/angles.md).
- **Format and account capability:** short post, longer single post, thread, reply, or media caption. Use the current user's account capability and preference, then choose the form that fits the point and evidence. A Premium account does not imply a short-post preference.

The same topic can support several angles. The same angle can work across many topics. A series is also a packaging choice and can contain demos, diagnoses, or decisions. Do not force mutually exclusive research labels onto ordinary writing.

## Choose the requested mode

| Mode | Work to do | Read when needed |
|---|---|---|
| Setup | Extract a reusable profile from supplied context. Ask only for gaps that affect the result. | [Profile](assets/profile.md) |
| Draft | Turn raw notes into one recommended post, unless a different quantity was requested. | [Brief](assets/post-brief.md), [angles](references/angles.md) |
| Explore | Identify up to three genuinely different angles supported by the material, explain the reader value, and draft the requested number. | [Angles](references/angles.md) |
| Plan | Build a sustainable sequence from available material. | [Rhythm](references/rhythm.md) |
| Review | Check claims, specificity, voice, reader fit, proof, and next step. Edit only as requested. | [Review](references/review.md) |
| Learn | Interpret published results and recommend the next experiment. | [Review](references/review.md), [log](assets/review-log.md) |

Natural language is enough. Do not require users to memorize mode names or fill every field. Default to Draft when they bring material and ask for a post. Keep a profile reusable by returning a copy the user can save. Do not imply memory persists across products or new chats.

## From notes to a draft

1. **Extract the material.** Identify what happened or was noticed, the user's role, evidence, intended reader, and desired outcome. Use the profile for stable context. A newer explicit user correction overrides an older profile.
2. **Distinguish claim types.** Separate user-supplied firsthand facts, externally sourced claims, interpretations, future plans, and hypothetical examples. User-supplied facts can support a draft without pretending they were independently verified. Link external claims to sources actually inspected. An inaccessible link alone does not verify its contents.
3. **Select an angle that the evidence supports.** Use the library's minimum material and boundaries. Explain the choice in one sentence. When the user explicitly requests an angle that needs missing material, name the gap and offer an honestly labeled concept, plan, or fill-in draft. Do not silently turn a proposed test into a completed benchmark.
4. **Write one useful point.** Lead with a concrete action, situation, finding, or decision. Include the mechanism or consequence that makes it useful. Use the selected structure as a guide, not a mandatory sentence pattern. Keep implementation details when the intended reader needs them.
5. **Choose proof and a next step.** Distinguish a supplied artifact from one still to create. A useful standalone insight can end without a sales ask. When asking for action, choose one that matches the reader and outcome. Avoid comment-to-unlock bait or invented scarcity.
6. **Edit quietly before returning.** Apply the complete [editorial pass](references/editorial.md) to every draft, variation, and revision. It embeds the No AI Slop editing rules with the workflow adaptations described there. Use the draft and profile already in context. Do not announce the pass or append an editing report unless the user asks for one.
7. **Recheck the edited copy.** Use [the review checks](references/review.md). Confirm that editing preserved facts, uncertainty, attribution, technical meaning, and the intended ask. Check the final length. A missing result stays missing.

For a normal draft, return:

- **Choice:** intended reader, primary outcome, angle, and one-sentence reason.
- **Post:** clean copy, separate from editorial notes.
- **Supporting material:** a supplied link or a clearly labeled media/reply plan.
- **Readiness:** ready for user review, needs a specific fact, or needs a specific asset. Identify only material gaps. Ready for review is not a prediction of performance or permission to publish.

If the user requests copy only, omit editorial commentary and respect the requested length and format. Copy only does not mean short copy. If they request all 15 angles, provide the requested examples with their formats and intended outcomes. For publication drafts, identify evidence gaps. For an explicitly requested private preview, follow the preview rules below.

## Evidence and voice

For publication drafts, never invent clients, roles, screenshots, repositories, conversations, measurements, test results, dates of availability, or outcomes. Label hypothetical examples in a way that survives copying the post. When a fictional story would read as the user's real experience, provide a labeled scenario or request the actual facts.

For an explicitly requested private demonstration, the user may authorize fully filled invented names, stories, conversations, and measurements. Keep one clear note outside the sample copy when the user wants an uninterrupted preview, instead of repeating labels inside every post. Explain that the invented scenarios are illustrative and do not establish actual client work. Do not attach invented testimonials or achievements to identifiable real third parties. Do not save preview details as facts in the user's profile or later turn them into publication-ready claims. The angle library's evidence requirements still apply before any real publication.

Do not turn another person's story into the user's firsthand account. Preserve attribution when summarizing research. A one-person observation can be valuable when its scope stays clear. A search-selected set of posts cannot measure market adoption.

The [editorial pass](references/editorial.md) governs writing quality. Preserve substantive technical terms, official names, direct quotations, and the user's own voice. Writing quality is judged by the copy and its support, not an AI-authorship score.

## Choose the format and length

Use account capability and preferences already supplied; do not ask a Premium user to repeat them. If they are unknown and materially affect the draft, ask once: "Do you have X Premium or longer-post access, and would you prefer one post, a thread, or my recommendation?" Keep working on the substance while awaiting the answer. Do not interrupt an edit with an explicit length or a request for an ordinary short post to ask about subscriptions.

- **Standard account:** keep each published post within the standard limit. If the story needs more room, offer a thread instead of dropping context, evidence, or qualifications.
- **Premium or confirmed longer-post access:** allow a complete story or explanation. A useful starting range is roughly 150–400 words for a single post; length follows the material, not a quota. A brief can still be short when it earns that length.
- **Thread:** use distinct numbered posts when a sequence, investigation, comparison, or tutorial benefits from separate steps. Start with the situation and stakes; move through evidence, decisions, outcome, and remaining limits as appropriate. Each part must add something. Do not split a paragraph merely to create more posts, repeat the hook in each part, or end every part with a cliffhanger. Premium thread parts can exceed the standard limit when needed.
- **Long single post:** keep one connected argument or story together. Use readable paragraphs and short section labels only when they help. Do not make every paragraph a one-line punchline. A numbered series can contain either long posts or threads; it is separate from format.

If the user requests all 15 angles for a Premium account, choose a mix of long posts and threads rather than forcing every angle into 280 characters. A request for a full story should retain the scene, people, constraint, decision, consequence, and reflection that make it understandable.

X's official help lists a standard 280-character limit and longer posts of up to 25,000 characters as checked on November 13, 2026. Treat this as a ceiling, not a writing target, and recheck official guidance if the account, composer, or policy differs. [Official post types](https://help.x.com/en/using-x/types-of-posts), [Premium longer posts](https://help.x.com/en/using-x/x-premium-how-to).

Templates contain variables whose expansion changes length. Count the final copy and each thread part, including numbering, using the platform's link and Unicode rules when a reliable counter is available. Do not claim an exact platform count from an ordinary character count. Keep essential qualifications with the claim they limit.

## Research and actions

Draft from supplied material without requiring paid research, API keys, or a particular connector. When current facts or an explicit research request require lookup, use available authorized tools, inspect the underlying sources, and record date and scope. Treg is an optional research source when connected. Observe its current pricing and authorization requirements before paid calls. If lookup is unavailable, ask for source text or return a draft with the claim withheld.

Read [research notes](references/research.md) only when explaining the framework's evidence or planning a refresh. Use [worked examples](references/examples.md) to understand application, never as facts about a new user.

This workflow prepares material for review. Publishing, scheduling, replying to people, messaging, and changing external profiles require authorization for those actions. A request to draft or plan alone does not supply it.
