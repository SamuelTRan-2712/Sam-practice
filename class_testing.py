class roman_numeral:

    def converter_roman_int(self, a):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer_values = 0

        for i in range(len(a)):

            if i > 0 and roman_values[a[i]] > roman_values[a[i-1]]:
                integer_values = integer_values + roman_values[a[i]] - 2 * roman_values[a[i - 1]]

            else:
                integer_values = integer_values + roman_values[a[i]]

        return integer_values


print(roman_numeral().converter_roman_int("XIV"))
