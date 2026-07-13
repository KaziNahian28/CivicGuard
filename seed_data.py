"""
seed_data.py — Adds realistic sample data to CivicGuard for testing and
MPR screenshots. Data is fabricated (per your DSR methodology) but modelled
on the patterns seen in real ICO enforcement cases, WITHOUT copying any
real personal data.

Run this from your CivicGuard folder (same place as app.py):
    python seed_data.py
"""
import sqlite3
from datetime import datetime, timedelta

DATABASE = 'civicguard.db'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

now = datetime.now()

# ── SAMPLE DISCLOSURES ──────────────────────────────────────────
disclosures = [
    ('Housing benefit records — court order request',
     'Third-party legal firm requesting disclosure of housing benefit records under a court order for ongoing tenancy dispute.',
     'Compliance Officer', 'Pending'),
    ('Social care case notes — police request',
     'Local police requesting social care case notes as part of a safeguarding investigation.',
     'Compliance Officer', 'Approved'),
    ('Council tax data — bailiff enforcement',
     'External enforcement agency requesting council tax arrears data for debt recovery action.',
     'Compliance Officer', 'Rejected'),
]
for title, desc, req_by, status in disclosures:
    cursor.execute('''
        INSERT INTO disclosures (title, description, requested_by, status, approved_by)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, desc, req_by, status,
          'Data Protection Officer' if status in ('Approved', 'Rejected') else None))

# ── SAMPLE BREACHES (modelled on ICO enforcement case patterns) ─
breaches = [
    # (title, description, hours_ago, severity, ico_notified)
    ('Unauthorised email disclosure — housing data',
     'Support worker sent housing benefit spreadsheet to an unintended external recipient via email, exposing records for 42 residents.',
     80, 'High', 0),  # over 72h, not notified -> should show OVERDUE
    ('Misdirected letter — social care correspondence',
     'Physical letter containing social care case summary posted to an incorrect address due to a data entry error.',
     30, 'Medium', 0),  # under 72h, not notified -> warning
    ('Lost unencrypted USB device',
     'USB device containing DSAR case files reported missing by a caseworker after an off-site meeting.',
     10, 'High', 1),  # notified already
]
for title, desc, hours_ago, severity, notified in breaches:
    discovered = (now - timedelta(hours=hours_ago)).strftime('%Y-%m-%dT%H:%M')
    if notified:
        cursor.execute('''
            INSERT INTO breaches (title, description, discovered_at, reported_by, severity, ico_notified, ico_notified_at, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, desc, discovered, 'Compliance Officer', severity, 1,
              now.strftime('%Y-%m-%d %H:%M:%S'), 'Closed'))
    else:
        cursor.execute('''
            INSERT INTO breaches (title, description, discovered_at, reported_by, severity, ico_notified, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, desc, discovered, 'Compliance Officer', severity, 0, 'Open'))

# ── SAMPLE DSARS ──────────────────────────────────────────────
dsars = [
    # (requester_name, email, details, days_ago_received, status)
    ('J. Whitmore', 'j.whitmore@example.com',
     'Requesting all records held relating to a housing application from the past 3 years.',
     35, 'Open'),  # overdue (>30 days)
    ('A. Chowdhury', 'a.chowdhury@example.com',
     'Requesting CCTV footage from council-operated car park on a specific date.',
     25, 'In Progress'),  # due soon
    ('R. Baptiste', 'r.baptiste@example.com',
     'Requesting copies of correspondence relating to a council tax dispute.',
     5, 'Open'),  # on track
    ('S. Nkemelu', 's.nkemelu@example.com',
     'Requesting social care file relating to a completed assessment.',
     40, 'Completed'),  # completed
]
for name, email, details, days_ago, status in dsars:
    received = (now - timedelta(days=days_ago))
    deadline = received + timedelta(days=30)
    if status == 'Completed':
        cursor.execute('''
            INSERT INTO dsars (requester_name, requester_email, request_details, received_at, deadline, status, assigned_to, completed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, details, received.strftime('%Y-%m-%d'), deadline.strftime('%Y-%m-%d'),
              status, 'Data Team', now.strftime('%Y-%m-%d %H:%M:%S')))
    else:
        cursor.execute('''
            INSERT INTO dsars (requester_name, requester_email, request_details, received_at, deadline, status, assigned_to)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, details, received.strftime('%Y-%m-%d'), deadline.strftime('%Y-%m-%d'),
              status, 'Data Team'))

conn.commit()
conn.close()

print("Sample data added successfully:")
print(f"  {len(disclosures)} disclosures")
print(f"  {len(breaches)} breaches (1 overdue, 1 warning, 1 notified)")
print(f"  {len(dsars)} DSARs (1 overdue, 1 due soon, 1 on track, 1 completed)")
print("Restart app.py if it's running, then check /disclosures, /breaches and /dsars.")
