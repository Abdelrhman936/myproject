import details
print(details.bio)
take_by_input = input("\n\nEnter what do you want of details: ").lower().strip()

if take_by_input == "name":
    print(details.name)
elif take_by_input == "age":
    print(details.age)
elif take_by_input == "username":
    print(details.username)
elif take_by_input == "programming_language":
    print(details.programming_language)