def input_name(prompt = "Vad heter du?"):
    while True:
        name = input(prompt)
        if len(name) >= 2:
            return name
        else: 
            print("Ogiltigt namn. Försök igen.")

name = input_name()
print(f"Ditt namn är {name}.")