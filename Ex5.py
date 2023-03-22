def roman_to_int(s):
    # Define a dictionary to map Roman numerals to their corresponding integer values
    roman_to_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    # Loop through the Roman numeral string from right to left
    for i in range(len(s) - 1, -1, -1):
        # If the current Roman numeral is smaller than the next one, subtract its value from the result
        if i < len(s) - 1 and roman_to_int_map[s[i]] < roman_to_int_map[s[i + 1]]:
            result -= roman_to_int_map[s[i]]
        # Otherwise, add its value to the result
        else:
            result += roman_to_int_map[s[i]]

    return result


s = input("Enter roman number: ")
s = list(s)
print(f"inputs: s = {s}")
num = roman_to_int(s)
print(f" output: {num}")
