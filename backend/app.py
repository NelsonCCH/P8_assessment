from flask import Flask, request, jsonify

app = Flask(__name__)

# for testing connections only
@app.route('/')
def hello_world():
    return jsonify("Hello World")


@app.route('/calculate_mortgage_payment', methods=["GET"])
def calculate_mortgage_payment():
    print(request.args)
    # look-up table for schedule conversion into numbers
    no_of_payment_per_year = {"monthly": 12, "bi_weekly": 24, "accelerated_bi_weekly": 26}

    # parsing the query parameters
    price = request.args.get('price')
    down_payment = request.args.get('down_payment')
    rate = request.args.get('rate')
    amortization = request.args.get('amortization')
    payment_schedule = request.args.get('payment_schedule')

    # check if all parameters are provided
    if not all([price, down_payment, rate, amortization, payment_schedule]): return jsonify("Not enough params."), 400

    # type conversion
    price = float(price)
    down_payment = float(down_payment)
    rate = float(rate) / 100
    amortization = float(amortization)

    # check for valid inputs
    isValid, err_msg = validate_input(price=price, down_payment=down_payment, rate=rate, amortization=amortization,
                             payment_schedule=payment_schedule)

    if not isValid: return jsonify(err_msg), 400

    # formula: M = P * ((r * ((1+r) ** n)) / ((1+r) ** n - 1))
    P = price - down_payment
    r = rate / no_of_payment_per_year.get(payment_schedule)
    n = amortization * no_of_payment_per_year.get(payment_schedule)

    M = round(P * ((r * ((1 + r) ** n)) / ((1 + r) ** n - 1)),2)

    return jsonify(M), 200


# double check in backend server, although frontend checked already
def validate_input(price, down_payment, rate, amortization, payment_schedule):
    print(price)
    if price <= 0: return [False, "Price cannot be smaller or equal to 0"]
    
    if rate < 0: return [False, "Interest rate cannot be smaller than 0."]

    if down_payment < 0: return [False, "Down payment cannot be smaller than 0."]

    if down_payment / price < 0.1: return [False, "Down payment should at least be 10% of property price."]

    if down_payment > price: return [False, "Down payment cannot be more than property price."]

    if amortization < 5 or amortization > 30 or amortization % 5 != 0:
        msg = "Amortization incorrect, can only be 5/10/15/20/25/30 years"
        return [False, msg]

    if payment_schedule not in ["monthly", "bi_weekly", "accelerated_bi_weekly"]: 
        return [False, "Wrong type of payment schedule."]

    return [True, ""]

if __name__ == '__main__':
    app.run()
