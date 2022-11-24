# simple server for cpu load test
from flask import Flask
import time
import random
# from flask_mysqldb import MySQL

app = Flask(__name__)
# app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
# app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
# app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")

# mysql = MySQL(app)


@app.route("/stress", methods=["GET", "POST"])
def stress():
    """_summary_: stress the cpu. It will run a loop for 1 second."""
    random_number = random.randint(2, 100)
    loop_end_time = time.time() + .5
    while time.time() < loop_end_time:
        random_number = random_number * random_number
    return "OK", 200


# @app.route("/db", methods=["GET", "POST"])
# def db():
#     """Read from DB and return."""
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM user;")
#     data = cur.fetchall()
#     return str(data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
