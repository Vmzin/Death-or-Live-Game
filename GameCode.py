
 
def startButton():
    history = input("E escuta um barulho vindo da sala a esquerda, ele abre a porta, e la está um elevador vermelhor com um placa dizendo START GAME, você deseja entrar?")
    
    if history.lower() in ["sim", "claro", "s"]:
        print("JOGO DA VIDA OU MORTE")
        print(" Você vai entrar em uma sala nela nela existira 2 ou 3 portas cada uma delas dara um desitno para você ")
    elif history.lower() in ["não", "n"]:
            history()

def game():
    h = ("Você está em um sala com 3 portas duas delas está escrito vida e uma morte qual você escolhera? ")
    
    print(f"{h}")
    
    choice = input("Opções: Esquerda, Direita, Frente. Escolha uma :")
    
    if choice.lower() in ["direita"]:
        print("GAME OVER")
        
    
    elif choice.lower() in ["esquerda"]: #choice 1
        print("Você está vivo")
        choice1()
    
    elif  choice.lower()  in ["frente"]: #choice 2
        print("Você está vivo")
        choice2()



def choice1():
    h2 = (" Agora você está em uma sala com duas portas esquerda e frente.")
    print(f"{h2}")
    
    
    choice = input("Qual você escolhe:") # choice 3
    if  choice.lower()  in ["frente"]:
        print("Você está vivo")
        choice3()
    
    if choice.lower() in ["esquerda"]:
        print("GAME OVER")
       
def choice2():
    h = ("Agora você está em uma sala com 3 portas, esquerda, direita e frente")
    
    print(f"{h}")
    
    choice = input("Qual você escolhe:")
    
    
    if  choice.lower()  in ["frente"]: #choice 4
        print("Você está vivo")
        choice4()
    elif choice.lower() in ["esquerda"]: #choice 5
    
        print("Você está vivo")
        choice5()
    if choice.lower() in ["direita"]:
        print("GAME OVER")

def choice3():
    h2 = (" você está em uma sala com duas portas esquerda e frente.")
    
    print(f"{h2}") 
    
    
    choice = input("Qual você escolhe:") 
    if  choice.lower()  in ["frente"]: # choice 6
        print("Você está vivo!")
        choice6
    
    if choice.lower() in ["esquerda"]:
        print("GAME OVER")

def choice4():
    h = (" Você está em uma sala com 3 portas, esquerda, direita e frente")
    
    print(f"{h}")
    choice = input("Qual você escolhe:")
    if choice.lower() in ["direita"]:
        print("GAME OVER")
    elif choice.lower() in ["frente"]:
        print("GAME OVER")
    elif  choice.lower()  in ["esquerda"]: 
        print("Você está vivo ")
        choice6 # choice 6

def choice5():
    h2 = (" você está em uma sala com duas portas esquerda e frente.")
    
    print(f"{h2}") 
    
    
    choice = input("Qual você escolhe:") 
    if  choice.lower()  in ["frente"]: # choice 6
        print("Você está vivo ")
        choice6
    
    if choice.lower() in ["esquerda"]:
        print("GAME OVER")

def choice6():
    h2 = (" você está em uma sala com duas portas esquerda e frente.")
    
    print(f"{h2}") 
    
    
    choice = input("Qual você escolhe:") 
    if  choice.lower()  in ["frente"]: 
        print("Você está GANHOU!!!!!!!!!! ")
    
    if choice.lower() in ["esquerda"]:
        print("Você PERDEUUUUUU, MAS FOI QUASE")
    
 
startButton()
game()
