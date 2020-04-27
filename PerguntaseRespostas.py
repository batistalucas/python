perguntas = {
    'Pergunta 1': {
        'p': 'Quanto é 1x2',
        'respostas': {'a': '5', 'b': '6', 'c': '2', 'd': '1'},
        'respCerta': 'c',
    },
    'Pergunta 2': {
        'p': 'Quanto é 3x5',
        'respostas': {'a': '5', 'b': '15', 'c': '21', 'd': '9'},
        'respCerta': 'b',
    },
    'Pergunta 3': {
        'p': 'Quanto é 8/2',
        'respostas': {'a': '7', 'b': '4', 'c': '9', 'd': '1'},
        'respCerta': 'b',
    },
}
acertos=0

for pk, pv in perguntas.items():
    print(f'{pk}) {pv["p"]}?')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] {rv}')
    respostaUsuario=input('Digite a resposta: ')
    if respostaUsuario == pv['respCerta']:
        print('Você acertou, parabéns.')
        acertos+=1
    else:
        print('Resposta errada.')
    print()

rend=(acertos/len(perguntas)*100)

print(f'Você acertou {acertos} resposta(s) de um total de {len(perguntas)}.')
print(f'Seu rendimento foi de {rend:.1f}%')