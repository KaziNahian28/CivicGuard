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
| D4 | 5 Aug | Disclosure | Em dash used as empty-state placeholder in Actions column | Hyphen or "No actions available" | Minor | **Closed 7 Aug** | Ch4 screenshots |
| D5 | 5 Aug | Disclosure | Test record 4 contains typo "Submisison" | Clean test data before final screenshots | Minor | Open. Clear on Saturday re-seed | Ch4 screenshots |
| D6 | 5 Aug | Disclosure | Seed data titles contain em dashes (rows 1, 2, 3) | No em dashes in seeded records | Minor | Open. Fix in seed_data.py, re-seed Saturday | Ch4 screenshots |
| D7 | 5 Aug | Disclosure | `update_disclosure()` treats any `action` value other than `approve` as a rejection, rather than validating against an expected set | Unrecognised input should error, not silently reject | Minor | Open. Safe default so not urgent, but note honestly in Ch4 | Ch4 |
| D8 | 5 Aug | Breach | **CLOSED 9 Aug.** ICO Notified overrides deadline status. Record 3, discovered 2026-07-13, 554h elapsed, displays green because it is marked notified. A breach notified late presents as compliant | Notification date recorded and compared against the 72-hour deadline. Four outcomes: notified on time, notified late, not notified and within deadline, not notified and overdue | **Blocker** | Open. Top of Saturday | Ch4, Ch5 |
| D9 | 5 Aug | Breach | **CLOSED 9 Aug.** Clock does not stop on notification. Record 3 shows 554h, being discovery to now rather than discovery to notification. The figure will climb indefinitely and measures nothing | Elapsed time freezes at the point of notification | **Blocker** | Open. Same fix as D8 | Ch4, Ch5 |
| D10 | 5 Aug | Breach | **WITHDRAWN 9 Aug, finding incorrect.** No amber band exists. Test record 4 at 40h displays green, identical to a breach discovered minutes ago. Badge is green under 72h and red over, so it only turns red after the statutory deadline has already been missed | Three bands: green while comfortable, amber inside the final 24 hours, red past 72 | **Blocker** | Open. Saturday | Ch4, Ch5 |
| D11 | 5 Aug | Breach | **CLOSED 9 Aug.** Summary cards and row badges disagree. Test record 4 counts toward the Warning card but shows a green badge | Card counts and badge states derive from the same status logic | Major | Open. Resolves with D10 | Ch4 |
| D12 | 5 Aug | Breach | **CLOSED 9 Aug.** Card labels do not describe real states. "Warning, Under 72 Hours" covers every compliant breach including one reported minutes ago. Cards also imply mutual exclusivity when a breach can be both overdue and notified | Labels match the three bands once D8 and D10 are done | Minor | Open | Ch4 |
| D13 | 5 Aug | Breach | Timestamps display in raw form, e.g. `2026-07-10T14:43` | Readable date and time | Minor | Open | Ch4 screenshots |
| D14 | 5 Aug | Breach | **CLOSED 9 Aug.** Em dashes in card titles, badge text, form placeholder and seed record titles | No em dashes anywhere | Minor | Open. Fold into Saturday re-seed | Ch4 screenshots |
| D15 | 5 Aug | Breach | Test record 4 is functional test data | Remove before final screenshots | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D16 | 5 Aug | DSAR | **CLOSED 8 Aug.** Deadline calculated as 30 days, not one calendar month. Page subtitle states "30-day statutory deadline". Rows 1 and 4 both show exactly 30 days, correct only coincidentally because June has 30 days. A request received 31 January would be given until 2 March instead of 28 February | One calendar month from the relevant time | **Blocker** | **Closed 8 Aug** | Ch4, Ch5, viva |
| D17 | 5 Aug | DSAR | **CLOSED 8 Aug.** Clock anchored to receipt only. Single date field assumed to be receipt. Article 12A runs the period from the relevant time, being the latest of receipt, identity confirmation or fee payment | Additional date fields, with the calculation taking the latest | **Blocker** | **Closed 8 Aug** | Ch4, Ch5, viva |
| D18 | 5 Aug | DSAR | **CLOSED 8 Aug.** Late completion presents as compliant. Record 4, deadline 2026-07-03, completed 2026-07-13, ten days late, displays a green "Done" badge | Completion date compared against deadline: completed on time or completed late | **Blocker** | **Closed 8 Aug** | Ch4, Ch5 |
| D19 | 5 Aug | DSAR | On Track card reads 0 while four records exist | Card counts reconcile with row states | Minor | Open. Recheck after Friday rebuild | Ch4 |
| D20 | 5 Aug | DSAR | Seed records are functional test data | Remove or refresh before final screenshots | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D21 | 5 Aug | DSAR | **CLOSED 8 Aug.** No identity verification capture. Nothing records whether the requester's identity was confirmed, or when. Identity confirmation is one of the three candidates for the relevant time under Art. 12A | Date field for identity confirmation, feeding the relevant-time calculation | **Blocker** | **Closed 8 Aug** | Ch4, Ch5, viva |
| D22 | 5 Aug | DSAR | **CLOSED 8 Aug.** No fee payment capture. Third candidate for the relevant time under Art. 12A has nowhere to be recorded | Optional date field for fee payment | Major | **Closed 8 Aug** | Ch4, Ch6 |
| D23 | 5 Aug | DSAR | **No extension capture.** The two-month complexity and volume extension cannot be recorded | Extension flag with reason and revised deadline | Major | Open. Friday rebuild | Ch4, Ch5 |
| D24 | 5 Aug | DSAR | The 30-day figure appears in the entry form banner as well as the list subtitle: "30-day deadline applies. The deadline will be calculated automatically from the date received." The error is embedded in interface language, not only in the calculation | Both statements revised to one calendar month from the relevant time | **Blocker** | Open. Same fix as D16, two locations | Ch4, viva |
| D25 | 5 Aug | DSAR | Date Request Received captures date only, with no time component, unlike the breach form which captures both | Acceptable, since the period runs in calendar months, but record as a deliberate choice rather than an inconsistency | Minor | Open. Decide and document Friday | Ch4 |
| D26 | 5 Aug | DSAR | Assign To is free text and not linked to a user account, so assignment cannot be filtered or reported on | Out of scope for this project, but state the limitation | Minor | Open | Ch4, Ch6 |
| D27 | 5 Aug | DSAR | Em dash in Assign To placeholder text | No em dashes anywhere | Minor | **Closed 8 Aug** | Ch4 screenshots |
| D28 | 5 Aug | DSAR | **CLOSED 8 Aug.** The 30-day figure also appears in the post-submission confirmation banner: "DSAR logged. 30-day deadline set for 02 March 2026". Three locations in total with D24 | All three revised to one calendar month from the relevant time | **Blocker** | **Closed 8 Aug** | Ch4, viva |
| D45 | 5 Aug | DSAR | **Future receipt date accepted.** A DSAR entered with receipt 2027-02-20 saved and displays 228 days left in green, counted under On Track, which rose from 0 to 1. No negative value results, so the display is internally coherent, but a request received in the future is reported as a healthy open case. Same absent guard as D43 | Receipt date later than the present rejected on submission | Major | Open. Friday, alongside the relevant-time work | Ch4, Ch5 |
| D48 | 8 Aug | DSAR | **Summary cards do not reflect the corrected completion logic.** After step 5 the Days Left column correctly flags late completions, but the cards do not. Observed twice: completing record 7, which was 162 days overdue, reduced Overdue from 4 to 3 and raised Completed from 2 to 3; the Completed card now reads 4, of which three were late. A DPO reading only the cards sees four clean successes and a falling failure count. Same contradiction as D11 in the Breach Tracker and the same shape as D8, where marking notification erased the overdue state | Cards derive from the same status logic as the rows, with late completions counted separately | **Blocker** | Open. Step 6 | Ch4, Ch5, viva |
| D49 | 8 Aug | DSAR | Test record 7 (Nahian, received 2026-01-31) is functional test data. Retained deliberately until the re-seed as it evidences the corrected calendar-month calculation alongside record 5 | Remove at re-seed, after evidence capture | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D46 | 5 Aug | DSAR | Test record 6 (Stephen King, received 2027-02-20) is functional test data | Remove before final screenshots | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D47 | 7 Aug | Disclosure | Disclosure record 5 ("request test") is functional test data | Remove before final screenshots | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D44 | 5 Aug | Breach | Breach record 5 (Unauthorised file disclosure, discovery 2027-03-15) is functional test data | Remove before final screenshots | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D29 | 5 Aug | DSAR | Test record 5 (Test Requester, received 2026-01-31) is functional test data | Remove before final screenshots, after the evidence screenshot is saved | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D30 | 5 Aug | DSAR | **Row order changes after every action.** Record 1 moved position between actions, causing a status change to be applied to the wrong record during testing. A compliance officer working a list would make the same error | Stable sort order, by deadline or by record number, unaffected by status changes | Major | Open. Real usability risk, not cosmetic | Ch4, Ch5 |
| D31 | 5 Aug | DSAR | Days Left badge reads "1 days left" rather than "1 day left" | Correct singular form | Minor | Open | Ch4 screenshots |
| D32 | 5 Aug | DSAR | Both action buttons remain available after a record advances to In Progress, so the advance action can be repeated | Controls reflect available transitions | Minor | Open. Confirm behaviour before deciding | Ch4 |
| D33 | 5 Aug | Dashboard | **CLOSED 9 Aug.** Nothing overdue is surfaced. Cards show Pending Disclosures 2, Open Breaches 3, Open DSARs 3. These are volume counts, not risk. At the time of testing two breaches and two DSARs were overdue, one by 157 days, and none of this appeared on the dashboard | Overdue and approaching-deadline items surfaced directly, per the stated design intent | **Blocker** | Open. Saturday, alongside the breach status fixes | Ch4, Ch5 |
| D34 | 5 Aug | Dashboard | **CLOSED 9 Aug.** The system contradicts itself on the DSAR deadline. The dashboard reminder card correctly states "within one calendar month under UK GDPR Article 12", while the DSAR module states 30 days in three places (D16, D24, D28) | Consistent statement of one calendar month from the relevant time across all screens | **Blocker** | Open. Friday, resolves with D16 | Ch4, viva |
| D35 | 5 Aug | Dashboard | **CLOSED 9 Aug.** Reminder card cites UK GDPR Article 12. After the Friday rebuild the governing provision is Article 12A as inserted by the Data (Use and Access) Act 2025, s. 76 | Citation updated to Art. 12A | Minor | Open. Friday | Ch4, viva |
| D36 | 5 Aug | Dashboard | **CLOSED 9 Aug.** Em dash in the welcome line, "Welcome to CivicGuard — GDPR Compliance Process Management System" | No em dashes anywhere | Minor | Open | Ch4 screenshots |
| D37 | 5 Aug | Disclosure | **CLOSED 7 Aug.** No decision date displayed. Every decided record reads "By Data Protection Officer" with no timestamp. Record 4, approved seconds earlier, is indistinguishable from record 2, approved weeks earlier. `updated_at` is written to the database but discarded by the interface. An approval gate that cannot state when approval occurred cannot demonstrate that approval preceded release, which is the mechanism the module exists to provide | Decision date and time displayed against every decided record | **Blocker** | **Closed 7 Aug** | Ch4, Ch5, viva |
| D38 | 5 Aug | Disclosure | **CLOSED 7 Aug.** Approve and reject are indistinguishable in the audit line. Both display "By Data Protection Officer". Only the status badge carries the decision, so a subsequent status change would leave the original decision untraceable | Audit line records the action taken, not only the actor | **Blocker** | **Closed 7 Aug** | Ch4, Ch5 |
| D39 | 5 Aug | Disclosure | **CLOSED 8 Aug.** No rejection reason captured. A DPO can refuse a disclosure without recording why | Free-text reason required on rejection, retained in the audit record | Major | **Closed 8 Aug** | Ch4, Ch5, viva |
| D43 | 5 Aug | Breach | **Future discovery date accepted.** A breach entered with discovery 2027-03-15 saved successfully and displays -5320h in a green badge. Worse, it counted toward the Warning card, which rose from 1 to 2, so a breach discovered in the future is treated as within its 72-hour window. The status logic tests whether elapsed time exceeds 72 and treats everything below as compliant, negative values included | Discovery date later than the present rejected on submission | Major | Open. One guard clause inside Saturday's breach status rewrite (D8, D9, D10), so effectively no additional cost | Ch4, Ch5 |
| D41 | 5 Aug | Disclosure | **No active state on filter buttons.** All four filters (All, Pending, Approved, Rejected) appear identical whether selected or not, so the applied filter is invisible | Selected filter visually distinguished | Major | Open | Ch4 |
| D42 | 5 Aug | Disclosure | **Empty-state message misleads when a filter is applied.** Filtering to Pending with no pending records displays "No disclosure requests found. Click New Disclosure Request to add one", implying the system holds no records at all when four exist. Combined with D41 a user has no indication a filter is active | Message reflects the filter, e.g. "No pending disclosure requests" | Major | Open | Ch4, Ch5 |
| D40 | 5 Aug | Disclosure | Audit line shows a role, "By Data Protection Officer", rather than a named individual. The code writes `session['full_name']`, and the demo account is named after its role, so a multi-DPO deployment could not identify who authorised a release | Named user accounts. Note as a deployment limitation if not built | Minor | Open | Ch4, Ch6 |

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

