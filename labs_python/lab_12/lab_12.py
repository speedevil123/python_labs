class Book:
    def __init__(self, author = '', title = '', pages = 0, rating = 0):
        self.__author = author
        self.__title = title
        self.__pages = pages
        self.__rating = rating
    
    def input_from_file(self, path):
        with open(path) as file:
            items = file.readline().strip().split(",")
            self.__author = items[0]
            self.__title = items[1]
            self.__pages = int(items[2])
            self.__rating = float(items[3])
    
    def output_to_file(self,path):
        with open(path, 'w'):
            line = f"{self.__author},{self.__title},{self.__pages},{self.__rating()}\n"
            path.write(line)
                

    def input_from_keyboard(self):
        self.__author = input("Введите автора: ")
        self.__title = input("Введие название книги: ")
        self.__pages = int(input("Введите количество страниц: "))
        self.__rating = float(input("Введите рейтинг: "))
        return self

    def rate(self):
        return (self.__rating) > 3
    
    def page_interval(self, start,end):
        return (start <= self.__pages and self.__pages <= end)
    
    def get_author(self):
        return self.__author
    
    def get_rate(self):
        return self.__rating
    
    def get_pages(self):
        return self.__pages
    
    def get_title(self):
        return self.__title
    
    def print_to_display(self):
        print(f'Автор {self.__author}\n'
              f'Название книги {self.__title}\n'
              f'Кол-во страниц {self.__pages}\n'
              f'Рейтинг {self.__rating}\n')

class Library:
    def __init__(self,booklst = None):
        if isinstance(booklst,list):
            self.__booklst = booklst
        else:
            self.__booklst = []

    def input_from_file(self,path):
        with open(path) as file:
            for line in file:
                items = line.strip().split(",")
                self.__author = items[0]
                self.__title = items[1]
                self.__pages = int(items[2])
                self.__rating = float(items[3])
                
                book = Book(self.__author, self.__title, self.__pages, self.__rating)
                self.__booklst.append(book)     

    def output_to_file(self,path):
        with open(path, 'w') as file:
            for book in self.__booklst:
                line = f"{book.get_author()},{book.get_title()},{book.get_pages()},{book.get_rate()}\n"
                file.write(line)


    
    def input_from_keyboard(self):
        num = int(input("Сколько книг вводите: "))
        for i in range(num):
            local_book = Book().input_from_keyboard()
            self.__booklst.append(local_book)        
    
    def print_to_display(self):
        for local_book in self.__booklst:
            local_book.print_to_display()

    def rate_sort(self):
        for i in range(len(self.__booklst)):
            for j in range(0, len(self.__booklst)-i-1):
                if(self.__booklst[j].get_rate() > self.__booklst[j+1].get_rate()):
                    self.__booklst[j], self.__booklst[j+1] = self.__booklst[j+1], self.__booklst[j]

    def add(self,x):
        self.__booklst.append(x)

    def rate_list(self):
        result = [x for x in self.__booklst if (x.rate())]
        return Library(result)

    def page_interval_list(self,start,end):
        result = [x for x in self.__booklst if (x.page_interval(start,end))]
        return Library(result)

    def author_name_list(self, name):
        result = [x for x in self.__booklst if (x.get_author() == name)]
        return Library(result)

def main():
    book_list = Library()
    path_in = "input.txt"
    path_out = "output.txt"
    book_list.input_from_file(path_in)
    book_list.print_to_display()
    book_list.rate_sort()
    auth_name = input("Какого автора ищете? ")
    list_author = book_list.author_name_list(auth_name)
    print(f'Книги с указанным автором {auth_name}: ')
    list_author.print_to_display()
    list_author.output_to_file(path_out)

    start = int(input("Введите начало интервала: "))
    end = int(input("Введите конец интервала: "))
    list_pages = book_list.page_interval_list(start,end)
    print(f'Книги с интервалом страниц от {start} до {end}: ')
    list_pages.print_to_display()


    print('Книги с рейтингом выше 3.0: ')
    list_rating = book_list.rate_list()
    list_rating.print_to_display()

    book_list.rate_sort()

if __name__ == '__main__':
    main()






    





    

    
    
