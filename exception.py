import random
import time

def comp_guess():
    print("Generating a random number.....")
    compguess=(random.randint(0,100))
    print("Your time starts now!")
    time1=time.time()
    while True:
        try:
            userguess=int(input("Enter a guess: "))
            if(userguess==compguess):
                time2 = time.time()
                time3=time2-time1
                print("Congrats correct guess")
                break
            elif((userguess > compguess - 5) & (userguess <= compguess + 5)):
                print("Hot")
            else:
                print("Cold")
        except:
            print('Invalid Input')

    print("The time taken by u t"
          "o guess the number is "+str(time2-time1)+"seconds")
    if(time3<=35):
        print("Ur an excellent guesser")
   # elif((time2-time1)>10&(time2-time1<=20)):
      #  print("Ur a good guesser")

    else:
        print("Next time guess better")


run=True
print("    *****                 *****     *************      *****                    ***********           ******           *******           ******      *************                  ")
print("     *****     *****     *****      *************      *****                   *************         *********         ********         *******      *************                             ")
print("      *****   *******   *****       ****               *****                  *****                 ***********        *********       ********      ****                  ")
print("       ***** **** **** *****        **********         *****                 *****                 *************       ****  ****     **** ****      **********                         ")
print("        ********   ********         **********         *****                 *****                 *************       ****   ****   ****  ****      **********                               ")
print("         ******     ******          ****               ****************       *****                 ***********        ****    **** ****   ****      ****                                   ")
print("          ****       ****           *************      ****************        *************         *********         ****     *******    ****      *************                                  ")
print("           **         **            *************      ****************         ***********           *******          ****      *****     ****      *************                         ")
print("                                                                                                                ")

while(run):
    flag=input("Enter quit to exit or press any key to start")
    if(flag=='quit'):
        print("Byeeeeeee")
        run=False
    else:
        comp_guess()
