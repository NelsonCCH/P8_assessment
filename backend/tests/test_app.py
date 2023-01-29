import json

def test_inputs_all_valid(client, sample_inputs):

    res = client.get('/calculate_mortgage_payment', query_string=sample_inputs)
    expected = 4676.72
    assert expected == json.loads(res.get_data(as_text=True))


def test_zero_price(client, sample_inputs):
    sample_inputs["price"] = 0
    res = client.get('/calculate_mortgage_payment', query_string=sample_inputs)
    assert res.status_code == 400
    expected = "Price cannot be smaller or equal to 0"
    assert expected == res.get_json()

def test_negative_down_payment(client, sample_inputs):
    sample_inputs["down_payment"] = -10000
    res = client.get('/calculate_mortgage_payment', query_string=sample_inputs)
    assert res.status_code == 400
    expected = "Down payment cannot be smaller than 0."
    assert expected == res.get_json()

def test_not_enough_down_payment(client, sample_inputs):
    sample_inputs["down_payment"] = 50000 #sample price is 1M, here is only 5% down payment
    res = client.get('/calculate_mortgage_payment', query_string=sample_inputs)
    assert res.status_code == 400
    expected = "Down payment should at least be 10% of property price."
    assert expected == res.get_json()

def test_too_much_down_payment(client, sample_inputs):
    sample_inputs["down_payment"] = 2000000 #sample price is 1M
    res = client.get('/calculate_mortgage_payment', query_string=sample_inputs)
    assert res.status_code == 400
    expected = "Down payment cannot be more than property price."
    assert expected == res.get_json()

def test_invaid_amortization(client, sample_inputs):
    sample_inputs["amortization"] = 0
    res = client.get('/calculate_mortgage_payment', query_string=sample_inputs)
    assert res.status_code == 400
    expected = "Amortization incorrect, can only be 5/10/15/20/25/30 years"
    assert expected == res.get_json()

def test_negative_rate(client, sample_inputs):
    sample_inputs["rate"] = -5
    res = client.get('/calculate_mortgage_payment', query_string=sample_inputs)
    assert res.status_code == 400
    expected = "Interest rate cannot be smaller than 0."
    assert expected == res.get_json()

def test_invaid_payment_schedule(client, sample_inputs):
    sample_inputs["payment_schedule"] = "daily"
    res = client.get('/calculate_mortgage_payment', query_string=sample_inputs)
    assert res.status_code == 400
    expected = "Wrong type of payment schedule."
    assert expected == res.get_json()

"""
price <0
down <0
down > price
down < 10% price
rate <0
amort not withing 5 and 30, not step of 5
schedule not in 3 only types


"""
 