import random
import asyncio


SEXES = ['male', 'female']
POPULATION = 2
CHANCE_OF_REPRODUCING_GENE = 0.02
CHILDREN = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3]

async def Breed(number_of_people_with_gene):
    chance_of_reproducing_gene = (number_of_people_with_gene // POPULATION) / CHANCE_OF_REPRODUCING_GENE
    calculate_chance = random.randint(0, POPULATION)
    number_of_children = random.choice(CHILDREN)
    child_sex = random.choice(SEXES)
    male = 0
    female = 0
    if number_of_children < 0:
        if calculate_chance < chance_of_reproducing_gene:
            has_gene = True
        else:
            has_gene = False
        if child_sex == 'male':
            male += 1
        elif child_sex == 'female':
            female += 1
        return has_gene, number_of_children, male, female
    else:
        return False, 0, 'none'

async def startSimulation():
    population = POPULATION
    females = 1
    males = 2
    available_females = 0
    number_of_people_gene = 0
    global years
    years = 18
    female_cache = []
    male_cache = []
    for i in range(available_females):
        has_gene, number_of_children, boys, girls= await Breed(number_of_people_gene)
        males += boys
        females += girls
        population += number_of_children
        if has_gene:
            number_of_people_gene += 1
        print(number_of_people_gene)
    print(population)

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(startSimulation())
    print('YEARS PASSED: ' + str(years))

main()
