def victory():

    people = {
        'Джими Хендрикс': '27.11.1942',
        'Оззи Осборн': '03.12.1948',
        'Пол Маккартни': '18.06.1942',
        'Эрик Клэптон': '30.03.1945',
        'Брайан Мэй': '19.07.1947',
        'Фил Коллинз': '30.01.1951',
        'Вилле Вало': '22.11.1976',
        'Джон Фогерти': '28.05.1945',
        'Стив Тайлер': '26.03.1948',
        'Джефф Линн': '30.12.1947'
    }
    days = {
        '03': 'третье',
        '18': 'восемнадцатое',
        '19': 'девятнадцатое',
        '22': 'двадцать второе',
        '26': 'двадцать шестое',
        '27': 'двадцать седьмое',
        '28': 'двадцать восьмое',
        '30': 'тридцатое'
    }
    months = {
        '01': 'января',
        '03': 'марта',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '11': 'ноября',
        '12': 'декабря'
    }

    import random

    while True:

        selection = random.sample(list(people.keys()), k=5)
        right = 0
        wrong = 0
        print()
        for i in range(len(selection)):
            person = input(f'Введите дату рождения следующего музыканта:\n{selection[i]}: ')
            answer = people.get(selection[i])
            if person != answer:
                day, month, year = answer.split('.')
                result = days[day] + ' ' + months[month] + ' ' + year + ' ' + 'года'
                print('Неверно! Правильнвй ответ - ', result)
            # Использование тернарных операторов
            right += 1 if person == answer else 0
            wrong += 1 if person != answer else 0

        print()
        print('Количество правильных ответов: ', right)
        print('Количество неправильных ответов: ', wrong)

        if input('Хотите начать игру сначала? ') != 'да':
            break
