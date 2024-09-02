import random
from colorama import Fore, Style, init

init(autoreset=True)

def quiz(perguntas):
    pontuacao = 0
    perguntas = random.sample(perguntas, 2) #SORTEAR A QUANTIDADE DE PERGUNTAS

    for pergunta, opcoes, resposta_correta in perguntas:
        print(Fore.MAGENTA + Style.BRIGHT + pergunta)
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{Fore.WHITE}{i}. {opcao}")

        try:
            resposta_usuario = int(input(Fore.MAGENTA + "Escolha a opção correta (1, 2 OU 3): "))
            if resposta_usuario == resposta_correta:
                print(Fore.GREEN + "Resposta correta!\n")
                pontuacao += 1
            else:
                print(Fore.RED + f"Resposta incorreta. A resposta correta era a opção {resposta_correta}.\n")
        except ValueError:
            print(Fore.RED + "Entrada inválida. Você perdeu esse ponto\n")

    print(Fore.YELLOW + f"Fim do jogo! Sua pontuação final é: {pontuacao}")

def main():
    perguntas_e_respostas = [
        ("IPv4: Quantas classes de endereçamento IP existem no IPv4?", ["Tres", "Quatro", "Cinco"], 3),
        ("IPv4: Qual é a característica principal do IPv4 em relação ao número de endereços disponíveis?", ["Possui um número limitado de endereços", "Suporta endereços de 128 bits", "Foi projetado exclusivamente para redes locais"], 1),
        ("Mascara de Rede: Qual é a máscara de rede padrão para a classe C?", ["255.255.0.0", "255.0.0.0", "255.255.255.0"], 3),
        ("Rede e Host: Em um endereço IPv4, o que a parte de rede identifica?", [" O dispositivo específico na rede", "A rede à qual o dispositivo pertence", "A sub-rede dentro da rede principal"], 2),
        
        #PERGUNTAS
    ]

    quiz(perguntas_e_respostas)

if __name__ == "__main__":
    main()
