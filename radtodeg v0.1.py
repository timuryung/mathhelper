import math
print('Math Helper v 0.1')
choice3 = input("""1. Конвертер (радианы-градусы), (градусы-радианы) 
2. Определение четверти и знака тригонометрической функции
: """)
try:
	if choice3 == '1':
		choice1 = input('1. Градусы в радианы; 2. Радианы в градусы: ')
		if choice1 == '1':
			degree = int(input('Введите значение угла в градусах: '))
			choice = input('Если хотите ответ без числа π напишите 1, если с числом π напишите 2: ')
			if choice == '1':
				result = str(degree/180)
				print('Ответ: ' + result + 'π' +  ' радиан' )
			elif choice == '2':
				result1 = str(degree/180 * math.pi)
				print('Ответ: ' + result1 + ' радиан')
			else:
				print('Неверный выбор ')
		elif choice1 == '2':
			rad = int(input('Введите значение угла в радианах: '))
			result2 = str(rad * 180/ math.pi)
			print('Ответ: ' + result2 + ' градусов')
	if choice3 == '2':
		functionchoice = input('sin - 1; cos - 2; tg или ctg - 3: ')
		if functionchoice == '1':
			tfunction = int(input('Введите значение синуса в градусах: '))
			if tfunction > 360 or tfunction < 0 and tfunction < 360:
				tfunction = tfunction % 360
			if tfunction < 0:
				tfunction = 360 + tfunction
			if tfunction > 0 and tfunction < 90:
				print('I четверть, +')
			elif tfunction > 90 and tfunction < 180:
				print('II четверть, +')
			elif tfunction > 180 and tfunction < 270:
				print('III четверть, -')
			elif tfunction > 270 and tfunction < 360:
				print('IV четверть, -')
			else:
				print('Данное значение находится на границе')
		if functionchoice == '2':
			tfunction = int(input('Введите значение косинуса в градусах: '))
			if tfunction > 360 or tfunction < 0 and tfunction < 360:
				tfunction = tfunction % 360
			if tfunction < 0:
				tfunction = 360 + tfunction
			if tfunction > 0 and tfunction < 90:
				print('I четверть, +')
			elif tfunction > 90 and tfunction < 180:
				print('II четверть, -')
			elif tfunction > 180 and tfunction< 270:
				print('III четверть, -')
			elif tfunction > 270 and tfunction < 360:
				print('IV четверть, +')
			else:
				print('Данное значение находится на границе')
		if functionchoice == '3':
			tfunction = int(input('Введите значение тангенса или котангенса в градусах: '))
			if tfunction > 360 or tfunction < 0 and tfunction < 360:
				tfunction = tfunction % 360
			if tfunction < 0:
				tfunction = 360 + tfunction
			if tfunction > 0 and tfunction < 90:
				print('I четверть, +')
			elif tfunction > 90 and tfunction < 180:
				print('II четверть, -')
			elif tfunction > 180 and tfunction < 270:
				print('III четверть, +')
			elif tfunction > 270 and tfunction < 360:
				print('IV четверть, -')
			else:
				print('Данное значение находится на границе')
except:
	print('Ошибка!')

