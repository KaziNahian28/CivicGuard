# CivicGuard Change and Evidence Ledger

Opened 10 August 2026, the freeze day. Records every change made from the
re-seed onward, every shift in a stated decision, and the evidence held
against each. Append to `CIVICGUARD_BUILD_LOG.md` or keep alongside it in the
repo root. Commit at the end of every session.

Purpose: the build log records what was built and why. This records what
changed after the build was declared finished, so that nothing in Chapter 4
or Chapter 5 rests on a decision whose reasoning has been lost.

---

## A. CHANGES MADE

| # | Date | What changed | Why | Evidence | Feeds |
|---|---|---|---|---|---|
| C1 | 18 Aug | `seed_data.py` replaced in full. Written 10 Aug, executed 18 Aug: the freeze day ran short and the build environment was unavailable 11 to 17 Aug | Old seed carried em dashes in three modules, thirty-day deadline arithmetic, and test records D5, D6, D15, D29, D44, D46, D47, D49. New seed loads a clean background caseload exercising every status band | `seed_verification_18aug.txt` and `.png`, plus post re-seed screen captures | Ch4 |
| C2 | 10 Aug | Seed now clears `disclosures`, `breaches`, `dsars` and `audit_log` before loading. `users` untouched | Handover step 1 required test records cleared at re-seed rather than accumulated | Terminal output | Ch4 |
| C3 | 10 Aug | Seed replicates `add_calendar_month` and `calculate_relevant_time` from `app.py` rather than using `timedelta(days=30)` | Seeded deadlines must agree with deadlines the application calculates. A seed using the old arithmetic would have reintroduced D16 at data level after it was fixed at code level | Printed deadline per record, checked against screen | Ch4, Ch5, viva |
| C4 | 10 Aug | Seed reads schema via `PRAGMA table_info` and writes only columns that exist | Defensive against schema drift between `init_db()` and the seed. Reports skipped columns rather than failing | Terminal output, skipped-column list | Ch4 |
| C5 | 18 Aug | Four `audit_log` rows written by the seed for decided disclosures, backdated | Chapter 4 figures otherwise show an empty Actions column. **Seeded rows are not officer actions and must not be presented as evidence that the audit trail functions.** The live scenario entries carry that claim | See note N1 | Ch4 |
| C6 | 18 Aug | Docstring header in `seed_data.py` converted to `#` comment lines | A duplicated `"""` introduced during file transfer opened and immediately closed an empty string, so the header text parsed as code and raised a SyntaxError on `Art. 12A`. Comment lines cannot fail this way | Terminal error, resolved | none |
| C7 | 23 Aug | Evidence folder reorganised into `defects/`, `ch4_figures/` and `scenarios/` | Defect before-and-after pairs and the clean Ch4 figure set are different kinds of artefact and were becoming hard to distinguish in a flat folder. **Filenames referenced throughout this ledger and `CIVICGUARD_BUILD_LOG.md` now sit one level down; references are descriptive rather than links, so nothing is broken, but a reader following one should look in `defects/`** | `dir` output before and after | none |
| C8 | 23 Aug | `after_D18_late_completion_flagged_08aug` converted from `.webp` to `.png` | Every other evidence file is PNG. Word embeds webp inconsistently and the fault would have surfaced during final formatting | none | Ch4 |
| C9 | 23 Aug | Disclosure 2 approved and disclosure 1 rejected through the interface as DPO | Produces genuine `audit_log` entries with real timestamps, addressing the limitation recorded at N1. The four seeded audit rows evidence display; these two evidence capture | `fig_flow_approve_23aug.png`, `fig_flow_reject_prompt_23aug.png`, `fig_flow_reject_result_23aug.png` | Ch4, viva |

---

## B. DECISIONS TAKEN OR SHIFTED

