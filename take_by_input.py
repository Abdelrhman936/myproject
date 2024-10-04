import details

print(f"details : {details}")
take_by_input = input("Enter what do you want of details?: ").lower().strip()

if take_by_input == "message":
    print(details.message)
elif take_by_input == "bio":
    print(details.bio)
elif take_by_input == "readme":
    print(details.readme)
elif take_by_input == "name":
    print(details.name)
elif take_by_input == "username":
    print(details.username)
elif take_by_input == "password":
    print(details.password)
elif take_by_input == "number_phone":
    print(details.number_phone)
elif take_by_input == "link_website":
    print(details.link_website)
elif take_by_input == "location":
    print(details.location)
elif take_by_input == "gmail":
    print(details.gmail)
elif take_by_input == "facebook":
    print(details.facebook)
elif take_by_input == "instgram":
    print(details.instgram)
elif take_by_input == "twitter":
    print(details.twitter)
elif take_by_input == "tiktik":
    print(details.tiktik)
elif take_by_input == "youtube":
    print(details.youtube)
elif take_by_input == "github":
    print(details.github)
else:
    input("Error, Enter what do you want of details only : ")