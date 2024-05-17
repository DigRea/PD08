def listdir():

    import os

    # Получаем содержимое рабочей директории
    files_and_dirs = os.listdir()

    # Разделяем файлы и папки
    files = [f for f in files_and_dirs if os.path.isfile(f)]
    dirs = [d for d in files_and_dirs if os.path.isdir(d)]

    # Сортируем элементы
    files.sort()
    dirs.sort()

    # Путь к файлу
    filename = 'listdir.txt'

    # Проверяем существование файла и пересоздаем, если нужно
    if os.path.exists(filename):
        os.remove(filename)

    # Записываем в файл
    with open(filename, 'w') as f:
        f.write("Files:\n")
        for file in files:
            f.write(file + '\n')

        f.write("\nDirectories:\n")
        for dir in dirs:
            f.write(dir + '\n')