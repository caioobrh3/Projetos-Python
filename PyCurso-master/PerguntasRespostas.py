perguntas = {
    "pergunta 1 ": {
        "pergunta":"Quanto é 2+2 ?",
        "Respostas" : {"a": "1", "b": "4", "c": "5", },
        "resposta_certa": "b",
    },
    "pergunta 2 ": {
        "pergunta": "Quanto é 3*2 ?",
        "Respostas": {"a": "4", "b": "10", "c": "6", },
        "resposta_certa": "c",
    },
    "pergunta 3 ": {
        "pergunta": "Quanto é 3*5 ?",
        "Respostas": {"a": "4", "b": "15", "c": "30", },
        "resposta_certa": "b",
    },
    "pergunta 4 ": {
        "pergunta": "Quanto é 2*5 ?",
        "Respostas": {"a": "1", "b": "10", "c": "6", },
        "resposta_certa": "b",
    },
}
print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f"{pk}:{pv['pergunta']}")
    print('Respostas: ')
    for rk , rv in pv ['Respostas'].items():
        print(f'[{rk}]:{rv}')
    resposta_usuario = input("Sua Resposta")

    if resposta_usuario == pv['resposta_certa']:
        print("Acertou!!!")
        respostas_certas += 1
    else:
        print("Errouuuu !!!")
    print()

qtd_perguntas = len(perguntas)
pct_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {pct_acerto}%.')