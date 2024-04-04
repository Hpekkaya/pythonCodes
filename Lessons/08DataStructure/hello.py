def changeAds(base10):
    first = base10
    count = 0
    while base10 > 0:
        count += 1
        base10 = base10 // 2
    rev = (2**count - 1) - first

    bin2 = binary_to_dec(first)

    return rev, count, bin2


def binary_to_dec(base10):
    if base10 == 0:
        return "0"
    bas_2 = []
    bas_2_u = []

    while base10 > 0:
        remainder = base10 % 2
        bas_2.append(str(remainder))
        bas_2_u.append(str(remainder))
        base10 = base10 // 2

    bas_2.reverse()
    return "".join(bas_2)


def bin_to_2(bin10):
    if bin10 == 0:
        return "0"

    bin_2 = []

    while bin10 > 0:
        rem = bin10 % 2
        bin_2.append(str(rem))
        bin10 = bin10 // 2

    bin_2.reverse()

    return "".join(bin_2)


def bin_to_2u(bin10):
    if bin10 == 0:
        return "0"

    bin_2 = []

    while bin10 > 0:
        rem = bin10 % 2
        bin_2.append(str(rem))
        bin10 = bin10 // 2

    return "".join(bin_2)


def bin2_to_10(bin2):
    numb = 0
    for i in bin2:
        numb += int(i)
        print(numb)

    return numb


val = 100
# base2 = binary_to_dec(val)
base2 = bin_to_2(val)
# base2u = bin_to_2u(val)
print(base2)
# print(base2u)

print(bin2_to_10(base2))

# base2 = changeAds(val)
# print(changeAds(val))
# print(base2)
