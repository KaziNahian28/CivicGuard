from flask import Flask, render_template, redirect, url_for, request, session, flash
import sqlite3
import os
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'civicguard_secret_key_2026'

DATABASE = 'civicguard.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            full_name TEXT NOT NULL,
            department TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS disclosures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            requested_by TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            approved_by TEXT,
            notes TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS breaches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            discovered_at TIMESTAMP NOT NULL,
            reported_by TEXT NOT NULL,
            status TEXT DEFAULT 'Open',
            severity TEXT DEFAULT 'Medium',
            ico_notified INTEGER DEFAULT 0,
            ico_notified_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dsars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            requester_name TEXT NOT NULL,
            requester_email TEXT NOT NULL,
            request_details TEXT NOT NULL,
            received_at TIMESTAMP NOT NULL,
            deadline TIMESTAMP NOT NULL,
            status TEXT DEFAULT 'Open',
            assigned_to TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP
        )
    ''')
    for column, definition in [
        ('identity_confirmed_at', 'TIMESTAMP'),
        ('fee_paid_at', 'TIMESTAMP'),
        ('extension_applied', 'INTEGER DEFAULT 0'),
        ('extension_reason', 'TEXT'),
        ('relevant_time', 'TIMESTAMP')
    ]:
        try:
            cursor.execute(f'ALTER TABLE dsars ADD COLUMN {column} {definition}')
        except sqlite3.OperationalError:
            pass

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_type TEXT NOT NULL,
            record_id INTEGER NOT NULL,
            action TEXT NOT NULL,
            performed_by TEXT NOT NULL,
            performed_by_role TEXT NOT NULL,
            reason TEXT,
            performed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password, role, full_name, department)
        VALUES (?, ?, ?, ?, ?)
    ''', ('admin', 'admin123', 'DPO', 'Data Protection Officer', 'Legal'))

    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password, role, full_name, department)
        VALUES (?, ?, ?, ?, ?)
    ''', ('officer', 'officer123', 'Officer', 'Compliance Officer', 'Compliance'))

    conn.commit()
    conn.close()

def calculate_relevant_time(received_at, identity_confirmed_at=None, fee_paid_at=None):
    candidates = [d for d in [received_at, identity_confirmed_at, fee_paid_at] if d]
    return max(candidates)


def add_calendar_month(date_str, months=1):
    from datetime import datetime
    d = datetime.fromisoformat(str(date_str)[:10])
    month = d.month - 1 + months
    year = d.year + month // 12
    month = month % 12 + 1
    day = d.day
    while True:
        try:
            return datetime(year, month, day).date().isoformat()
        except ValueError:
            day -= 1
    
def get_hours_elapsed(discovered_at_str, end_at_str=None):
    try:
        discovered = datetime.strptime(discovered_at_str[:16], '%Y-%m-%dT%H:%M')
    except:
        try:
            discovered = datetime.strptime(discovered_at_str[:16], '%Y-%m-%d %H:%M')
        except:
            return 0
    if end_at_str:
        try:
            end = datetime.strptime(str(end_at_str)[:16], '%Y-%m-%d %H:%M')
        except:
            try:
                end = datetime.strptime(str(end_at_str)[:16], '%Y-%m-%dT%H:%M')
            except:
                end = datetime.now()
    else:
        end = datetime.now()
    elapsed = end - discovered
    return int(elapsed.total_seconds() / 3600)

def get_days_remaining(deadline_str):
    try:
        deadline = datetime.strptime(deadline_str[:10], '%Y-%m-%d')
        remaining = (deadline - datetime.now()).days
        return remaining
    except:
        return 0

# ── AUTH ──────────────────────────────────────────────────────────

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        user = conn.execute(
            'SELECT * FROM users WHERE username = ? AND password = ?',
            (username, password)
        ).fetchone()
        conn.close()
        if user:
            session['user'] = username
            session['role'] = user['role']
            session['full_name'] = user['full_name']
            flash('Welcome back, ' + user['full_name'] + '!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# ── DASHBOARD ─────────────────────────────────────────────────────

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    disclosure_count = conn.execute(
        'SELECT COUNT(*) FROM disclosures WHERE status = "Pending"'
    ).fetchone()[0]
    breach_count = conn.execute(
        'SELECT COUNT(*) FROM breaches WHERE status = "Open"'
    ).fetchone()[0]
    dsar_count = conn.execute(
        'SELECT COUNT(*) FROM dsars WHERE status != "Completed"'
    ).fetchone()[0]
    conn.close()
    return render_template('dashboard.html',
                           disclosure_count=disclosure_count,
                           breach_count=breach_count,
                           dsar_count=dsar_count)

# ── DISCLOSURES ───────────────────────────────────────────────────

@app.route('/disclosures')
def disclosures():
    if 'user' not in session:
        return redirect(url_for('login'))
    status_filter = request.args.get('status')
    conn = get_db()
    if status_filter:
        rows = conn.execute(
            '''SELECT d.*,
                      (SELECT performed_at FROM audit_log
                       WHERE record_type = 'disclosure' AND record_id = d.id
                       ORDER BY id DESC LIMIT 1) AS last_action_at,
                      (SELECT action FROM audit_log
                       WHERE record_type = 'disclosure' AND record_id = d.id
                       ORDER BY id DESC LIMIT 1) AS last_action,
                       (SELECT reason FROM audit_log
                       WHERE record_type = 'disclosure' AND record_id = d.id
                       ORDER BY id DESC LIMIT 1) AS last_reason
               FROM disclosures d WHERE d.status = ? ORDER BY d.created_at DESC''',
            (status_filter,)
        ).fetchall()
    else:
        rows = conn.execute(
            '''SELECT d.*,
                      (SELECT performed_at FROM audit_log
                       WHERE record_type = 'disclosure' AND record_id = d.id
                       ORDER BY id DESC LIMIT 1) AS last_action_at,
                      (SELECT action FROM audit_log
                       WHERE record_type = 'disclosure' AND record_id = d.id
                       ORDER BY id DESC LIMIT 1) AS last_action,
                       (SELECT reason FROM audit_log
                       WHERE record_type = 'disclosure' AND record_id = d.id
                       ORDER BY id DESC LIMIT 1) AS last_reason
               FROM disclosures d ORDER BY d.created_at DESC'''
        ).fetchall()
    conn.close()
    return render_template('disclosures.html', disclosures=rows)

@app.route('/disclosures/add', methods=['POST'])
def add_disclosure():
    if 'user' not in session:
        return redirect(url_for('login'))
    title = request.form['title']
    description = request.form['description']
    conn = get_db()
    conn.execute(
        'INSERT INTO disclosures (title, description, requested_by) VALUES (?, ?, ?)',
        (title, description, session['full_name'])
    )
    conn.commit()
    conn.close()
    flash('Disclosure request submitted for DPO approval.', 'success')
    return redirect(url_for('disclosures'))

@app.route('/disclosures/update/<int:id>', methods=['POST'])
def update_disclosure(id):
    if 'user' not in session or session['role'] != 'DPO':
        flash('Only the DPO can approve or reject disclosures.', 'danger')
        return redirect(url_for('disclosures'))
    action = request.form['action']
    reason = request.form.get('reason') or None
    status = 'Approved' if action == 'approve' else 'Rejected'
    conn = get_db()
    conn.execute(
        '''UPDATE disclosures SET status = ?, approved_by = ?,
           updated_at = CURRENT_TIMESTAMP WHERE id = ?''',
        (status, session['full_name'], id)
    )
    conn.execute(
        '''INSERT INTO audit_log
           (record_type, record_id, action, performed_by, performed_by_role, reason)
           VALUES (?, ?, ?, ?, ?, ?)''',
        ('disclosure', id, status, session['full_name'], session['role'], reason)
    )
    conn.commit()
    conn.close()
    flash(f'Disclosure request {status.lower()} successfully.', 'success')
    return redirect(url_for('disclosures'))

# ── BREACHES ──────────────────────────────────────────────────────

@app.route('/breaches')
def breaches():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    rows = conn.execute(
        'SELECT * FROM breaches ORDER BY created_at DESC'
    ).fetchall()
    conn.close()
    breaches_list = []
    for b in rows:
        b_dict = dict(b)
        b_dict['hours_elapsed'] = get_hours_elapsed(
                b_dict['discovered_at'], b_dict.get('ico_notified_at'))
        b_dict['notified_late'] = bool(
                b_dict.get('ico_notified') and b_dict['hours_elapsed'] > 72)
        breaches_list.append(b_dict)
    return render_template('breaches.html', breaches=breaches_list)

@app.route('/breaches/add', methods=['POST'])
def add_breach():
    if 'user' not in session:
        return redirect(url_for('login'))
    title = request.form['title']
    description = request.form['description']
    discovered_at = request.form['discovered_at']
    severity = request.form['severity']
    conn = get_db()
    conn.execute(
        '''INSERT INTO breaches
           (title, description, discovered_at, reported_by, severity)
           VALUES (?, ?, ?, ?, ?)''',
        (title, description, discovered_at, session['full_name'], severity)
    )
    conn.commit()
    conn.close()
    flash('Breach reported. 72-hour ICO notification countdown has started.', 'warning')
    return redirect(url_for('breaches'))

@app.route('/breaches/notify/<int:id>', methods=['POST'])
def notify_ico(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    conn.execute(
        '''UPDATE breaches SET ico_notified = 1,
           ico_notified_at = CURRENT_TIMESTAMP,
           status = "Closed" WHERE id = ?''',
        (id,)
    )
    conn.commit()
    conn.close()
    flash('ICO notification recorded successfully.', 'success')
    return redirect(url_for('breaches'))

# ── DSARS ─────────────────────────────────────────────────────────

@app.route('/dsars')
def dsars():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    rows = conn.execute(
        'SELECT * FROM dsars ORDER BY deadline ASC'
    ).fetchall()
    conn.close()
    dsars_list = []
    for d in rows:
        d_dict = dict(d)
        d_dict['days_remaining'] = get_days_remaining(d_dict['deadline'])
        dsars_list.append(d_dict)
    return render_template('dsars.html', dsars=dsars_list)

@app.route('/dsars/add', methods=['POST'])
def add_dsar():
    if 'user' not in session:
        return redirect(url_for('login'))
    requester_name = request.form['requester_name']
    requester_email = request.form['requester_email']
    request_details = request.form['request_details']
    received_at = request.form['received_at']
    assigned_to = request.form.get('assigned_to', '')
    identity_confirmed_at = request.form.get('identity_confirmed_at') or None
    fee_paid_at = request.form.get('fee_paid_at') or None
    relevant_time = calculate_relevant_time(received_at, identity_confirmed_at, fee_paid_at)
    deadline = add_calendar_month(relevant_time)
    conn = get_db()
    conn.execute(
        '''INSERT INTO dsars
            (requester_name, requester_email, request_details,
             received_at, deadline, assigned_to,
             identity_confirmed_at, fee_paid_at, relevant_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (requester_name, requester_email, request_details,
         received_at, deadline, assigned_to,
         identity_confirmed_at, fee_paid_at, relevant_time)
    )
    conn.commit()
    conn.close()
    flash('DSAR logged. Deadline set for ' + deadline +
          ', one calendar month from the relevant time.', 'success')
    return redirect(url_for('dsars'))

@app.route('/dsars/update/<int:id>', methods=['POST'])
def update_dsar(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    action = request.form['action']
    conn = get_db()
    if action == 'complete':
        conn.execute(
            '''UPDATE dsars SET status = "Completed",
               completed_at = CURRENT_TIMESTAMP WHERE id = ?''',
            (id,)
        )
        flash('DSAR marked as completed.', 'success')
    elif action == 'progress':
        conn.execute(
            'UPDATE dsars SET status = "In Progress" WHERE id = ?',
            (id,)
        )
        flash('DSAR status updated to In Progress.', 'info')
    conn.commit()
    conn.close()
    return redirect(url_for('dsars'))

# ── RUN ───────────────────────────────────────────────────────────

if __name__ == '__main__':
    init_db()
    app.run(debug=True)