from fractions import Fraction

def decimal_to_fraction(decimal: str) -> Fraction:
    integer_part, decimal_part = decimal.split('.')
    non_repeating, repeating = decimal_part.split('(')
    repeating = repeating.rstrip(')')
    numerator = int(integer_part + non_repeating + repeating) - int(integer_part + non_repeating)
    denominator = int('9' * len(repeating) + '0' * len(non_repeating))
    return Fraction(numerator, denominator)

print(decimal_to_fraction('0.(428571)'))

