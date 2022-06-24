import math
print('Math Helper v0.3 beta')
choice3 = input("""1. Конвертер (радианы-градусы), (градусы-радианы) 
2. Определение четверти и знака тригонометрической функции
3. Определение периода тригонометрической функции (T)
4. Нахождение тригонометрических функций
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
	if choice3 == '3':
		tfunction1 = input('Введите функцию: ')
		if 'sin' or 'cos' or 'tan' or 'tg' or 'ctg' in tfunction1:
			if "(" in tfunction1:
				tfunction2 = (tfunction1.partition("(")[2])
			if "sin" in tfunction1:
				tfunction2 = (tfunction1.partition("sin")[2])
			tfunction3 = tfunction2.split('x')[0]
			if '(' in tfunction3:
				tfunction3 = tfunction3.replace('(', '')
			if '-' in tfunction3:
				tfunction3 = tfunction3.replace('-', '')
			if 'sin' in tfunction1:
				result2 = 2 * math.pi / int(tfunction3)
				print('Период (T): ' + str(result2))
			if 'cos' in tfunction1:
				result2 = 2 * math.pi / int(tfunction3)
				print('Период (T): ' + str(result2))
			if 'tan' in tfunction1:
				result2 = math.pi / int(tfunction3)
				print('Период (T): ' + str(result2))
			if 'tg' in tfunction1:
				result2 = math.pi / int(tfunction3)
				print('Период (T): ' + str(result2))
			if 'ctg' in tfunction1:
				result2 = 2 * math.pi / int(tfunction3)
				print('Период (T): ' + str(result2))
		else:
			print('Неверная функция!')
	if choice3 == '4':
		functionname = input('Введите название (sin, cos, tan, tg, ctg) ИЗВЕСТНОЙ ВАМ функции: ')
		functionnum = float(input('Введите значение ИЗВЕСТНОЙ ВАМ функции: '))
		quorternum = input('Введите номер четверти РИМСКИМИ ЦИФРАМИ в которой лежит угол (вы можете узнать его через определитель четверти и знака тригонометрических функций: ')

		if functionname == 'sin':
			if functionnum < 0 and quorternum == 'I':
				print('Неверная четверть!')
				exit()
			if functionnum < 0 and quorternum == 'II':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'III':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'IV':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'IIII':
				print('Неверная четверть!')
				exit()
			result5 = math.sqrt(1-functionnum**2)
			result5 = float(result5)
			if quorternum == 'I':
				print('Косинус: ' + str(result5))
			if quorternum == 'II':
				result5 = float(result5 * (-1))
				print('Косинус: ' + str(result5))
			if quorternum == 'III':
				result5 = float(result5 * (-1))
				print('Косинус: ' + str(result5))
			if quorternum == 'IV':
				print('Косинус: ' + str(result5))
			if quorternum == 'IIII':
				print('Косинус: ' + str(result5))
			tangents = functionnum / result5
			print('Тангенс: ' + str(tangents))
			cotangents = result5 / functionnum
			print('Котангенс: ' + str(cotangents))
		if functionname == 'cos':
			if functionnum < 0 and quorternum == 'I':
				print('Неверная четверть!')
				exit()
			if functionnum < 0 and quorternum == 'IV':
				print('Неверная четверть!')
				exit()
			if functionnum < 0 and quorternum == 'IIII':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'II':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'III':
				print('Неверная четверть!')
				exit()
			result16 = math.sqrt(1-functionnum**2) #синус
			result16 = float(result16)
			if quorternum == 'I':
				print('Синус: ' + str(result16))
			if quorternum == 'II':
				result16 = float(result16)
				print('Синус: ' + str(result16))
			if quorternum == 'III':
				result16 = float(result16 * (-1))
				print('Синус: ' + str(result16))
			if quorternum == 'IV':
				print('Синус: ' + str(result16 * (-1)))
			if quorternum == 'IIII':
				print('Синус: ' + str(result16 * (-1)))
			cotangents1 = functionnum / result16
			tangents1 = result16 / functionnum
			print('Тангенс: ' + str(tangents1))
			print('Котангенс: ' + str(cotangents1))
		if functionname == 'tan':
			if functionnum < 0 and quorternum == 'I':
				print('Неверная четверть!')
				exit()
			if functionnum < 0 and quorternum == 'III':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'II':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'IIII':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'IV':
				print('Неверная четверть!')
				exit()
			result20 = 1/functionnum #котангенс
			result21 = 1/math.sqrt(1+functionnum**2) #косинус
			if quorternum == 'I':
				print('Косинус: ' + str(result21))
			if quorternum == 'II':
				result21 = float(result21 * (-1))
				print('Косинус: ' + str(result21))
			if quorternum == 'III':
				result21 = float(result21 * (-1))
				print('Косинус: ' + str(result21))
			if quorternum == 'IV':
				print('Косинус: ' + str(result21))
			if quorternum == 'IIII':
				print('Косинус: ' + str(result21))
			result22 = functionnum * result21 #синус
			print('Синус: ' + str(result22))
			print('Котангенс: ' + str(result20))	
		if functionname == 'tg':
			if functionnum < 0 and quorternum == 'I':
				print('Неверная четверть!')
				exit()
			if functionnum < 0 and quorternum == 'III':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'II':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'IIII':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'IV':
				print('Неверная четверть!')
				exit()
			result20 = 1/functionnum #котангенс
			result21 = 1/math.sqrt(1+functionnum**2) #косинус
			if quorternum == 'I':
				print('Косинус: ' + str(result21))
			if quorternum == 'II':
				result21 = float(result21 * (-1))
				print('Косинус: ' + str(result21))
			if quorternum == 'III': 
				result21 = float(result21 * (-1))
				print('Косинус: ' + str(result21))
			if quorternum == 'IV':
				print('Косинус: ' + str(result21))
			if quorternum == 'IIII':
				print('Косинус: ' + str(result21))
			result22 = functionnum * result21 #синус
			print('Синус: ' + str(result22))
			print('Котангенс: ' + str(result20))	
		if functionname == 'ctg':
			if functionnum < 0 and quorternum == 'I':
				print('Неверная четверть!')
				exit()
			if functionnum < 0 and quorternum == 'III':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'II':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'IIII':
				print('Неверная четверть!')
				exit()
			if functionnum > 0 and quorternum == 'IV':
				print('Неверная четверть!')
				exit()
			result23 = 1/functionnum #тангенс
			result24 = 1/math.sqrt(1+result23**2) #косинус
			if quorternum == 'I':
				print('Косинус: ' + str(result24))
			if quorternum == 'II':
				result24 = float(result24 * (-1))
				print('Косинус: ' + str(result24))
			if quorternum == 'III':
				result24 = float(result24 * (-1))
				print('Косинус: ' + str(result24))
			if quorternum == 'IV':
				print('Косинус: ' + str(result24))
			if quorternum == 'IIII':
				print('Косинус: ' + str(result24))
			result25 = result23 * result24
			print('Синус: ' + str(result25))
			print('Тангенс: ' + str(result23))

except Exception as e:
	print(e)