| # | Date | Decision | Previous position | Reason for the shift |
|---|---|---|---|---|
| S1 | 10 Aug | The five ICO scenarios are **not** seeded. They are entered live during the replay session | Handover section 6 step 1 had the seed reconstruct the five cases, with step 4 also replaying them | Seeding and replaying duplicates the records. Live entry produces genuine `audit_log` timestamps, which is what makes Chapter 5 evidence rather than illustration |
| S2 | 10 Aug | Scenario dates are scaled, not copied from the real cases | Not previously stated | Real dates from 2021 to 2023 render every record hundreds of days overdue and make the figures unreadable. Intervals that carry meaning are preserved: 43 days for DPP Law, the two-year exposure for Hammersmith and Fulham |
| S3 | 10 Aug | Recipient and lawful basis carried in the disclosure description text | D2 remains open, the form captures title and description only | Honest reflection of what the artefact records. **State this openly in Ch4 rather than letting the seeded text imply fields that do not exist** |
| S4 | 10 Aug | Hammersmith and Fulham replayed as a Disclosure Workflow scenario only, with the breach dimension written up rather than replayed | Considered treating it as a two-module scenario | MPR Table 1 is submitted and maps it to Disclosure Workflow. Changing the mapping now creates an inconsistency between two assessed documents |
| S5 | 23 Aug | Rejection reasoning left as a browser `prompt()` dialog rather than moved into a form field | Considered replacing it with a Bootstrap modal and textarea on 23 Aug | The change would touch the rejection route, which is the audit-writing path closed as D37 and D39 and the most heavily tested code in the system. Function is already correct: reasoning is captured, stored and displayed. What a modal buys is presentation. Changing it after the scenario replays would mean the code producing the Ch5 evidence is not the code submitted, so the only clean options were before the replays or not at all. Not at all was chosen, with 22 days remaining and 3,000 words of Ch4 outstanding. **Write up as a known limitation alongside D2 and DD6, not as an oversight** |

---

## C. CORRECTIONS CARRIED INTO THE DISSERTATION

Identified 10 August from the submitted MPR. Each must be fixed in the
dissertation text, not left to carry across.

| # | Where | Error | Correction |
|---|---|---|---|
| X1 | Introduction, and DSAR Management section | Art. 12A cited to `Regulation (EU) 2016/679` | Art. 12A is a UK-only insertion by the Data (Use and Access) Act 2025, s. 76. Never attributable to Regulation (EU) 2016/679. Same class of error as the thirty-day figure removed on 8 August |
| X2 | Reference list, 2025b | Listed as "Reprimand: DPP Law" | DPP Law received a £60,000 monetary penalty, not a reprimand. Body text is correct; the reference entry is not. Verified against the ICO enforcement page, 1 Sep 2026 |
| X5 | **This ledger and the 10 Aug handover, now corrected** | Both recorded that the DPP Law fine was for Arts. 5(1)(f) and 32 and **not** for the late notification | **Wrong.** The ICO fined DPP Law "for its infringements of Articles 5(1)(f), 32(1), 32(2) and 33(1)". Art. 33(1), the notification duty, is expressly among the infringements. The Commissioner calculated a single penalty rather than separate ones, capped at the maximum for Art. 5(1)(f) as the gravest, which is presumably where the misreading arose. **This correction helps the project:** the breach notification failure is part of the enforcement, which strengthens the justification for the 72-Hour Breach Tracker rather than weakening it. Verified 1 Sep 2026 |
| X6 | Ch4 wherever Hammersmith and Fulham is described | Risk of stating that 35 hidden worksheets contained personal data | The response contained an Excel spreadsheet with **35 hidden workbooks, of which ten contained personal information**. Of the 6,528 people affected, 2,342 were children, and 96 of those were unaccompanied asylum-seeking children. Verified 1 Sep 2026 |
| X7 | Ch4, Ch2 wherever the calendar month is attributed to Art. 12A | Risk of claiming the DUAA introduced the calendar-month deadline | It did not. One month from receipt was already the rule under Art. 12(3). What s.76 introduced, as Art. 12A in force 5 February 2026, is the **relevant time**, being the latest of receipt, receipt of information requested under Art. 12(6), and payment of any fee under Art. 12(5), plus the two-month extension mechanism. **Defect D16 was a thirty-days-versus-calendar-month error, which is an Art. 12(3) point; the identity and fee fields are the Art. 12A point.** Conflating the two is a viva risk |
| X8 | Ch4, T. Ferreira record | The record is received 31 January 2026, before Art. 12A commenced on 5 February 2026 | SI 2026/82 saves the previous position for requests already in hand at commencement. The deadline of 28 February is correct either way, since calendar-month arithmetic applies under both, so the figure stands. But do not describe that record as an Art. 12A demonstration. It demonstrates calendar-month arithmetic. P. Okonkwo and M. Kowalczyk are the Art. 12A records |
| X3 | Report Structure section | States six chapters | Handbook confirms five, with evaluation folded into Chapter 4. Section needs rewriting, not carrying across |
| X4 | Throughout | Reference labels | MPR labelling governs: 2023a Lewisham, 2023b Nottinghamshire, 2023c Plymouth and Norfolk, 2025b DPP Law, 2025c Hammersmith and Fulham |

