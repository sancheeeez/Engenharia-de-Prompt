import requests

def consultar_cep(cep):
    try:
        # URL da API
        url = f"https://viacep.com.br/ws/{cep}/json/"

        resposta = requests.get(url)

        # Verifica se a requisição deu certo
        if resposta.status_code != 200:
            print("Erro na requisição.")
            return

        dados = resposta.json()

        # Verifica se o CEP existe
        if "erro" in dados:
            print("CEP inválido!")
            return

        # Exibe formatado
        print("\n📍 Endereço encontrado:")
        print(f"Rua: {dados.get('logradouro')}")
        print(f"Bairro: {dados.get('bairro')}")
        print(f"Cidade: {dados.get('localidade')}")
        print(f"Estado: {dados.get('uf')}")

    except requests.exceptions.RequestException:
        print("Erro de conexão! Verifique sua internet.")

# Entrada do usuário
cep = input("Digite o CEP (somente números): ")

consultar_cep(cep)