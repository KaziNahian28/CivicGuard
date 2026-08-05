# CivicGuard Build and Testing Log

Running record from the functional test pass onward. Every entry is tagged with the dissertation chapter it feeds, so the write-up can be assembled from this file rather than from memory.

Opened 5 August 2026. Keep in the repo root. Update as you go.

---

## A. DEFECT LOG

| ID | Date | Module | What happened | Expected | Severity | Status | Feeds |
|---|---|---|---|---|---|---|---|
| D1 | 5 Aug | Disclosure | DPO badge and Approve/Reject buttons visible when officer expected | Officer session shows Officer badge, no approval controls | Blocker | **Closed.** Wrong login, not a defect. Officer session verified correct | Ch5 |
| D2 | 5 Aug | Disclosure | New Disclosure Request form captures Title and Description only | Form should capture recipient and lawful basis | Major | **Open.** Fix before Sunday scenario replay | Ch4, Ch5 |
| D3 | 5 Aug | Disclosure | Em dash in Disclosure Title placeholder text | No em dashes anywhere in the interface | Minor | Open | Ch4 screenshots |
| D4 | 5 Aug | Disclosure | Em dash used as empty-state placeholder in Actions column | Hyphen or "No actions available" | Minor | Open | Ch4 screenshots |
| D5 | 5 Aug | Disclosure | Test record 4 contains typo "Submisison" | Clean test data before final screenshots | Minor | Open. Clear on Saturday re-seed | Ch4 screenshots |
| D6 | 5 Aug | Disclosure | Seed data titles contain em dashes (rows 1, 2, 3) | No em dashes in seeded records | Minor | Open. Fix in seed_data.py, re-seed Saturday | Ch4 screenshots |
| D7 | 5 Aug | Disclosure | `update_disclosure()` treats any `action` value other than `approve` as a rejection, rather than validating against an expected set | Unrecognised input should error, not silently reject | Minor | Open. Safe default so not urgent, but note honestly in Ch4 | Ch4 |
| D8 | 5 Aug | Breach | **ICO Notified overrides deadline status.** Record 3, discovered 2026-07-13, 554h elapsed, displays green because it is marked notified. A breach notified late presents as compliant | Notification date recorded and compared against the 72-hour deadline. Four outcomes: notified on time, notified late, not notified and within deadline, not notified and overdue | **Blocker** | Open. Top of Saturday | Ch4, Ch5 |
| D9 | 5 Aug | Breach | **Clock does not stop on notification.** Record 3 shows 554h, being discovery to now rather than discovery to notification. The figure will climb indefinitely and measures nothing | Elapsed time freezes at the point of notification | **Blocker** | Open. Same fix as D8 | Ch4, Ch5 |
| D10 | 5 Aug | Breach | **No amber band exists.** Test record 4 at 40h displays green, identical to a breach discovered minutes ago. Badge is green under 72h and red over, so it only turns red after the statutory deadline has already been missed | Three bands: green while comfortable, amber inside the final 24 hours, red past 72 | **Blocker** | Open. Saturday | Ch4, Ch5 |
| D11 | 5 Aug | Breach | Summary cards and row badges disagree. Test record 4 counts toward the Warning card but shows a green badge | Card counts and badge states derive from the same status logic | Major | Open. Resolves with D10 | Ch4 |
| D12 | 5 Aug | Breach | Card labels do not describe real states. "Warning, Under 72 Hours" covers every compliant breach including one reported minutes ago. Cards also imply mutual exclusivity when a breach can be both overdue and notified | Labels match the three bands once D8 and D10 are done | Minor | Open | Ch4 |
| D13 | 5 Aug | Breach | Timestamps display in raw form, e.g. `2026-07-10T14:43` | Readable date and time | Minor | Open | Ch4 screenshots |
| D14 | 5 Aug | Breach | Em dashes in card titles, badge text, form placeholder and seed record titles | No em dashes anywhere | Minor | Open. Fold into Saturday re-seed | Ch4 screenshots |
| D15 | 5 Aug | Breach | Test record 4 is functional test data | Remove before final screenshots | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D16 | 5 Aug | DSAR | **Deadline calculated as 30 days, not one calendar month.** Page subtitle states "30-day statutory deadline". Rows 1 and 4 both show exactly 30 days, correct only coincidentally because June has 30 days. A request received 31 January would be given until 2 March instead of 28 February | One calendar month from the relevant time | **Blocker** | Open. Absorbed into Friday's DUAA rebuild | Ch4, Ch5, viva |
| D17 | 5 Aug | DSAR | **Clock anchored to receipt only.** Single date field assumed to be receipt. Article 12A runs the period from the relevant time, being the latest of receipt, identity confirmation or fee payment | Additional date fields, with the calculation taking the latest | **Blocker** | Open. Friday rebuild | Ch4, Ch5, viva |
| D18 | 5 Aug | DSAR | **Late completion presents as compliant.** Record 4, deadline 2026-07-03, completed 2026-07-13, ten days late, displays a green "Done" badge | Completion date compared against deadline: completed on time or completed late | **Blocker** | Open. Friday rebuild | Ch4, Ch5 |
| D19 | 5 Aug | DSAR | On Track card reads 0 while four records exist | Card counts reconcile with row states | Minor | Open. Recheck after Friday rebuild | Ch4 |
| D20 | 5 Aug | DSAR | Seed records are functional test data | Remove or refresh before final screenshots | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D21 | 5 Aug | DSAR | **No identity verification capture.** Nothing records whether the requester's identity was confirmed, or when. Identity confirmation is one of the three candidates for the relevant time under Art. 12A | Date field for identity confirmation, feeding the relevant-time calculation | **Blocker** | Open. Friday rebuild, largest single addition | Ch4, Ch5, viva |
| D22 | 5 Aug | DSAR | **No fee payment capture.** Third candidate for the relevant time under Art. 12A has nowhere to be recorded | Optional date field for fee payment | Major | Open. Friday rebuild. If descoped, state the reasoning rather than omitting silently | Ch4, Ch6 |
| D23 | 5 Aug | DSAR | **No extension capture.** The two-month complexity and volume extension cannot be recorded | Extension flag with reason and revised deadline | Major | Open. Friday rebuild | Ch4, Ch5 |
| D24 | 5 Aug | DSAR | The 30-day figure appears in the entry form banner as well as the list subtitle: "30-day deadline applies. The deadline will be calculated automatically from the date received." The error is embedded in interface language, not only in the calculation | Both statements revised to one calendar month from the relevant time | **Blocker** | Open. Same fix as D16, two locations | Ch4, viva |
| D25 | 5 Aug | DSAR | Date Request Received captures date only, with no time component, unlike the breach form which captures both | Acceptable, since the period runs in calendar months, but record as a deliberate choice rather than an inconsistency | Minor | Open. Decide and document Friday | Ch4 |
| D26 | 5 Aug | DSAR | Assign To is free text and not linked to a user account, so assignment cannot be filtered or reported on | Out of scope for this project, but state the limitation | Minor | Open | Ch4, Ch6 |
| D27 | 5 Aug | DSAR | Em dash in Assign To placeholder text | No em dashes anywhere | Minor | Open | Ch4 screenshots |
| D28 | 5 Aug | DSAR | The 30-day figure also appears in the post-submission confirmation banner: "DSAR logged. 30-day deadline set for 02 March 2026". Three locations in total with D24 | All three revised to one calendar month from the relevant time | **Blocker** | Open. Friday, same fix as D16 and D24 | Ch4, viva |
| D29 | 5 Aug | DSAR | Test record 5 (Test Requester, received 2026-01-31) is functional test data | Remove before final screenshots, after the evidence screenshot is saved | Minor | Open. Saturday re-seed | Ch4 screenshots |