---

## D. NOTES

**N1. Seeded audit rows.** The four `audit_log` entries loaded by
`seed_data.py` were written by the seed script with backdated timestamps.
They populate the Chapter 4 figures. They do not evidence that the audit
mechanism captures officer actions. That claim rests on the live entries made
during the scenario replays, and on the two rows written on 7 and 8 August
recorded in the build log at section C2. A viva answer that conflates the two
would be a weak one.

**N2. Error in the seed's own summary line.** The "Expected card states" block
printed by `seed_data.py` states the Breach Tracker should show 2 overdue. It
should read 1. That line is hardcoded text; the per-record lines above it are
computed from the data and are correct, showing one record at 96h overdue. The
application is right and the summary line is wrong. Identified 23 August by
reconciling the interface against the printout. Left uncorrected in the script
so that `seed_verification_18aug.txt` remains the artefact actually produced on
the day, with the discrepancy recorded here instead.

**N3. Breach Tracker cards do not account for every row.** Four cards totalling
four, against five rows. The planning objection record at 14h elapsed sits in
no card. This differs from the DSAR module, whose five cards were reconciled to
cover every row under D48. The breach cards surface risk rather than count
records, which is defensible, but the inconsistency between the two modules is
visible on screen and should be stated in Ch4 as a design choice rather than
left for a reader to notice.

**N4. Days-left arithmetic differs between seed and application by one day.**
The seed subtracts whole dates; `app.py` compares the deadline against the
current time, so a deadline five days out at 15:39 renders as four full days
remaining. Consistent across every row. The deadline dates themselves agree
exactly, which is where the legal obligation sits, and the drift is
conservative, flagging risk a day early rather than a day late. This is
therefore not a recurrence of finding F1. Ch4 states that "days left" means
complete days remaining.

**N5. Interface verified against the printout, 18 and 23 August.** All seven
DSAR deadlines match. T. Ferreira renders 2026-01-31 to 2026-02-28, confirming
D16 closed in the application and not only in the seed, and is flagged
"Completed late" against a completion date of 2026-04-16, confirming D18 closed
and evaluation risk R3 cleared. The Revenues mailbox breach renders "240h to
notify, LATE" in red despite ICO Notified reading Yes, confirming D8 closed and
evaluation risk R2 cleared. Dashboard risk strip reads 1 / 1 / 2 / 1 and
reconciles against the module rows.

**N6. Rejection prompt is a browser dialog.** `fig_flow_reject_prompt_23aug.png`
shows a native `window.prompt()` dialog labelled with the origin
`127.0.0.1:5000`. The label is a browser security feature and cannot be
removed or styled. Three consequences to state in Ch4 rather than leave for a
reader to raise: the reason is collected outside the application's own
interface; "mandatory" holds in the sense that the rejection does not proceed
without input, since Cancel dismisses the action entirely; and the local
address is visible in the figure, which is consistent with a prototype running
on a development server. Decision to leave it recorded at S5.

