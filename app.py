# Lista
campos_endereco = ["Plano Piloto", "Asa Sul", "SQS 210", "Bloco A", "Apartamento 404"]

# delimitador
delimitador = ", "

# juntar os valores em uma única variável
endereco = delimitador.join(campos_endereco)

# exibe a variável na tela
print(f"Endereço: {endereco}.")