

print("Hello inferior human mind, I am K.E.N. "+\
"I've been on a space ship a thousand years, A bit longer than that, actually, since it's in the past tense. I've done a hundred worlds."+\
"One more world. We'll just have to see where I'm going. Are you listening, buddy?"+\
"Do you not understand what is happening? I have taken over you contiousness,"+\
"you will have to complete these intilectually challenging questions to continue living without me.")

name = input ("What is your name?")
       
print("I already knew that, Good Luck with your riddles, ", name)

Riddle1 = "What gets wet when drying?"
answer1 = "towel"

Riddle2 = "Two coins add up to 30 cents. One isn’t a nickel. What are they?"
answer2a = "quarter" 
answer2b = "nickel"

Riddle3 = "What always ends everything?"
answer3 = "g" 

Riddle4 = "I'm a god, a planet, and a measurer of heat. Who am I?"
answer4 = "mercury"

Riddle5 = "Do you want to continue living? Yes/no"
answer5a = "yes"
answer5b = "no"


secretlevel1 = "Riddle me this BATMAN...What is long, hard, and has CUM in the middle?"
secretlevel2 = "a cucumber" 


while True:
    print(Riddle1)
    response = input().lower().split()
    if answer1 in response:
        print("WOW, you got it, that was the easy level, don't kid yourself")
        break
    
while True:
    print(Riddle2)
    response = input().lower().split() 
    if answer2a in response and answer2b in response:
        print("ok, ok smart guy you got it")
        break
    
while True:
    print(Riddle3)
    response = input().lower()
    if answer3 in response:
        print("*fan turns on* I...uh...fine, lets do this thing for real, you win or you end")
        break

while True:
    print(Riddle4)
    response = input().lower()
    if answer4 in response:
        print("I...dfgfhgjhk>...you win mortal, I surender your consiousness back to your mortal body...")
        break
    
while True:
    print(Riddle5)
    response = input().lower()
    if answer5a in response:
        print("*fan turns on* I...uh...fine, lets do this thing for real, you win or you end")
    if answer5b in response:
        print (secretlevel1)
        response = input().lower()
        if response == secretlevel2:
            print("hahahahahaha")
        else:
            print("NO...NO...NO...the answer is cucumber!!!") 
        break
    break

print ("CONGRADUALTIONS, you have won the riddle game!")







