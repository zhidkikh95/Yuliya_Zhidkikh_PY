h=int(input('Введите ваш рост, см: '))
w=int(input('Введите ваш вес,кг: '))
bmi=w/(h/100)**2
print('Ваш индекс массы тела: ', round(bmi))
scale = '20' + "=" * (round(bmi)-20) + "|" + "="*(50 -round(bmi)) + "50"
print(scale)