**Severity rule for this week:** blockers fixed Saturday, majors only if they touch the five ICO scenarios, minors written up as known limitations if time runs out.

---

## B. DESIGN DECISIONS (deliberate, not defects)

These are choices to defend in Chapter 4 and at the viva. Each one needs its reasoning stated in the report.

**DD1. Disclosure requests cannot be edited after submission.**
Reasoning: the DPO approves a specific request, being specific data to a specific recipient on a specific lawful basis. If an officer could amend a pending request after submission, what was approved and what is released could differ, and the approval would carry no evidential weight. The alternative design, allowing edits but resetting status to Pending for re-approval, was considered and rejected as unnecessary complexity for the scope. Feeds Ch4 (design rationale), Ch6 (future work).

**DD2. Deadline escalation beyond the status badge is out of scope.**
Reasoning: without mail or messaging infrastructure any notification would be a further on-screen flag, which the coloured badge and dashboard already provide. Scoped as future work rather than attempted and left half-built. Feeds Ch5 (evaluation limitations), Ch6 (future work).

**DD3. Compliance summary and reporting view is out of scope.**
Reasoning: no dependency for the five scenario replays that constitute the evaluation. Deprioritised against the audit trail and the DSAR clock rebuild given the fixed working window to 10 August. Feeds Ch6 (future work).

**DD4. Commercial tool comparison is documentation-based, not hands-on.**
Reasoning: OneTrust is demo-only and the Keepabl trial requires a business signup, so neither is accessible under a student licence. Stated openly as a method limitation. Feeds Ch5 (evaluation method and its limitations).

**DD5. Demo credentials are displayed on the login screen.**
Reasoning: deliberate demonstration convenience, would not exist in a deployed system. Already noted in the MPR. Feeds Ch4, Ch6.

