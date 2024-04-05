def happy():
    print('Счастливый билетик')
    a = int(input('Введите первое число и нажмите Enter: '))
    b = int(input('Введите второе число и нажмите Enter: '))
    c = int(input('Введите третье число и нажмите Enter: '))
    aa = int(input('Введите четвёртое число и нажмите Enter: '))
    bb = int(input('Введите пятое число и нажмите Enter: '))
    cc = int(input('Введите шестое число и нажмите Enter: '))
    if a + b + c != aa + bb + cc:
        print('билетик обычный')
    else:
        print('ЭТО СЧАСТЛИВЫЙ БИЛЕТИК!')



happy()
