print("Hello! I am AI Bot. What's your name? : ")

name=input()

print(f"Nice to meet you,{name}!")

print("How are you feeling today?(good/bad/other):")
mood= input().lower()

if mood == "good":
    print("I'm glad to hear that!")

elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon")

elif mood =="other":
    print("It's okay, hope you have a good day")
else:
    print("I see. Sometimes it's hard to put feelings into words.")

print(f"It was a nice chatting with you{name}. Goodbye! ")