**DD8. Marking ICO notification closes the breach record.**
`notify_ico()` sets `status = "Closed"` alongside the notification timestamp. This models notification as the end of the process, whereas Art. 33 notification is its beginning: investigation, remediation and any Art. 34 communication to affected individuals all follow. The system cannot currently represent those stages. Noted rather than built, given the window to 10 August. Feeds Ch4 (limitation), Ch6 (future work), and is a fair viva question.

**DD7. Rejection requires a stated reason; approval does not.**
The reject form blocks submission without a reason, while approval proceeds without one. The asymmetry is deliberate: refusing a data subject or a requesting body access to personal data is the decision most likely to be challenged and therefore the one requiring recorded justification. Approvals are already evidenced by actor, authority and timestamp. Feeds Ch4 (design rationale), viva.

**DD6. Field validation is browser-level, not server-level.**
All three forms block empty submission through HTML `required` attributes, so the Flask routes are not consulted. This is sufficient for ordinary use and for demonstration, but can be bypassed by a request sent directly or by editing the page in developer tools, after which the server accepts whatever it receives. Scoped out this week deliberately: it is not a blocker, no ICO scenario depends on it, and the build window to 10 August is fully committed. Worth stating that the security-critical server-side checks are present, namely authentication (E17) and role authorisation (E4); it is only field validation that relies on the browser. Feeds Ch4 (implementation), Ch6 (future work).

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

