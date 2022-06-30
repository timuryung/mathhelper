import math
answers = []
def sin():
				tfunction = tfunction1
				if tfunction > 360 or tfunction < 0 and tfunction < 360:
					tfunction = tfunction % 360
				if tfunction < 0:
					tfunction = 360 + tfunction
				if tfunction > 0 and tfunction < 90:
					print('I четверть, +')
					answer = '1p'
					answers.append(answer)
				elif tfunction > 90 and tfunction < 180:
					print('II четверть, +')
					answer = '2p'
					answers.append(answer)
				elif tfunction > 180 and tfunction < 270:
					print('III четверть, -')
					answer = '3m'
					answers.append(answer)
				elif tfunction > 270 and tfunction < 360:
					print('IV четверть, -')
					answer = '4m'
					answers.append(answer)
				else:
					print('Данное значение находится на границе')
def cos():
				tfunction = tfunction2
				if tfunction > 360 or tfunction < 0 and tfunction < 360:
					tfunction = tfunction % 360
				if tfunction < 0:
					tfunction = 360 + tfunction
				if tfunction > 0 and tfunction < 90:
					print('I четверть, +')
					answer = '1p'
					answers.append(answer)
				elif tfunction > 90 and tfunction < 180:
					print('II четверть, -')
					answer = '2m'
					answers.append(answer)
				elif tfunction > 180 and tfunction< 270:
					print('III четверть, -')
					answer = '3m'
					answers.append(answer)
				elif tfunction > 270 and tfunction < 360:
					print('IV четверть, +')
					answer = '4p'
					answers.append(answer)
				else:
					print('Данное значение находится на границе')
def tgctg():
				tfunction = tfunction3
				if tfunction > 360 or tfunction < 0 and tfunction < 360:
					tfunction = tfunction % 360
				if tfunction < 0:
					tfunction = 360 + tfunction
				if tfunction > 0 and tfunction < 90:
					print('I четверть, +')
					answer = '1p'
					answers.append(answer)
				elif tfunction > 90 and tfunction < 180:
					print('II четверть, -')
					answer = '2m'
					answers.append(answer)
				elif tfunction > 180 and tfunction < 270:
					print('III четверть, +')
					answer = '3p'
					answers.append(answer)
				elif tfunction > 270 and tfunction < 360:
					print('IV четверть, -')
					answer = '4m'
					answers.append(answer)
				else:
					print('Данное значение находится на границе')
