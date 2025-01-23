def verify_card_number(card_number):
    """
    Verify a card number using the Luhn Algorithm.
    
    Parameters:
        card_number (str): The card number as a string of digits (spaces and dashes removed).
    
    Returns:
        bool: True if the card number is valid, False otherwise.
    """
    sum_of_odd_digits = 0
    # Reverse the card number for processing
    card_number_reversed = card_number[::-1]
    # Extract all odd-positioned digits (1st, 3rd, etc., in 0-based index)
    odd_digits = card_number_reversed[::2]

    # Sum all the odd-positioned digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    # Extract all even-positioned digits (2nd, 4th, etc., in 0-based index)
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        # Double the digit
        number = int(digit) * 2
        # If the doubled value is >= 10, sum its digits
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Calculate the total sum of odd and even digits
    total = sum_of_odd_digits + sum_of_even_digits
    # Return True if the total modulo 10 equals 0 (valid card number)
    return total % 10 == 0

def main():
    """
    Main function to test the Luhn Algorithm.
    """
    # Sample card number with spaces and dashes
    card_number = '4111-1111-4555-1142'
    # Create a translation table to remove '-' and ' ' from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    # Translate the card number to remove spaces and dashes
    translated_card_number = card_number.translate(card_translation)

    # Check if the card number is valid
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Run the main function
main()
