print('CALCULADORA')
print('+ adição')
print('- subtração')
print('* multiplicação')
print('/ divisão')
print('Pressione outra tecla para sair')
print(35*'-')

op=input('Qual operação deseja realizar?')
if (op == '+') or (op == '-') or (op =='*') or (op =='/'):
   x=int(input('Digite o primeiro valor:'))
   y=int(input('Digite o segundo valor:'))
if (op=='+'):
   res=x+y/
   print('Resultado:{} + {} = {}'.format(x,y,res))
elif(op=='-'):
    res= x-y
    print('Resultado:{} - {} = {}'.format(x, y, res))
elif(op=='*'):
    res = x*y
    print('Resultado:{} * {} = {}'.format(x, y, res))
elif(op=='/'):
    res = x/y
    print('Resultado:{} / {} = {}'.format(x, y, res))
else:
   print('Operação inválida')

print('Encerrando o programa...')
