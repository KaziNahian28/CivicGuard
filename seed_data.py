# seed_data.py - CivicGuard demonstration data
#
# Clears all case records and loads a fabricated background caseload that
# exercises every status band across the three modules. No real personal data
# is used. Requester names, addresses and case details are invented.
#
# This file deliberately does NOT contain the five ICO enforcement scenarios.
# Those are entered live through the interface during the evaluation session so
# that each one writes genuine audit_log entries with real timestamps. Seeding
# them would produce records that no officer ever actioned.
#
# Deadline arithmetic here mirrors app.py exactly: one calendar month from the
# relevant time under UK GDPR Art. 12A as inserted by the Data (Use and Access)
# Act 2025, not thirty days. If the two ever diverge the seeded deadlines would
# disagree with the deadlines the application calculates, which is precisely the
# class of fault recorded as D16.
#
# Run from the CivicGuard folder, alongside app.py:
#     python seed_data.py

import sqlite3
from datetime import datetime, timedelta
from calendar import monthrange

DATABASE = 'civicguard.db'

now = datetime.now()
TODAY = now.date()


# ---------------------------------------------------------------------------
# Calculation helpers, mirroring app.py
# ---------------------------------------------------------------------------

def add_calendar_month(date_str, months=1):
    """One calendar month forward, clamping to the last valid day of the
    target month. 31 January returns 28 February, not 2 March."""
    d = datetime.strptime(date_str[:10], '%Y-%m-%d').date()
    month_index = d.month - 1 + months
    year = d.year + month_index // 12
    month = month_index % 12 + 1
    day = min(d.day, monthrange(year, month)[1])
    return d.replace(year=year, month=month, day=day).strftime('%Y-%m-%d')


def calculate_relevant_time(received_at, identity_confirmed_at=None, fee_paid_at=None):
    """The relevant time under Art. 12A: the latest of the date of receipt, the
    date identity was confirmed, and the date any fee was paid. Absent values
    are discarded, so a request with neither falls back to the receipt date."""
    candidates = [d for d in (received_at, identity_confirmed_at, fee_paid_at) if d]
    return max(d[:10] for d in candidates)


def days_ago(n):
    return (TODAY - timedelta(days=n)).strftime('%Y-%m-%d')


def hours_ago_iso(n):
    return (now - timedelta(hours=n)).strftime('%Y-%m-%dT%H:%M')


def hours_ago_stamp(n):
    return (now - timedelta(hours=n)).strftime('%Y-%m-%d %H:%M:%S')


def days_ago_stamp(n):
    return (now - timedelta(days=n)).strftime('%Y-%m-%d %H:%M:%S')


# ---------------------------------------------------------------------------
# Schema-aware insert. Only columns that exist in the table are written.
# ---------------------------------------------------------------------------

def columns_of(cursor, table):
    cursor.execute(f'PRAGMA table_info({table})')
    return {row[1] for row in cursor.fetchall()}


def insert(cursor, table, values):
    available = columns_of(cursor, table)
    used = {k: v for k, v in values.items() if k in available}
    skipped = [k for k in values if k not in available]
    cols = ', '.join(used)
    marks = ', '.join('?' for _ in used)
    cursor.execute(f'INSERT INTO {table} ({cols}) VALUES ({marks})', tuple(used.values()))
    return cursor.lastrowid, skipped


# ---------------------------------------------------------------------------
# Disclosure Workflow
#
# The form captures title and description only (D2 remains open), so the
# recipient and the lawful basis are carried in the description text rather
# than in dedicated fields. This is an honest reflection of what the artefact
# records, not a workaround.
# ---------------------------------------------------------------------------