**N7. One frame carries both DSAR scenarios.**
`S3_02_long_running_request.png` was captured for Plymouth and Norfolk but also
contains the Lewisham record. Reading down the overdue rows: G. Mensah 176 days,
J. Whitmore 59, D. Oyelaran 32, A. Chowdhury 10, H. Ademola 7. Five requests
past deadline at five visibly different magnitudes in a single list. Two points
for Ch4. First, the ordering distinguishes a request three weeks late from one
nearly six months late without anyone running a report, which is the Plymouth
failure: a backlog reported as one number cannot separate the two, and
Plymouth's two-year cases were invisible for that reason. Second, the Lewisham
and Plymouth patterns coexist in one caseload rather than in separate staged
demonstrations, which is closer to how a council would actually encounter them.

**N8. Scenario 2 captures are seven days apart and unstaged.** H. Ademola was
captured on 25 August at one day before deadline, and again on 1 September at
seven days overdue, still open. No action was taken between the two, and the gap
arose because work paused rather than by design. The system surfaced the
deadline correctly at both points and the request still went late. This is the
Lewisham failure occurring inside the artefact rather than a demonstration of
it, and it gives concrete form to the limitation stated in the MPR, that
replaying documented scenarios cannot establish whether staff would act on what
the system surfaces. Recorded in `evidence/scenarios/S2_lewisham/NOTE.txt`.

**N9. Rejection prompt truncates at roughly sixty characters.** Observed during
the Nottinghamshire replay. `window.prompt()` renders a single-line input, so a
DPO cannot re-read a long reason before submitting it. The text stores and
displays in full afterwards. This is a usability consequence of the browser
dialog rather than a cosmetic one, and it strengthens the case for the modal as
future work. Extends N6.

**N10. Dashboard risk counts change with elapsed time.** The 23 August figure
shows 1 breach past 72 hours; on 1 September the same view shows 3, as seeded
breaches aged past the window with no code change. Any Ch4 reference to the risk
strip must cite the specific figure it came from rather than treating the
dashboard as a fixed state.

**N11. Seeded and live audit rows appear in the same frame.**
`S4_02_rejection_audit.png` shows seven decided disclosures with reasoning:
records 1 and 2 decided through the interface on 23 August, record 7 on 25
August and record 8 on 1 September, all four written by an officer action.
Records 3, 4, 5 and 6 carry backdated timestamps written by `seed_data.py`.
The frame is strong evidence that the audit trail functions across a caseload,
but Ch4 must say which rows are which. Presenting all seven as officer
decisions would not survive a single question. See N1.

**N12. Scenario note files use mixed formats.** `S2_lewisham` and `S4` hold
`.txt`, `S5` holds `.docx`. No practical consequence, but convert to a single
format before submission if any are reproduced in an appendix.

---

## E. EVIDENCE ADDED FROM 18 AUGUST

| File | Shows | Status |
|---|---|---|
| `seed_verification_18aug.txt` | Terminal printout, every record with its computed deadline and expected state. The only artefact stating expected values independently of the interface. See N2 on the summary line | **Saved 18 Aug** |
| `seed_verification_18aug.png` | The same printout as an image | **Saved 18 Aug** |
| `post_reseed_dashboard_18aug.png` | Risk strip 1 / 1 / 2 / 1, volume cards 2 / 3 / 5 | **Not retained** |
| `post_reseed_disclosures_18aug.png` | Six records, 2 pending, 2 approved, 2 rejected | **Not retained** |
| `post_reseed_breaches_18aug.png` | Five rows across four states, including 240h notified late in red. See N3 | **Not retained** |
| `post_reseed_dsars_18aug.png` | Seven rows, five cards, T. Ferreira at 2026-02-28 flagged completed late | **Not retained** |

