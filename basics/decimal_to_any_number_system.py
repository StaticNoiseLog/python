def convert(decimal, target_base):
    if decimal <= 0:
        return ""
    remainder = decimal % target_base
    integer_part = decimal // target_base
    return convert(integer_part, target_base) + str(remainder)


target_base = int(input("Target number base: "))
decimal = int(input("Decimal number to convert: "))

print("{decimal} dec in base {base} is {result}".format(decimal=decimal, base=target_base, result=convert(decimal, target_base)))