---

## C. EVIDENCE CAPTURED

Every verified behaviour, with what proves it. This is what Chapter 5 is written from.

| Ref | Date | Claim evidenced | Evidence held | Feeds |
|---|---|---|---|---|
| E1 | 5 Aug | Role separation applies at session level: officer account displays Officer badge and Compliance Officer label | Screenshot, officer session, Disclosure Workflow page | Ch4, Ch5 |
| E2 | 5 Aug | An officer can raise a disclosure request. Record created with status Pending, dated 2026-08-05, attributed to Compliance Officer | Screenshot, disclosure list showing row 4 and confirmation banner | Ch5 |
| E3 | 5 Aug | An officer is not offered approval controls. Actions column shows placeholder where the DPO session shows Approve and Reject | Screenshot pair, same page under both roles | Ch5 |
| E4 | 5 Aug | **Server-side role enforcement confirmed.** `update_disclosure()` in app.py checks session presence and `session['role'] != 'DPO'` before any state change, and redirects with a flash message if the check fails. Enforcement is in the route handler, not the template, so it holds regardless of how the request is made | Screenshot of app.py, route `/disclosures/update/<int:id>` | Ch4, Ch5, viva |
| E5 | 5 Aug | Partial audit data already persisted. The UPDATE writes `approved_by` from the session and `updated_at` as CURRENT_TIMESTAMP, so the record carries who approved it and when. What is absent is a durable action history rather than current state only | Screenshot of app.py, same route | Ch4, Ch5 |
| E6 | 5 Aug | Breach discovery date and time is entered by the user rather than defaulting to record creation. Legally correct, since the Article 33 clock runs from awareness, which commonly precedes system entry. Verified by entry of 03/08/2026 23:00 returning 40h elapsed | Screenshot, Report Data Breach form and resulting record | Ch4, Ch5 |
| E7 | 5 Aug | The breach form states the legal basis on screen: "72-hour countdown starts from discovery", citing UK GDPR Article 33. The interface communicates the obligation rather than only recording data | Screenshot, Report Data Breach form | Ch4 |
| E8 | 5 Aug | A working three-state deadline display already exists in the DSAR module: overdue in red, due soon in amber (record 3, 1 day left), and completed. This is the pattern the Breach Tracker lacks (D10), so the fix has a working reference implementation within the same codebase | Screenshot, DSAR Manager list | Ch4 |
| E9 | 5 Aug | **The 30-day error confirmed empirically, not inferred.** A test DSAR received 2026-01-31 returned a deadline of 2026-03-02. One calendar month from 31 January is 28 February, so the system granted two days with no legal basis. The confirmation banner states the fault explicitly: "DSAR logged. 30-day deadline set for 02 March 2026" | Screenshot, DSAR Manager list with record 5 and banner. **Retain as the "before" half of a before-and-after figure pair for Ch4** | Ch4, Ch5, viva |

### Cross-cutting finding

**F1. The system tracks whether an action was taken, but not whether it was taken in time.** The same fault appears three times independently: a late ICO notification displays green (D8), a late DSAR completion displays green (D18), and the DSAR deadline itself runs two days long (D16, confirmed at E9). In every case the error direction favours the council, presenting compliance that is not present. The Disclosure Workflow escapes only because a disclosure carries no statutory deadline. Three of the eight blockers are one conceptual error repeated across modules. Worth stating directly in Ch5 as a finding of the testing phase rather than presenting the fixes without their history. Feeds Ch4, Ch5, viva.

### Evaluation risk arising from testing

**R1. The DPP Law Ltd scenario cannot currently be replayed as intended.** That case is in the evaluation set because the ICO was notified 43 days late. Under the present logic (D8, D9) the record would be entered, marked notified, and display green, so CivicGuard would present a documented compliance failure as compliant. D8 and D9 must be fixed before the Sunday scenario replay or the scenario produces the wrong result. Feeds Ch5.

**R2. The early-warning claim is not yet supported by the artefact.** The Breach Tracker argument rests on surfacing the deadline before it is missed, against an evidence base in which 47.5% of local government incidents were reported beyond 72 hours. With only two bands (D10) the badge turns red only once the deadline has already passed, which reports failure rather than preventing it. Fixing D10 is what makes the Chapter 5 claim defensible. Feeds Ch5, viva.

**R3. The Lewisham scenario cannot currently be replayed as intended.** That case is in the evaluation set because 35% of requests were not answered within statutory deadlines. Under the present logic (D18) a request completed after its deadline displays a green "Done" badge, so the system cannot surface the failure it was built to surface. Fix required before the Sunday replay. Feeds Ch5.

