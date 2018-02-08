print("Hello welcome to the best online skin care store!")
print("May I ask what is your name?")
name = input()
print("Hello " + name)

print("Would you like to try our newest anti wrinkle cream " + name + "?")
answer = input().lower()
if answer == "yes":
    print("Great! I will add it to your shopping cart.")
elif answer == "no":
    print("I'm sorry to hear that " + name + " but we hope to see you again soon!")
else:
    while answer != "yes" or answer != "no":
        print("Please reanswer the question with yes or no")
        print("Would you like to try our newest anti wrinkle cream " + name + "?")
        answer = input().lower()
        if answer == "yes":
            print("Great! I will add it to your shopping cart.")
            break
        elif answer == "no":
            print("I'm sorry to hear that but we hope to see you again soon!")  
            break 
print("Have a great day " + name + "!")