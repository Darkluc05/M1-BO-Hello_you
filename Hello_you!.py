def s_end():
    valid_input = False
    while not valid_input:
        print("would you like to try again")
        A = input("(Y/N)")
        if A == "Y":
            print ("good luck")
            s1()
            valid_input=True
        elif A == "N":
            print("have a nice day")
            valid_input = True
        else:
            print("answer with capital Y or capital N")
            

def s26():
    print("You have completed the day and live to see another day by making allot of correct choices along the way in this very dangerous world that we live in.")
    print("Good luck to you tomorow")
    s_end()

def s25():
    valid_input = False 
    while not valid_input: 
        print("You see a ridiculous amount of fans for someone who isn’t known at all in the gaming community")
        print("and you start getting really worried because before you even realise it you are almost completely surrounded by them ")
        print("you see one final gap to escape the crowd but you also realise that this fame could be the start of a new career. ")
        print("What do you do")
        print("1 start running")
        print("2 take the fame")
        A = input("")
        if A == "1":
            s24()
            valid_input = True
        elif A == "2":
            s5()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s24():
        print("as you look behind you you see hundreds of people running affter you and all kinds of black cars pulling up eventually they trap you in an alley")
        print("and the mafia boss steps out.")
        s_end()

def s23():
    valid_input = False 
    while not valid_input: 
        print("You start researching the competition a bit closer and you call one of your good buddies who's good at discovering dark secrets online.")
        print("He soon comes back showing proof that this competition had weird ties to the mafia.")
        print(". Which is weird considering this isn’t Italy or America. But he does also tell you that the mafia doesn’t often actually respond badly to these types of things but just gains money out of it ")
        print("and that you could also gain allot of money from it.")
        print("1 money")
        print("2 safety")
        A = input("")
        if A == "1":
            s25()
            valid_input = True
        elif A == "2":
            s21()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s22():
    valid_input = False 
    while not valid_input: 
        print("You start looking at where the competition actually is and you see that it is right around the corner but in a fairly dark alleyway garage.")
        print("You start second guessing yourself a bit but it is still bright out so its not like you’re going to get stabbed in the middle of the night.")
        print("You can either.")
        print("1 go with the flow")
        print("2  be supiscous ")
        print("3 do some research")
        A = input("")
        if A == "1":
            s25()
            valid_input = True
        elif A == "2":
            s21()
            valid_input = True
        elif A == "3":
            s23()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s21():
    valid_input = False 
    while not valid_input: 
        print("You decide to compete in the lower level competition and you end up finishing second place. ")
        print("after a very fair battle with the number one You see weirdly enough that there are allot of fans for you.")
        print("which is weird on such a small competition but you don’t really enjoy fame that much anyway.")
        print("So you can either avoid the crowd or get smothered in it.")
        print("1 stay")
        print("2 go home")
        A = input("")
        if A == "1":
            s25()
            valid_input = True
        elif A == "2":
            s26()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s20():
    valid_input = False 
    while not valid_input: 
        print("You start getting bored of your game. ")
        print("So you start thinking about how to spice up what you’re doing.")
        print("the best you can think off is either going golfing or playing the game at a higher level.")
        print("1 esports")
        print("2 golf")
        A = input("")
        if A == "1":
            s19()
            valid_input = True
        elif A == "2":
            s18()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s19():
    valid_input = False 
    while not valid_input: 
        print("You start searching for different tournaments to compete in and you see the options of low end tournaments or high end tournaments")
        print("now normally high end tournaments take place at larger events and take planning.")
        print("but you see one odd one out paying allot of money for a competition that is weirdly enough on the same day.")
        print("1 low level")
        print("2 high level")
        A = input("")
        if A == "1":
            s21()
            valid_input = True
        elif A == "2":
            s22()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s18():
    print("You decide to go golfing and when you arrive you see one of your golf buddies is also there. ")
    print("You walk up to them and after about an hour of talking and golfing you start giving each other dares like keeping one eye closed.")
    print("Eventually you get the dare of a happy Gilmore(the run and slam).")
    print("but in your leap you miss the ball and swing your club through the air falling the ground face first and breaking your neck.")
    s_end()


def s17():
    valid_input = False 
    while not valid_input: 
        print("Which sport would you like to play.")
        print("you see that golf and esports are probably the best options.")
        print("1 golf")
        print("2 esports")
        A = input("")
        if A == "1":
            s18()
            valid_input = True
        elif A == "2":
            s19()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s16():
    valid_input = False 
    while not valid_input: 
        print("You’re at home and you’re looking for something to do. ")
        print("You see two viable options.")
        print("1 sport")
        print("2 game")
        A = input("")
        if A == "1":
            s17()
            valid_input = True
        elif A == "2":
            s20()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s15():
    print("Now your teacher is completely flipping out and start waving around a random bat in the air. ")
    print("Now with your angry self you keep shouting at her and start moving you point of interest to her face. ")
    print("but in her anger she lets go of the bat and it flies in your face. ")
    print("Causing you to black out.")
    s_end()
    
