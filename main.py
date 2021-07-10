import random
import asyncio

GENDERS = ['male', 'female']
MIN_NUMBER_OF_CHILDREN = 0
MAX_NUMBER_OF_CHILDREN = 3

async def Breed():
    children_produced = random.randint(MIN_NUMBER_OF_CHILDREN, MAX_NUMBER_OF_CHILDREN)
    current_child = 0
    males = 0
    females = 0
    while current_child < children_produced:
        child_sex = random.choice(GENDERS)
        print(child_sex)
        if child_sex == 'male':
            males = males + 1
        else:
            females = females + 1
        current_child = current_child + 1
    
    return children_produced, males, females
    
async def startGame():
    population = 0
    males = 2
    females = 1

    while population < 1000000:
        if males > females:
            current_sex = 0
            if current_sex < females:
                number_of_children_produced, boys, girls = await Breed()
                males += boys
                females += girls
                population += number_of_children_produced
                print(population, number_of_children_produced)
        elif females > males:
            current_sex = 0
            if current_sex < males:
                number_of_children_produced, boys, girls = await Breed()
                males += boys
                females += girls
                population += number_of_children_produced
                print(population, number_of_children_produced)
        else:
            current_sex = 0
            if current_sex < males:
                number_of_children_produced, boys, girls = await Breed()
                males += boys
                females += girls
                population += number_of_children_produced
                print(population, number_of_children_produced)

        print(males, females)
        await asyncio.sleep(1)
        print('---1 year passed---')

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(startGame())

main()