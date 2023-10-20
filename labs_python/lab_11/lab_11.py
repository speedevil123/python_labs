from lab_11_func import read_file, finding, result

start_path = "lab_11_start.txt"
finish_path = "lab_11_finish.txt"

contents = read_file(start_path)

numbers = finding(contents)

result(numbers,finish_path)

