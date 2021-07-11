import random
import asyncio

CHANCE_OF_INFECTION = 34
MIN_NUMBER_OF_PEOPLE_MET_DAILY = 0
MAX_NUMBER_OF_PEOPLE_MET_DAILY = 15
POPULATION = 10

async def Infect():
    number_of_people_met = random.randint(MIN_NUMBER_OF_PEOPLE_MET_DAILY, MAX_NUMBER_OF_PEOPLE_MET_DAILY)
    if number_of_people_met > 0:
        for i in range(number_of_people_met):
            calculate_infection = random.randint(0, 1000)
            if calculate_infection < CHANCE_OF_INFECTION:
                is_infected = True
                return is_infected
            else:
                is_infected = False
        return is_infected
    else:
        is_infected = False
        return is_infected

async def startSimulation():
    global infected
    infected = 0
    for i in range(POPULATION):
        is_infected = await Infect()
        if is_infected:
            infected += 1

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(startSimulation())
    #print('YEARS PASSED: ' + str(years))
    print('Number of Infections: ' + str(infected))

main()