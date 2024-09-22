def tasks(task):
    if task == "1":
        time = int(input("Введите время звучания(в минутах): "))
        frequency = input("Введите частоту дискретизации(в кГц): ")
        resolution = int(input("Введите разрешение(в бит): "))
        print(task_1(time, frequency, resolution))
    elif task == "2":
        time = int(input("Введите время записи(в минутах): "))
        size = input("Введите сколько занимает на диске(в Мб): ")
        capacity = int(input("Введите разрядность: "))
        print(task_2(time, size, capacity))
    elif task == "3":
        size = input("Введите объем свободной памяти(в Гб): ")
        capacity = int(input("Введите разрядность: "))
        frequency = int(input("Введите частоту дискретизации(в Гц): "))
        print(task_3(size, capacity, frequency))
    elif task == "4":
        capacity = int(input("Введите величину кодирования(в бит): "))
        frequency = int(input("Введите частоту дискретизации(в кГц): "))
        size = int(input("Введите объем(в Кб): "))
        print(task_4(capacity, frequency, size))
    elif task == "5":
        time = int(input("Введите длительность звучания(в минутах): "))
        capacity = int(input("Введите глубину кодирования(в бит): "))
        frequency = int(input("Введите частоту дискретизации(в кГц): "))
        print(task_5(time, capacity, frequency))
    else:
        print("Этого задания нет")

def task_1(time, frequency, resolution):
    res = 0
    time = time * 60# перевод в секунды
    frequency = float(str(frequency).replace(",", ".")) * 1000# перевод в Гц
    res = time * frequency * (resolution / 8)# решение по формуле: Размер(байт) = (частота дискретизации в Гц) * (времязаписи в секундах) * (разрешение в битах) / 8
    return f"{int(res)} байт"

def task_2(time, size, capacity):
    size = float(str(size).replace(",", ".")) * 1024 * 1024# перевод в байт
    time = time * 60# перевод в секунды
    res = size / (time * (capacity / 8))# решение по формуле: (частота дискретизации в Гц) = Размер(байт) / (времязаписи в секундах) * (разрешение в битах) / 8
    return f"{int(res)} Гц"

def task_3(size, capacity, frequency):
    size = float(str(size).replace(",", ".")) * 1024 * 1024 * 1024# перевод в байт
    res = size / (frequency * (capacity / 8))# решение по формуле: (времязаписи в секундах) = Размер(байт) / (частота дискретизации в Гц) * (разрешение в битах) / 8
    return f"{int(res)} сек"

def task_4(capacity, frequency, size):
    frequency = frequency * 1000# перевод в Гц
    size = size * 1024# перевод в байт
    res = size / (frequency * (capacity / 8))# решение по формуле: (времязаписи в секундах) = Размер(байт) / (частота дискретизации в Гц) * (разрешение в битах) / 8
    return f"{res} сек"

def task_5(time, capacity, frequency):
    time = time * 60# перевод в секунды
    frequency = frequency * 1000# перевод в Гц
    res = (frequency * time * (capacity / 8)) / 1024# решение по формуле: Размер(байт) = (частота дискретизации в Гц) * (времязаписи в секундах) * (разрешение в битах) / 8
    return f"{res} килобайт"

if __name__ == "__main__":
    task = input("Введите номер задания(только с 1 по 5) : ")
    tasks(task)