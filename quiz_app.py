print("Welcome to the quiz app.")
print("Instructions:\n 1.Each question has four options \n 2.Enter A, B, c, D to select your answer \nGood luck!")
# print("\n Please enter your name and press 'ENTER' to begin :")

name = input("\nPlease enter your name and press 'ENTER' to begin : ")
score=0

print("\nQUESTION 1: Which country is famous for the Amazon Rainforest? \nA.Argentina \nB.India \nC.Brazil \nD.Peru")
while True:
 answer = input("ANSWER : ").upper()
 if answer in ['A','B','C','D']:
     break
 else:
    print("INVALID ANSWER !! \nplease enter a valid option")

if answer == "C":
    print("\nCORRECT !")
    score+=1
else :
    print("\nINCORRECT- The answer is C")


print("\nQUESTION 2: Which country is known as 'The Land of The Rising Sun'? \nA.Japan \nB.China \nC.United States \nD.Thailand")
while True:
 answer = input("ANSWER : ").upper()
 if answer in ['A','B','C','D']:
     break
 else:
    print("INVALID ANSWER !! \nplease enter A, B, C, D to select your answer.")
    
if answer == "A":
    print("\nCORRECT !")
    score+=1
else :
 print("\nINCORRECT- The answer is A")


print("\nQUESTION 3: Which country has a city named 'Timbuktu'? \nA.Australia \nB.Nepal \nC.South Korea \nD.Mali")
while True:
 answer = input("ANSWER : ").upper()
 if answer in ['A','B','C','D']:
     break
 else:
    print("INVALID ANSWER !! \nplease enter a valid option")

if answer == "D":
    print("\nCORRECT !")
    score+=1
else :
    print("\nINCORRECT- The answer is D")


print("\nQUESTION 4: Which country has the most volcanoes in the world? \nA.Indonesia \nB.Italy \nC.Mexico \nD.Sri Lanka")
while True:
 answer = input("ANSWER : ").upper()
 if answer in ['A','B','C','D']:
     break
 else:
    print("INVALID ANSWER !! \nplease enter a valid option")

if answer == "A":
    print("\nCORRECT !")
    score+=1
else :
    print("\nINCORRECT- The answer is A")


print("\nQUESTION 5: Where did 'Gelato' originate? \nA.Portugal \nB.Italy \nC.France \nD.United States")
while True:
 answer = input("ANSWER : ").upper()
 if answer in ['A','B','C','D']:
     break
 else:
    print("INVALID ANSWER !! \nplease enter a valid option")

if answer == "B":
    print("\nCORRECT !")
    score+=1
else :
    print("\nINCORRECT- The answer is B")

percentage= (score / 5)*100

if percentage >= 60:
    print("\nResult: PASS \nCongrats!")
else:
    print("Result: FAIL\nBetter luck next time.")

print(f"\n{name.capitalize()} Your score is : {score} out of 5 \nYou scored {percentage} % on the quiz." )