| E10 | 5 Aug | DSAR status transition works. Record 3 advanced from Open to In Progress with a confirmation banner, and the amber "1 days left" badge correctly persisted, since the request was not yet complete | Screenshot, DSAR Manager after advance | Ch4 |
| E11 | 5 Aug | **Late completion presents as compliant, confirmed on a live record.** Record 1 (J. Whitmore), deadline 2026-07-08, showing 29 days overdue, was completed on 2026-08-05, being 28 days late. It now displays a green "Done" badge and "Completed 2026-08-05", visually identical to a request completed on time. The Overdue card fell from 3 to 2, so completing a late request removes it from the failure count entirely | Screenshot, DSAR Manager after completion. **Retain, cannot be recreated after Friday** | Ch4, Ch5, viva |
| E12 | 5 Aug | Dashboard counts reconcile correctly with module contents. Pending Disclosures 2, Open Breaches 3 (those not yet ICO-notified), Open DSARs 3 (those not completed), all verified against the three module lists | Screenshot, DPO dashboard | Ch4 |
| E13 | 5 Aug | **The correct legal rule already exists in the interface.** The dashboard reminder card states the DSAR deadline as "within one calendar month under UK GDPR Article 12", two clicks from a DSAR module stating 30 days. The requirement was understood at design time and the implementation drifted from it. Stronger to report as a drift caught during testing than as a simple error | Screenshot, DPO dashboard. Pair with `before_D16_dsar_30day_05aug.png` to show the contradiction across two frames | Ch4, Ch5, viva |

