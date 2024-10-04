name = input("What's your name: ")
age = int(input("What's your age: ").strip())
username = input(f"{name}0{age}1").lower().strip()
level = input("Choose yor level:\n[Beginner, Intermediate, Advanced, Expert, Master]\nWhat's your level: ")
programming_language = input("What's programming language: ")
bio = f"""
My Name is {name}.
I {level} in programming.
I have {age} years.
I have {programming_language} programming language.
Thanks and Goodbye.
"""