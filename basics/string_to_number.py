string = input("Decimal as string: ")

string_reversed = string.strip()[::-1]

result = 0
power_of_ten = 1
for i, c in enumerate(string_reversed):
    # result += 10**i * int(c)
    result += power_of_ten * int(c) # less multiplications
    power_of_ten *= 10
#    print(i, c)  # index and character at the index

print("String >{string}< as number: {result}".format(string=string, result=result))
