def shift_left(lst, k):
    for i in range(k):
        lst.append(lst.pop(0)) #извлекаем 1 элемент и добавляем в конец
        
def shift_right(lst,k):
    for i in range(k):
        lst.insert(0, lst.pop()) #извлекаем последний и добавляем в начало

    