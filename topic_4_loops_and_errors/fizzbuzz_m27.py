# Klases uzdevums - cikli
start = 1
finish = 100
fizz = 3
buzz = 5
# 1. Uzdevums - FizzBuzz
for i in range(start,finish+1):
    end_sym = ", "
    if i == finish:
        end_sym = " 🍺\n"
    # i could have done this differently
    # else:
    # 		end_sym = ", "
    # it is crucial that check the most particular case first
    if i % fizz == 0 and i % buzz == 0:
        print("Fizzbuzz", end = end_sym)
    elif i % fizz == 0:
        print("Fizz", end = end_sym)
    elif i % buzz == 0:
        print("Buzz", end = end_sym)
    else:
        print(i, end = end_sym)