| E16 | 5 Aug | Disclosure list filtering returns correct results across all four filters. All returns four records, Pending an empty set (both pending records having been decided during testing), Approved records 4 and 2, Rejected records 1 and 3. The filter logic is sound; its presentation is not (D41, D42) | Screenshots, four filter states | Ch4 |
| E19 | 5 Aug | **The 30-day error is systematic, not month-specific.** A second test DSAR received 2027-02-20 returned a deadline of 2027-03-22, confirmed by the banner "30-day deadline set for 22 March 2027". One calendar month from 20 February is 20 March, so the system again granted two days beyond the statutory period. Independent confirmation of E9 on a different month | Screenshot, DSAR Manager list with record 6 and banner | Ch4, Ch5, viva |
| E18 | 5 Aug | All three entry forms reject empty submission. Disclosure, breach and DSAR forms each block on the first empty required field. Validation is browser-level, arising from HTML `required` attributes, rather than server-level (see DD6) | Screenshots, three forms with validation messages | Ch4 |
| E17 | 5 Aug | **Authentication enforced on protected routes.** With no active session, direct requests to `/dashboard` and `/dsars` both redirect to the login page rather than rendering. `/dsars` matters most, holding requester names and email addresses. Together with E4 this establishes both mechanisms: E4 shows authorisation, that a logged-in officer cannot perform a DPO action; E17 shows authentication, that an unauthenticated request sees nothing. Logout also verified as functioning | Verified in browser, both routes | Ch4, Ch5, viva |
| E15 | 5 Aug | **Late ICO notification erases the failure, confirmed on a live record.** Record 1, discovered 2026-07-10, was displaying red with an OVERDUE label. Marked notified on 2026-08-05, being 26 days past a 72-hour deadline, it turned green, lost the OVERDUE label and the highlighted row background, and the Critical card fell from 2 to 1. The system does not merely fail to flag late notification, it removes the record from the failure count | Screenshot, Breach Tracker after marking notified. **Retain, cannot be recreated after Saturday** | Ch4, Ch5, viva |
| E14 | 5 Aug | Approve and reject both function correctly. Status badges update, confirmation banners are appropriately worded, and action controls are withdrawn once a decision is recorded. The workflow mechanism is sound; the audit record it produces is not (D37 to D40) | Screenshot pair, DPO disclosure list after approve and after reject | Ch4, Ch5 |

### Cross-cutting finding

**F1a. The conceptual error recurs at summary level after being fixed at row level.** Correcting the DSAR completion logic (D18) fixed the row display but not the summary cards, which continue to count a late completion as a success and to reduce the overdue tally when one occurs (D48). The same pattern holds in the Breach Tracker, where D10 governs the row badge and D11 the cards. This is worth reporting in Ch5: the fault was not a single line of logic but an assumption running through the design, and correcting it required addressing every place the assumption surfaced rather than the first one found.

**F1. The system tracks whether an action was taken, but not whether it was taken in time.** The same fault appears four times independently: a late ICO notification displays green (D8), a late DSAR completion displays green (D18, confirmed live at E11), the DSAR deadline itself runs two days long (D16, confirmed at E9), the dashboard reports volume rather than risk so that nothing overdue is surfaced at all (D33), and a breach discovered in the future counts as compliant because negative elapsed time falls below the 72-hour test (D43). In every case the error direction favours the council, presenting compliance that is not present. The Disclosure Workflow escapes only because a disclosure carries no statutory deadline. Four of the eleven blockers are one conceptual error repeated across modules. Worth stating directly in Ch5 as a finding of the testing phase rather than presenting the fixes without their history. Feeds Ch4, Ch5, viva.

### Evaluation risk arising from testing

**R1. RESOLVED 9 August.** The DPP Law Ltd scenario cannot currently be replayed as intended. That case is in the evaluation set because the ICO was notified 43 days late. Confirmed live at E15: a breach notified 26 days past deadline turned green, lost its OVERDUE label, and was removed from the Critical count. CivicGuard would present the documented failure as compliant and reduce its own failure tally in doing so. D8 and D9 must be fixed before the Sunday scenario replay or the scenario produces the wrong result. Feeds Ch5.

**R2. The early-warning claim is not yet supported by the artefact.** The Breach Tracker argument rests on surfacing the deadline before it is missed, against an evidence base in which 47.5% of local government incidents were reported beyond 72 hours. With only two bands (D10) the badge turns red only once the deadline has already passed, which reports failure rather than preventing it. Fixing D10 is what makes the Chapter 5 claim defensible. Feeds Ch5, viva.

**R3. The Lewisham scenario cannot currently be replayed as intended.** That case is in the evaluation set because 35% of requests were not answered within statutory deadlines. Confirmed live at E11: a request completed 28 days after its deadline displays a green "Done" badge and is removed from the Overdue count. A council relying on this display would see a healthy DSAR position while failing in exactly the way Lewisham failed. D18 must be fixed before the Sunday replay. Feeds Ch5.

**R4. Legal accuracy is the sharpest viva exposure.** The DSAR interface currently states a 30-day deadline (D16) where the law provides one calendar month, and anchors the period to receipt (D17) where Article 12A provides for the relevant time. An examiner reading the subtitle has an immediate line of questioning. Friday's rebuild resolves both, and having resolved them converts the weakness into evidence of currency with the Data (Use and Access) Act 2025. Feeds Ch4, Ch5, viva.

---

## C2. BUILD WORK COMPLETED

Running record of changes made to the artefact, so Chapter 4 can be written from what was actually done rather than from recollection.

### Thursday 6 August and Friday 7 August, audit trail

**Step 1. audit_log table created.** Added as a `CREATE TABLE IF NOT EXISTS` block inside `init_db()` in `app.py`, positioned after the `dsars` table and before the user seed inserts. Verified present in the database alongside users, disclosures, breaches and dsars.

Columns and their rationale:

| Column | Purpose |
|---|---|
| `record_type` | Module the action belongs to, so one table can serve disclosures, breaches and DSARs |
| `record_id` | The record acted upon within that module |
| `action` | What was done, e.g. Approved, Rejected |
| `performed_by` | Name taken from the session |
| `performed_by_role` | Authority held at the moment of action. Stored separately because roles change over time and the record must reflect authority as it was, not as it is now |
| `reason` | Free text, nullable. Populated for rejections at step 4 |
| `performed_at` | Timestamp, defaulting to CURRENT_TIMESTAMP |

