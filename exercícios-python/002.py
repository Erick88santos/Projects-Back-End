# Sequência de Fibonacci 

## **Python** 🐍 


print('*'*30)

print('Sequência de Fibonacci')

print('*'*30)

n = int(input('Insira um numero para gerar a sequência de Fibonnaci: '))

t1 = 0

t2 = 1

t3 = ""

print('~'*30)

print('{} -> {}'.format(t1, t2), end = '')

cont = 3

while cont <= n:

    t3 = t1 + t2

    print('-> {}'.format(t3), end = '  ')

    t1 = t2

    t2 = t3

    cont += 1

if(t3 == cont):
    print('Esse número EXISTE na sequência de Fibonacci')
else:
    print('Esse número NÃO EXISTE na sequência de Fibonacci')

print('-> FIM')
