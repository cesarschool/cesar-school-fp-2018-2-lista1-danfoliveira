## QUESTÃO 5 ##
# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule 
# quantos dias de vida um fumante perderá. Exiba o total em dias. 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    cigarros = int(input('digite a quantidade de cigarros fumados por dia '))
    anos = int(input('Digite a quantidade de anos pelos quais você fumou '))
    minutos = (cigarros * 10) * (anos * 365)
    dias = minutos // 1440
if __name__ == '__main__':
    main()