Design principle: no row is ever updated. Every action inserts. This is what distinguishes an audit trail from a status field, and it is the direct answer to D37 and D38.

**Step 2. Write on approval and rejection.** An `INSERT INTO audit_log` added to `update_disclosure()` in `app.py`, placed between the existing UPDATE and `conn.commit()` so both writes commit together. Parameterised with placeholders rather than string concatenation, which also addresses SQL injection exposure.

Verified live. First audit row written on 7 August:

`(1, 'disclosure', 5, 'Approved', 'Data Protection Officer', 'DPO', None, '2026-08-07 16:59:32')`

This timestamp is the capability the system lacked at test 13. It is now permanent and cannot be overwritten by subsequent actions on the same record.

**Step 3. Display of audit information in the interface.** Complete.

Two changes. First, the `disclosures()` route in `app.py`: both queries, filtered and unfiltered, were extended with correlated subqueries fetching the most recent audit entry for each record, exposed as `last_action_at` and `last_action`. Records with no audit entry return null rather than failing, which matters because all records decided before 7 August predate the table.

Second, `templates/disclosures.html`, the Actions column. The previous line displayed `By {{ approved_by }}` with an em dash placeholder. It now displays the action, the actor, and the timestamp on a second line, falling back to the current status where no audit entry exists. The em dash placeholder was replaced with a hyphen, closing D4.

Verified on screen 7 August. Record 5 displays "Approved by Data Protection Officer" with "2026-08-07 16:59:32" beneath. Records 1 to 4, decided before the audit table existed, display action and actor without a timestamp, which is an honest representation of what the system knows about them.

**Closes D37** (no decision date displayed) and **D38** (approve and reject indistinguishable in the audit line). **Closes D4** (em dash placeholder).

**Step 4. Rejection reason capture.** Complete, 8 August. Closes D39.

Three changes. First, `templates/disclosures.html`, the reject form: an `onsubmit` handler now prompts for a reason, and a hidden `reason` input carries it with the submission. If the reason is empty or cancelled, `return false` halts the submission, so a rejection cannot be recorded without stated reasoning. The approve form was deliberately left unchanged (see DD7).

Second, `update_disclosure()` in `app.py`: reads `request.form.get('reason') or None` and passes it into the audit insert in place of the previous hard-coded `None`. `.get()` rather than subscript because approvals submit no reason field.

Third, display: both `disclosures()` queries gained a `last_reason` correlated subquery, and the Actions column in the template renders it in italics beneath the timestamp.

Verified live 8 August. Record 6 displays "Rejected by Data Protection Officer", "2026-08-08 15:27:28", and "Reason: No lawful basis identified for third-party release". Audit row confirmed in the database:

`(2, 'disclosure', 6, 'Rejected', 'Data Protection Officer', 'DPO', 'No lawful basis identified for third-party release', '2026-08-08 15:27:28')`

### Audit trail complete

All four steps done. The Disclosure Workflow can now state, for any record, what was decided, by whom, under what authority, when, and on what reasoning, with every action retained rather than overwritten.

**Defects closed by this work:** D4, D37, D38, D39.

---

### Saturday 8 August, DSAR rebuild for the Data (Use and Access) Act 2025

**Step 1. Schema extension.** Complete. Five columns added to the `dsars` table in `init_db()` via `ALTER TABLE` rather than by editing the `CREATE TABLE` block, because `CREATE TABLE IF NOT EXISTS` does not run against a table that already exists. Each `ALTER` is wrapped in `try/except sqlite3.OperationalError` so the block runs harmlessly on every start once the columns are present.

| Column | Purpose |
|---|---|
| `identity_confirmed_at` | Date identity was verified. Second candidate for the relevant time |
| `fee_paid_at` | Date any fee was paid. Third candidate |
| `extension_applied` | Whether the two-month extension was invoked |
| `extension_reason` | Justification for the extension |
| `relevant_time` | The calculated latest of the three dates, stored rather than derived at display time so each record shows what its deadline was actually based on |

Verified present via `PRAGMA table_info(dsars)`.

**Step 2. Calculation helpers.** Complete. Two functions added above `get_hours_elapsed`.

`calculate_relevant_time(received_at, identity_confirmed_at, fee_paid_at)` discards empty values and returns the latest of those supplied. This implements the relevant time under Art. 12A as inserted by the Data (Use and Access) Act 2025. ISO date storage means text comparison sorts chronologically.

`add_calendar_month(date_str, months=1)` replaces the thirty-day arithmetic. It advances the month, then decrements the day until a valid date is produced, so 31 January returns 28 February rather than 2 March. The `months` parameter allows the same function to serve the two-month extension.

**Step 3. Form capture of the new dates.** Complete, 8 August. Three changes to `templates/dsars.html`.

The entry-form banner previously read "30-day deadline applies. The deadline will be calculated automatically from the date received." It now reads "One calendar month applies. The deadline runs from the relevant time, being the latest of the date received, the date identity was confirmed, or the date any fee was paid (UK GDPR Art. 12A)." This states the governing rule at the point of entry rather than merely recording data, matching the approach already used in the breach form (E7).

Two date inputs added, `identity_confirmed_at` and `fee_paid_at`, positioned directly beneath Date Request Received so that the three dates feeding one calculation are grouped. Neither is marked required, since most requests involve no identity query and no fee; where both are absent the relevant time correctly falls back to the receipt date. Each carries helper text explaining when to leave it blank.

Assign To placeholder em dash replaced with a comma, **closing D27**.