def s14():
    valid_input = False 
    while not valid_input: 
        print("14.	You decide to apologize for the fact that you raised your voice.")
        print("You start calming down but now you’re hearing whispers from everywhere.")
        print("But you also realise you’re very tired and I could just be you imagining it.")
        print("1 just move on")
        print("2 get angry again")
        A = input("")
        if A == "1":
            s13()
            valid_input = True
        elif A == "2":
            s15()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s13():
    valid_input = False 
    while not valid_input: 
        print("13.	You decide to ignore the fact they were probably talking about you and they luckily quickly stop.")
        print("A few hours go by and you’re starting to get really bored and almost falling asleep. ")
        print("You see an opportunity that after your teacher asked if you were there you could just leave.")
        print("1 just complete the day")
        print("2 go back home")
        A = input("")
        if A == "1":
            s26()
            valid_input = True
        elif A == "2":
            s16()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s12():
    valid_input = False 
    while not valid_input: 
        print("You’re sitting down while your teacher is introducing herself and doing her signature start to the lesson.")
        print("But you start hearing quiet whispers in the back of the class.")
        print("Your almost certain they are talking about you but getting angry at them could cause a scene,")
        print("and especially if they weren’t actually talking about you.")
        print("1 ignore")
        print("2 argue")
        A = input("")
        if A == "1":
            s13()
            valid_input = True
        elif A == "2":
            s10()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s11():
    print("you arrive late for class unfortanatly and your teacher quickly asks you why you are late and you just say the first thing that comes to mind and you apoligize")
    s12()
    

def s10():
    valid_input = False 
    while not valid_input: 
        print("The teacher walks into the classroom and immediately notices you aren’t doing anything. ")
        print("And she starts shouting at you and scolding you for this fact. She starts handing out extra exercises for you to teach you a lesson.")
        print("But you think this is unfair because there were other people that weren’t doing anything. But she insist that it was just you.")
        print("So you start getting slightly pissed at her but she quickly puts you in your place  by shouting that:  ")
        print("“if you don’t calm down I will remove you from the class.”")
        print("do you:")
        print("1 keep shouting")
        print("2 apoligize")
        A = input("")
        if A == "1":
            s5()
            valid_input = True
        elif A == "2":
            s14()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s9():
    valid_input = False 
    while not valid_input: 
        print("You get in your class but the teacher isn’t there yet you see that she wrote something on the board. ")
        print("it’s says something about working a bit in the time she isn’t there yet but it looks really boring. What’s your next move")
        print("What's your next move")
        print("1 do nothing")
        print("2 be bored but work")
        A = input("")
        if A == "1":
            s10()
            valid_input = True
        elif A == "2":
            s12()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s8():
    valid_input = False 
    while not valid_input: 
        print("You run to the station and see two viable options either the metro or the train.")
        print("1 metro")
        print("2 train")
        A = input("")
        if A == "1":
            s9()
            valid_input = True
        elif A == "2":
            s11()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s7():
    valid_input = False 
    while not valid_input: 
        print("The bus is quickly delayed by atleast 10 minutes but when you look at google maps you see that by running you may be able to cut off the bus to the station. But that would mean being extremely tired.")
        print("1 wait")
        print("2 run")
        A = input("")
        if A == "1":
            s11()
            valid_input = True
        elif A == "2":
            s8()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s6():
    print("Right before you answer a you hear a huge explosion in the distance followed by another even closer and before you can think everything is black")
    print("(bad ending(bomb zone/mafia death))")
    s_end()

def s5():
    valid_input = False 
    while not valid_input: 
        print("You go back to where your friends were but you quickly realise they have left already so you figure they probably went to the burger king down the road.")
        print("You walk out of the building and start walking with some music but you start vibing so hard you get lost in an industrial area and when you check your phone it wont work anymore.")
        print("Its completely quiet but you do see a black car standing still. ")
        print("You walk up to them to see if they could possibly help you. But when you knock on the window you see two huge guys in full black suits just sitting there. ")
        print("You hesitantly ask for a ride back to your school. But once you get in you quickly realise they have no intention to drive to your school and suddenly everything goes black once you wake up you’re strapped to a chair you start shouting for help and quickly huge guys with guns start coming out. And they ask you one simple question.")
        print("1 join")
        print("2 die")
        A = input("")
        if A == "1":
            s6()
            valid_input = True
        elif A == "2":
            s6()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s4():
    valid_input = False 
    while not valid_input: 
        print("You go to your friends and are having a really good time after about 10 minutes you realise you should have gone to class but you realise your friends aren’t phased by this fact that’s when you remember that their teacher was sick so they got to skip the hour. ")
        print("You start quickly running to your class but when you reach it the doors are closed and you’re not allowed to get in anymore. ")
        print("You have two choices now you can either wait till your teacher lets you in but this would mean that your parents get a mail and they would most likely get mad at you or you can just leave to go back to your friends")
        print("1 leave")
        print("2 wait")
        A = input("")
        if A == "1":
            s5()
            valid_input = True
        elif A == "2":
            s10()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s3():
    valid_input = False 
    while not valid_input: 
        print("You start cycling and reach the station with 1 minute left to go but once you sit down everything is smooth sailing and you get to school with ease. ")
        print("Except once you get in your school you see your friends standing one hallway down, ")
        print("but when you check your watch you realise you only have 5 minutes till your lesson starts.")
        print("1 go to your friends")
        print("2 go to class")
        A = input("")
        if A == "1":
            s4()
            valid_input = True
        elif A == "2":
            s9()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s2():
    valid_input = False 
    while not valid_input: 
        print("To get to school you must first get to the train station there are a few ways but the best one’s are")
        print("1 Take the bike")
        print("2 take the bus")
        A = input("")
        if A == "1":
            s3()
            valid_input = True
        elif A == "2":
            s7()
            valid_input = True
        else:
            print("answer with 1 or 2.")
            
def s1():
    valid_input = False 
    while not valid_input:
        print("Its morning and you wake up once you finally get up what do you do")
        print("1 go to school")
        print("2 stay home")
        A = input("")
        if A == "1":
            s2()
            valid_input = True
        elif A == "2":
            s16()
            valid_input = True
        else:
            print("answer with 1 or 2.")
            
s1()