def calc(first_num, choice, second_num):
    if(choice=='addition'):
        return first_num+second_num
    elif (choice=='subtraction'):
        return first_num-
    second_num

print("This is the Basic Calculator Program")
start=input("Do you wish to start? Type 1 for YES and 0 for NO: ")
st=int(start)
if(st!=1 and st!=0):
    print("I'm going to take that as a YES")
while (st==1):
    num1=input("Enter the first number: ")
    first_num=int(num1)
    choice=input("Addition or Subtraction? ")
    choice=choice.lower()
    num2=input("Enter the second number: ")
    second_num=int(num2)
    answer=calc(first_num, choice, second_num)
    a=int(answer)
    print("The answer is "+str(a))
    continue_=input("Do you want to continue? Press 1 for YES and 0 for NO: ")
    st=int(continue_)
    if(st!=1 and st!=0):
        print("I'm going to take that as a NO")

print("Thank you for trying out the Bacic Calculator Program!")
