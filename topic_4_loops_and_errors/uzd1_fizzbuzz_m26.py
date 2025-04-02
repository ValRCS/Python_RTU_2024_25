# 1_uzdevums
start = 1
finish = 100
fizz = 5
buzz = 7
 
for i in range(start, finish+1):
    end_sym = ", "
    if i == finish:
        end_sym = "\n" # back to default
    
    if i % fizz == 0 and i % buzz == 0:
        print("FizzBuzz", end=end_sym)
    elif i % fizz == 0:
        print("Fizz", end=end_sym)
    elif i % buzz == 0:
        print("Buzz", end=end_sym)
    else:
        print(i, end=end_sym)