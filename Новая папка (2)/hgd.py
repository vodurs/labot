from os import strerror
try:
    with open('C:/Users/11/Desktop/пакп/labot/Новая папка/o.txt') as file:
        text = file.read()
except IOError as err :
    print(f'не удалось открыть файл {setattr(err.errno)}')
print(text)
word_f = input('ведите старое слово')
word_c = input('ведите новое слово')
text =text.replace(word_f,word_c)
print(text)
try:
    with open('C:/Users/11/Desktop/пакп/labot/Новая папка/Текстовый документ.txt','w') as file:
        text = file.write(text)
except IOError as err :
    print(f'не удалось открыть файл {setattr(err.errno)}')