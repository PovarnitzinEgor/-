def sh_f(arr):
    l = len(arr)
    left_part = []
    right_part = []
    index = 1
    if l > 2:
        symb = 1
        ver_1 = arr[0][1]
        ver = arr[-1][1]
        l_p = 2
        while l > l_p:
            if ver_1 >= ver:
                l -= 1
                ver +=arr[l - 1][1]
                index += 1
            else:
                ver_1 += arr[symb][1]
                l_p += 1
                symb += 1
        left_part = arr[:len(arr) - index]
        right_part = arr[len(arr) - index:]
        if len(left_part) > 1:
            for i in left_part:
                i[2] += "1"
        for j in right_part:
            j[2] += "0"
        sh_f(left_part)
        sh_f(right_part)
    elif l == 2:
        arr[0][2] += "1"
        arr[1][2] += "0"
    else:
        arr[0][2] += "1"
    return arr

def search_probability(string):
    arr = []
    str_1 = ""
    for i in string:
        if i not in str_1:
            str_1 += i
    for j in str_1:
        count = 0
        for g in string:
            if j == g:
                count += 1
        arr += [[j, count, ""]]
    return sh_f(sort(arr))

def sort(arr):
    l = len(arr)
    index = 0
    while index != l:
        i = 0
        while i != l - 1:
            if arr[i][1] < arr[i + 1][1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
        index += 1
    return arr

if __name__ == "__main__":
    string = input("Введите текст: ")
    print(search_probability(string))