DISCLOSURES = [
    {
        'title': 'Housing benefit records for tenancy dispute',
        'description': 'Recipient: Marchmont and Bell Solicitors, acting for the landlord. '
                       'Lawful basis: Art. 6(1)(c), legal obligation, disclosure ordered by the county court. '
                       'Scope: benefit award history covering 2024 to 2026 for one named tenant.',
        'status': 'Pending',
        'created_days_ago': 2,
    },
    {
        'title': 'Adult social care assessment for hospital discharge',
        'description': 'Recipient: Ashgrove NHS Foundation Trust discharge team. '
                       'Lawful basis: Art. 6(1)(e) and Art. 9(2)(h), health and social care provision. '
                       'Scope: current care and support plan for one adult service user.',
        'status': 'Pending',
        'created_days_ago': 1,
    },
    {
        'title': 'Social care case notes for safeguarding investigation',
        'description': 'Recipient: Westbury Constabulary public protection unit. '
                       'Lawful basis: Sch. 2 Pt 1 para. 2, Data Protection Act 2018, prevention and detection of crime. '
                       'Scope: chronology and contact records for one child, redacted for third party identities.',
        'status': 'Approved',
        'created_days_ago': 12,
        'decided_days_ago': 9,
        'action': 'Approved',
        'reason': None,
    },
    {
        'title': 'Electoral register extract for statutory audit',
        'description': 'Recipient: Hallowmere Audit Partnership, appointed external auditor. '
                       'Lawful basis: Art. 6(1)(c), legal obligation under the Local Audit and Accountability Act 2014. '
                       'Scope: open register extract for two wards, no edited register entries included.',
        'status': 'Approved',
        'created_days_ago': 20,
        'decided_days_ago': 18,
        'action': 'Approved',
        'reason': None,
    },
    {
        'title': 'Council tax arrears data for debt recovery',
        'description': 'Recipient: Crossgate Enforcement Ltd, instructed on liability orders. '
                       'Lawful basis asserted by requester: Art. 6(1)(f), legitimate interests. '
                       'Scope: arrears balances and contact details for 118 accounts.',
        'status': 'Rejected',
        'created_days_ago': 15,
        'decided_days_ago': 14,
        'action': 'Rejected',
        'reason': 'Bulk request covering 118 accounts, of which only 12 are subject to a liability order. '
                  'No lawful basis identified for the remainder. Resubmit limited to accounts with an order in force.',
    },
    {
        'title': 'Pupil attendance data for research study',
        'description': 'Recipient: postgraduate researcher, unnamed institution. '
                       'Lawful basis asserted by requester: consent obtained from schools. '
                       'Scope: attendance and exclusion records for four secondary schools.',
        'status': 'Rejected',
        'created_days_ago': 30,
        'decided_days_ago': 27,
        'action': 'Rejected',
        'reason': 'Consent from schools is not consent from data subjects and does not provide a lawful basis '
                  'for release of pupil records. No data sharing agreement or ethics approval supplied.',
    },
]


# ---------------------------------------------------------------------------
# 72-Hour Breach Tracker
#
# Five records covering every state the status logic can produce after the
# 9 August rewrite: overdue and unnotified, urgent inside the final 24 hours,
# on track, notified within 72 hours, and notified late.
# ---------------------------------------------------------------------------

BREACHES = [
    {
        'title': 'Housing benefit spreadsheet emailed to wrong recipient',
        'description': 'Support worker attached an unfiltered benefit caseload to an email intended for a '
                       'single external advocate. Records for 42 residents were exposed, including bank '
                       'details and vulnerability markers.',
        'severity': 'High',
        'discovered_hours_ago': 96,
        'notified_hours_ago': None,
        'status': 'Open',
    },
    {
        'title': 'Social care correspondence posted to previous address',
        'description': 'Case summary letter sent to an address superseded on the record eight months earlier. '
                       'Returned unopened by the current occupier, who confirmed the envelope had been opened.',
        'severity': 'Medium',
        'discovered_hours_ago': 60,
        'notified_hours_ago': None,
        'status': 'Open',
    },
    {
        'title': 'Planning objection published without redaction',
        'description': 'Objection letters uploaded to the planning portal retained objector names, addresses '
                       'and signatures. Twenty three documents affected, live on the portal for four days.',
        'severity': 'Medium',
        'discovered_hours_ago': 14,
        'notified_hours_ago': None,
        'status': 'Open',
    },
    {
        'title': 'Unencrypted USB device lost after off-site meeting',
        'description': 'Device holding working copies of nine access request files reported missing by a '
                       'caseworker. No evidence of access, device not recovered.',
        'severity': 'High',
        'discovered_hours_ago': 52,
        'notified_hours_ago': 8,
        'status': 'Closed',
    },
    {
        'title': 'Revenues mailbox accessible to unauthorised team',
        'description': 'Permissions change during a directory migration left a shared revenues mailbox '
                       'readable across two additional service areas. Identified during a routine access review.',
        'severity': 'High',
        'discovered_hours_ago': 336,
        'notified_hours_ago': 96,
        'status': 'Closed',
    },
]


