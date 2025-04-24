import decimal
import logging
from pywebio.input import slider, FLOAT, NUMBER
from pywebio.output import put_html, put_success
from pywebio.input import input as pw_input

APPLE_PRICE = decimal.Decimal(52.75)
BANANA_PRICE = decimal.Decimal(81.40)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("result.log"), logging.StreamHandler()],
)

put_html("<h1>Welcome to our shop</h1>")
### Apple
apple_weight = slider(
    "Apple (max 5kg)", type=FLOAT, min_value=0, max_value=5, value=0.01, required=True
)
apple_weight = decimal.Decimal(apple_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)

### Banana
banana_weight = pw_input(
    "Banana (max 10)", type=NUMBER, min=0, max=10, value=1, required=True
)
banana_weight = decimal.Decimal(banana_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)
###
apple_cost = (APPLE_PRICE * apple_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
banana_cost = (BANANA_PRICE * banana_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
total_cost = apple_cost + banana_cost

logging.info(f"Apple: {apple_weight}")
logging.info(f"Banana: {banana_weight}")

put_success(
    f"Total cost \n\nApple:\t{apple_cost} \nBanana:\t{banana_cost} \n\nTotal:\t{total_cost}"
)
