#try exept
numero_str=input(
    'vou dobrer seu numero, digite:'

)
'''if numero_str.isdigit():
    numero_float=float(numero_str)
    print(f'o dobro e de {numero_float * 2}')
else:
    print('voce nao digitou um numero')  '''

# o if no evita erros que no  pyhon sao chamedas de exceçoes  
# 
try:
    numero_float=float(numero_str)
    print(f'o dobro e de {numero_float * 2}')

except:    
    print('voce nao digitou um numero') 
    #fail fast onde ele acha o erro ele pula imediatamente 
    #par o exept