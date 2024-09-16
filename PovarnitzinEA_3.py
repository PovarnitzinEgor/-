zero_one = {
    "0": "1",
    "1": "0"
}
num_sixteen = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F",
}

sixteen_num = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13",
    "E": "14",
    "F": "15",
}

two_sixteen = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}

sixteen_two = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

def int_fract(num, base, base_2):
    sign = False
    if (base == "2" or base == "8" or base == "10" or base == "16" or base == "Внутреннее представление в 16 форме") and (base_2 == "2" or base_2 == "8" or base_2 == "10" or base_2 == "16" or base_2 == "Внутреннее представление" or base_2 == "внутреннее представление"):
        if str(num)[0] == "-":
            num = num[1:]
            sign = True   
        if str(base) == base_2:
            return num
        else:
            int_part = ""
            fract_part = ""
            flag = False
            for i in str(num):
                if i == "," or i == ".":
                    flag = True
                if flag == False:
                    int_part += i
                elif flag and i != "," and i != ".":
                    fract_part += i
            if base != "Внутреннее представление в 16 форме":
                for g in int_part:
                    if int(sixteen_num[g]) > int(base):
                        return "Некорректный ввод"
                for q in fract_part:
                    if int(sixteen_num[g]) > int(base):
                        return "Некорректный ввод" 
            if flag == False:
                fract_part = 0
            if base_2 == "Внутреннее представление" or base_2 == "внутреннее представление":
                return f"Внутреннее представление числа: {internal_representation(int_part, fract_part, base, sign)}"
            elif base == "Внутреннее представление в 16 форме":
                return invers_internal_representation(int_part, base_2)
            elif int(base_2) == 10:
                if sign:
                    return f"Внутреннее представление числа: -{int_conv_ten(int_part, fract_part, base)}"
                else:
                    return f"{int_conv_ten(int_part, fract_part, base)}"
            elif int(base) != 10:
                if sign:
                    return f"-{int_fract(int_conv_ten(int_part, fract_part, base), 10, base_2)}"
                else:
                    return f"{int_fract(int_conv_ten(int_part, fract_part, base), 10, base_2)}"
            else:
                if sign:
                    return f"-{int_conv_other(int_part, fract_part, base_2)}"
                else:
                    return f"{int_conv_other(int_part, fract_part, base_2)}"
    else:
         return "Некорректный ввод"
    

def int_conv_ten(int_part, fract_part, base):
    result = 0
    length = len(int_part) - 1
    for i in str(int_part):
        result += int(sixteen_num[i]) * (int(base) ** length)
        length -= 1
    if fract_part == 0:
        return result
    else:
        for j in str(fract_part):
            result += int(sixteen_num[j]) * (int(base) ** length)
            length -= 1
    return result

def int_conv_other(int_part, fract_part, base_2):
    remainder = int_part
    quotient = int(int_part)
    fract_num = fract_part
    res_int = ""
    res_fract = ""
    lenght_fract = len(str(fract_part))
    anti_fraсt_num = 1
    count = 15
    while quotient > (int(base_2) - 1):
        remainder = quotient % int(base_2)
        quotient = quotient // int(base_2)
        res_int += num_sixteen[str(remainder)]
    res_int += num_sixteen[str(quotient)]
    res_int = res_int[::-1]
    if fract_part == 0:
        return res_int
    else:
        while anti_fraсt_num != 0 and count != 0:
            fract_num = int(fract_num) * int(base_2)
            res_fract += num_sixteen[str(int(fract_num) // (10 ** (int(lenght_fract))))]
            fract_num = str(fract_num)[-lenght_fract:]
            anti_fraсt_num = int(fract_num[::-1])
            count -= 1
        return f"{res_int},{res_fract}"

def internal_representation(int_part, fract_part, base, sign):
    form = input("Введи в какой форме(Варианты ввода: 2, 16): ")
    int_p = int_part
    longitude_remainder = 0
    count = 0
    res = ""
    number = 0
    count_1 = 0
    con = 0
    resultat = ""
    longitude_remainder_1 = 0
    if fract_part == 0:
        int_p = int_fract(int_part, base, str(2))
        longitude_remainder  = len(str(int_p)) % 16
        if longitude_remainder > 0:
            while longitude_remainder < 16:
                longitude_remainder += 1
                count += 1
        r = ("0" * count) + str(int_p)
        if form == "16" and sign:
            for y in r:
                res += zero_one[y]
            res = str(int(res) + 1)
            con = len(res)
            while con > 0:
                resultat += two_sixteen[res[:4]]
                res = res[4:]
                con -= 4
            return resultat
        elif form == "16":
            con = len(r)
            while con > 0:
                resultat += two_sixteen[r[:4]]
                r = r[4:]
                con -= 4
            return resultat
        else:
            return r
    else:
        number = int_fract((f"{int_part},{fract_part}"), base, str(2))
        int_part_1 = ""
        fract_part_1 = ""
        flag = False
        for i in str(number):
            if i == "," or i == ".":
                flag = True
            if flag == False:
                int_part_1 += i
            elif flag and i != "," and i != ".":
                fract_part_1 += i
        number = int_part_1 + fract_part_1
        len_int_part = len(int_part_1)
        num_len = int_fract(len_int_part, base, str(2))
        if sign:
            res = "1" + str(1000000 + int(num_len)) + str(number)
        else:
            res = "0" + str(1000000 + int(num_len)) + str(number)
        if (int(len(res)) % 16) == 0 and form == "2":
            return res
        elif form == "2":
            longitude_remainder_1 = int(len(res)) % 16
            while longitude_remainder_1 < 16:
                longitude_remainder += 1
                count_1 += 1
            res = str(res) + ("0" * count_1)
        if form == "2":
            return res
        elif form == "16":
            con_1 = len(res)
            resultat_1 = ""
            while con_1 > 0:
                resultat_1 += two_sixteen[res[:4]]
                res = res[4:]
                con_1 -= 4
        return resultat_1

def invers_internal_representation(int_part, base_2):
    res_1 = ""
    degree = 0
    flg = False
    for t in int_part:
        res_1 = res_1 + str(sixteen_two[t])
    if str(res_1[0]) == "1":
        flg == True
    degree = int(res_1[1:8]) - 1000000
    degree = int(int_fract(degree, "2", "10"))
    res_1 = res_1[8:]
    res_1 = res_1[:degree] + "," + res_1[degree:]
    res_1 = int_fract(res_1, "2", base_2)
    if flg:
        return f"-{res_1}"
    else:
        return res_1


if __name__ == "__main__":
    num = input("Введите число: ")
    base = input("Введите базу числа(Варианты ввода: 2, 8, 10, 16, Внутреннее представление в 16 форме): ")
    base_2 = input("Введите во что перевести число(Варианты ввода: 2, 8, 10, 16, Внутреннее представление): ")
    print(int_fract(num, base, base_2))