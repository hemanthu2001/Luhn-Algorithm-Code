# Luhn-Algorithm-Code
# Luhn Algorithm: Credit Card Validation

This project demonstrates the implementation of the **Luhn Algorithm**, also known as the Modulus 10 or Mod 10 algorithm, in Python. The Luhn algorithm is widely used to validate credit card numbers and other identification numbers by performing a simple checksum validation.

---

## How the Luhn Algorithm Works

1. **Reverse the Card Number**: Start processing the card number from right to left.
2. **Double Every Second Digit**: Starting from the first digit (from the right), double every second digit.
   - If the resulting value is 10 or greater, sum the digits of the result (e.g., `14` becomes `1 + 4 = 5`).
3. **Sum All Digits**: Add all digits, including the processed even-positioned digits and the unprocessed odd-positioned digits.
4. **Check Modulo 10**: If the total sum modulo 10 equals 0, the card number is valid; otherwise, it is invalid.

---

## Code Overview

The project includes:

### `verify_card_number(card_number)`

A function to verify the validity of a card number using the Luhn algorithm. It:

- Processes the card number to reverse it.
- Separates the odd and even digits.
- Performs calculations as described above to validate the number.

### `main()`

A sample test function that demonstrates the usage of `verify_card_number`. It:

- Accepts a card number with spaces and dashes.
- Cleans the input to remove spaces and dashes.
- Validates the card number and prints whether it is valid or invalid.

## How to Run

1. Clone or download this repository.
2. Save the script as `luhn_algorithm.py`.
3. Run the script using Python:
   ```bash
   python luhn_algorithm.py
   ```
4. Modify the `card_number` variable in the `main()` function to test with different card numbers.

---

## Example Output

For the card number `4111-1111-4555-1142`, the output will be:

```
VALID!
```

---

## Applications of the Luhn Algorithm

- Credit card validation
- Bank account number validation
- IMEI (International Mobile Equipment Identity) number validation
- Other identification numbers

---

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and share it as needed.

---

## Contribution

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

