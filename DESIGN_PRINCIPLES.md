# Research Agent Kit — Design Principles, Aims and Core Idea

## In brief

Research Agent Kit is a platform-agnostic framework for using AI agents in research while keeping scientific judgment, data governance, and accountability under researcher control.

The core idea is simple: **AI should not merely be added to existing research tasks as an ad hoc assistant. Research workflows should be designed so that agents can contribute efficiently, while important decisions, evidence, and provenance remain explicit, inspectable, and portable.**

The framework therefore separates four things that are often mixed together:

* **Shared research record** — what is currently known, agreed, and in progress in a specific project.
* **Reusable agent skills** — procedures for recurring research tasks.
* **Research and data rules** — constraints on what agents may do.
* **Tool-specific setup** — minimal configuration for particular AI systems.

The aim is not to automate research end to end. It is to support **safe delegation with epistemic control**.

A central principle is:

> **Epistemic control is not a property of the AI model. It is a property of the research workflow.**

Agents may implement, transform, critique, propose, and help verify. Researchers retain control over consequential methodological choices, interpretation, and scientific claims.

For quantitative research, the framework additionally supports a traceable chain:

**research question → agreed analysis plan → implementation → research output → reported result → scientific claim**

The framework is designed so that each important transition in this chain can later be checked.

This file is the **workflow design**. It is not an ethics review, not a journal policy, and not a substitute for national research-integrity guidance. How the kit relates to those texts — and where it leaves things to the researcher — is in [`policies/ai-policy.md`](policies/ai-policy.md).

---

# Main idea

AI agents are becoming capable of doing more than answering questions or drafting text. They can inspect project files, write and run code, maintain context, use tools, revise manuscripts, and act across extended research workflows.

This creates a different methodological problem from ordinary generative-AI use.

The key question is no longer only:

> Is the AI output correct?

It is increasingly:

> **What was delegated, what did the agent decide, what evidence did it use, what did the researcher approve, and can another person or agent reconstruct that process?**

Research Agent Kit addresses this by making the research workflow explicit.

Rather than relying on a single long AI conversation or proprietary project memory, important project information is stored in a shared research record. Rather than repeatedly prompting an AI to perform common research tasks, reusable procedures are encoded as agent skills. Rather than relying on researchers to remember when AI should stop, the workflow identifies researcher decision points where substantive scientific choices require explicit human judgment.

The result is intended to make AI-assisted research simultaneously:

* faster where delegation is appropriate;
* more explicit where scientific judgment matters;
* safer where data access is restricted;
* more reproducible where computation matters;
* more transparent about the role of AI;
* and more verifiable from analysis through manuscript claims.

---

# Aims

## 1. Make AI-assisted research portable across tools

Research projects should not become dependent on the memory, conventions, or proprietary project structure of one AI product.

A researcher may use different systems for different tasks. Co-authors may use different systems entirely. The durable research record and reusable procedures should therefore live in ordinary project files and open or broadly supported formats.

The workflow should remain intelligible even if the preferred agent changes.

The framework is therefore **agent-agnostic at the workflow level**, while acknowledging that different agents have different technical capabilities.

---

## 2. Preserve scientific ownership

AI agents can perform substantial intellectual and technical work, but the research team remains responsible for the science. The researcher remains responsible for content, conclusions, and reliability. An AI system is not an author.

Agents may:

* implement an agreed analysis;
* generate alternatives;
* critique reasoning;
* draft or transform text;
* inspect consistency;
* identify possible errors;
* propose new analyses or interpretations.

Agents should not silently convert their own proposals into accepted scientific decisions.

When a proposed action would materially change the study design, measurement, sample, analysis, interpretation, or claims, the workflow should surface a **researcher decision needed** point.

The objective is not constant human approval of trivial actions. Human attention should instead be concentrated on **epistemically consequential transitions**.

---

## 3. Move important research knowledge out of chat history

AI conversations are useful working spaces, but poor long-term research records.

They are often:

* lengthy;
* difficult to search reliably;
* selective in what they retain;
* tied to a particular platform;
* inaccessible to collaborators using another tool;
* unclear about which ideas became actual project decisions.

The framework therefore distinguishes temporary conversation from a durable **shared research record**.

The shared record contains the current project overview, analysis plan, important research decisions, status, and other authoritative project information.

Chat can be discarded without losing the scientific state of the project.

---

## 4. Distinguish current truth from history and transient work

Different kinds of research information should not be mixed into a single growing notebook or task ledger.

The framework distinguishes:

* **project overview** — what is currently known about the study;
* **analysis plan** — analyses the researchers have agreed to perform or report;
* **research decision notes** — why important choices were made;
* **tasks** — temporary work still to be completed; kind of work is the role for that run;
* **project status** — a concise orientation summary;
* **Git history** — how files changed over time.

