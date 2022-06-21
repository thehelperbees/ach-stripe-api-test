import stripe
import json


stripe.api_key = "sk_test_REslpMtFSmqbJ1l5uIPBp9DW"


##########################
# GET OR CREATE CUSTOMER #
##########################

try:
    with open('customer.json', 'r+') as f:
        customer_data = json.load(f)
        customer = stripe.Customer.retrieve(
            id=customer_data.get('id')
        )
except:
    with open('customer.json', 'w') as f:
        customer = stripe.Customer.create(
            name="Eric McTest",
            email="eric.seibt+test@thehelperbees.com"
        )
        f.write(json.dumps(customer, indent=4))


####################
# ADD BANK ACCOUNT #
####################

try:
    with open ('bank_account.json', 'r+') as f:
        bank_account_data = json.load(f)
        bank_account = stripe.Customer.retrieve_source(
            customer.id,
            bank_account_data.get('id')
        )
except:
    with open('bank_account.json', 'w') as f:
        bank_account = stripe.Customer.create_source(
            customer.id,
            source={
                "object": "bank_account",
                "country": "US",
                "currency": "usd",
                "account_holder_name": "Eric McTest",
                "account_holder_type": "individual",
                "routing_number": "110000000",
                "account_number": "000123456789"
            }
        )
        f.write(json.dumps(bank_account, indent=4))


#################################
# CUSTOMER AFTER ADDING ACCOUNT #
#################################

try:
    with open ('customer_after_adding_account.json', 'r') as f:
        pass
except:
    with open ('customer_after_adding_account.json', 'w') as f:
        f.write(json.dumps(customer, indent=4))


#######################
# VERIFY BANK ACCOUNT #
#######################

try:
    with open ('verified_bank_account.json', 'r') as f:
        pass
except:
    with open ('verified_bank_account.json', 'w') as f:
        bank_account.verify(amounts= [32,45])
        f.write(json.dumps(bank_account, indent=4))


##########
# CHARGE #
##########

try:
    with open('charge.json', 'r') as f:
        charge_data = json.load(f)
        charge = stripe.Charge.retrieve(
            charge_data.get('id')
        )
except:
    with open('charge.json', 'w') as f:
        charge = stripe.Charge.create(
            amount="1000",
            currency="usd",
            customer=customer.id,
            description="Test Charge"
        )
        f.write(json.dumps(charge, indent=4))


#################
# CHARGE REFUND #
#################

try:
    with open('refund.json', 'r') as f:
        refund_data = json.load(f)
        refund = stripe.Refund.retrieve(
            refund_data.get('id')
        )
except:
    with open('refund.json', 'w') as f:
        refund = stripe.Refund.create(
            charge=charge.id
        )
        f.write(json.dumps(refund, indent=4))


#######################
# CHARGE AFTER REFUND #
#######################

try:
    with open('charge_after_refund.json', 'r') as f:
        pass
except:
    with open('charge_after_refund.json', 'w') as f:
        f.write(json.dumps(charge, indent=4))


print("CUSTOMER:", customer, '\n')
print("BANK ACCOUNT:", bank_account, '\n')
print("CHARGE", charge, '\n')
print("REFUND", refund, '\n')