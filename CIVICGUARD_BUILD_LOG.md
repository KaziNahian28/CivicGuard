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
| D45 | 5 Aug | DSAR | **Future receipt date accepted.** A DSAR entered with receipt 2027-02-20 saved and displays 228 days left in green, counted under On Track, which rose from 0 to 1. No negative value results, so the display is internally coherent, but a request received in the future is reported as a healthy open case. Same absent guard as D43 | Receipt date later than the present rejected on submission | Major | Open. Friday, alongside the relevant-time work | Ch4, Ch5 |
| D46 | 5 Aug | DSAR | Test record 6 (Stephen King, received 2027-02-20) is functional test data | Remove before final screenshots | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D44 | 5 Aug | Breach | Breach record 5 (Unauthorised file disclosure, discovery 2027-03-15) is functional test data | Remove before final screenshots | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D29 | 5 Aug | DSAR | Test record 5 (Test Requester, received 2026-01-31) is functional test data | Remove before final screenshots, after the evidence screenshot is saved | Minor | Open. Saturday re-seed | Ch4 screenshots |
| D30 | 5 Aug | DSAR | **Row order changes after every action.** Record 1 moved position between actions, causing a status change to be applied to the wrong record during testing. A compliance officer working a list would make the same error | Stable sort order, by deadline or by record number, unaffected by status changes | Major | Open. Real usability risk, not cosmetic | Ch4, Ch5 |
| D31 | 5 Aug | DSAR | Days Left badge reads "1 days left" rather than "1 day left" | Correct singular form | Minor | Open | Ch4 screenshots |
| D32 | 5 Aug | DSAR | Both action buttons remain available after a record advances to In Progress, so the advance action can be repeated | Controls reflect available transitions | Minor | Open. Confirm behaviour before deciding | Ch4 |
| D33 | 5 Aug | Dashboard | **Nothing overdue is surfaced.** Cards show Pending Disclosures 2, Open Breaches 3, Open DSARs 3. These are volume counts, not risk. At the time of testing two breaches and two DSARs were overdue, one by 157 days, and none of this appeared on the dashboard | Overdue and approaching-deadline items surfaced directly, per the stated design intent | **Blocker** | Open. Saturday, alongside the breach status fixes | Ch4, Ch5 |
| D34 | 5 Aug | Dashboard | **The system contradicts itself on the DSAR deadline.** The dashboard reminder card correctly states "within one calendar month under UK GDPR Article 12", while the DSAR module states 30 days in three places (D16, D24, D28) | Consistent statement of one calendar month from the relevant time across all screens | **Blocker** | Open. Friday, resolves with D16 | Ch4, viva |
| D35 | 5 Aug | Dashboard | Reminder card cites UK GDPR Article 12. After the Friday rebuild the governing provision is Article 12A as inserted by the Data (Use and Access) Act 2025, s. 76 | Citation updated to Art. 12A | Minor | Open. Friday | Ch4, viva |
| D36 | 5 Aug | Dashboard | Em dash in the welcome line, "Welcome to CivicGuard — GDPR Compliance Process Management System" | No em dashes anywhere | Minor | Open | Ch4 screenshots |
| D37 | 5 Aug | Disclosure | **No decision date displayed.** Every decided record reads "By Data Protection Officer" with no timestamp. Record 4, approved seconds earlier, is indistinguishable from record 2, approved weeks earlier. `updated_at` is written to the database but discarded by the interface. An approval gate that cannot state when approval occurred cannot demonstrate that approval preceded release, which is the mechanism the module exists to provide | Decision date and time displayed against every decided record | **Blocker** | Open. Thursday | Ch4, Ch5, viva |
| D38 | 5 Aug | Disclosure | **Approve and reject are indistinguishable in the audit line.** Both display "By Data Protection Officer". Only the status badge carries the decision, so a subsequent status change would leave the original decision untraceable | Audit line records the action taken, not only the actor | **Blocker** | Open. Thursday | Ch4, Ch5 |
| D39 | 5 Aug | Disclosure | **No rejection reason captured.** A DPO can refuse a disclosure without recording why | Free-text reason required on rejection, retained in the audit record | Major | Open. Thursday | Ch4, Ch5, viva |
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

**F1. The system tracks whether an action was taken, but not whether it was taken in time.** The same fault appears four times independently: a late ICO notification displays green (D8), a late DSAR completion displays green (D18, confirmed live at E11), the DSAR deadline itself runs two days long (D16, confirmed at E9), the dashboard reports volume rather than risk so that nothing overdue is surfaced at all (D33), and a breach discovered in the future counts as compliant because negative elapsed time falls below the 72-hour test (D43). In every case the error direction favours the council, presenting compliance that is not present. The Disclosure Workflow escapes only because a disclosure carries no statutory deadline. Four of the eleven blockers are one conceptual error repeated across modules. Worth stating directly in Ch5 as a finding of the testing phase rather than presenting the fixes without their history. Feeds Ch4, Ch5, viva.

### Evaluation risk arising from testing

**R1. The DPP Law Ltd scenario cannot currently be replayed as intended.** That case is in the evaluation set because the ICO was notified 43 days late. Confirmed live at E15: a breach notified 26 days past deadline turned green, lost its OVERDUE label, and was removed from the Critical count. CivicGuard would present the documented failure as compliant and reduce its own failure tally in doing so. D8 and D9 must be fixed before the Sunday scenario replay or the scenario produces the wrong result. Feeds Ch5.

**R2. The early-warning claim is not yet supported by the artefact.** The Breach Tracker argument rests on surfacing the deadline before it is missed, against an evidence base in which 47.5% of local government incidents were reported beyond 72 hours. With only two bands (D10) the badge turns red only once the deadline has already passed, which reports failure rather than preventing it. Fixing D10 is what makes the Chapter 5 claim defensible. Feeds Ch5, viva.

**R3. The Lewisham scenario cannot currently be replayed as intended.** That case is in the evaluation set because 35% of requests were not answered within statutory deadlines. Confirmed live at E11: a request completed 28 days after its deadline displays a green "Done" badge and is removed from the Overdue count. A council relying on this display would see a healthy DSAR position while failing in exactly the way Lewisham failed. D18 must be fixed before the Sunday replay. Feeds Ch5.

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
| `before_D18_late_completion_green_05aug.png` | DSAR list after completing record 1 (J. Whitmore) 28 days past deadline. Green "Done" badge, "Completed 2026-08-05", Overdue count fallen from 3 to 2. Evidence for the Lewisham scenario risk R3 | **To save 5 Aug** |
| `before_D16_dashboard_states_calendar_month_05aug.png` | DPO dashboard reminder card stating one calendar month under Art. 12, contradicting the DSAR module. Second frame of the E13 pair | **To save 5 Aug** |
| `before_D8_late_notification_green_05aug.png` | Breach Tracker after marking record 1 notified 26 days late. Green badge, OVERDUE label gone, Critical count fallen from 2 to 1. Strongest single image for the DPP Law scenario risk R1 | **To save 5 Aug** |

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
