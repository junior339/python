'''
constante = variaveis que nao devem mudar 
no python nao existe constante
par definir uma constante 
existe uma convenção de usar 
letras maiusculas
LOCAL="balsa nova"

'''
velocidade =60
local_carro=100

RADAR_1=60
LOCAL_1=100
RADAR_RANGE=1 #a distancia que o radar pega

limite= velocidade>RADAR_1 
multa=local_carro==(LOCAL_1-RADAR_RANGE)or local_carro==(LOCAL_1) or local_carro==(LOCAL_1+RADAR_RANGE)
limite= velocidade>RADAR_1 and multa

if limite:
    print('passou do radar 1')
    if multa:
       print('o carro foi multado em radar 1 ') 
else:
    print("o carro nao foi multado ")
    #constantes e retribuiçoes de variaveis
    #de parametro do meu if atraves de variaveis