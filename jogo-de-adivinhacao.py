import random

def guessing_game():
    """
    Jogo de adivinhação com bônus de tentativas extras.
    
    Regras:
    - O jogador tem 5 tentativas iniciais
    - Cada vez que chegar muito perto (diferença de 1), ganha +1 tentativa
    - Objetivo: descobrir um número entre 1 e 10
    """
    secret_number = random.randint(1, 10)
    max_attempts = 5
    attempts_used = 0
    guessed = False
    
    print("🎮 Bem-vindo ao Jogo de Adivinhação!")
    print("Descubra o número secreto entre 1 e 10")
    print(f"Você começa com {max_attempts} tentativas\n")
    
    while attempts_used < max_attempts:
        attempts_used += 1
        remaining = max_attempts - attempts_used
        
        try:
            guess = int(input(f"Tentativa {attempts_used}: Digite um número entre 1 e 10: "))
            
            # Validação de entrada
            if guess < 1 or guess > 10:
                print("❌ Por favor, digite um número entre 1 e 10!\n")
                attempts_used -= 1  # Não conta como tentativa
                continue
            
            # Verifica se acertou
            if guess == secret_number:
                guessed = True
                print(f"🎉 Parabéns! Você acertou! O número era {secret_number}")
                print(f"Você usou {attempts_used} tentativa(s)")
                break
            
            # Verifica se está muito perto (bônus de tentativa)
            difference = abs(guess - secret_number)
            if difference == 1:
                max_attempts += 1
                print(f"🔥 Muito perto! Você ganhou +1 tentativa!")
                print(f"   Agora você tem {max_attempts - attempts_used} tentativa(s) restante(s)\n")
            else:
                # Dica de direção
                if guess < secret_number:
                    direction = "MAIOR"
                else:
                    direction = "MENOR"
                
                remaining = max_attempts - attempts_used
                print(f"❌ Errado! Tente um número {direction}")
                print(f"   Tentativas restantes: {remaining}\n")
        
        except ValueError:
            print("❌ Entrada inválida! Digite um número inteiro\n")
            attempts_used -= 1  # Não conta como tentativa
    
    # Resultado final
    if not guessed:
        print(f"\n😢 Game Over! Você esgotou todas as tentativas")
        print(f"O número secreto era: {secret_number}")
    
    # Pergunta se quer jogar novamente
    while True:
        replay = input("\nDeseja jogar novamente? (s/n): ").lower()
        if replay == 's':
            print("\n" + "="*50 + "\n")
            guessing_game()
            break
        elif replay == 'n':
            print("Obrigado por jogar! 👋")
            break
        else:
            print("Digite 's' para sim ou 'n' para não")

# Executa o jogo
if __name__ == "__main__":
    guessing_game()
