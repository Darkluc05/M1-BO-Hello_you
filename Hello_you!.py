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
    print("")
    s_end()

def s25():
    valid_input = False 
    while not valid_input: 
        print("")
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
    valid_input = False 
    while not valid_input: 
        print("")

def s23():
    valid_input = False 
    while not valid_input: 
        print("")
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
        print("")
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
        print("")
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
        print("")
        A = input("")
        if A == "1":
            s11
            valid_input = True
        elif A == "2":
            s19()
            valid_input = True
        else:
            print("answer with 1 or 2.")

def s19():
    valid_input = False 
    while not valid_input: 
        print("")
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
    print("")
    s_end()


def s17():
    valid_input = False 
    while not valid_input: 
        print("")
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
        print("")
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
    print("")
    s_end()
    
def s14():
    valid_input = False 
    while not valid_input: 
        print("")
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
        print("")
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
        print("12.	You’re sitting down while your teacher is introducing herself and doing her signature start to the lesson.")
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
            s12
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