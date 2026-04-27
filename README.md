Python
📖 Sobre o projeto

Este projeto demonstra, de forma prática, a importância da engenharia de prompt na geração de código com inteligência artificial.

A atividade consiste em evoluir um prompt simples até chegar em uma solução mais robusta e próxima de um cenário real de desenvolvimento, utilizando Python para validar e-mails.

🎯 Objetivo

Mostrar como a qualidade de um prompt influencia diretamente na qualidade da resposta gerada por IA.

⚙️ Etapas do processo
🔹 1. Prompt inicial (vago)

Um prompt simples foi utilizado:

Faça um código para validar e-mail

Resultado: código básico e pouco confiável.

🔹 2. Problema identificado

A solução inicial apenas verificava a presença do caractere “@”, o que não é suficiente para validar um e-mail corretamente.

🔹 3. Refinamento do prompt

Foi aplicada a Equação do Prompt:

Persona: Desenvolvedor Python experiente
Contexto: Sistema de cadastro
Restrições: Uso de regex, código limpo, retorno booleano
🔹 4. Resultado melhorado
import re

def validar_email(email):
    padrao = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(padrao, email))
🔹 5. Versão final (refinada)
import re

def validar_email(email: str) -> bool:
    if not isinstance(email, str):
        return False

    email = email.strip()
    padrao = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'

    return bool(re.match(padrao, email))
🚀 Tecnologias utilizadas
Python 🐍
Regex (Expressões Regulares)
Conceitos de Engenharia de Prompt
💡 Aprendizados
Prompts vagos geram respostas fracas
Prompts estruturados geram soluções mais completas
O refinamento iterativo melhora significativamente os resultados
Engenharia de prompt é essencial para obter respostas mais precisas da IA