Partially addresses D24. The list subtitle and post-submission banner remain outstanding at step 5.

**Step 4. Route calculation.** Complete, 8 August. **Closes D16, D17, D28.**

`add_dsar()` in `app.py` previously computed `deadline = received_date + timedelta(days=30)`. It now reads the two new form fields, calls `calculate_relevant_time(received_at, identity_confirmed_at, fee_paid_at)` to establish the Art. 12A relevant time, and derives the deadline via `add_calendar_month(relevant_time)`. The INSERT was extended to persist `identity_confirmed_at`, `fee_paid_at` and `relevant_time`, so each record carries the basis on which its deadline was set rather than only the result.

`deadline` is now an ISO date string rather than a datetime object, so `.strftime()` was removed from both the INSERT and the flash message. The confirmation banner now reads "DSAR logged. Deadline set for [date], one calendar month from the relevant time", **closing D28**.

Verified live. A DSAR received 2026-01-31 with no identity or fee date returned a deadline of **2026-02-28**, against **2026-03-02** for the identically dated record 5 created under the old logic. Both records appear in the same list, so a single frame demonstrates the defect and its correction directly.

**Step 5. Completion measured against deadline.** Complete, 8 August. **Closes D18.**

In `templates/dsars.html` the Days Left cell previously rendered a green "Done" badge on any record whose status was Completed, without reference to the deadline. It now compares `completed_at` against `deadline` and renders "Completed late" in red or "Completed on time" in green accordingly. Date comparison is textual, which sorts correctly given ISO storage; `[:10]` strips any time component, and a guard on `completed_at` prevents failure on a record marked complete without a completion date.

Verified live. Record 4 (deadline 2026-07-03, completed 2026-07-13) and record 1 (deadline 2026-07-08, completed 2026-08-05) both moved from green "Done" to red "Completed late". Prior to this change both presented as clean completions.

**Step 6. Remaining interface wording and summary cards.** Not started for the DSAR module. D24 (list subtitle), D34 and D48 remain open.

---

### Sunday 9 August, Breach Tracker status logic

**Correction to a Tuesday finding.** D10 recorded that no amber band existed. This was wrong. Reading `templates/breaches.html` showed an existing `elif b.hours_elapsed > 48` branch rendering an amber "Urgent" badge. The Tuesday test breach sat at 40h, below that threshold, so it correctly displayed green and I inferred an absent band from a single observation. The real defect was narrower and is properly D11: the Warning summary card counted everything under 72 hours while the row badge used 48, so card and row disagreed. **D10 is withdrawn as recorded.** Worth noting in Ch5 as an instance of a testing inference corrected by later code reading.

**Clock stops at notification.** `get_hours_elapsed()` in `app.py` took only a discovery date and always measured to the present. It now accepts an optional end point and measures discovery to notification where one exists, falling back to the present otherwise. The `breaches()` route passes `ico_notified_at` and derives a `notified_late` flag. **Closes D9.**

Verified: record 3 fell from 556h to 10h, being discovery 13 July 12:43 to notification the same day. The figure now measures the notification interval rather than accumulating indefinitely.

**Notification split by lateness.** The Time Elapsed cell previously coloured by elapsed time alone, so any notified breach rendered green. It now tests notification first and branches on `notified_late`, giving "Xh to notify, LATE" in red or "Xh to notify" in green. The row highlight condition was extended so a late notification retains its warning background. **Closes D8.**

Verified: record 1, discovered 2026-07-10 and notified 2026-08-05, moved from green with no label to red "625h to notify, LATE" with the row highlighted. On 5 August the same action turned the record green and removed it from the Critical count.

**Summary cards rebuilt.** Three cards became four, deriving from the same logic as the rows: Overdue not notified; Urgent under 24 hours left; Notified within 72 hours; Notified late. The previous "Warning, Under 72 Hours" card counted every unnotified breach including one reported minutes earlier, and the single "ICO Notified" card made no distinction between timely and late notification. A late notification now appears in its own red card rather than disappearing into a neutral tally. **Closes D11, D12.** This is the card-level half of F1a.

Em dashes removed from three card titles and the breach title placeholder. **Closes D14.**

**Still open in this module:** D43, future discovery dates accepted, record 5 displaying -5230h.

---

### Sunday 9 August, dashboard

**Risk surfaced ahead of volume.** `dashboard()` previously ran three COUNT queries returning pending disclosures, open breaches and open DSARs. Four risk figures were added: DSARs open and past deadline, DSARs completed after deadline, breaches past 72 hours and not notified, and breaches notified after deadline. The breach figures are derived by calling `get_hours_elapsed()` over the breach rows rather than by a separate SQL expression, so the dashboard and the Breach Tracker cannot diverge. This was a deliberate response to D11, where card and row logic had been written independently and disagreed.

`templates/dashboard.html` gained an "Attention required" strip above the existing cards, rendering only those categories with a non-zero count and linking each to its module. Where nothing is overdue the strip renders a single green line stating that no statutory deadlines are currently breached. **Closes D33.**

Verified live: nine failures surfaced that were entirely invisible on 5 August, being two breaches past 72 hours, one notified late, three DSARs overdue and three completed late.

**Reminder card corrected.** The DSAR reminder cited UK GDPR Art. 12. It now cites Art. 12A as inserted by the Data (Use and Access) Act 2025, and states that the period runs from the relevant time. This resolves the internal contradiction recorded at E13, where the dashboard and the DSAR module stated different rules. **Closes D34, D35.** Em dash removed from the welcome line, **closing D36.**

### Note for Chapter 4 and the viva

