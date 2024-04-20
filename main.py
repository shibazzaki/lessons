import os

print(os.path.getctime("file.txt"))
print(os.path.getmtime("file.txt"))





"""file = open("file.txt", "w")
file.write("Hello World")
file.close()
file = open("file.txt", "a")
file.write("\nHello class")
file.close()
file = open("file.txt", "r")
print(file.read())
file.close()"""

"""
open() - відкрити йоу
r - відкриття файлу для читання
w - відкриття файлу для запису, попередня інформація в файлі буде видалятися
a - відкриття файлу на дозаписування, тобто попередня інформація в файлі буде збережена

isfile() - чи веде шлях до файлу
isdir() - чи веде шлях до папки(директорії)
islink() - чи веде шлях до посилання(лінки)
isabs() - чи є шлях абсолютним
"""
