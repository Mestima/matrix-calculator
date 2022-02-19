from tkinter import * # подключаем библиотеку графического интерфейса
import numpy # подключаем математическую библиотеку

# Функция упрощает установку нового значения элементу Entry (TextField)
def set(elem, text):
    elem.delete(0, "end")
    elem.insert(0, text)

# Создание основного окна программы
root = Tk()
root.title("Калькулятор Матриц")
root.geometry("505x300")
root.resizable(False, False)

# Создание интерфейса для ввода первой входной матрицы
inputMatrix = [[], [], []]
counter = 0 # Необходимо для правильного и красивого расположения элементов интерфейса
for i in range(3):
    for j in range(3):
        field = Entry(width=2)
        field.insert(0, "0") # стандартное значение каждого элемента матрицы = 0
        field.grid(row=i, column=j, ipadx=10, ipady=6, padx=10, pady=10)
        inputMatrix[counter].append(field)
    counter = counter + 1 # доходит максимум до 2 (0, 1, 2)
counter = 0 # обнуляется, так как далее используется с той же целью
label = Label(text="Первая матрица", width=20, height=20) # текст - элемент интерфейса, подписывающий первую матрицу
label.place(x = 34, y = 150, width = 100, height = 15)

# Создание интерфейса для ввода второй входной матрицы
inputMatrix2 = [[], [], []]
for i in range(3):
    for j in range(6, 9):
        field = Entry(width=2)
        field.insert(0, "0") # стандартное значение каждого элемента матрицы = 0
        field.grid(row=i, column=j, ipadx=10, ipady=6, padx=10, pady=10)
        inputMatrix2[counter].append(field)
    counter = counter + 1
counter = 0
label = Label(text="Вторая матрица", width=20, height=20) # текст - элемент интерфейса, подписывающий вторую матрицу
label.place(x = 370, y = 150, width = 100, height = 15)

# Создание интерфейса для вывода матрицы-ответа
answer = [[], [], []]
for i in range(3):
    for j in range(3, 6):
        field = Entry(width=2, background="#34A2FE")
        field.grid(row=i, column=j, ipadx=10, ipady=6, padx=10, pady=10)
        answer[counter].append(field)
    counter = counter + 1
label = Label(text="Ответ", width=20, height=20) # текст - элемент интерфейса, подписывающий матрицу-ответ
label.place(x=201, y=150, width=100, height = 15)

# Создание интерфейса для вывода определителя
label = Label(text="Определитель:", width=20, height=20)
label.place(x=15, y=200, width=100, height = 15)
determ = Entry(width=63)
determ.place(x = 110, y = 200)

# Функция, выполняющая сложение двух матриц
def additionAct():
    for i in range(3):
        for j in range(3):
            set(answer[i][j], float(inputMatrix[i][j].get()) + float(inputMatrix2[i][j].get())) # получаем значения обоих матриц, приводим к типу float и складываем, выводим в поле ответа

# Функция, выполняющая умножение двух матриц
def multiplicationAct():
    for i in range(3):
        for j in range(3):
            set(answer[i][j], float(inputMatrix[i][j].get()) * float(inputMatrix2[i][j].get())) # аналогично комментарию выше

# Функция, выполняющая деление двух матриц
def divisionAct():
    for i in range(3):
        for j in range(3):
            set(answer[i][j], float(inputMatrix[i][j].get()) / float(inputMatrix2[i][j].get())) # аналогично комментарию выше

# Функция, выполняющая вычитание двух матриц
def subtractionAct():
    for i in range(3):
        for j in range(3):
            set(answer[i][j], float(inputMatrix[i][j].get()) - float(inputMatrix2[i][j].get())) # аналогично комментарию выше

# Функция, выполняющая подсчёт определителя первой матрицы
def detAction():
    matrix = [[], [], []]
    for i in range(3):
        for j in range(3):
            matrix[i].append(float(inputMatrix[i][j].get())) # заполняем матрицу, конвертируя всё в float
    set(determ, numpy.linalg.det(matrix)) # устанавливает подсчитанное значение определителя соответствующему текстовому полю

# Функция, выполняющая поиск обратной матрицы, работает только для первой матрицы, только если определитель не равен 0
def inverseAct():
    matrix = [[], [], []]
    for i in range(3):
        for j in range(3):
            matrix[i].append(float(inputMatrix[i][j].get()))
    if (numpy.linalg.det(matrix) != 0.0):
        err["text"] = "[ OK! ]"
        err["background"] = "#00FF00"
        inversed = numpy.linalg.inv(matrix)
        for i in range(3):
            for j in range(3):
                set(answer[i][j], inversed[i][j])
    else:
        err["text"] = "[ определ = 0 ]" # поле статуса-ошибки, сигнализирует о том, что определитель = 0, подсчёт обратной матрицы невозможен
        err["background"] = "#FF0000" # устанавливаем красный цвет

# Функция, выполняющая транспонирование матрицы
def transposeAct():
    matrix = [[], [], []]
    for i in range(3):
        for j in range(3):
            matrix[i].append(float(inputMatrix[i][j].get())) # берем значение каждого поля и собираем из них матрицу типа float
    npMatrix = numpy.array(matrix) # необходимо обернуть в объект numpy.array
    transposed = npMatrix.transpose()
    for i in range(3):
        for j in range(3):
            set(answer[i][j], transposed[i][j])
    
# Массив соответсвий {имя, функция}, используется в инициализации управляющих кнопок программы
actions = [
    {"name": "Сложить", "action": additionAct}, # сложение
    {"name": "Умножить", "action": multiplicationAct}, # умножение
    {"name": "Разделить", "action": divisionAct}, # деление
    {"name": "Вычесть", "action": subtractionAct}, # вычитание
    {"name": "Определитель", "action": detAction}, # определитель
    {"name": "Обратная матрица", "action": inverseAct}, # обратная матрица
    {"name": "Транспонировать", "action": transposeAct} # транспонирование
]

actionButts = []
xAdd = 0 # необходимо для правильного расположения элементов интерфейса

# Цикл создаёт управляющие кнопки программы
for i in range(7):
    yAdd = 0 # необходимо для правильного расположения элементов интерфейса
    if (i != 0 and i % 2 == 0):
        xAdd += 120
    if (i % 2 != 0):
        yAdd = 30
    
    butt = Button(text=actions[i]["name"], command=actions[i]["action"]) # каждая кнопка получает имя и функцию из массива соответствий
    butt.place(x = 10 + xAdd, y = 230 + yAdd, width = 115, height = 25)
    actionButts.append(butt)

# текстовый элемент, отображающий статус выполнения подсчёта обратной матрицы. Если определитель матрицы равен нулю, поле становится красным и сообщает об ошибке.
err = Label(text = "[ статус ]", width = 115, height = 25, background="#00FF00")
err.place(x = 370, y = 260, width = 115, height = 25)

root.mainloop() # инициализация жизненного цикла программы