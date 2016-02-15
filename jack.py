print('Поиграем в очко?')
count = 0
koloda = [6,7,8,9,10,2,3,4,11]*4
import random
random.shuffle(koloda)
while True:
    choice = input('Будете брати карту? y/n\n')
	if choice == 'y':
	    current = koloda.pop()
		print('Вам попоалась карта %d' %current)
		count += current
		if count > 21:
		    print('Пробачте, але ви програли')
			break
		elif count == 21:
		    print('Поздоровляю ви набрали 21!')
			break
		else:
		    print('У вас %d очків.' %count)
	elif choice == 'n':
        print('У вас %d очків і ви закінчили гру' %count)
        break 
 
 
 print("До нових зустрічей")
 
