import random

print("Bonjour & bienvenue 👋\n")
user_name = input("Saisissez votre nom d'utilisateur : ")
user_rules = input("Souhaitez-vous voir les règles du jeu ? [Y/N] ").strip().lower()

if user_rules == "y":
    print("Les règles sont simples :")
    print("- Facile : Un nombre aléatoire entre 1 et 50 va être tiré, vous avez 20 essais pour le trouver")
    print("- Normal : Un nombre aléatoire entre 1 et 100 va être tiré, vous avez 15 essais pour le trouver")
    print("- Difficile : Un nombre aléatoire entre 1 et 200 va être tiré, vous avez 10 essais pour le trouver")
    print("- Impossible : Un nombre aléatoire entre 1 et 200 va être tiré, vous avez 5 essais pour le trouver")

user_level = input("Choisissez une difficulté : [Facile/Normal/Difficile/Impossible]").strip().lower()

ready_game = input("Êtes-vous prêt à jouer ? [Y/N] ").strip().lower()

if ready_game == "n":
    print("Une prochaine fois peut-être ! 😜")
else:
    random_number = random.randint(1, 100)
    tentative = 0

    for _ in range(20):
        try:
            user_answer = int(input("Saisissez votre réponse : "))
            tentative += 1

            if user_answer < random_number:
                print(f"C'est + que {user_answer} !\n")
            elif user_answer > random_number:
                print(f"C'est - que {user_answer} !\n")
            else:
                print("🌟 Félicitations ! Vous avez gagné ! 🌟")
                break
            print(f"Vous avez fait {tentative} tentative(s).")
        except ValueError:
            print("Veuillez entrer un nombre valide.\n")

    else:
        print(f"Dommage ! Le nombre à trouver était {random_number}.")