Pre-reseed captures were not taken. The 14 items in the build log evidence
table already document that state, and `civicguard_prereseed_10aug.db` holds
the data itself, so the loss is covered. The four post-reseed captures listed
above were displayed on 18 August but not retained to disk; the 23 August
figure set supersedes them.

---

## F. CHAPTER 4 FIGURE SET, CAPTURED 23 AUGUST

All in `evidence/ch4_figures/`. Ten of ten captured.

| File | Shows | Status |
|---|---|---|
| `fig_dashboard_dpo_23aug.png` | Risk strip surfacing five failures across two modules ahead of volume counts. Captured while both disclosures were still Pending, so the volume cards read 2 / 3 / 5. The visible correction of finding F1 | **Saved 23 Aug** |
| `fig_form_disclosure_23aug.png` | Disclosure entry form. Title and description only; recipient and lawful basis absent, per D2 and S3 | **Saved 23 Aug** |
| `fig_form_breach_23aug.png` | Breach entry form, discovery timestamp field where the 72-hour clock starts | **Saved 23 Aug** |
| `fig_form_dsar_23aug.png` | DSAR entry form including identity confirmation and fee payment fields, the visible evidence of Art. 12A relevant time | **Saved 23 Aug** |
| `fig_login_roles_23aug.png` | Two demonstration accounts | **Saved 23 Aug** |
| `fig_flow_approve_23aug.png` | Disclosure 2 approved, audit line written 2026-08-23 04:07:25 by DPO | **Saved 23 Aug** |
| `fig_flow_reject_prompt_23aug.png` | Reasoning prompt before submission. See N6 | **Saved 23 Aug** |
| `fig_flow_reject_result_23aug.png` | Disclosure 1 rejected, reasoning persisted into the audit line | **Saved 23 Aug** |
| `fig_dashboard_officer_23aug.png` | Dashboard as Officer | **Saved 23 Aug** |
| `fig_disclosures_officer_23aug.png` | Disclosure list as Officer, Approve and Reject absent. Role separation evidenced by absence against the DPO frames | **Saved 23 Aug** |

**Data state after this session:** Pending Disclosures now reads 0. Any figure
needing a pending record must be captured before further approvals, or the
seed re-run, which would delete the two genuine audit entries at C9.

---

## G. STILL TO DO

| Item | Notes | Status |
|---|---|---|
| S1 Nottinghamshire | Disclosure raised as Officer, rejected as DPO with redaction reasoning. 4 captures | **Done 25 Aug** |
| S2 Lewisham | Two DSARs: H. Ademola for deadline visibility, P. Okonkwo for Art. 12A relevant time. 5 captures plus `NOTE.txt`. See N8 | **Done 1 Sep** |
| S3 Plymouth and Norfolk | G. Mensah, received 2026-02-10, 176 days overdue. 2 captures. See N7 | **Done 1 Sep** |
| S4 Hammersmith and Fulham | FOI publication with unchecked worksheets, rejected as DPO. 2 captures plus note | **Done 1 Sep** |
| S5 DPP Law | Breach logged, shown overdue, then marked notified and flagged late. 3 captures plus note | **Done 1 Sep** |
| Comparative analysis | OneTrust and Keepabl, documentation-based per DD4 | |
| Ch4 design and implementation | 3,000 words, 35% of the report, the largest remaining block | |


---

## H. SCENARIO REPLAY LOG

Entered live through the interface, per decision S1. Officer raises, DPO
decides, so the approval gate is exercised across a real role boundary.

**All case facts below were verified against ICO sources on 1 September 2026.**
Where the ICO notice does not state something, this log does not either.

### S1 Nottinghamshire County Council, 25 August

**Case, verified.** A social worker sent copies of a Child and Family
Assessment concerning two children to the children's mother and to two of her
former partners. The copies sent to the former partners should have been
redacted. The material disclosed related to previous domestic violence enacted
on the mother and the two children. Reprimand issued August 2023; the ICO URL
carries a 2023/09 path and the accompanying press release is dated 27 September
2023, so cite the reprimand rather than a bare month.

