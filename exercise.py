# Exercise 0: Example

def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

print_greeting()

print("===============================")

# Exercise 1: Vowel or Consonant


def check_letter():
    letter = input('Enter a letter: ')
    vowels = "aeiou"
    if letter in vowels:
        print(f'The letter {letter} is a vowel.')
    else:
        print(f'The letter {letter} is a consonant.')

check_letter()

print("===============================")

# Exercise 2: Old enough to vote?

age = int(input('Please enter your age: '))

def check_voting_eligibility():
    # print(type(age))
    # input_age = int(age)
    # print(type(input_age))
    if (age >= 21):
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

check_voting_eligibility()

# Exercise 3: Calculate Dog Years

dog_age = int(input("Input a dog's age: "))

def calculate_dog_years():
    if dog_age <= 2:
        dog_years = dog_age * 10
    else:
        dog_years = 2 * 10 + (dog_age - 2) * 7
    print(f"The dog's age in dog years is {dog_years}")

calculate_dog_years()

# Exercise 4: Weather Advice

temp_prompt = input("Is it cold outside: ")
raining_prompt = input("Is it raining outisde: ")

def weather_advice():
    if temp_prompt == "yes" and raining_prompt == "yes":
        print("Wear a water coat.")
    elif temp_prompt == "yes" and raining_prompt == "no":
        print("Wear a warm coat.")
    elif temp_prompt == "no" and raining_prompt == "yes":
        print("Carry an umbrella.")
    elif temp_prompt == "no" and raining_prompt == "no":
        print("Wear light clothing.")
    
weather_advice()

