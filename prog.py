import random
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

def input_clamp(stat_name, prompt, clamp = 6) -> int:
    while player_horse[stat_name] < 1 or player_horse[stat_name] > clamp:
            player_horse[stat_name] = input_int(prompt)

stats_ok = False
while stats_ok == False:
    input_clamp("speed", "Hur snabb är din häst?(1-6)")
    input_clamp("agility", "Hur länge orkar din häst springa?(1-6)")
    input_prompt = f"Din häst har {player_horse['speed']} i speed och {player_horse['agility']} i agility. Det blir totalt {player_horse['speed'] + player_horse['agility']}. Stämmer det? (j/n)"
    answer = input(input_prompt)
  
    if player_horse["speed"] + player_horse["agility"] == 8:
            stats_ok = True
    else:
        print("Slut å fusk, gubbe")
        player_horse["speed"] = 0
        player_horse["agility"] = 0

def create_computer_horse():
    speed = random.randint (2,6)
    name_parts = ["clanker", "rust-bucket", "oil-drinker", "ai", "metal-ball", "electricity-eater", "steel-feet"]
    horse = {
     "name": random.choice(name_parts).capitalize() + " " + random.choice(name_parts),
     "speed": speed,
     "agility": 8 - speed
}
    
    return horse
for i in range(10):
     print(create_computer_horse())

computer_horse = create_computer_horse()
print(player_horse)
print(computer_horse)

def game_turn():
    player_speed = player_horse["speed"] + random.randint(1, 6)
    player_agility = player_horse["agility"] - random.randint(1, 6)
    if player_agility >= 0:
        player_speed -= player_agility
    computer_speed = computer_horse["speed"] + random.randint(1, 6)
    computer_agility = random.randint(1, 6) - computer_horse["agility"]
    if computer_agility >= 0:
        computer_speed -= computer_agility
    print(f"Spelarens häst {player_horse["name"]} springer {player_speed} steg")
    print(f"Datorns häst {computer_horse["name"]} springer {computer_speed} steg")

    return [player_speed, computer_speed]

player_steps = 0
computer_steps = 0
for i in range(10):
    steps = game_turn()
    player_steps += steps[0]
    computer_steps += steps [1]

print(f"Antal steg: player {player_steps}, computer {computer_steps}")

