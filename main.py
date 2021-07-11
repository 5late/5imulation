import random
import asyncio

SEXES = ['male', 'female']
MIN_NUMBER_OF_CHILDREN = 1
MAX_NUMBER_OF_CHILDREN = 3

async def Breed():
    children_produced = random.randint(MIN_NUMBER_OF_CHILDREN, MAX_NUMBER_OF_CHILDREN)
    current_child = 0
    males = 0
    females = 0
    while current_child < children_produced:
        child_sex = random.choice(SEXES)
        if child_sex == 'male':
            males = males + 1
        else:
            females = females + 1
        current_child = current_child + 1
    
    return children_produced, males, females
    
  
async def startGame():
    global years
    years = 0
    
    population = 3
    males = 2
    females = 1
    available_males = 2
    available_females = 1
    cache_females = []
    cache_males = []

    while population < 10000:
        if years >= 20:
            if len(cache_males) > 20:
                available_females += cache_females[0]
                cache_males.pop(0)
            if len(cache_females) > 20:
                available_males += cache_males[0]
                cache_females.pop(0)
            if available_males > available_females:
                current_sex = 0
                while current_sex < available_females:
                    number_of_children_produced, boys, girls = await Breed()
                    males += boys
                    females += girls
                    population += number_of_children_produced
                    cache_males.append(boys)
                    cache_females.append(girls)
                    print(number_of_children_produced)
                    current_sex += 1
            elif available_females > available_males:
                current_sex = 0
                while current_sex < available_males:
                    number_of_children_produced, boys, girls = await Breed()
                    males += boys
                    females += girls
                    population += number_of_children_produced
                    cache_males.append(boys)
                    cache_females.append(girls)
                    print(number_of_children_produced)
                    current_sex += 1
            else:
                current_sex = 0
                while current_sex < available_males:
                    number_of_children_produced, boys, girls = await Breed()
                    males += boys
                    females += girls
                    population += number_of_children_produced
                    cache_males.append(boys)
                    cache_females.append(girls)
                    print(number_of_children_produced)
                    current_sex += 1
            
            print(f"Males: {males}",f"Females: {females}, Total Population: {population}")
            print(f'Available males: {available_males}, Available females: {available_females}')
            await asyncio.sleep(.5)
            years += 1
            print('---1 year passed---')
        if years < 20:
            print(f"Males: {males}",f"Females: {females}, Total Population: {population}")
            await asyncio.sleep(.5)
            years += 1
            print('---1 year passed---')        
            
    
def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(startGame())
    print('YEARS PASSED: ' + str(years))

main()