# ---------------------------------------------------------------------------
# DSAR Manager
#
# Seven records covering all five summary card states, plus two that exercise
# the Art. 12A relevant time and one fixed at 31 January to evidence the
# calendar-month arithmetic at a month end.
# ---------------------------------------------------------------------------

DSARS = [
    # Open and overdue
    {
        'requester_name': 'J. Whitmore',
        'requester_email': 'j.whitmore@example.com',
        'request_details': 'All records held in connection with a housing application and subsequent '
                           'homelessness assessment, covering the past three years.',
        'received_days_ago': 74,
        'status': 'Open',
        'assigned_to': 'Information Governance Team',
    },
    # Open and overdue, with identity confirmation moving the relevant time
    {
        'requester_name': 'D. Oyelaran',
        'requester_email': 'd.oyelaran@example.com',
        'request_details': 'Copies of all correspondence and internal notes relating to a disputed '
                           'council tax liability, including officer file notes.',
        'received_days_ago': 62,
        'identity_confirmed_days_ago': 48,
        'status': 'In Progress',
        'assigned_to': 'Revenues and Benefits',
    },
    # Due within seven days
    {
        'requester_name': 'A. Chowdhury',
        'requester_email': 'a.chowdhury@example.com',
        'request_details': 'CCTV footage recorded at a council-operated car park on a specified date, '
                           'together with any incident report referring to the requester.',
        'received_days_ago': 26,
        'status': 'In Progress',
        'assigned_to': 'Corporate Security',
    },
    # On track
    {
        'requester_name': 'R. Baptiste',
        'requester_email': 'r.baptiste@example.com',
        'request_details': 'All personal data held by the parking service, including notices issued, '
                           'appeals submitted and any related photographic evidence.',
        'received_days_ago': 6,
        'status': 'Open',
        'assigned_to': 'Information Governance Team',
    },
    # On track, with a fee payment setting the relevant time
    {
        'requester_name': 'M. Kowalczyk',
        'requester_email': 'm.kowalczyk@example.com',
        'request_details': 'Repeat request for a further copy of a social care file previously supplied '
                           'in March. Reasonable fee charged for the additional copy.',
        'received_days_ago': 18,
        'identity_confirmed_days_ago': 15,
        'fee_paid_days_ago': 9,
        'status': 'Open',
        'assigned_to': 'Adult Social Care',
    },
    # Completed on time
    {
        'requester_name': 'S. Nkemelu',
        'requester_email': 's.nkemelu@example.com',
        'request_details': 'Social care file relating to a completed needs assessment, including the '
                           'assessment document and supporting correspondence.',
        'received_days_ago': 44,
        'completed_days_ago': 21,
        'status': 'Completed',
        'assigned_to': 'Adult Social Care',
    },
    # Completed late, fixed at a month end to evidence calendar-month arithmetic
    {
        'requester_name': 'T. Ferreira',
        'requester_email': 't.ferreira@example.com',
        'request_details': 'All records held by children services relating to a school transport appeal, '
                           'including the panel decision and officer recommendations.',
        'received_fixed': f'{TODAY.year}-01-31',
        'completed_fixed': f'{TODAY.year}-04-16',
        'status': 'Completed',
        'assigned_to': 'Children and Families',
    },
]


# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------

