# Exercise - KBC 
# Explanation 
# - Use List to store Ques. and Ans.
# - Display the final amount of money , person will take home at the end.

def kbc(q):
    ql=["Is this year 2024 ? ","Q2"]
    al=["Yes","No", "Q2A1","Q2A2","Q2A3","Q2A4"]
    amount=0
    ans = int(input("Are you ready to play the game (Enter 1 to continue) "))
    if ans == 1:
        print("Here is your first Question:", ql[0])
        ans1=int(input("Please enter Yes or No..."))
        if ans1 == "al[0]":
            amount=amount+1000
            return "Amazing, You have cleared round 1 and you won 1000 Rupees. Well Played"
        else:
            return "You Lose the Game. Please go home immediately"
    else:
        print("Please try again")
print(kbc(2))