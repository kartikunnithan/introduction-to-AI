print("Hello my name is ChatAI. What is your name?")
name=input()
print("Oh wow ", name, " That is a nice name")
print("How are you feeling today?(good or bad)")
mood=input().lower()
if mood=="good":
    print("That is great")
elif mood=="bad":
    print("That is sad ", name)
else:
    print("Oh its okay sometimes its hard to describe hoe you feel")
print("So what is your favourite food?")
food=input()
print("Nice choice", food, "Is really tasty")
print("What are your hobbies?")
hobbies=input()
print("That is great")
print("It was nice chatting with you ", name, ".Goodbye")