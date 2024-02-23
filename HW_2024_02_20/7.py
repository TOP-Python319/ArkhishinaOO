# Написать программу, которая очищает текст от знаков препинания.
# Это очень распространённая задача по подготовке текста к дальнейшему анализу. 
# Существует много способов её решения, в том числе с помощью генераторов.
# Программа получает из stdin строку текста.
# Далее, с помощью генераторного выражения и строкового метода join() программа создаёт новую строку, 
# аналогичную исходной, но без знаков препинания.
# Новую строку программа выводит в stdout.

text = input('Введите текст: ')

symbols =  '.,:;!?–—\'\"()*/'

sentences = ''.join(word for word in text if word not in symbols)
print(f'Предложение без знаков: {sentences}')


# Вывод:
# Введите текст: Было темно в гостиной. Лаптев, не садясь и держа шляпу в руках, стал извиняться за беспокойство; 
# он спросил, что делать, чтобы сестра спала по ночам, и отчего она так страшно худеет, 
# и его смущала мысль, что, кажется, эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита.

# Предложение без знаков: Было темно в гостиной Лаптев не садясь и держа шляпу в руках стал извиняться за беспокойство
# он спросил что делать чтобы сестра спала по ночам и отчего она так страшно худеет и его смущала мысль что кажется
# эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита