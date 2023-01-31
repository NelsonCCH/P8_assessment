from marshmallow import Schema, fields, validates_schema, ValidationError
from marshmallow.validate import Length, Range, OneOf

class CreateMortgageInputsRules(Schema):

    price = fields.Float(required=True, validate=Range(min=0, error="Price cannot be smaller or equal to 0"))
    down_payment = fields.Float(required=True, validate=Range(min=0, min_inclusive=True, error="Down payment cannot be smaller than 0."))
    rate = fields.Float(required=True, validate=Range(min=0, min_inclusive=True, error="Interest rate cannot be smaller than 0."))
    amortization = fields.Int(required=True, validate=OneOf([5,10,15,20,25,30], error="Amortization incorrect, can only be 5/10/15/20/25/30 years"))
    payment_schedule = fields.Str(required=True, validate=OneOf(["monthly", "bi_weekly", "accelerated_bi_weekly"], error="Amortization incorrect, can only be monthly / bi_weekly / accelerated_bi_weekly."))

    @validates_schema
    def too_little_down_payment(self, data, **kwargs):
        if data['down_payment'] < data['price']*0.1:
            raise ValidationError("Down payment should at least be 10% of property price.")

    @validates_schema  
    def too_much_down_payment(valself, data, **kwargs):
        if data['down_payment'] > data['price']:
            raise ValidationError("Down payment cannot be more than property price.")

