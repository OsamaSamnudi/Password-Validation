# Password Validation :

def Password_Validation():
    PASS = input(
        "Please add your Passowrd (Should be Has:\n-Capital & Small letters\n-Speacial Characters\n-Numbers)")
    ALPHA_Count = sum(c.isalpha() for c in PASS)
    Number_Count = sum(c.isnumeric() for c in PASS)
    Speacial_Char = "~!@#$%^&*()_+=-][}{|:?؟<,>\|"
    O_Check = 0
    O_Flage = False
    for x in PASS:
        if x in Speacial_Char:
            O_Flage = True
            O_Check += 1

    U_Check = sum(c.isupper() for c in PASS)
    L_Check = sum(c.islower()for c in PASS)
    N_Check = sum(c.isnumeric() for c in PASS)

    if U_Check != 0:
        U_Flage = True
    else:
        U_Flage = False
    if L_Check != 0:
        L_Flage = True
    else:
        L_Flage = False
    if N_Check != 0:
        N_Flage = True
    else:
        N_Flage = False
    if O_Check != 0:
        O_Flage = True
    else:
        O_Flage = False

    while True:
        if len(PASS) not in range(6, 12):
            print("Password lenght should have 6 : 12 Character")
            break
        if U_Flage and L_Flage and N_Flage and O_Flage:
            General_Chek = True
            print("Good Password")
        else:
            if U_Flage == False:
                print("Password Should has Upper Case")
            if L_Flage == False:
                print("Password Should has Lower Case")
            if N_Flage == False:
                print("Password Should has Numer")
            if O_Flage == False:
                print("Password Should has Special Character from below :\n#\t@\t$")
        break


Password_Validation()
