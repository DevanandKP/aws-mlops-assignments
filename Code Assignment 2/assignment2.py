from flask import Flask, render_template
from flask_mysqldb import MySQL
from datetime import date, datetime, timedelta

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'host-name'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'database-name'

mysql = MySQL(app)
def log():
    cursor = mysql.connection.cursor()
    add_log= ("INSERT INTO logs "
               "(timestamp)"
               "VALUES (%(timestamp)s)")

    data_log = {
        'timestamp': datetime.now()
    }
    query=("Select * from logs")
    cursor.execute(add_log,data_log)
    cursor.execute(query)
    logs=cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return logs


@app.route('/')
def home():
    logs=log()
    logs=[list(item) for item in logs]
    for i in logs:
      i[1] = i[1] and i[1].strftime("%d/%m/%Y, %H:%M:%S")
    return render_template('index.html',logs=logs)

if __name__ == '__main__':
   app.run()