import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('http://omdbapi.com/?apikey=3a0eac0f&t=' + titulo)
        dic_filme = json.loads(req.text)
        return dic_filme
    except:
        print("Erro de conexão")
        return None

def printar_detalhes(dic_filme):
    print('Título:', dic_filme['Title'])
    print('Ano:', dic_filme['Year'])
    print('Diretor:', dic_filme['Director'])
    print('Atores:', dic_filme['Actors'])
    print('Nota:', dic_filme['imdbRating'])
    print('Premios:', dic_filme['Awards'])
    print('Poster:', dic_filme['Poster'])
    print('')



sair = False

while not sair:
    op = input('Digite o nome do filme para pesquisar ou SAIR para encerrar: ')
    if op == 'SAIR':
        print('Saindo...')
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print(filme['Error'])
        else:
            printar_detalhes(filme)






