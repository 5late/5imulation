import random
import asyncio

SEXES = ['male', 'female']
CHILDREN = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]

async def Breed():
    children_produced = int(random.choice(CHILDREN))
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
    cache_females = [1]
    cache_males = [2]
    second_cache_females = []
    third_cache_females = []

    while population < 1000000:
        if years >= 18:
            if years % 80 == 0:
                global number_of_dead_people
                number_of_dead_people = round((available_males + available_females) * 0.56)
                available_females -= (number_of_dead_people // 2)
                available_males -= (number_of_dead_people // 2)
                print(f'Dying People: {number_of_dead_people}')
            if len(cache_males) > 1:
                available_males += cache_males[0]
                cache_males.pop(0)
            if len(cache_females) > 1:
                available_females += cache_females[0]
                cache_females.pop(0)
                available_females -= second_cache_females[0]
                second_cache_females.pop(0)
            if available_males > available_females:
                for i in range(available_females):
                    number_of_children_produced, boys, girls = await Breed()
                    males += boys
                    females += girls
                    population += number_of_children_produced
                    cache_males.append(available_males // 2)
                    cache_females.append(available_males // 2)
                    #print(number_of_children_produced)
            else:
                for i in range(available_males):
                    number_of_children_produced, boys, girls = await Breed()
                    males += boys
                    females += girls
                    population += number_of_children_produced
                    cache_males.append(available_males // 2)
                    cache_females.append(available_males // 2)
                    #print(number_of_children_produced)
            second_cache_females.append(cache_females[0])
            third_cache_females.append(second_cache_females[0])
            available_females += third_cache_females[0]
            third_cache_females.pop(0)

            
            print(f"Males: {males}",f"Females: {females}, Total Population: {population}, Year: {years}")
            print(f'Available males: {available_males}, Available females: {available_females}.')
            await asyncio.sleep(.15)
            years += 1
            print('---1 year passed---')
        if years < 18:
            print(f"Males: {males}",f"Females: {females}, Total Population: {population}")
            await asyncio.sleep(.1)
            years += 1
            print('---1 year passed---')        
            
    
def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(startGame())
    print('YEARS PASSED: ' + str(years))

main()