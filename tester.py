
def weather_advice():
    temp_prompt = input("Is it cold outside: ").lower() == "yes"
    raining_prompt = input("Is it raining outisde: ").lower() == "yes"

    if temp_prompt and raining_prompt:
        print("Wear a water coat.")
    elif temp_prompt and not raining_prompt:
        print("Wear a warm coat.")
    elif not temp_prompt and raining_prompt:
        print("Carry an umbrella.")
    elif not temp_prompt and not raining_prompt:
        print("Wear light clothing.")
    
weather_advice()
