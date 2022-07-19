email = input("Enter your Email: ")
j,k,l = 0,0,0
if len(email) >= 6:
    if email[0].isalpha:
        if "@" in email and (email.count("@")==1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        j = 1
                    elif i == i.isalpha:
                        if i == i.upper():
                            k = 1
                    elif i == i.isdigit:
                        continue
                    elif i== "_" or i == "." or i == "@":
                        continue
                    else:
                        print("correct email id")
                        break
                if j == 1 or k == 1 or l == 1:
                    print("Invalid Input")  
            else:
                print("Invalid Email Format. Issue with '.' position")
        else: 
            print("Invalid Email Format. @ character issue")
    else:
        print("Invalid Email Format. First letter should always be alphabet")
else:
    print("Invalid Email Format. Size of email is less than min requirement")