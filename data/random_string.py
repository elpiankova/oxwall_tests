import random
import string


# print(random.random())
# print(random.randint(50, 100))
# print(random.randrange(50, 101))
# print(random.randrange(50, 101, 2))
#
# l = string.printable
# print(string.punctuation)
#
# print(random.choice(l))
# print(random.choices(l, k=10))


def random_string(minlen=1, maxlen=255, enter=False):
    length = random.randint(minlen, maxlen)
    symbols = (string.ascii_letters + string.digits +
               string.punctuation + " "*10)
    if enter:
        symbols += "\n" * 5
    result = ''.join(random.choices(symbols, k=length))
    return result


def random_string2(minlen=1, maxlen=256, spaces=False, whitespases=False, enter=False, cyr=False):
    length = random.randint(minlen, maxlen)
    symbols = string.ascii_letters + string.digits + string.punctuation
    if spaces:
        symbols += ' ' * 10
    if whitespases:
        symbols += string.whitespace[:-2] * 3
    if enter:
        symbols += "\n"*3
    if cyr:
        cyr_symbol = ''.join([chr(l) for l in range(0x0400, 0x04FF)
                              if chr(l).isprintable()])
        symbols += cyr_symbol
    result = ''.join(random.choices(symbols, k=length))
    return result


if __name__ == '__main__':
    print(random_string(1, 100, enter=True))
