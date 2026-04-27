import random
import time

# ----- CONFIG -----
LIMITE_CRITICO = 80


# ----- FUNÇÕES -----
def coletar_dado():
    """Simula leitura de um valor (ex: temperatura)"""
    return random.randint(50, 100)


def verificar_critico(valor):
    """Verifica se o valor atingiu nível crítico"""
    return valor >= LIMITE_CRITICO


def enviar_alerta(valor):
    """Simula envio de alerta"""
    print("\n🚨 ALERTA CRÍTICO!")
    print(f"Valor atingido: {valor}")
    print("Ação necessária imediatamente!\n")


def monitorar():
    """Loop principal do sistema"""
    while True:
        valor = coletar_dado()
        print(f"Valor atual: {valor}")

        if verificar_critico(valor):
            enviar_alerta(valor)

        time.sleep(2)  # espera 2 segundos


# ----- EXECUÇÃO -----
monitorar()