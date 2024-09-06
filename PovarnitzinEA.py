from math import log2


def task18(byte, pages, lines, symbol):
    all_symbols = pages * lines * symbol
    one_symbol = byte * 8 / all_symbols
    return 2 ** one_symbol

def task19(first, second):
    f = log2(first)
    s = log2(second)
    if s > f:
        return s / f
    else:
        return f / s

def task20(symbols, bit):
    i = log2(symbols)
    return bit / i

def task7(bit1, blue):
    all = (2 ** bit1) * blue
    return all - (blue * 2)

def task19_1(bit2):
    return 2 ** bit2

def task20_1(bit3):
    return 2 ** bit3

if __name__ == "__main__":

    # №18

    inp1 = int(input("Количество байт: "))
    inp2 = int(input("Количество страниц: "))
    inp3 = int(input("Количество строк: "))
    inp4 = int(input("Количество символов: "))
    print("Символов в алфавите равно ", task18(inp1, inp2, inp3, inp4))


    # №19

    inp1 = int(input("Количество символов в первом алфавите: "))
    inp2 = int(input("Количество символов во втором алфавите: "))
    print("Количество иформации в текстах отличается в "f"{task19(inp1, inp2)} раз")


    # №20

    inp1 = int(input("Количество символов в алфавите: "))
    inp2 = int(input("Количество бит: "))
    print("Количество символов в сообщении равно ", task20(inp1, inp2))


    # №7

    inp1 = int(input("Количество бит: "))
    inp2 = int(input("Количество синей краски: "))
    print(task7(inp1, inp2), "банок коричневой краски израсходовали")


    # №19

    inp1 = int(input("Количество бит: "))
    print(task19_1(inp1), "этажей в доме")


    # №20

    inp1 = int(input("Количество бит: "))
    print(task19_1(inp1), "подъездов в доме")