**Not verified, do not assert.** The specific Article infringed. Earlier drafts
of this ledger stated Art. 32(1); the ICO summary page does not state it.
Either confirm from the reprimand PDF or describe the failure without an
Article number.

**Replayed as:** disclosure raised by Officer stating three recipients and one
report; rejected by DPO requiring separate redacted versions per recipient.

**What it evidences:** the release could not proceed on the officer's own
authority, and the refusal is recorded with named actor, timestamp and grounds.

### S2 London Borough of Lewisham, 25 August and 1 September

**Case, verified.** Between 3 January 2022 and 3 January 2023, 35% of subject
access requests received were not responded to within the statutory deadlines
of one and three months. Reprimand, no fine, 16 August 2023.

**Do not conflate.** Lewisham also received a separate FOIA **enforcement
notice** in March 2023 concerning 338 overdue FOI requests, 221 of them over
twelve months old. That is a different action under different legislation. The
MPR cites the SAR reprimand as 2023a and that is the correct anchor for the
DSAR module.

**Replayed as:** H. Ademola, received 26 July, deadline 26 August, captured at
one day remaining and again seven days overdue. P. Okonkwo, received 20 July
with identity confirmed 10 August, deadline 10 September.

**What it evidences:** deadlines visible in the due-soon band before they pass,
and the relevant time running from the latest of receipt, identity confirmation
and fee payment. See X7 on what is and is not an Art. 12A point.

**Unplanned finding:** see N8.

### S3 Plymouth City Council and Norfolk County Council, 1 September

**Case, verified.** Joint reprimands issued 15 May 2023. Norfolk responded to
51% of SARs on time between April 2021 and April 2022, meaning 251 residents
did not receive a response within the legal timeframe. At Plymouth, over three
years, 18 requests took up to two years to complete and a further 18 took
between three months and one year; 20 requests were outstanding up to a year
old and eight still outstanding up to two years later. Plymouth's highest
compliance rate was 77% in 2022-23. The Plymouth reprimand cites Arts. 12(3),
15(1) and 15(3).

**Replayed as:** G. Mensah, received 2026-02-10, deadline 2026-03-10, rendering
176 days overdue and still open.

**What it evidences:** duration rather than lateness. See N7 on magnitudes.

### S4 Hammersmith and Fulham, 1 September

**Case, verified.** In October 2021 the council answered an FOI request made
via WhatDoTheyKnow. The published response included an Excel spreadsheet
containing **35 hidden workbooks, ten of which held personal information**. The
ICO noted the hidden files were not apparent, but that anyone with knowledge of
Excel would know how to inspect a spreadsheet for hidden data. In November
2023, almost two years later, WhatDoTheyKnow informed the council following a
review of its own site, and the information was removed from both sites
immediately. 6,528 people were affected, of whom 2,342 were children; that
data was classed as sensitive as it included looked-after children, 96 of them
unaccompanied asylum-seeking children.

The ICO assessed that the council lacked adequate technical and organisational
measures, including when it adopted the practice of using Excel spreadsheets
for FOI responses. Mitigating factors included the age of the data and the
absence of evidence of inappropriate access. Recommendations included using the
ICO's sign-off checklist when releasing information containing Excel
spreadsheets, and **requiring all material intended for publication to be
signed off by a manager**. Reprimand May 2025.

**Scope limit to state plainly in Ch4.** The artefact cannot open the file and
cannot detect hidden workbooks. What it does is create the moment at which
someone must confirm the check was done, and record who required it. That is
the manager sign-off the ICO recommended, arrived at from the other direction.
Claiming detection would be indefensible at the viva.

### S5 DPP Law Ltd, 1 September

