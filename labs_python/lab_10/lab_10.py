text = "Сегодня прекрасный день для прогулки в парке. Солнце светит ярко, птицы поют, а воздух свежий и чистый. Нет поводов для печали и грусти, ведь любые проблемы решаемы, стоит лишь попробовать пофиксить"
words = text.split()

for i in range(len(words)):
    if len(words[i]) % 2 == 0:
        words[i] = words[i][:-1]
    else:
        center = len(words[i]) // 2
        words[i] = words[i][:center] + words[i][center+1:]

new_text = ' '.join(words)
print(new_text)


