import mysql.connector
from dotenv import load_dotenv
from flask import Flask, jsonify
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")


def get_airport(ident):
    connection = mysql.connector.connect(
        host=db_host,
        port=int(db_port),
        database=db_name,
        user=db_user,
        password=db_pass,
        autocommit=True
    )

    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (ident,))

    result = cursor.fetchone()
    cursor.close()

    connection.close()
    if result:
        return {
            "name": result[0],
            "municipality": result[1]
        }
    else:
        return None


app = Flask(__name__)


@app.route('/')
def wrong_url():
    return jsonify({
        "message": "Missing some parts of the url",
        "status": 404
    }), 404


@app.route('/airport', defaults={'ident': None})
@app.route('/airport/<ident>')
def airport_route(ident):

    if ident is None:
        return jsonify({
            "message": "Missing airport ident",
            "status": 400
        }), 400

    try:
        airport = get_airport(ident)

        if not airport:
            return jsonify({"error": "Airport not found"}), 404

        response = {
            "ICAO": ident,
            "Municipality": airport["municipality"],
            "Name": airport["name"]
        }

        return jsonify(response)

    except Exception:
        return jsonify({
            'message': "Something Went Wrong",
            "status": 500
        }), 500


if __name__ == '__main__':
    app.json.ensure_ascii = False
    app.run(debug=True, host='127.0.0.1', port=5000)
