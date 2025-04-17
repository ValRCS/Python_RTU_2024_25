# 3. Pilsēta
 
def get_city_year(current_pop:int, 
                  perc:float, 
                  delta:int, 
                  target_pop:int,
                  verbose = False
                  ) -> int:
    """
    Function to calculate the number of years it will take for a city to reach a target population.
    The population increases by a percentage and a fixed number each year.
    Inputs:
    - current_pop: Current population of the city (int)
    - perc: Percentage increase of the population each year (float)
    - delta: Fixed number of people added to the population each year (int)
    - target_pop: Target population of the city (int)
    Returns:
    - Number of years it will take to reach the target population (int)
    returns -1 if the target population cannot be reached.
    """
    years = 0
    while current_pop < target_pop:
        # first let's calculate yearly increase
        yearly_increase = int(current_pop * (perc / 100)) + delta
        if yearly_increase <= 0:
            # if yearly increase is negative or zero, we can't reach the target population
            return -1 # -1 represents that the target population cannot be reached
        current_pop += yearly_increase # same as current_pop = current_pop + yearly_increase
        years += 1 # same as years = years + 1
        if verbose:
            print(f"Year {years}: Population = {current_pop} (Increased by: {yearly_increase})")
    return years

print(get_city_year(1000, 2, 50, 1200))         # -> 3
print(get_city_year(1000, 2, -50, 5000))        # -> -1
print(get_city_year(1500, 5, 100, 5000))        # -> 15
print(get_city_year(1500000, 2.5, 10000, 2000000)) # -> 10

print(get_city_year(1000, -2, 50, 2000))         
print(get_city_year(1000, -2, 30, 2000))     

print(get_city_year(1000, 2, 50, 1200, verbose=True)) 

# let's use full names for parameters
print(get_city_year(current_pop=1000, 
                    perc=-2, 
                    delta=30, 
                    target_pop=2000,
                    verbose=True
                    )) 
