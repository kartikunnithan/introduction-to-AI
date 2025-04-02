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
print("It was nice chatting with you ", name, ".Goodbye")