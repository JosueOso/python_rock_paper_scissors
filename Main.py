
def get_choices():
  
  player_Choice = input("Enter a choice: rock paper scissors: ")
  cpu_Options = ["rock", "paper", "scissors"]
  cpu_Choice = random.choice(cpu_Options)
  choice = {"player": player_Choice, "cpu": cpu_Choice}
  return choice

def check_Win(player, cpu):
  print(f"You chose {player}, Cpu chose {cpu}")
  if player == cpu:
    return "It's a tie!"
  elif player == 'rock':
    if cpu == 'sicssors':
      return "Rock beats scissors! Player Wins"
    else:
      return "Paper beats rock! Cpu Wins"

  elif player == 'paper':
    if cpu == 'rocks':
      return "Paper beats rock! Player Wins"
    else:
      return "Scissors beat paper Cpu Wins"
      
  elif player == 'scissors':
    if cpu == 'paper':
      return "Scissors beats paper! Player Wins"
    else:
      return "Rock beats scissors! Cpu Wins"

      
choices = get_choices()
result = check_Win(choices["player"], choices["cpu"])
print(result)
