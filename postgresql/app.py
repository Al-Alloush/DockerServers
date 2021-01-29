from flask import Flask, render_template, request, json, redirect, jsonify
from flask_socketio import SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

import psycopg2




@socketio.on('test_alert')
def check_admin_login(msg):
    text = msg['in_text']
    date = msg['date']
    try:
        conn = psycopg2.connect(host="postgresDB", user="user", password="example")


        cursor = conn.cursor()
        # Print PostgreSQL Connection properties
        print(conn.get_dsn_parameters(), "\n")
    
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
    
        if(conn):
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
    
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL" + str(error))


    socketio.emit('back_test_alert', f" text: {text} and the date : {str(date)}")




@app.route('/')
@app.route('/login')
def loginPage():
    return render_template("login.html")


@app.route('/index')
def indexPage():
    return render_template("index.html")



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')