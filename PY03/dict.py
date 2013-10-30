file = open('dict.txt', 'a')

while True:
    a = input('comp: ')
    b = input('mnemonic: ')
    output = '\'' + a + '\': \'' + b + '\',\n'
    file.write(output)
