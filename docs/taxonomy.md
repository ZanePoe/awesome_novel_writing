# Scope and taxonomy

## What gets included

Tools that directly help with novel conception, character and worldbuilding, long-form chaptered generation, story-state maintenance, revision and screenplay adaptation are in scope. User-provided adjacent projects are kept with their boundaries labeled — for example, general article revision and film narration.

A project is never excluded for having few stars. Every entry at least has an identifiable repository, a verifiable source for its purpose, and a clear category. Promotional pages, pure readers, novel download sites, generic novel CMSes and general model APIs unrelated to writing do not enter the core catalogue. A repository with no declared license can still be listed as a lead, but it is never defaulted to an open license.

## The six primary categories

| Primary category | Decision criterion | Typical input and output |
| --- | --- | --- |
| Novel-writing software and workbenches | The main entry point is an editor or project workspace, with the author continuously involved in writing and review | Inspiration/manuscript → settings, plans, candidate chapters, revised drafts |
| Automated writing agents and creation engines | The main value is executable generation, review, state management or file-operation flows | Goal/outline → multi-step runs and chapter artifacts |
| Long-form creation skills and method frameworks | The main deliverable is Skills, prompts, rules or process documents for an external agent to use | User material + host agent → a writing process executed per the method |
| Style revision, de-templating and quality checks | The main job is diagnosing or rewriting existing text | Manuscript → located issues, rewrite suggestions or revised drafts |
| Screenplays, short-drama adaptation and film narration | Output leans toward scripts, episode structure, scenes, storyboards or narration | Novel/story/film → script or narration production material |
| Creative writing evaluation tools | The main goal is evaluating models or methods, not providing an everyday editor for authors | Models and tasks → evaluation artifacts |

Each entry has exactly one primary category to avoid double counting; the form field further specifies desktop app, web workbench, CLI, Skill, methodology or evaluation framework. Multi-feature projects are categorized by their main entry point and output, which does not mean they only cover one stage.

## Boundaries that must be kept apart

- A Skill is a resource that makes a host agent follow a workflow; it is not standalone software with a built-in model.
- Long-term memory, RAG, character state tables and foreshadowing ledgers record different things; the presence of these terms does not mean contradictions have been eliminated.
- "Can generate many chapters" and "those chapters are publishable quality" are not the same conclusion.
- De-templating, narrative-structure repair, grammar polishing and literary editing each have different goals; a rule hit cannot prove a text was written by AI.
- Storing drafts locally does not mean manuscripts are never transmitted when a remote model is called.
- Short-drama adaptation, original screenplays and film narration are not the same writing task, and the entries keep them distinct.
- An in-progress branch, a preview release and a roadmap do not automatically inherit the full capabilities of an older version or a demo video.

## Reference-project mapping for this round

All deduplicated reference projects are included. `Denova` maps to `alfredxw/denova`, Easy Writing maps to `yilujian/easy-writing`, and the user confirmed `ai-juben` maps to `VanGong1999/juben`. The duplicated `Nanako0129/sepia -g` is treated as the same project: `-g` is not part of the repository name and does not trigger an install.

The original references and mapping results are in [seed-references.json](../data/seed-references.json). Feature evidence and license notes are in the [project details](projects.md).
