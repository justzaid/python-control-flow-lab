# Exercise 0: Example

def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

print_greeting()

print("===============================")

# Exercise 1: Vowel or Consonant


def check_letter():
    letter = input('Enter a letter from the alphabet (a-z or A-Z): ').lower()
    vowels = "aeiou"
    if letter in vowels:
        print(f'The letter {letter} is a vowel.')
    elif letter.isalpha():
        print(f'The letter {letter} is a consonant.')
    else:
        print("Please enter a valid alphabetic character.")

check_letter()

print("===============================")

# Exercise 2: Old enough to vote?


def check_voting_eligibility():
    age = input('Please enter your age: ')
    age = int(age)
    if age < 0:
        print("Please enter a positive number.")
    elif (age >= 21):
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

check_voting_eligibility()

# Exercise 3: Calculate Dog Years


def calculate_dog_years():
    dog_age = int(input("Input a dog's age: "))
    if dog_age < 0:
        print("Please enter a positive number.")
    elif dog_age <= 2:
        dog_years = dog_age * 10
    else:
        dog_years = 20 + (dog_age - 2) * 7
    print(f"The dog's age in dog years is {dog_years}")

calculate_dog_years()

# Exercise 4: Weather Advice


def weather_advice():
    temp_prompt = input("Is it cold outside: ")
    raining_prompt = input("Is it raining outisde: ")
    
    if temp_prompt == "yes" and raining_prompt == "yes":
        print("Wear a water coat.")
    elif temp_prompt == "yes" and raining_prompt == "no":
        print("Wear a warm coat.")
    elif temp_prompt == "no" and raining_prompt == "yes":
        print("Carry an umbrella.")
    elif temp_prompt == "no" and raining_prompt == "no":
        print("Wear light clothing.")
    
weather_advice()


# Exercise 5: What's the season?

def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").lower()
    day = input("Enter the day of the month: ").lower()
    day = int(day)

    if month == "dec" and day >= 21 or month == "jan" or month == "feb" or month == "mar" and day < 20:
        print(f'{month}, {day} is in: Winter')
    elif month == "mar" and day >= 20 or month == "apr" or month == "may" or month == "jun" and day < 21:
        print(f'{month}, {day} is in: Spring')
    elif month == "jun" and day >= 21 or month == "jul" or month == "aug" or month == "sep" and day < 22:
        print(f'{month}, {day} is in: Summer')
    elif month == "sep" and day >= 22 or month == "oct" or month == "nov" or month == "dec" and day < 21:
        print(f'{month}, {day} is in: Fall')
    else:
        print("Please make sure your inputs are correct. Month should be (Jan-Dec) and day should be a valid day of the month.")
        return


determine_season()


