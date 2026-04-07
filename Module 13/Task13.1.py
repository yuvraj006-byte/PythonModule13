from flask import Flask, request

app = Flask(__name__)

@app.route('/prime_number')
def calculate_prime_number():
    args = request.args
    number = int(args.get("number"))

    if number <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break 

    response = {
        "number": number,
        "is_prime": is_prime
    }

    return response

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)