This separation reduces duplicated or contradictory project memory and makes it easier for a new agent or collaborator to understand the project.

A key design rule is:

> **One fact should have one authoritative home.**

---

## 5. Encode recurring research procedures as reusable agent skills

Many research tasks are not project-specific.

Examples include:

* understanding a research project;
* developing analysis code using safe data;
* documenting a consequential methodological decision;
* checking whether project records should be updated;
* auditing code against an analysis plan;
* reviewing the relationship between results and manuscript claims.

These procedures should not need to be reconstructed through prompts in every project.

The framework therefore packages recurring procedures as **agent skills** that can be versioned, tested, improved, and reused across projects.

A skill describes **how a task should be performed**.

It should not contain the scientific facts of a particular project.

---

## 6. Separate skills, project knowledge, rules, and tools

A major architectural principle is to avoid putting everything into one instruction file.

The framework separates:

### Shared research record

What is true or agreed in this particular study.

### Agent skills

How recurring research tasks should be performed.

### Research and data rules

What agents are permitted or required to do.

### Tool-specific setup

Minimal configuration necessary for a particular agent environment.

This separation reduces duplication and makes it easier to update one layer without silently changing another.

---

## 7. Make specification precede consequential execution

AI systems are particularly useful at implementation. They are also capable of quietly filling gaps in underspecified instructions.

In research, those gaps may contain substantive choices.

The framework therefore encourages an explicit transition from a research question to an agreed analysis plan before an analysis becomes a reportable result.

For quantitative research:

**research question → agreed analysis → implementation → output → claim**

An agent may explore or prototype more freely, but a result that enters the scientific evidence base should correspond to an analysis the researchers have explicitly agreed to.

This does not require a fully preregistered project from day one. Different analyses can become agreed at different times.

---

## 8. Support exploration without confusing exploration with evidence

Research is iterative. Agents should be allowed to:

* inspect metadata;
* create synthetic examples;
* profile data;
* write experimental code;
* investigate unexpected patterns;
* propose alternative models.

The framework should not turn exploratory work into a bureaucratic process.

The important boundary occurs when exploratory work is promoted into a result the research team intends to rely on.

Draft analyses and draft outputs therefore remain distinct from approved research results.

---

## 9. Make sensitive-data boundaries structural

For register data and other sensitive research material, a warning in a prompt is not sufficient protection.

Where required by the project, the workflow should ensure that:

* restricted row-level data remain outside the agent-accessible project;
* agents work with metadata, codebooks, synthetic data, or approved aggregate outputs;
* real-data execution occurs only through an authorised analyst or approved secure process;
* outputs crossing the boundary satisfy project-specific privacy rules.

The exact technical implementation may vary between environments.

The general principle is:

> **High-risk boundaries should be enforced structurally where possible, not merely requested in natural-language instructions.**

Projects using public or otherwise agent-accessible data may use a less restrictive data-access profile.

Restricted mode covers **row-level real data**. A cloud assistant may still send **project text** (plans, drafts, notes) to a vendor. That is a separate boundary. Use a tool your organisation allows.

---

## 10. Treat research outputs as traceable artifacts

A reported result should not be an unexplained number copied from an analysis console into a manuscript.

Where feasible, research outputs should carry enough provenance to reconstruct:

**agreed analysis → producing script or process → approved result**

For quantitative workflows, this may later extend to:

**approved result → table or figure → manuscript statement → scientific claim**

Machine-readable provenance reduces manual copying, makes auditing easier, and allows future agents to answer questions such as:

> Where did this estimate come from?

---

## 11. Build verification into the workflow

AI reliability should not depend on a general instruction to “double-check everything.”

Verification should instead target specific transitions in the research evidence chain.

Examples include:

* Does the code implement the agreed analysis?
* Was the result generated from the stated analysis?
* Are reported numbers derived from approved outputs?
* Does the manuscript accurately describe the statistical result?
* Does the scientific claim exceed what the design permits?

The run that produced a change should not be treated as sufficient independent verification of that same change.

Different models, tools, computational checks, or human review may provide stronger forms of verification depending on the importance of the task.

---

## 12. Keep a lightweight record of material AI involvement

Disclosure should not depend on remembering months later which parts of a project involved AI.

At the same time, attempting to track every AI-generated sentence or every interaction would create substantial noise and provide little scientific value.

The framework therefore aims to record **material AI contributions**.

Relevant information may include:

* research stage;
* affected research artifact;
* role played by AI;
* whether the substantive idea originated from the researcher, AI, or both;
* what the researcher did with the contribution;
* how the contribution was checked.

