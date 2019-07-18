import os
from baqueiro_utils import *


def main():
    qtd_processos = int(input('Digite quantos processos estão em execução:\n' \
                               '>>> '))
    qtd_tipos_recursos = int(input('Digite quantos tipos de recursos necessitará cada processo:\n' \
                               '>>> '))
    recursos_totais = get_recursos_totais(qtd_tipos_recursos)
    matriz_alocados = get_matriz_alocados(qtd_processos, qtd_tipos_recursos)
    recursos_alocados = get_vetor_recursos_alocados(matriz_alocados)
    recursos_disponiveis = get_vetor_recursos_disponiveis(recursos_totais, recursos_alocados)
    matriz_recursos_necessarios = get_matriz_recursos_necessarios(qtd_processos, qtd_tipos_recursos)
    input('Pressione Enter para continuar.....')
    os.system('clear')
    imprimir_os_dados(recursos_totais, matriz_alocados, recursos_alocados, recursos_disponiveis, matriz_recursos_necessarios)
    algoritmo_banqueiro(qtd_processos, qtd_tipos_recursos, recursos_disponiveis, matriz_recursos_necessarios, matriz_alocados)


if __name__ == '__main__':
    main()