**Case, verified, and previously recorded wrongly. See X5.** The ICO fined DPP
Law Ltd £60,000 for infringements of **Articles 5(1)(f), 32(1), 32(2) and
33(1)** between 25 May 2018 and 17 July 2022. Penalty notice dated 14 April
2025.

A brute-force attack reached an infrequently used administrator account on a
legacy case management system that lacked multi-factor authentication. The
attacker moved laterally and took over 32GB of data. DPP became aware only when
the National Crime Agency contacted the firm to say client information had been
posted on the dark web. DPP did not consider that loss of access to personal
information amounted to a personal data breach, and did not report to the ICO
until 43 days after becoming aware. The Commissioner calculated a single
penalty capped at the maximum for Art. 5(1)(f) as the gravest infringement,
rather than separate penalties per Article.

**Two things to state honestly in Ch4.** First, DPP Law is a law firm, not a
local authority, so it sits outside the council population the artefact targets
and is included because it is the clearest recent UK enforcement on Art. 33(1)
timing. Second, DPP was reported in April 2025 to be appealing the penalty;
check the current status before submission and describe the outcome accurately.

**What the replay should evidence.** The failure was one of classification, not
of ignorance of the deadline. The firm did not recognise the incident as
reportable. A tracker that starts a visible clock at the point of awareness
addresses the timing but not the classification judgement that precedes it.
That distinction is the honest limit of what the Breach Tracker can claim.

---

### S4, what was replayed

Disclosure raised by Officer for an FOI response containing an Excel workbook
assembled from operational extracts, with the description stating explicitly
that supporting worksheets had not been checked. Rejected by DPO on 1 September
at 17:00:58, requiring confirmation that all worksheets were removed or
verified as non-personal before resubmission.

**What it evidences.** A release nobody had reviewed was stopped, and a named
officer required the check, with grounds recorded. This is the manager sign-off
the ICO recommended, implemented as a system control rather than a procedure.

**What it does not evidence.** The artefact cannot open the file or detect
hidden workbooks. Recorded in the folder note.

### S5, what was replayed

Breach logged by Officer as loss of access to a case management system with the
extent of exfiltration unknown, the description recording the classification
decision and its reasoning explicitly. Discovery backdated approximately 96
hours, severity High. Captured overdue and unnotified, then marked ICO
notified and captured again showing the notification flagged late rather than
green.

**What it evidences.** The correction of finding F1. Before 9 August a
notification made after the deadline displayed as compliant and dropped out of
the failure count; it now records both that notification occurred and that it
was late.

**What it does not evidence.** The DPP failure was classification, not timing.
The tracker begins its clock when an incident is logged, which presupposes
someone has judged it reportable. Recorded in the folder note.

---

## I. STATE AT CLOSE OF 1 SEPTEMBER

All work requiring the running system is complete. Nothing remaining depends on
the build environment.

**Evidence held:** 16 defect captures in `defects/`, 10 Chapter 4 figures in
`ch4_figures/`, 16 scenario captures across five folders in `scenarios/` with
three explanatory notes, and `civicguard_prereseed_10aug.db`.

**Live audit entries created through the interface:** four disclosure decisions
on 23 August, 25 August and 1 September, plus one breach notification on 1
September. These, not the seeded rows, carry the claim that the audit mechanism
captures officer actions.

**Remaining work, none of it requiring the system:**

| Item | Weight | Notes |
|---|---|---|
| Ch4 design and implementation | 35% combined | Largest block, roughly 3,000 words |
| Ch4 critical evaluation | 5% | Draws on the five scenarios |
| Ch3 research methods | 10% | |
| Ch2 problem analysis | 10% | |
| Comparative analysis, OneTrust and Keepabl | within Ch2 | Documentation-based per DD4 |
| Ch1 introduction | 5% | Expand from MPR |
| Ch5 conclusions and future work | 5% | |
| Abstract | 5% | Write last |
| Corrections X1 to X8 | within structure 5% | Must be applied, not carried across |

**Thirteen days to submission on 14 September, viva 15 September.**
