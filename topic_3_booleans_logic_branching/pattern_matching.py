# Python 3.10 introduce pattern matching
# it is similar to switch case in other languages but more powerful

# we can use match if we have a long if elif elif elfi else chain brewing 

n = int(input("Enter a number"))

match n:
    case 0:
        print("nulle!")
    case 1:
        print("viens")
    case 2:
        print("divi")
    case 3:
        print("tris")
    case _: # for default case
        print(f"Ahh nezinu bet ir {n}")
        
# we could have done this same thing with if elif elif

if n == 0:
    print("nulle!")
elif n == 1:
    print("viens")
elif n == 2:
    print("divi")
else:
    print("nezinu")