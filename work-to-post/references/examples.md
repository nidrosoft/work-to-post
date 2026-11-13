# Worked examples

These examples demonstrate decisions about reader, evidence, angle, and format. They are not facts to reuse in another person's profile. The short Nidrosoft example uses user-supplied context and public descriptions. The other profiles and explicitly illustrative scenarios are teaching material, not verified accounts of the author's work.

The two Premium format demonstrations below use invented scenarios, explicitly identified outside the copy. They demonstrate narrative depth and thread structure, not actual client outcomes or the author's experience. Short examples later in this document remain useful when the reader and material call for them.

## Premium long post: a pattern observation

**Illustrative profile and material:** An AI architect observed three imagined support pilots. The intended reader is an engineering lead considering the author for a personal assignment. The repeated work of checking facts supports A08. This is a private-preview teaching example, not a verified case study.

**Format:** One connected long post. The observation and proposed next experiment benefit from being read together. No sales ask or artificial thread split is necessary.

**Post:**

> Elena's support team could generate a reply in seconds and still needed four systems open before sending it.
>
> The order status was in one place. Delivery information was in another. Refund rules lived in a document. The conversation history was in the support tool.
>
> The draft arrived quickly. Checking whether it was correct took the work.
>
> I saw the same pattern in two other support pilots: faster writing exposed how much time people spent finding and verifying the facts.
>
> That changes what I'd measure in the next experiment.
>
> I'd follow a ticket from opening it to sending an answer someone had checked. I'd record which systems the person visited, what they corrected, and what they still had to decide.
>
> Then I'd test whether providing current order details and the relevant policy reduced that work.
>
> There will still be cases where a person needs to make a judgment. I want those cases visible.
>
> A useful support benchmark should tell me whether the team reached a correct, reviewable answer with less effort. Draft generation time is one part of that measurement.

**Readiness:** Complete as an illustrative format example. Real publication as a firsthand observation requires the author's actual sessions and findings. Preserve the bounded scope and proposed-test language when adapting it.

## Premium thread: an engineering case study

**Illustrative profile and material:** A product engineer explains an imagined import repair to an engineering lead. A03 fits the actual decision sequence within the scenario. The named person and implementation history are invented teaching material.

**Format:** Four numbered posts. Each adds a different part of the explanation: the trigger, architecture, retry behavior, and verification. Premium access permits longer parts; a standard-account adaptation would need different splits.

**Post 1 of 4:**

> 1/4
>
> Evan closed his laptop during a customer import, and the import stopped halfway through.
>
> I had built the first version around an open browser session. It worked during a demonstration because nobody closed the tab.
>
> Once customers started importing larger files while doing other work, that assumption stopped holding.
>
> I moved the import into a background worker.

**Post 2 of 4:**

> 2/4
>
> The server now creates an import record, stores the file, and queues the work.
>
> The browser receives a job ID and displays progress from that record.
>
> Closing the page no longer owns the fate of the import. When Evan opens it again, the page retrieves the same job and shows its current state.
>
> That also gives support a specific job to inspect when someone reports a problem.

**Post 3 of 4:**

> 3/4
>
> Moving the work introduced another question: what happens when a worker retries a batch?
>
> I gave each imported row a stable identity within its import and enforced uniqueness in the database.
>
> That protects against the same logical row being inserted twice, including when two attempts overlap.
>
> Progress only advances after the batch has been committed.

**Post 4 of 4:**

> 4/4
>
> I tested closing the tab, refreshing during an import, and interrupting the worker between batches.
>
> The job resumed, and the imported rows stayed unique.
>
> Cancellation is the next piece. A queued job needs a stop request the worker can observe; closing a browser tab can't serve that purpose anymore.
>
> I'm keeping that distinction visible in the interface so "close" and "cancel" don't promise the same behavior.

**Readiness:** Complete as an illustrative thread. A real case study must use the author's actual architecture, tests, and remaining work. The copy does not promise an attached recording or repository.

## Nidrosoft and a delivered integration

**Profile supplied for this example:** Cyriac runs Nidrosoft and describes 15+ years across product engineering, full-stack development, AI architecture, design, founding, consulting, and forward-deployed engineering. The personal account should support both studio projects and individual opportunities.

**Brief:** A published client testimonial describes an HVAC owner working on roofs while calls and lead details were being missed. Nidrosoft built a phone-agent and CRM workflow that captures the job and alerts the owner. The intended reader is a business owner with the same problem. The goal for this post is CLIENTS. A public testimonial is available, but a demonstration recording has not been supplied.

