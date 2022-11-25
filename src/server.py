# simple server for cpu load test
from flask import Flask
import time
import random
import sqlite3


app = Flask(__name__)

# connect to sqlite3
def db_connect():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=["GET", "POST"])
def stress():
    """_summary_: stress the cpu. It will run a loop for 1 second."""
    random_number = random.randint(2, 100)
    loop_end_time = time.time() + 0.2
    while time.time() < loop_end_time:
        random_number = random_number * random_number
    return "OK", 200


@app.route("/db", methods=["GET", "POST"])
def db():
    """Fill random data to the database."""
    random_int = random.randint(1, 100)
    try:
        conn = db_connect()
        conn.execute("INSERT INTO reqs ( req_rand) VALUES (?)", (random_int,))
        conn.commit()
        conn.close()
    except Exception as e:
        return "Error: " + str(e), 500
    return "OK", 200


@app.route("/db_init", methods=["GET", "POST"])
def db_init():
    """Create the database."""
    try:
        connection = sqlite3.connect("database.db")
        with open("do_spin.sql") as f:
            connection.executescript(f.read())
    except Exception as e:
        return "Error: " + str(e), 500
    return "OK", 200


@app.route("/db_fetch", methods=["GET", "POST"])
def db_fetch():
    """Fetch data from the database."""
    try:
        conn = db_connect()
        cursor = conn.execute("SELECT * FROM reqs")
        rows = cursor.fetchall()
        count = len(rows)
        conn.close()
    except Exception as e:
        return "Error: " + str(e), 500
    return str(count), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
