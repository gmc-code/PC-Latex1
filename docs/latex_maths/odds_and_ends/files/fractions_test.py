from fractions import Fraction


def count_decimal_places(num):
    num_str = str(num)
    if "." not in num_str:
        return 0
    return len(num_str) - num_str.index(".") - 1

def decimal_to_unsimplified_fraction(decimal_part):
    dp = count_decimal_places(decimal_part)
    den = 10**dp
    num = int(decimal_part * den)
    return num, den


def decimal_to_mixed_number(decimal):
    whole_part = int(decimal)
    decimal_part = decimal - whole_part
    num, den = decimal_to_unsimplified_fraction(decimal_part)
    simplified_fraction = Fraction(decimal_part).limit_denominator()
    return (decimal_part, whole_part, num, den, simplified_fraction)


decimal = 1.875
fractional_part, whole, num, den, simplified_fraction = decimal_to_mixed_number(decimal)
print(
    f"{decimal} as a mixed number is {whole} and {fractional_part} and {num} / {den} or {simplified_fraction.numerator}/{simplified_fraction.denominator} (simplified)"
)