The paired dashboard captures, 5 August against 9 August, are the clearest single illustration of the project's argument. The earlier screen counted open work; the later screen measures that work against statutory deadlines and surfaces every failure on the landing page. This is the most direct available answer to the question of what the artefact provides beyond a spreadsheet or a shared inbox.

**Step 5. Completion measured against deadline.** Complete, 8 August. **Closes D18.**

In `templates/dsars.html` the Days Left cell previously rendered a green "Done" badge on any record whose status was Completed, without reference to the deadline. It now compares `completed_at` against `deadline` and renders "Completed late" in red or "Completed on time" in green accordingly. Date comparison is textual, which sorts correctly given ISO storage; `[:10]` strips any time component, and a guard on `completed_at` prevents failure on a record marked complete without a completion date.

Verified live. Record 4 (deadline 2026-07-03, completed 2026-07-13) and record 1 (deadline 2026-07-08, completed 2026-08-05) both moved from green "Done" to red "Completed late". Prior to this change both presented as clean completions.

**Step 6. Remaining interface wording and summary cards.** Not started for the DSAR module. D24 (list subtitle), D34 and D48 remain open.

---

### Sunday 9 August, Breach Tracker status logic

**Correction to a Tuesday finding.** D10 recorded that no amber band existed. This was wrong. Reading `templates/breaches.html` showed an existing `elif b.hours_elapsed > 48` branch rendering an amber "Urgent" badge. The Tuesday test breach sat at 40h, below that threshold, so it correctly displayed green and I inferred an absent band from a single observation. The real defect was narrower and is properly D11: the Warning summary card counted everything under 72 hours while the row badge used 48, so card and row disagreed. **D10 is withdrawn as recorded.** Worth noting in Ch5 as an instance of a testing inference corrected by later code reading.

**Clock stops at notification.** `get_hours_elapsed()` in `app.py` took only a discovery date and always measured to the present. It now accepts an optional end point and measures discovery to notification where one exists, falling back to the present otherwise. The `breaches()` route passes `ico_notified_at` and derives a `notified_late` flag. **Closes D9.**

Verified: record 3 fell from 556h to 10h, being discovery 13 July 12:43 to notification the same day. The figure now measures the notification interval rather than accumulating indefinitely.

**Notification split by lateness.** The Time Elapsed cell previously coloured by elapsed time alone, so any notified breach rendered green. It now tests notification first and branches on `notified_late`, giving "Xh to notify, LATE" in red or "Xh to notify" in green. The row highlight condition was extended so a late notification retains its warning background. **Closes D8.**

Verified: record 1, discovered 2026-07-10 and notified 2026-08-05, moved from green with no label to red "625h to notify, LATE" with the row highlighted. On 5 August the same action turned the record green and removed it from the Critical count.

**Summary cards rebuilt.** Three cards became four, deriving from the same logic as the rows: Overdue not notified; Urgent under 24 hours left; Notified within 72 hours; Notified late. The previous "Warning, Under 72 Hours" card counted every unnotified breach including one reported minutes earlier, and the single "ICO Notified" card made no distinction between timely and late notification. A late notification now appears in its own red card rather than disappearing into a neutral tally. **Closes D11, D12.** This is the card-level half of F1a.

Em dashes removed from three card titles and the breach title placeholder. **Closes D14.**

**Still open in this module:** D43, future discovery dates accepted, record 5 displaying -5230h.

---

### Sunday 9 August, dashboard

**Risk surfaced ahead of volume.** `dashboard()` previously ran three COUNT queries returning pending disclosures, open breaches and open DSARs. Four risk figures were added: DSARs open and past deadline, DSARs completed after deadline, breaches past 72 hours and not notified, and breaches notified after deadline. The breach figures are derived by calling `get_hours_elapsed()` over the breach rows rather than by a separate SQL expression, so the dashboard and the Breach Tracker cannot diverge. This was a deliberate response to D11, where card and row logic had been written independently and disagreed.

`templates/dashboard.html` gained an "Attention required" strip above the existing cards, rendering only those categories with a non-zero count and linking each to its module. Where nothing is overdue the strip renders a single green line stating that no statutory deadlines are currently breached. **Closes D33.**

Verified live: nine failures surfaced that were entirely invisible on 5 August, being two breaches past 72 hours, one notified late, three DSARs overdue and three completed late.

**Reminder card corrected.** The DSAR reminder cited UK GDPR Art. 12. It now cites Art. 12A as inserted by the Data (Use and Access) Act 2025, and states that the period runs from the relevant time. This resolves the internal contradiction recorded at E13, where the dashboard and the DSAR module stated different rules. **Closes D34, D35.** Em dash removed from the welcome line, **closing D36.**

### Note for Chapter 4 and the viva

The paired dashboard captures, 5 August against 9 August, are the clearest single illustration of the project's argument. The earlier screen counted open work; the later screen measures that work against statutory deadlines and surfaces every failure on the landing page. This is the most direct available answer to the question of what the artefact provides beyond a spreadsheet or a shared inbox.

Root cause identified during step 3 while reading `templates/dsars.html`: the Days Left cell tests `{% if d.status == 'Completed' %}` **before** any comparison against the deadline, so a completed record renders a green "Done" badge unconditionally. The Lewisham failure therefore arises from a single ordering decision in the display logic rather than from any defect in the underlying data, which is worth stating plainly in Ch4.

**Step 6. Remaining interface wording.** Not started. List subtitle and confirmation banner. Addresses D16, D24, D28, D34.

---

### Step 5 verification, both branches

Both branches confirmed live on 8 August. Record 6 (deadline 2027-03-22, completed 2026-08-08, within time) renders green "Completed on time". Records 7, 4 and 1, all completed past their deadlines, render red "Completed late". No untested branch remains in this logic.

---

