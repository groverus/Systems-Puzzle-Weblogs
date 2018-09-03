import datetime
import os
import psycopg2

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def index():
    # Connect to database
    conn = psycopg2.connect(host='db', database=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'])
    cur = conn.cursor()

    # Get number of all GET requests
    sql_all = """SELECT COUNT(*) FROM weblogs;"""
    cur.execute(sql_all)
    all = cur.fetchone()[0]

    # Get number of all succesful requests
    sql_success = """SELECT COUNT(*) FROM weblogs WHERE status LIKE \'2__\';"""
    cur.execute(sql_success)
    success = cur.fetchone()[0]

    # Get number of all local GET requests
    sql_all_local = """SELECT COUNT(*) FROM weblogs WHERE source = \'local\';"""
    cur.execute(sql_all_local)
    all_local = cur.fetchone()[0]

    # Get number of all remote GET requests
    sql_all_remote = """SELECT COUNT(*) FROM weblogs WHERE source = \'remote\';"""
    cur.execute(sql_all_remote)
    all_remote = cur.fetchone()[0]

    # Get number of all local succesful requests
    sql_success_local = """SELECT COUNT(*) FROM weblogs WHERE status LIKE \'2__\' AND source = \'local\';"""
    cur.execute(sql_success_local)
    success_local = cur.fetchone()[0]

    # Get number of all remote succesful requests
    sql_success_remote = """SELECT COUNT(*) FROM weblogs WHERE status LIKE \'2__\' AND source = \'remote\';"""
    cur.execute(sql_success_remote)
    success_remote = cur.fetchone()[0]

    # Determine rate if there was at least one request
    rate = "No entries yet!"
    rate_local = "No entries yet!"
    rate_remote = "No entries yet!"

    if all != 0:
        rate = str( success / all )
    if all_local != 0:
        rate_local = str( success_local / all_local )
    if all_remote != 0:
        rate_remote = str( success_remote / all_remote )
    return render_template('index.html', rate = rate, rate_local = rate_local, rate_remote = rate_remote)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
