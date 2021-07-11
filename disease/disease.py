import random
import asyncio

CHANCE_OF_INFECTION = 34
MIN_NUMBER_OF_PEOPLE_MET_DAILY = 0
MAX_NUMBER_OF_PEOPLE_MET_DAILY = 15
POPULATION = 1000
DAYS = 7

async def Infect():
    number_of_people_met = random.randint(MIN_NUMBER_OF_PEOPLE_MET_DAILY, MAX_NUMBER_OF_PEOPLE_MET_DAILY)
    if number_of_people_met > 0:
        for i in range(number_of_people_met):
            calculate_infection = random.randint(0, 1000)
            if calculate_infection < CHANCE_OF_INFECTION:
                is_infected = True
                return is_infected, number_of_people_met
            else:
                is_infected = False
        return is_infected, number_of_people_met
    else:
        is_infected = False
        return is_infected, number_of_people_met

async def startSimulation():
    global infected_population
    infected_population = 0
    healthy_population = POPULATION
    cache = []
    for day in range(DAYS):
        for i in range(healthy_population):
            is_infected, number_of_people_met = await Infect()
            if is_infected:
                infected_population += 1
                healthy_population -= 1
            print(f'Number of people met: {number_of_people_met}, Infected: {is_infected}')
        cache.append(infected_population)
        if day == 0:
            print(f'Infected today: {cache[0]}')
        else:
            print(f'Infected today: {cache[day] - cache[day -1]}, Total Infected: {cache[day]}')
        print('---1 day passed---')
        await asyncio.sleep(1)

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(startSimulation())
    #print('YEARS PASSED: ' + str(years))
    print('Number of Infections: ' + str(infected_population))

main()
