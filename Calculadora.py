title = {
    1: '_________     _____  .____   _________  ____ ___.____       _____  ________   ________ __________    _____   ',
    2: '\_   ___ \   /  _  \ |    |  \_   ___ \|    |   \    |     /  _  \ \______ \  \_____  \ \______   \  /  _  \  ',
    3: '/    \  \/  /  /_\  \|    |  /    \  \/|    |   /    |    /  /_\  \ |    |  \  /   |   \|       _/ /  /_\  \ ',
    4: '\     \____/    |    \    |__\     \___|    |  /|    |___/    |    \|    `   \/    |    \    |   \/    |    \ ',
    5: ' \______  /\____|__  /_______ \______  /______/ |_______ \____|__  /_______  /\_______  /____|_  /\____|__  / ',
    6: '        \/         \/        \/      \/                 \/       \/        \/         \/       \/         \/ '
}

tabla_hexadecimal = {
    '0':0, '1':1, '2':2, '3':3, 
    '4':4, '5':5, '6':6, '7':7, 
    '8':8, '9':9, 'A':10, 'B':11, 
    'C':12, 'D':13, 'E':14, 'F':15,
    'a':10, 'b':11, 'c':12, 'd':13,
    'e':14, 'f':15
}

for i in range (1,6):
    print(title[i])

flag_control = True

while(flag_control == True):
    print('\n1. Convertir de hexadecimal a decimal \n2. Convertir de decimal a hexadecimal \n3. Salir')
    op = input('U:\> ')

    if(op == '1'):
        print('\n--------------------HEXADECIMAL A DECIMAL-------------------- \nIngrese el valor a convertir:')
        valueHex = input('U:\> ')
        valueDec = 0
        tamExp = len(valueHex)-1
        for digito in valueHex:
            valueDec += (tabla_hexadecimal[digito])*(16**tamExp)
            tamExp -= 1
        print('\n------------------------------------------------------------- \nEl valor ingresado equivale a: '+str(valueDec)+'\n-------------------------------------------------------------\n')
    elif(op == '2'):
        pass
    elif(op == '3'):
        flag_control = False
    else:
        print('\n¡VALOR INGRESADO INVALIDO! POR FAVOR VUELVA A INTENTAR\n')