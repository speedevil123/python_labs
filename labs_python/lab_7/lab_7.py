x = float(input("Введите x: "))
if(x == 0):
    exit("x не может быть равен 0")
a = float(input("Введите малое a: "))
count = 0
sum = 0
i = 1
last_slog = 0

while(a < 1/(i*x**i)):
    count += 1
    if(count % 2 == 0):
        sum += -(1/(i*x**i))
    else:
        sum += (1/(i*x**i))
    last_slog = (1/(i*x**i))
    print(f"{sum}  {i}  {1/(i*x**i)}")
    i += 2
print(f"Cлагаемое после которого остановился цикл: {1/(i*x**i)}\nПоследнее слагаемое: {last_slog}\nСумма: {sum}\nКол-во итераций: {count}")


    