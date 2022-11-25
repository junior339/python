#no python assim como em c existe o local de memoria da variavel em questao.
##mas como eu faço para acessar esse endereço de memoria
##pelo id
nome="junior"
nome1="junior"
print(id(nome))
print(id(nome1))
#1647397977392
#1647397977392
#note que os valores de memorias sao os mesmos 
#pq isso acontece 
##pq o py nao e burro ele sabe que dentro da variavel
##tem o mesmo valor mas e se eu fizer diferente
nome="junior"
nome1="santos"
print(id(nome))
print(id(nome1))
#2372487232816
#2372488801520

#o valor fica diferente
##funcao id()

