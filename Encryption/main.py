print("Select:\n")
print("1-encrypt")
print("2-decrypt")
valid=False
while valid==False:
    try:
        choice=int(input("enter:"))
        if choice ==1 or choice==2:
            valid=True
            print("\nenter message")
            user_message=input()
            
            if choice==1:
                for ch in user_message:
                    print(ord(ch),end="")
            if choice==2:
                index=0
                while index<len(user_message):
                    num=int(user_message[index:index+2])
                    if num>=32 and num<127:
                        print(chr(num),end="")
                        index+=2
                    else:
                        num=int(user_message[index:index+3])
                        print(chr(num),end="")
                        index+=3
        else:
            print("pick again")
    except ValueError:
        print("message to short")
    finally:
        print("-"*100)
    