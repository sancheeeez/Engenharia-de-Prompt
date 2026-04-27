import os
import shutil

# Caminho da pasta que você quer organizar
pasta = "arquivos"  # pode mudar para o caminho que quiser

# Percorre todos os arquivos da pasta
for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)

    # Verifica se é arquivo (ignora pastas)
    if os.path.isfile(caminho_arquivo):
        # Pega a extensão
        extensao = arquivo.split(".")[-1]

        # Cria a pasta da extensão (se não existir)
        pasta_extensao = os.path.join(pasta, extensao)
        os.makedirs(pasta_extensao, exist_ok=True)

        # Move o arquivo
        novo_caminho = os.path.join(pasta_extensao, arquivo)
        shutil.move(caminho_arquivo, novo_caminho)

print("Arquivos organizados com sucesso!")