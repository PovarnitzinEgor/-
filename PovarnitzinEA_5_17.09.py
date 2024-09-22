from math import log2

def tasks(task):
    if task == "1":
        print(task_1(input("Введите размер изображения: ")))
    elif task == "2":
        colors_1 = int(input("Количество цветов увеличилось с : "))
        colors_2 = int(input("до : "))
        print(task_2(colors_1, colors_2))
    elif task == "3":
        size = input("Введите размер изображения: ")
        mem = input("Введите размер памяти (в Кбайт): ")
        print(task_3(size, mem))
    elif task == "4":
        colors = input("Введите количество цветов: ")
        mem = input("Введите размер информации(в байт): ")
        print(task_4(colors, mem))
    else:
        print("Этого задания нет")

def task_1(size):
    # Так как изображение двухцветное, количество бит отведённых под каждый пиксель равно 1. Cледовательно, количество бит в изображении будет равно количеству точек в нём.
    flag = False
    count = 0
    # Поиск знака умножения
    for i in size:
        if i != "*":
            count += 1
        else:
            flag = True
            break
    # Нахождение результата задачи
    if flag:
        res = int(size[:count]) * int(size[count + 1:])
    else:
        res = size
    return res

def task_2(colors_1, colors_2):
    colors_1 = log2(colors_1) # нахождение кол-ва бит, отводимых под каждый пиксель
    colors_2 = log2(colors_2) # нахождение кол-ва бит, отводимых под каждый пиксель
    # Нахождение результата задачи
    return colors_2 / colors_1

def task_3(size, mem):
    size = int(task_1(size)) # нахождение размера изображения
    mem = int(mem) * 1024 * 8 # перевод из Кбайт в бит
    res = mem / size # нахождение кол-ва бит, отводимых под каждый пиксель
    res = 2 ** res # нахождение количества цветов
    return res
        
def task_4(colors, mem):
    mem = int(mem) * 8 # перевод в биты
    colors = log2(int(colors))# нахождение кол-ва бит, отводимых под каждый пиксель
    res = mem / colors # нахождение количества точек
    return res

if __name__ == "__main__":
    task = input("Введите номер задания(только с 1 по 4) : ")
    tasks(task)