**R4. Legal accuracy is the sharpest viva exposure.** The DSAR interface currently states a 30-day deadline (D16) where the law provides one calendar month, and anchors the period to receipt (D17) where Article 12A provides for the relevant time. An examiner reading the subtitle has an immediate line of questioning. Friday's rebuild resolves both, and having resolved them converts the weakness into evidence of currency with the Data (Use and Access) Act 2025. Feeds Ch4, Ch5, viva.

---

## D. EVIDENCE CAPTURE PROTOCOL

Governs what gets saved and when, so nothing one-time-only is lost.

**Folder:** `CivicGuard/evidence/`. Committed to the repo, not left loose on the machine.

**Capture immediately, as encountered:**
- Any behaviour that is about to be fixed. One-time-only, cannot be recreated after the fix. Name `before_[defect]_[description]_[date].png`.
- Any error message, crash or stack trace. Hard to reproduce on demand.

**Do not capture now:**
- Normal screens working normally. The frozen Saturday build gives cleaner versions with tidy seed data, corrected wording and no em dashes. Today's screenshots would be discarded.

**Saturday, systematic capture session (Ch4 figure set):**
Once the build is frozen and re-seeded, walk every screen in every state: login, dashboard under both roles, all three list views, all three entry forms, every status band including the new amber breach band, the audit trail, and the approve and reject flows. Name by chapter and figure intent.

**Sunday, scenario capture (Ch5 evidence):**
One folder per ICO case, five in total. Each holds the replay screenshots plus the audit log extract for that scenario.

**Held so far:**

| File | Shows | Status |
|---|---|---|
| `before_D16_dsar_30day_05aug.png` | DSAR row 5, received 2026-01-31, deadline 2026-03-02, with the "30-day statutory deadline" subtitle in frame. The "before" half of the Ch4 before-and-after pair | **Saved 5 Aug** |

**Highest-risk item is not the screenshots.** It is this log. Commit it to the repo now and after every working session. The screenshots are reproducible from the running system until Friday. The log is not reproducible at all.

---

## E. TEST INVENTORY

Nothing is marked complete unless it was actually observed on screen or in code.

| # | Test | Status |
|---|---|---|
| 1 | Officer login and role display | Done, E1 |
| 2 | Officer raises disclosure | Done, E2 |
| 3 | Officer denied approval controls | Done, E3 |
| 4 | Server-side role enforcement | Done, E4 |
| 5 | Disclosure form fields | Done, D2 |
| 6 | Breach list and status display | Done, D8 to D14 |
| 7 | Breach form fields | Done, E6, E7 |
| 8 | Breach creation and elapsed calculation | Done, D10 |
| 9 | DSAR list and status display | Done, D16 to D19 |
| 10 | New DSAR form fields | Done, D21 to D27 |
| 11 | DSAR creation, deadline on a known date | Done, E9. Confirms D16 |
| 12 | DSAR status advance and complete buttons | Outstanding |
| 13 | Disclosure approve and reject as DPO | Outstanding |
| 14 | Mark ICO Notified button | Outstanding |
| 15 | Dashboard as officer | Outstanding |
| 16 | Dashboard as DPO | Outstanding |
| 17 | Session protection when logged out | Outstanding |
| 18 | Blank required field on all three forms | Outstanding |
| 19 | Future date as breach discovery | Outstanding |
| 20 | Very old DSAR receipt date | Outstanding |
| 21 | Disclosure list filter buttons | Outstanding |
| 22 | Logout function | Outstanding |
| 23 | Handbook word band and weightings | Outstanding |

---

## F. FRIDAY SCOPE, DSAR REBUILD

Established by test 10. Roughly half form work, half logic. A full day, not a morning.

**Form additions:** identity confirmation date (D21), fee payment date (D22), extension flag with reason and revised deadline (D23).

**Logic changes:** calendar-month arithmetic replacing 30-day (D16), relevant time as the latest of receipt, identity confirmation and fee payment (D17), stop-the-clock for time awaiting scope clarification, two-month extension handling (D23), completion compared against deadline (D18).

**Interface wording:** list subtitle and entry-form banner both revised (D24).

---

## G. OPEN QUESTIONS- **Dissertation word band and chapter marking weightings.** Needed from the module handbook before chapter word budgets can be set.
- **Supervisor repository access.** Repo is private. Decide whether Dr Aldmour needs read access for marking, and grant before 11 August if so.

---

## H. CHAPTER FEED SUMMARY

Quick view of where this log lands in the report.

**Ch4 Design and Implementation:** D2 (field capture), D3 to D6 (interface presentation in screenshots), DD1, DD5, E1, E4.

**Ch5 Testing, Demonstration and Evaluation:** the full defect log as testing evidence, DD2 and DD4 as evaluation limitations, E1 to E4 as demonstration evidence, plus the five ICO scenario replays to come.

**Ch6 Discussion and Conclusion:** DD1, DD2, DD3 as future work with reasoning already recorded.
