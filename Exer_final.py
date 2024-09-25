## Gerenciamento de Jogadores e Times

"""Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

- Adicionar um time
- Remover um time
- Listar times
- Adicionar jogador em um time
- Remover jogador de um time
- Listar jogadores de um time
1. A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
2. A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
3. A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
4. A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
5. A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
6. A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.
"""

teams = {}
done = False

# Função para listar times
def print_teams():
    print("Listed Teams")
    for i, team in enumerate(teams.values()):
        print(f"{i+1} . {team['name']} ({len(team['Players'])} players)")

# Função para listar jogadores de um time
def print_players(team):
    print(f"Players of the team {team['name']}")
    for i, player in enumerate(team['players']):
        print(f"{i+1} . {player}")


while not done:
    print("What you wanna do?")
    print("1 - Add a team")
    print("2 - Remove a team")
    print("3 - List the teams")
    print("4 - Add a player to the team")
    print("5 - Remove a player from a team")
    print("6 - List the players of a team")
    print("7 - Leave")

    choice = int(input(">"))
    if choice == 1:
        addTeam = input("Whats the team name?\n")
        teams[addTeam] = {'name' : addTeam, 'Players' : []}
        print("The team", addTeam, "was included")

    elif choice == 2:
        print_teams()
        team_num = int(input("Whats the team number that you want to remove?\n"))
        if team_num <= len(teams):
            addTeam = list(teams.keys())[team_num - 1 ]
            del teams[addTeam]
            print("The team was removed")
        else:
            print("Invalid number")

    elif choice == 3:
        print_teams()
    elif choice == 4:
        print_teams()
        team_num = int(input("Whats the team number you want to add a player?\n"))
        if team_num <= len(teams):
            addTeam = list(teams.keys())[team_num - 1 ]
            playerName = input("Whats the player name?\n")
            teams[addTeam]['Players'].append(playerName)
            print("Player included")
        else:
            print("Team number is invalid!!!")

    elif choice == 5:
        print_teams()
        team_num = int(input("Whats the team number you want to remove a player?\n"))
        if team_num <= len(teams):
            addTeam = list(teams.keys())[team_num - 1 ]
            print_players(teams[addTeam])
            playerNum = int(input("Which player number you wanna remove?\n"))
            if playerNum <= len(teams[addTeam])['Players']:
                del teams[addTeam]['Players'][playerNum - 1]
                print("Player removed!")
            else:
                print("Invalid number, please try again.")
        else:
            print("Team number invalid")

    elif choice == 6:
        print_teams()
        team_num = int(input("Whats the team number you want to show the players?\n"))
        if team_num <= len(teams):
            addTeam = list(teams.keys())[team_num - 1 ]
            print_players(teams[addTeam])

    elif choice == 7:
        done = True
    else:
        print("Invalid number")




    



