# CivicGuard

A GDPR compliance process management system for UK local councils.

Built as the artefact for an MSc Business Computing dissertation at Staffordshire
University (module COIS71052). The system responds to three failures that recur in
Information Commissioner's Office enforcement action against local authorities:
personal data released without internal authorisation, breaches notified outside the
seventy-two hour statutory period, and data subject access requests missed at scale.

---

## Important

**All data in this repository is fabricated.** No real personal data was processed at
any stage of the project. The individuals named in the seeded records and in the
scenario replays do not exist. The scenarios are reconstructions from published ICO
enforcement notices; they are not the incidents themselves.

The demonstration credentials below are published deliberately, since this is a
prototype with no real data behind it. Passwords are stored in plain text, which is
acceptable here and would not be in any deployment.

---

## What it does

Three modules behind a shared dashboard.

**Disclosure Workflow.** An Officer records a proposed release of personal data and
submits it for approval. The record cannot reach an approved state through any action
available to the account that raised it. A Data Protection Officer approves or rejects
it, and every decision writes an audit row recording the actor, the authority held, the
timestamp and, for a rejection, the stated grounds.

**72-Hour Breach Tracker.** Elapsed time runs from the point of awareness rather than
from data entry, in accordance with Article 33 of the UK GDPR. The badge turns amber at
forty-eight hours and red at seventy-two. Recording a notification stops the clock, and
a notification made after the deadline is flagged as late rather than returned to a
compliant state.

**DSAR Manager.** Requests are tracked against one calendar month under Article 12(3),
calculated from the relevant time introduced by Article 12A as inserted by section 76 of
the Data (Use and Access) Act 2025, being the latest of receipt, identity confirmation
and payment of any fee. Completion is measured against the deadline, so a request
answered late is displayed as completed late.

---

## Running it

Requires Python 3 and Flask. From the project folder:

```
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS and Linux

pip install flask

python seed_data.py
python app.py
```

Then open `http://127.0.0.1:5000`.

`seed_data.py` drops and rebuilds the tables. Running it against the committed database
will destroy the live audit rows on which the evaluation rests, so back up
`civicguard.db` first if you intend to keep that state.

### Accounts

| Username | Password | Role |
|---|---|---|
| `officer` | `officer123` | Compliance Officer |
| `admin` | `admin123` | Data Protection Officer |

---

## Repository contents

| Path | What it is |
|---|---|
| `app.py` | The application. A single Flask module of 454 lines. The compliance logic sits in four helper functions: `calculate_relevant_time`, `add_calendar_month`, `get_hours_elapsed` and `get_days_remaining` |
| `templates/` | Jinja2 templates and the Bootstrap 5 interface |
| `seed_data.py` | Creates the demonstration dataset and prints a verification summary of the card states each set should produce |
| `civicguard.db` | The database as it stood when the Chapter 4 figures were captured, including the audit rows written live during the scenario replays |
| `civicguard_prereseed_10aug.db` | The database before the rebuild of 7 to 9 August 2026, retained so that the pre-remediation behaviour described in the report is reproducible rather than only photographed |
| `evidence/` | Interface captures and scenario replay evidence |
| `CIVICGUARD_BUILD_LOG.md` | Test inventory, defect register, design decisions and session notes |
| `CHANGE_LEDGER_10AUG.md` | Record of changes made during the rebuild |

---

## Notes on the implementation

**The audit table is insert-only.** No statement anywhere in the application updates or
deletes a row in `audit_log`. This is what distinguishes an audit trail from a status
field: a status field records the present position, an audit trail retains the sequence
that produced it.

**The authority is stored alongside the action.** `performed_by_role` is written at the
moment of the decision rather than read from the user account at display time, because
roles change and the record must reflect the authority as it stood.

**The relevant time is stored, not recalculated.** Each access request carries the basis
on which its deadline was set, not merely the resulting date.

**No foreign key constraints are declared.** The associations between tables are
maintained by the application rather than enforced by the database, and personnel are
recorded as text rather than by reference to a user account. Both are documented in the
dissertation as limitations.

**Known scope exclusions.** The two-month extension for complex requests is present in
the data model but not captured by the interface. Recording a notification closes a
breach record, whereas Article 33 notification begins a process rather than concludes
one. Role authorisation is applied to the disclosure approval decision alone. Required
fields are enforced by the browser rather than the server, though authentication and
role authorisation are enforced server-side.

---

## Author

Kazi Nahian Isfar Omar
MSc Business Computing, Staffordshire University, 2026