print('Math Helper v0.5 финальная версия от alexei-lg и timuryunuk2022')
choice3 = input("""1. Конвертер (радианы-градусы), (градусы-радианы) 
2. Определение четверти и знака тригонометрической функции
3. Определение периода тригонометрической функции (T)
4. Нахождение тригонометрических функций
5. Формулы приведения 
: """)
try:
	if choice3 == '1':
		while True:
			choice1 = input('1. Градусы в радианы; 2. Радианы в градусы: ')
			if choice1 == '1':
				degree = float(input('Введите значение угла в градусах: '))
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
				rad = float(input('Введите значение угла в радианах: '))
				result2 = str(rad * 180/ math.pi)
				print('Ответ: ' + result2 + ' градусов')
	if choice3 == '2':
		while True:
			functionchoice = input('sin - 1; cos - 2; tg или ctg - 3: ')
			if functionchoice == '1':
				tfunction1 = float(input('Введите значение синуса в градусах: '))
				sin()
			if functionchoice == '2':
				tfunction2 = float(input('Введите значение косинуса в градусах: '))
				cos()
			if functionchoice == '3':
				tfunction3 = float(input('Введите значение тангенса или котангенса в градусах: '))
				tgctg()
	if choice3 == '3':
		while True:
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
		while True:
			functionname = input('Введите название (sin, cos, tan, tg, ctg) ИЗВЕСТНОЙ ВАМ функции: ')
			functionnum = float(input('Введите значение ИЗВЕСТНОЙ ВАМ функции: (оно должно быть меньше 1, но больше чем -1): '))
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
	if choice3 == '5':
		while True:
			functionname1 = input('Введите название тригонометрической функции: (sin, cos, tan, tg, ctg): ')
			functionnum2 = float(input('Введите значение угла: '))	
			if (functionnum2 > 360) or (functionnum2 < 0):
				functionnum2 = functionnum2 % 360
			if functionname1 == 'sin':
				tfunction1 = functionnum2
				sin()
				answers1 = str(answers)
				answers2 = answers1.replace('[', '').replace(']', '').replace("'", '') 
				if answers2 == '1p':
					answer3 = 90 - functionnum2
					answer5 = str(answer3)
					functionnum3 = str(functionnum2)
					print(functionname1 + functionnum3)
					print('или ' + 'cos' + answer5)
				elif answers2 == '2p':
					answer3 = 180 - functionnum2
					answer5 = str(answer3)
					functionnum2  = functionnum2 - 90
					functionnum3 = str(functionnum2)
					print('cos' + functionnum3)
					print('или ' + 'sin' + answer5) 
				elif answers2 == '3m':
					answer3 = 270 - functionnum2
					answer5 = str(answer3)
					functionnum2 = functionnum2 - 180
					functionnum3 = str(functionnum2)
					print('-' + functionname1 + functionnum3)
					print('или ' + '-cos' + answer5)
				elif answers2 == '4m':
					answer3 = 360 - functionnum2
					answer5 = str(answer3)
					functionnum2 = functionnum2 - 270
					functionnum3 = str(functionnum2)
					print('-' + 'cos' + functionnum3)
					print('или ' + '-sin' + answer5)
				answers.clear()
			if functionname1 == 'cos':
				tfunction2 = functionnum2
				cos()
				answers1 = str(answers)
				answers2 = answers1.replace('[', '').replace(']', '').replace("'", '') 
				if answers2 == '1p':
					answer3 = 90 - functionnum2
					answer5 = str(answer3)
					functionnum3 = str(functionnum2)
					print(functionname1 + functionnum3)
					print('или ' + 'sin' + answer5)
				elif answers2 == '2m':
					answer3 = 180 - functionnum2
					answer5 = str(answer3)
					functionnum2  = functionnum2 - 90
					functionnum3 = str(functionnum2)
					print('-' + 'sin' + functionnum3) 
					print('или ' + '-cos' + answer5)
				elif answers2 == '3m':
					answer3 = 270 - functionnum2
					answer5 = str(answer3)
					functionnum2 = functionnum2 - 180
					functionnum3 = str(functionnum2)
					print('-' + functionname1 + functionnum3)
					print('или ' + '-sin' + answer5)
				elif answers2 == '4p':
					answer3 = 360 - functionnum2
					answer5 = str(answer3)
					functionnum2 = functionnum2 - 270
					functionnum3 = str(functionnum2)
					print('sin' + functionnum3)
					print('или ' + 'cos' + answer5)
				answers.clear()
			if functionname1 == 'tan':
				tfunction3 = functionnum2
				tgctg()
				answers1 = str(answers)
				answers2 = answers1.replace('[', '').replace(']', '').replace("'", '') 
				if answers2 == '1p':
					answer3 = 90 - functionnum2
					answer5 = str(answer3)
					functionnum3 = str(functionnum2)
					print(functionname1 + functionnum3)
					print('или ' + 'ctg' + answer5)
				elif answers2 == '2m':
					answer3 = 180 - functionnum2
					answer5 = str(answer3)
					functionnum2  = functionnum2 - 90
					functionnum3 = str(functionnum2)
					print('-' + 'ctg' + functionnum3) 
					print('или ' + '-' + 'tg' + answer5)
				elif answers2 == '3p':
					answer3 = 270 - functionnum2
					answer5 = str(answer3)
					functionnum2 = functionnum2 - 180
					functionnum3 = str(functionnum2)
					print(functionname1 + functionnum3)
					print('или ' + 'ctg' + answer5)
				elif answers2 == '4m':
					answer3 = 360 - functionnum2
					answer5 = str(answer3)
					functionnum2 = functionnum2 - 270
					functionnum3 = str(functionnum2)
					print('-' + 'ctg' + functionnum3)
					print('или ' + '-' + 'tg' + answer5)
				answers.clear()
			if functionname1 == 'tg':
				tfunction3 = functionnum2
				tgctg()
				answers1 = str(answers)
				answers2 = answers1.replace('[', '').replace(']', '').replace("'", '') 
				if answers2 == '1p':
					answer3 = 90 - functionnum2
					answer5 = str(answer3)
					functionnum3 = str(functionnum2)
					print(functionname1 + functionnum3)
					print('или ' + 'ctg' + answer5)
				elif answers2 == '2m':
					answer3 = 180 - functionnum2
					answer5 = str(answer3)
					functionnum2  = functionnum2 - 90
					functionnum3 = str(functionnum2)
					print('-' + 'ctg' + functionnum3) 
					print('или ' + '-' + 'tg' + answer5)
				elif answers2 == '3p':
					answer3 = 270 - functionnum2
					answer5 = str(answer3)
					functionnum2 = functionnum2 - 180
					functionnum3 = str(functionnum2)
					print(functionname1 + functionnum3)
					print('или ' + 'ctg' + answer5)
				elif answers2 == '4m':
					answer3 = 360 - functionnum2
					answer5 = str(answer3)
					functionnum2 = functionnum2 - 270
					functionnum3 = str(functionnum2)
					print('-' + 'ctg' + functionnum3)
					print('или ' + '-' + 'tg' + answer5)
			if functionname1 == 'ctg':
				tfunction3 = functionnum2
				tgctg()
				answers1 = str(answers)
				answers2 = answers1.replace('[', '').replace(']', '').replace("'", '') 
				if answers2 == '1p':
					answer3 = 90 - functionnum2
					answer5 = str(answer3)
					functionnum3 = str(functionnum2)
					print(functionname1 + functionnum3)
					print('или ' + 'tg' + answer5)
				elif answers2 == '2m':
					answer3 = 180 - functionnum2
					answer5 = str(answer3)
					functionnum2  = functionnum2 - 90
					functionnum3 = str(functionnum2)
					print('-' + 'tg' + functionnum3)
					print('или ' + '-' + 'ctg' + answer5) 
				elif answers2 == '3p':
					answer3 = 270 - functionnum2
					answer5 = str(answer3)
					functionnum2 = functionnum2 - 180
					functionnum3 = str(functionnum2)
					print(functionname1 + functionnum3)
					print('или ' + 'tg' + answer5)
				elif answers2 == '4m':
					answer3 = 360 - functionnum2
					answer5 = str(answer3)
					functionnum2 = functionnum2 - 270
					functionnum3 = str(functionnum2)
					print('-' + 'ctg' + functionnum3)
					print('или ' + '-' + 'tg' + answer5)
				answers.clear()
except:
	print('Ошибка!')


