from flask import Flask, request, jsonify, abort
from validators.create_mortgage_inputs_rule import CreateMortgageInputsRules
app = Flask(__name__)

# for testing connections only
@app.route('/')
def hello_world():
    return jsonify("Hello World")

@app.route('/calculate_mortgage_payment', methods=["POST"])
def calculate_mortgage_payment():
    try:
        req_json = request.get_json()
        # look-up table for schedule conversion into numbers
        no_of_payment_per_year = {"monthly": 12, "bi_weekly": 24, "accelerated_bi_weekly": 26}

        # validate inputs
        create_mortgage_inputs_schema = CreateMortgageInputsRules()
        errors = create_mortgage_inputs_schema.validate(req_json)
        if errors:
            return jsonify(str(errors)), 400

        # parsing the input parameters
        price = req_json.get('price')
        down_payment = req_json.get('down_payment')
        rate = req_json.get('rate') /100
        amortization = req_json.get('amortization')
        payment_schedule = req_json.get('payment_schedule')

        # formula: M = P * ((r * ((1+r) ** n)) / ((1+r) ** n - 1))
        P = price - down_payment
        r = rate / no_of_payment_per_year.get(payment_schedule)
        n = amortization * no_of_payment_per_year.get(payment_schedule)

        M = round(P * ((r * ((1 + r) ** n)) / ((1 + r) ** n - 1)),2)

        return jsonify(M), 200

    except Exception as e:
        msg = f"Something went wrong, {e}"
        return jsonify(msg), 400

if __name__ == '__main__':
    app.run()
