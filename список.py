spisok = []
t = input('Что вы хотите добавить в список? Если закончили, то напишите - выход ')
while t.lower() != 'выход':
    spisok.append(t)
    print(f'Текущий список покупок содержит: {spisok}')
    t = input('Что вы хотите добавить в список? Если закончили, то напишите - выход ')
    