def main():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    existing = {r[0] for r in cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table'").fetchall()}

    # Clear case data. User accounts are left untouched.
    for table in ('audit_log', 'disclosures', 'breaches', 'dsars'):
        if table in existing:
            cursor.execute(f'DELETE FROM {table}')
    if 'sqlite_sequence' in existing:
        cursor.execute("DELETE FROM sqlite_sequence "
                       "WHERE name IN ('audit_log','disclosures','breaches','dsars')")

    has_audit = 'audit_log' in existing
    skipped_columns = set()
    report = {'disclosures': [], 'breaches': [], 'dsars': []}

    # Disclosures ----------------------------------------------------------
    for d in DISCLOSURES:
        decided = d.get('decided_days_ago')
        row = {
            'title': d['title'],
            'description': d['description'],
            'requested_by': 'Compliance Officer',
            'status': d['status'],
            'approved_by': 'Data Protection Officer' if decided else None,
            'created_at': days_ago_stamp(d['created_days_ago']),
        }
        if decided:
            row['updated_at'] = days_ago_stamp(decided)
        rec_id, skipped = insert(cursor, 'disclosures', row)
        skipped_columns.update(skipped)

        if decided and has_audit:
            audit = {
                'record_type': 'disclosure',
                'record_id': rec_id,
                'action': d['action'],
                'performed_by': 'Data Protection Officer',
                'performed_by_role': 'DPO',
                'reason': d.get('reason'),
                'performed_at': days_ago_stamp(decided),
            }
            _, skipped = insert(cursor, 'audit_log', audit)
            skipped_columns.update(skipped)

        report['disclosures'].append(f"{rec_id}. {d['status']:<8} {d['title']}")

    # Breaches -------------------------------------------------------------
    for b in BREACHES:
        notified = b['notified_hours_ago']
        row = {
            'title': b['title'],
            'description': b['description'],
            'discovered_at': hours_ago_iso(b['discovered_hours_ago']),
            'reported_by': 'Compliance Officer',
            'severity': b['severity'],
            'ico_notified': 1 if notified is not None else 0,
            'status': b['status'],
        }
        if notified is not None:
            row['ico_notified_at'] = hours_ago_stamp(notified)
        rec_id, skipped = insert(cursor, 'breaches', row)
        skipped_columns.update(skipped)

        if notified is None:
            elapsed = b['discovered_hours_ago']
            state = 'overdue' if elapsed > 72 else ('urgent' if elapsed > 48 else 'on track')
            detail = f'{elapsed}h elapsed, not notified, {state}'
        else:
            interval = b['discovered_hours_ago'] - notified
            state = 'notified late' if interval > 72 else 'notified in time'
            detail = f'{interval}h to notify, {state}'
        report['breaches'].append(f'{rec_id}. {detail:<38} {b["title"]}')

    # DSARs ----------------------------------------------------------------
    for s in DSARS:
        received = s.get('received_fixed') or days_ago(s['received_days_ago'])
        identity = days_ago(s['identity_confirmed_days_ago']) if 'identity_confirmed_days_ago' in s else None
        fee = days_ago(s['fee_paid_days_ago']) if 'fee_paid_days_ago' in s else None

        relevant = calculate_relevant_time(received, identity, fee)
        deadline = add_calendar_month(relevant)

        row = {
            'requester_name': s['requester_name'],
            'requester_email': s['requester_email'],
            'request_details': s['request_details'],
            'received_at': received,
            'identity_confirmed_at': identity,
            'fee_paid_at': fee,
            'relevant_time': relevant,
            'deadline': deadline,
            'status': s['status'],
            'assigned_to': s['assigned_to'],
        }

        completed = None
        if s['status'] == 'Completed':
            completed = s.get('completed_fixed') or days_ago(s['completed_days_ago'])
            row['completed_at'] = completed

        rec_id, skipped = insert(cursor, 'dsars', row)
        skipped_columns.update(skipped)

        if completed:
            state = 'completed late' if completed > deadline else 'completed on time'
        elif deadline < TODAY.strftime('%Y-%m-%d'):
            state = 'open and overdue'
        else:
            left = (datetime.strptime(deadline, '%Y-%m-%d').date() - TODAY).days
            state = f'{left} days left'
        anchor = ''
        if relevant != received:
            anchor = f' [relevant time {relevant}, not receipt]'
        report['dsars'].append(
            f'{rec_id}. received {received}, deadline {deadline}, {state}{anchor}')

    conn.commit()
    conn.close()

    # Verification output --------------------------------------------------
    print('CivicGuard demonstration data loaded.\n')
    for module in ('disclosures', 'breaches', 'dsars'):
        print(f'{module.upper()} ({len(report[module])})')
        for line in report[module]:
            print('  ' + line)
        print()

    if skipped_columns:
        print('Columns present in this script but absent from the database, '
              'and therefore not written:')
        for c in sorted(skipped_columns):
            print(f'  {c}')
        print()

    print('Expected card states:')
    print('  Breach Tracker: 2 overdue, 1 urgent, 1 on track, 1 notified in time, 1 notified late')
    print('  DSAR Manager:   2 open and overdue, 1 due within 7 days, 2 on track, '
          '1 completed on time, 1 completed late')
    print('  Disclosures:    2 pending, 2 approved, 2 rejected')
    print('\nThe five ICO scenarios are NOT seeded. Enter them live so each one '
          'writes its own audit trail.')
    print('Restart app.py, then check /dashboard, /disclosures, /breaches and /dsars.')


if __name__ == '__main__':
    main()