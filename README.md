# ach-stripe-api-test

.json files contain the data shape coming from stripe / in the stripe objects at various points throughout this process.

stripetest.py contains code that interacts with stripe's api. it automatically saves the return data shapes. For the input format, look in the "except" blocks and ignore the "write" lines.

Stripe documentation: https://stripe.com/docs/api



you need a settings.py file with an API_KEY set in order to run any code.
