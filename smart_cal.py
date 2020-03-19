def dacoration():
    print("\t\t\t\t###################################################################")
    print("\t\t\t\t\t\t\t\tWELCOME!!!!!")
    print("\t\t\t\t*******************************************************************")
    print("\t\t\t\t\t\t    SMART CALCULATOR!!!!!!!!")
    print("\t\t\t\t\t\tMy  name  is  smart  calculator.")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t By SAURABH SHARMA")
    print("\t\t\t\t###################################################################")

def help():
    print("\n\n\n___________________________________________________________________________________________________\n")
    print("\n                                  \t\t WELCOME ")
    print("\n\n\t\t            This is a smart calculator. ")
    print("\n\n\t In this calculator, We find the addition, subtraction, multiplication, division, HCF(highest common factor), LCM(least common multiple) of more than 2 digits.")
    print("\n FOR EXAMPLE")
    print("     Enter The Some Text")
    print("           find the sum of 3 , 4 ,5 and 6")
    print("\t\t\t\t*******************************************************************")
    print(f"\t\t\t\t\t\tThe sum of [3.0,4.0,5.0,6.0] =  {sum([3.0,4.0,5.0,6.0])} ")
    print("\t\t\t\t*******************************************************************")
    print("\n\n When we want to exit from this calculator, than we write the following form..... ")
    print("     1. exit game")
    print("     2. quit\n     :\n     :\n     : \n     : \n    and so on")
    print("\n\n\n___________________________________________________________________________________________________\n")


def check(l):
    """"take the one list and return the list of the all integer value """
    temp1 = ""
    for i in l:
        if i != ' ':
            temp1 = temp1 + i

        elif temp1[0] in "1234567890":
            a.append(float(temp1))
            temp1 = ""

        else:
            temp1 = ""


def subtraction(t):
    return t[0] - t[1]


def multiplication(t):
    result = 1
    for i in t:
        result *= i
    return result


def division(t):
    return t[0] / t[1]


def highest_common_factor(t):
    result = min(t)
    for i in t:
        for j in range(0, 6):
            if i % result != 0:
                result = i % result
                if j==1:
                    result = i % result
    return result


def least_common_multiple(num1 ,num2):
    t = [num1,num2]
    result = int(int(num1 * num2) / int(highest_common_factor(t)))
    return result

if __name__ == "__main__":
    print("\n\n\n\n")
    dacoration()
    temp = ""
    a = []
    while True:
        l = "find "
        print("\n\n\tEnter The Some Text \t ")

        l += input()
        l = l + " text"

        check(l)

        for i in l:
            if i != ' ':
                temp = temp + i

            elif temp in ["sum", "plus", "add", "addition", "+"]:
                print("\t\t\t\t*******************************************************************")
                check(l)
                print(f"\t\t\t\t\t\tThe {temp} of {a} =  {sum(a)} ")
                a = []
                print("\t\t\t\t*******************************************************************")

            elif temp in ["exit", "quit"]:
                exit()

            elif temp in ["subtract", "minus","-"]:
                print("\t\t\t\t#################################################################")
                check(l)
                print(f"\t\t\t\t\t\tThe {temp} of {a} = {subtraction(a)} ")
                a = []
                print("\t\t\t\t#################################################################")

            elif temp in ["multiply", "mul", "cross","*"]:
                print("\t\t\t\t*******************************************************************")
                check(l)
                print(f"\t\t\t\t\t\tThe {temp} of {a} = {multiplication(a)} ")
                a = []
                print("\t\t\t\t*******************************************************************")

            elif temp in ["divide", "div", "/"]:
                print("\t\t\t\t#################################################################")
                check(l)
                print(f"\t\t\t\t\t\tThe {temp} of {a} = {division(a)}")
                a = []
                print("\t\t\t\t#################################################################")

            elif temp in ["hcf", "HCF", "h.c.f.", "H.C.F.", "highest_common_factor"]:
                print("\t\t\t\t*******************************************************************")
                check(l)
                print(f"\t\t\t\t\t\tThe {temp} of {a} = {highest_common_factor(a)}")
                a = []
                print("\t\t\t\t*******************************************************************")

            elif temp in ["lcm", "LCM", "l.c.m.", "L.C.M.", "highest_common_factor"]:
                print("\t\t\t\t#################################################################")
                check(l)
                num1 = a[0]
                num2 = a[1]
                lcm = least_common_multiple(num1, num2)
                for j in range(2, len(a)):
                    lcm = least_common_multiple(lcm, a[j])
                print(f"\t\t\t\t\t\tThe {temp} of {a} = {lcm}")
                a = []
                print("\t\t\t\t#################################################################")

            elif temp in ["introduction", "name"]:
                dacoration()

            elif temp in ["help", "HELP"]:
                help()

            else:
                #check(l)
                temp = ""
                a = []
    input()