### Note for Chapter 4

On 8 August the list displayed records at three levels of evidential completeness simultaneously: record 3 (decided 13 July) showing action and actor only; record 5 (approved 7 August) showing action, actor and timestamp; record 6 (rejected 8 August) showing action, actor, timestamp and reasoning. A single screenshot capturing all three demonstrates what each stage of the audit work added. This contrast is destroyed by the Saturday re-seed and must be captured before then.

### Note for Chapter 4

The contrast between record 5 and records 1 to 4 on 7 August is a useful illustration of what the audit trail adds, since the older records genuinely cannot be dated. This contrast disappears at the Saturday re-seed, so it must be captured before then if it is to be used.

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
| `before_D18_late_completion_green_05aug.png` | DSAR list after completing record 1 (J. Whitmore) 28 days past deadline. Green "Done" badge, "Completed 2026-08-05", Overdue count fallen from 3 to 2. Evidence for the Lewisham scenario risk R3 | **To save 5 Aug** |
| `before_D16_dashboard_states_calendar_month_05aug.png` | DPO dashboard reminder card stating one calendar month under Art. 12, contradicting the DSAR module. Second frame of the E13 pair | **To save 5 Aug** |
| `before_D8_late_notification_green_05aug.png` | Breach Tracker after marking record 1 notified 26 days late. Green badge, OVERDUE label gone, Critical count fallen from 2 to 1. Strongest single image for the DPP Law scenario risk R1 | **Saved 5 Aug** |
| `audit_log_first_write_07aug.png` | Terminal output showing the first audit row written, with timestamp to the second. Raw proof that the audit trail persists actions rather than overwriting state | **To save 7 Aug** |
| `after_D37_audit_display_07aug.png` | Disclosure list showing record 5 with action, actor and timestamp, against records 1 to 4 which predate the audit table and carry no date. The "after" half of the D37 before-and-after pair | **Saved 7 Aug** |
| `after_D39_rejection_reason_08aug.png` | Disclosure list showing record 6 with action, actor, timestamp and reasoning, against record 5 (no reason) and record 3 (no timestamp). Three levels of evidential completeness in one frame | **To save 8 Aug, before re-seed** |
| `audit_log_with_reason_08aug.png` | Terminal output showing both audit rows, an approval with no reason and a rejection with reasoning captured. Proof the trail persists as data, not only as display | **To save 8 Aug** |
| `after_D33_dashboard_risk_09aug.png` | Dashboard after the risk strip was added. Nine compliance failures surfaced on the landing page where none appeared on 5 August. Pairs with the Tuesday dashboard capture to form the strongest single figure available for Ch4 | **To save 9 Aug** |
| `after_D8_late_notification_flagged_09aug.png` | Breach Tracker after the status rewrite. Record 1 red, "625h to notify, LATE", row highlighted, counted under a dedicated Notified late card. The "after" half of the pair with `before_D8_late_notification_green_05aug.png` | **To save 9 Aug** |
| `after_D18_both_branches_08aug.png` | DSAR list with all four completed records showing the correct distinction: record 6 green "Completed on time", records 7, 4 and 1 red "Completed late". Cleaner Ch4 figure than the single-branch capture, and evidences that both branches were exercised | **To save 8 Aug** |
| `after_D18_late_completion_flagged_08aug.png` | DSAR list after step 5. Records 4 and 1, both completed past deadline, now display "Completed late" in red where they previously showed green "Done". The "after" half of the pair with `before_D18_late_completion_green_05aug.png` | **To save 8 Aug** |
| `after_D16_calendar_month_comparison_08aug.png` | DSAR list after step 4. Record 7 (received 2026-01-31, deadline 2026-02-28, correct) sits directly above record 5 (identical receipt date, deadline 2026-03-02, old logic). Demonstrates defect and fix in a single frame. **Cannot be reconstructed after the re-seed removes record 5** | **To save 8 Aug** |
| `before_dsar_rebuild_full_list_08aug.png` | DSAR list immediately before the rebuild. Shows four faults in one frame: record 1 completed 28 days late displaying green "Done" (D18), records 5 and 6 carrying thirty-day deadlines (D16), and record 3 newly overdue. Stronger single image than the Tuesday capture | **To save 8 Aug, before the calculation changes** |

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
| 12 | DSAR status advance and complete buttons | Done, E10, E11. Confirms D18 |
| 13 | Disclosure approve and reject as DPO | Done, E14. Found D37 to D40 |
| 14 | Mark ICO Notified button | Done, E15. Confirms D8, D9 |
| 15 | Dashboard as officer | Outstanding |
| 16 | Dashboard as DPO | Done, E12, E13. Found D33 to D36 |
| 17 | Session protection when logged out | Done, E17. Pass |
| 18 | Blank required field on all three forms | Done, E18. Pass, with DD6 |
| 19 | Future date as breach discovery | Done, D43. Fail |
| 20 | DSAR receipt date boundary | Done, D45. Fail |
| 21 | Disclosure list filter buttons | Done, E16. Found D41, D42 |
| 22 | Logout function | Done, verified during test 17 |
| 23 | Handbook word band and weightings | Outstanding |

---

## F. FRIDAY SCOPE, DSAR REBUILD

Established by test 10. Roughly half form work, half logic. A full day, not a morning.

**Form additions:** identity confirmation date (D21), fee payment date (D22), extension flag with reason and revised deadline (D23).

**Thursday scope, audit trail.** Established by test 13, and larger than originally assumed. The module does not merely lack history, it discards data it already holds. Four items: a separate audit table recording every action rather than overwriting current state (D37, D38); display of decision timestamp (D37); a rejection reason field (D39); a per-case history view. A full day, with no slack against Friday.

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
