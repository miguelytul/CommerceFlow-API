CommerceFlow - Requirements
1. objective
The commerceFlow is an API developed with Python and Django REST Framework.
It's objective is allow the consultation of products, the creation of orders and the integretion of payments with Mercado Pago.

2. Functional requirements
-RF01: List the avaiable products
-RF02: Consult the details of an product
-RF03: Create orders with one or more products
-RF04: Calculate the total value of the orders in the backend
-RF05: Start the checkout by Mercado Pago
-RF06: Get notifications of payments by webhook
-RF07: Consulct the status of the ordes and payments
-RF08: Allow payments tests in test ambience

3. Not Functional requirements
-RNF01: Protect the payment API credential
-RNF02: Validate the notifications received by Mercado Pago
-RNF03: Treate doubled notifications without process the payments by the wrong way
RNF04: Allow automized tests of the main funcionalities