**Facts available:** The client's reported situation and workflow are described on [Nidrosoft's website](https://nidrosoft.com/). There is no supplied numerical revenue, booking, or time-saving result. The author's experience comes from the author's current statement, rather than an independently checked employment history.

**Choice:** A02 Client deliverable showcase. The material describes a real engagement and an operational change. It does not support a benchmark or a numerical before-and-after claim.

**Draft:**

> An HVAC owner was missing leads while working on roofs.
>
> I built a phone agent connected to his CRM. It captures the job and alerts him while he's still on site.
>
> If your leads disappear between a call and a callback, let's talk about it at Nidrosoft.

**Supporting material:** Link the published testimonial. A demonstration with sample data would help, but the copy does not claim that a video is attached.

**Readiness:** Ready for the author's review against the source and actual scope. No fabricated conversion metric. If the copy is changed to promise a recording, readiness changes to Needs an asset until that recording exists.

**Same use case, different reader:** For an engineering team evaluating the author personally, A13 can show a diagnostic without inventing implementation details:

> If your form says "sent" but no lead reaches the CRM, submit one test with a unique name.
>
> Trace it through the form, server, integration and CRM.
>
> Investigate the first missing record. Check what was saved before trusting the success message.

The topic is still an integration. The contribution changed from showing delivered client work to helping diagnose a failure. This second draft does not claim that the HVAC system had that particular bug.

## A software engineer with an architecture idea

**Fictional profile:** A backend engineer wants contract or full-time opportunities at teams building data-heavy products. They are thinking through import reliability and have not supplied a shipped implementation or benchmark.

**Brief:** Explain when a CSV import should run as a background job. The intended reader is an engineering lead. Outcome is OFFERS. Available material is reasoning about cancellation, progress, and recovery after a disconnect. No measured latency or customer result is available.

**Choice:** A14 Decision rule. There is enough material for a conditional recommendation, but not a shipped demo or a postmortem.

**Draft:**

> I'd keep a small, bounded import in the request.
>
> When users need cancellation, progress or recovery after a disconnect, I'd move it to a background job.
>
> The design question is who owns the work after the browser closes.

**Supporting material:** Optional sketch of request ownership and background-job ownership. It must be labeled as a design proposal if created.

**Readiness:** Ready for review as a recommendation. No assertion that the engineer has shipped a queue, reduced latency, or solved an outage. No sales CTA is necessary for this post.

## An independent small-business consultant

**Fictional profile:** A consultant helps service businesses improve intake and scheduling. They want scoped client engagements through their practice. They have no performance study to cite.

**Brief:** Help an owner investigate appointments that are confirmed to customers but missing from the team's calendar. Give them a next check that can reveal where the process fails.

**Choice:** A13 Public help and diagnosis. Use a conditional symptom, rather than claiming the consultant found the cause inside a particular client's system.

**Draft:**

> If a customer has a booking confirmation but your team can't find the appointment, trace one test booking.
>
> Check the form, calendar and notification separately.
>
> A confirmation email tells you what was sent. Verify which calendar received the booking.

**Supporting material:** A simple diagram can help. The diagnostic is useful without a downloadable resource or invented case study.

**Readiness:** Ready for review as conditional advice. A follow-up can explain a real investigation once it has happened.

## An early-career designer moving into engineering

**Fictional profile:** A designer is learning frontend implementation and wants personal offers. They have no senior title, client results, or employer history to cite. They can offer a short component handoff checklist.

**Brief:** Help a teammate implement form behavior consistently. The resource is the content of the post itself.

**Choice:** A06 Free tool or template. The artifact exists inline. No GitHub release or years-of-experience claim is needed.

**Draft:**

> A form handoff checklist you can paste into a component spec:
>
> [ ] Loading, success and error states
> [ ] Values kept after a failed submission
> [ ] Keyboard path and error focus
> [ ] Small-screen behavior with long input

**Supporting material:** Optional filled example for one component. If the writer has only tried it on a learning project, keep that context when discussing results.

**Readiness:** Ready for review as an inline checklist. The author can demonstrate useful knowledge without borrowing someone else's seniority.

## A requested comparison without test results

**Request:** "Write a post saying model A is better than model B at customer support. I have not tested them yet."

**Choice:** A11 is the intended angle, but it needs measurements. Do not manufacture them or silently describe a test as complete. Offer a proposed experiment.

**Draft:**

> My proposed support-model test would use the same held-out tickets, tools and scoring rules for each model.
>
> I'd compare verified answers, escalation quality and cost per resolved ticket, then publish the failures alongside the totals.

**Readiness:** Ready for review as a proposed test. A result-bearing comparison still needs the actual experiment, versions, conditions, denominator, and measurements.
