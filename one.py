print('''Яку ОС ви використовуєте?
1 - windowsr
2 - windowsXP
3 - windowsVista''')
os = input('Введіть число, яке відповідає відповіді: ')
os = os.rstrip('\r')
if os == '1' :
    print('Ви вибрали Windows 7 ')
elif os == '2':
     print('Ви вибрали Windows XP ')
     
elif os == '3':
     print('Ви вибрали Windows Vista ')
else:
     print('Ми не можемо оприділити вашу ОС ')
