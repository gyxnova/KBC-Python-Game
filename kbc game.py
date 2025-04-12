import random
import time

questions = [[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country is known as “the Land of festivals?","india","uk","australia","nepal",1],
[" Which country has the highest life expectancy?"," Hong Kong","uk","australia","nepal",1]]


random.shuffle(questions)
# time.sleep (30)


level =[1000,2000,3000,5000,10000,15000,25000,50000,100000,320000,500000,1500000,2500000,5000000,7500000,10000000,75000000]
money=0
i=0
for i in range(len(questions)):
    start=time.time()
    question= questions[i]
    print(f"\n\nquestion for {level[i]} is {question[0]}")
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")
   

    reply=(int(input("enter your answer in 1-4 range or 0 for quit or poll in range5-6")))
    end=time .time()
    elapsed_time=end-start
    if elapsed_time>3:
        print("time out")
        money=level[i-1] if i>0 else 0
        break
    if (reply==5):
        print("audiance poll")
        print("a=78%,b=2%,c=10%,d=10%")
        reply=(int(input("enter your answer in 1-4 range or 0 for quit or poll in range5-7")))
    if (reply==6):
        print("expert opinion")
        reply=(int(input("enter your answer in 1-4 range or 0 for quit or poll in range5-7")))

    if reply<0 or reply>6:
        print("invalid input. please enter a number from 0 to 6.")
        continue

    if (reply == 0 ):
        money=level[i-1] if i>0 else 0
        break
    if (reply==question[-1]):
        print(f"correct answer and you won rs {level[i]}")

        if (i==4):
            money=10000
        elif (i==9):
            money=320000
        elif (i==14):
            money= 7500000
    else:
        print("wrong answer!!")
        break

   
print(f"your take home money is {money} ") 
# print(elapsed_time)   
