from abc import abstractmethod

class PrintEdition:
    def __init__(self,title ='', format = '',pages = 0):
        self.__title = title
        self.__format = format
        self.__pages = pages
    
    def print(self):
        print(f'Название: {self.__title}\nФормат: {self.__format}\nКоличество страниц: {self.__pages}')
    
    def scan(self):
        self.__title = input("Введите название: ")
        self.__format = input("Введите формат: ")
        self.__pages = int(input("Введите количество страниц: "))
    
    def format_bool(self, name):
        return (self.__format == name)
            
    
    def pages_interval(self, start, end):
        return (start <= self.__pages and self.__pages <= end)
    
    def print_file(self, file):
        file.write(f'Название: {self.__title}\nФормат: {self.__format}\nКоличество страниц: {self.__pages}\n')
    
    def scan_file(self,path):
            items = path.readline().strip().split(",")
            self.__title = items[0]
            self.__format = items[1]
            self.__pages = int(items[2])

class Book(PrintEdition):
    def __init__(self, title = '', format = '', pages = 0, author =''):
        super().__init__(title,format,pages)
        self.__author = author
    
    def print(self):
        super().print()
        print(f'Автор: {self.__author}\n')

    def scan(self):
        print('Заполните данные о книге: ')
        super().scan()
        self.__author = input("Введите имя автора: ")
    
    def print_file(self,file):
        file.write('\nКнига\n')
        super().print_file(file)
        file.write(f'Автор: {self.__author}\n')
    
    def scan_file(self,path):
        super().scan_file(path)
        self.__author = path.readline().strip()
        

    def get_author(self):
        return self.__author
    
    def GetCopy(self):
        return self()

class Magazine(PrintEdition):
    def __init__(self, title = '', format = '', pages = 0, editor = ''):
        super().__init__(title, format, pages)
        self.__editor = editor
    
    def get_editor(self):
        return self.__editor
    
    def print(self):
        super().print()
        print(f'Редактор: {self.__editor}\n')

    def scan(self):
        print('Заполните данные о журнале: ')
        super().scan()
        self.__editor = input("Введите имя редактора: ")
    
    def print_file(self,file):
        file.write('\nЖурнал\n')
        super().print_file(file)
        file.write(f'Редактор: {self.__editor}\n')
    
    def scan_file(self,path):
        super().scan_file(path)
        self.__editor = path.readline().strip()
    
    def GetCopy(self):
        return self()
class Print_Collection(PrintEdition):
    def __init__(self, printlist = None):
        if isinstance(printlist,list):
            self.__printlist = printlist
        else:
            self.__printlist = []
    
    def scan_from_keyboard(self):
        num = int(input("Введите количество печатных изданий: "))
        ps = []
        for _ in range(num):
            p = ''
            ans = input('Выберите тип Книга(К) / Журнал(Ж): ').strip()
            if ans in ('К', 'Книга'):
                p = Book()
            elif ans in ('Ж', 'Журнал'):
                p = Magazine()
            p.scan()
            ps.append(p)
        self.__printlist = ps
    
    def print_to_display(self):
        for elem in self.__printlist:
            if(isinstance(elem,Book)):
                print("Книга")
                elem.print()
            elif(isinstance(elem,Magazine)):
                print("Журнал")
                elem.print()
    
    def scan_from_file(self,path):
        ps2 = []
        with open(path) as file:
            num = int(file.readline())
            for _ in range(num):
                p = ''
                ans = file.readline().strip()
                if ans == 'B':
                    p = Book()
                elif ans == 'M':
                    p = Magazine()
                p.scan_file(file)
                ps2.append(p)
        self.__printlist = ps2

    def pages_intervals(self,start,end):
        result = []
        for p in self.__printlist:
            if(p.pages_interval(start,end)):
                result.append(p)
        return result
    
    def special_format(self, format):
        result = []
        for p in self.__printlist:
            if(p.format_bool(format)):
                result.append(p)
        return result
    
    def output_to_file(self,path):
        # with open(path,'w',encoding="UTF-8") as file:
        for p in self.__printlist:
            p.print_file(path)



def main():
    path = "input.txt"
    ps = Print_Collection()
    ps.scan_from_keyboard()
    print("\nСписок добавленный с клавиатуры: ")
    ps.print_to_display()

    ps2 = Print_Collection()
    print("\nСписок, добавленный из файла: ")
    ps2.scan_from_file(path)
    ps2.print_to_display()

    start = int(input("Введите начало интервала: "))
    end = int(input("Введите конец интервала: "))
    diapazone = Print_Collection(ps2.pages_intervals(start,end))
    print(f'\nСписок с интервалом от {start} до {end} страниц: \n')
    diapazone.print_to_display()

    format = input("Введите формат: ")
    format_list = Print_Collection(ps2.special_format(format))
    print(f'\nСписок с указанным форматом "{format}" \n')
    format_list.print_to_display()

    out_path = "output.txt"
    with open(out_path, 'w', encoding="UTF-8") as file:
        file.write('\nСписок элементов с клавиатуры: \n')
        ps.output_to_file(file)

        file.write('\nСписок элементов из файла: \n')
        ps2.output_to_file(file)

        file.write(f'\nСписок с интервалом от {start} до {end} страниц: \n')
        diapazone.output_to_file(file)

        file.write(f'\nСписок с указанным форматом "{format}" \n')
        format_list.output_to_file(file)
    


if __name__ == '__main__':
    main()

