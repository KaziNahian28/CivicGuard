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
| X2 | Reference list, 2025b | Listed as "Reprimand: DPP Law" | DPP Law received a £60,000 monetary penalty, not a reprimand. Body text is correct; the reference entry is not |
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

---

## E. EVIDENCE ADDED FROM 18 AUGUST

| File | Shows | Status |
|---|---|---|
| `seed_verification_18aug.txt` | Terminal printout, every record with its computed deadline and expected state. The only artefact stating expected values independently of the interface. See N2 on the summary line | **Saved 18 Aug** |
| `seed_verification_18aug.png` | The same printout as an image | **Saved 18 Aug** |
| `post_reseed_dashboard_18aug.png` | Risk strip 1 / 1 / 2 / 1, volume cards 2 / 3 / 5 | **Saved 18 Aug** |
| `post_reseed_disclosures_18aug.png` | Six records, 2 pending, 2 approved, 2 rejected, both rejections showing reasoning and a timestamped decision line | **Saved 18 Aug** |
| `post_reseed_breaches_18aug.png` | Five rows across four states, including 240h notified late in red. See N3 | **Saved 18 Aug** |
| `post_reseed_dsars_18aug.png` | Seven rows, five cards, T. Ferreira at 2026-02-28 flagged completed late | **Saved 18 Aug** |

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
| Five ICO scenario replays | `evidence/scenarios/`, one folder per case. Order: Nottinghamshire, Lewisham, Plymouth and Norfolk, Hammersmith and Fulham, DPP Law | |
| Comparative analysis | OneTrust and Keepabl, documentation-based per DD4 | |
| Ch4 design and implementation | 3,000 words, 35% of the report, the largest remaining block | |
| Supervisor reply on marking scope | Email sent 23 Aug. Answer determines whether the replays are written under Implementation and testing at 20% or Critical evaluation at 5% | Sent |