This provenance can later support transparent team communication and publication disclosure.

The optional on-disk log is a project file and defaults to off. **Disclosure in the paper** when AI affected reliability remains the researcher’s duty. Turning the log off does not mean the use may stay hidden.

The focus is on **AI's role in the research process**, not percentages of AI-generated text.

---

## 13. Make epistemic control visible

A central risk of agentic research is not simply hallucination.

It is gradual transfer of scientific decision-making to the agent without either the researcher or collaborators noticing.

For example:

**AI proposes a methodological change → implements it → interprets the resulting pattern → revises the manuscript**

Each individual step may appear reasonable, while the overall workflow has allowed the AI to make the scientific decision.

The framework therefore treats such transitions explicitly.

The minimal distinction is:

### Already agreed

The relevant choice has already been made by the researchers. The agent may implement it.

### Researcher decision needed

The proposed action would materially change the science. The agent should surface the decision rather than silently proceed.

This is the operational meaning of **epistemic control** in the framework.

---

## 14. Support collaboration across researchers and agents

A research team should not need every co-author to use the same AI system.

The long-term architecture should allow:

**researcher + preferred agent → shared research record**

while maintaining governance over what becomes accepted project knowledge.

Collaborators and their agents may propose analyses, interpretations, literature findings, or manuscript changes. Those contributions should be distinguishable from the authoritative project record until they have been reviewed appropriately.

For co-author wording, use a **review copy** (Google Docs). Suggestions are accepted there; leftover open comments become inbox items. Do not duplicate every small edit in the project folder.

This makes AI-assisted collaboration a property of the project rather than a collection of disconnected private chats.

---

## 15. Use existing conventions rather than inventing a new standard

The framework should reuse established or emerging conventions wherever they are adequate.

Examples include:

* Git for file history;
* `AGENTS.md` for repository-level agent guidance;
* Agent Skills for reusable procedural capabilities;
* research-compendium principles for reproducible project organisation;
* decision-record approaches for documenting consequential choices.

The objective is not to create a new universal AI-research standard.

The objective is to combine useful existing conventions into a coherent research workflow and add only the research-specific structures that are genuinely missing.

---

## 16. Keep the core simple and extend through profiles

The core workflow should remain small enough to understand and adopt.

More specialised capabilities should be added as optional profiles or skills.

Examples include:

* quantitative research / Quarto workflow;
* register-research data boundaries;
* research-chain auditing;
* co-author review;
* journal reviewer-response workflows;
* AI-use disclosure generation;
* more formal provenance;
* systematic skill evaluation.

This prevents specialised requirements from making the basic workflow unnecessarily complex.

---

# Design principles

The framework can be summarised in the following principles.

### Human scientific ownership

Researchers retain responsibility for consequential scientific decisions and claims. An AI system is not an author.

### Explicit before consequential

Important analysis or interpretation choices should become explicit before they are treated as settled results.

### Delegate implementation, not accountability

Agents can perform substantial work without becoming the authority for that work.

### Research state outside chat

Durable project knowledge belongs in portable project files.

### One fact, one authority

Avoid duplicated sources of truth.

### Event-driven project updates

Record durable knowledge when meaningful research events occur, not because a chat session happens to end.

### Exploration is cheap; promotion to evidence is controlled

Agents can explore freely within data rules, but draft work is distinct from accepted evidence.

### Structural controls for structural risks

Sensitive-data access should be technically restricted where possible.

### Provenance over recollection

Important results, decisions, and material AI contributions should be reconstructable later.

### Verification at transitions

Check the interfaces between plan, code, output, manuscript, and claim.

### Skills are procedures, not project memory

Reusable research practice belongs in skills; project facts remain in the project.

### Platform independence

The workflow should survive changes in AI vendors and tools.

### Progressive complexity

Start with a small working core; add collaboration, auditing, formal provenance, and integrations only when needed.

### Cite existing integrity guidance

Do not invent a parallel ethics code. Point to national and field guidance; say honestly where this kit does not try to cover it. See `policies/ai-policy.md`.

---

# Intended outcome

A researcher using the framework should eventually be able to open a project with a capable AI agent and have that agent answer, from the project itself:

* What are we studying?
* What analyses have we agreed to?
* Which analyses are still proposals?
* Why did we make this methodological choice?
* What can I safely do with the available data?
* Which results are approved for use?
* Where did this result come from?
* Which decisions still require researcher judgment?
* What material role has AI played so far?
* What work remains?

The framework should also make it possible for another researcher, another agent, or a future version of the same project to reconstruct those answers without depending on the original chat history.

That is the core proposition:

> **AI agents should increase research capacity without making the scientific process less inspectable, less reproducible, or less researcher-controlled.**
