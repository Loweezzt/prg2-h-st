print("Skapa din trav-häst")

player_horse = {
     "name": "",
     "speed": 0,
     "agility": 0,
}

def input_int(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("Invalid input. Please enter a number")

player_horse["name"] = input("Vad ska din häst heta?")
print("Din häst har olika stats som du kommer ge till den!") 
print("6 per stat är max och du har 8 stat points att ge ut")
print("Vad väljer du?")
stats_ok = False
while stats_ok == False:
    while player_horse["speed"] < 1 or player_horse["speed"] > 6:
            player_horse["speed"] = input_int("Hur snabb är din häst?")
    while player_horse["agility"] < 1 or player_horse["agility"] > 6:
            player_horse["agility"] = input_int("Hur länge orkar din häst springa?")
  
  
  
    if player_horse["speed"] + player_horse["agility"] == 8:
            stats_ok = True
    else:
        print("Slut å fusk, gubbe")
        player_horse["speed"] = 0
        player_horse["agility"] = 0

print(player_horse)