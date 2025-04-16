# 3. Uzdevums
 
def get_city_year(current_pop, perc, delta, pop_target, verbose=False):
    years = 0
    while current_pop < pop_target:
        yearly_increase = int(current_pop * perc / 100) + delta
        if verbose:
            print(f"Year {years}: current population = {current_pop}, yearly increase = {yearly_increase}")
        if yearly_increase <= 0: # 0 or less means city is not growing
            return -1
        current_pop += yearly_increase  # same as p0 = p0 + yearly_increase
        years += 1
    return years

# some tests

print(get_city_year(1000,2,50,1200))
print(get_city_year(1000, 2, -50, 5000) )
print(get_city_year(1500000, 2.5, 10000, 2000000) )

# let's test with negative percentage but positive delta

print(get_city_year(1000,-2,50,2000))
print(get_city_year(1000,-2,30,2000))

# let's run the last example in verbose mode
print(get_city_year(
    current_pop=1000,
    perc=-2,
    delta=30,
    pop_target=2000, 
    verbose=True))
