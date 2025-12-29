tipos_mensagens = ["trabalho", "pessoal", "spam"]

quantidade_trabalho = 0
quantidade_pessoal = 0
quantidade_spam = 0
remetentes_importantes = []

mensagens_validas = 0

quantidade_mensagens_recebidas = input("Quantidade de mensagens recebidas: ")
quantidade_mensagens_recebidas = quantidade_mensagens_recebidas.strip()
quantidade_mensagens_recebidas = int(quantidade_mensagens_recebidas)


for quantidade in range(quantidade_mensagens_recebidas):

    nome_remetente = input("Nome do remetente: ")
    nome_remetente = nome_remetente.title().strip()

    texto_mensagem = input("Texto: ")
    texto_mensagem = texto_mensagem.strip()

    tipo_mensagem = input("Tipo da mensagem: ")
    tipo_mensagem = tipo_mensagem.lower().strip()

    if tipo_mensagem not in tipos_mensagens:
        print("mensagem inválida!".upper())
        continue
    else:
        mensagens_validas += 1

        if tipo_mensagem == "spam":
            quantidade_spam += 1

        elif tipo_mensagem == "pessoal":
            quantidade_pessoal += 1
            if texto_mensagem != "":
                remetentes_importantes.append(nome_remetente)        
        else:
            quantidade_trabalho += 1
            remetentes_importantes.append(nome_remetente)


calculo_prioridade = (quantidade_trabalho / mensagens_validas) * 100

if calculo_prioridade >= 60:
    prioridade_dia = "alta"
elif calculo_prioridade >= 30 and calculo_prioridade < 60:
    prioridade_dia = "média"
else:
    prioridade_dia = "baixa"

mensagem_final = f""" 

Resumo do dia:
Mensagens válidas: {mensagens_validas}
Trabalho: {quantidade_trabalho}
Pessoal: {quantidade_pessoal}
Spam: {quantidade_spam}
Remetentes importantes: {remetentes_importantes}
Prioridade do dia: {prioridade_dia}
"""

print(mensagem_final)
