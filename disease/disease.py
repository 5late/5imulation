import random
import asyncio

CHANCE_OF_INFECTION = 0.034
MIN_NUMBER_OF_PEOPLE_MET_DAILY = 0
MAX_NUMBER_OF_PEOPLE_MET_DAILY = 15
POPULATION = int(1000000)
ROUND_TO = int(len(str(POPULATION)[1:]))
DAYS = 10
RECOVERY_DAYS = 2

async def Infect(infected_population):
    number_of_people_met = int(random.randint(MIN_NUMBER_OF_PEOPLE_MET_DAILY, MAX_NUMBER_OF_PEOPLE_MET_DAILY))
    if number_of_people_met > 0:
        chance_of_being_infected = round(number_of_people_met *((int(infected_population) / POPULATION ) / CHANCE_OF_INFECTION), ROUND_TO)
        if str(chance_of_being_infected).split('.')[0] == "0":
            infect_chance_whole_number = int(str(chance_of_being_infected).split('.')[1])
        else:
            infect_chance_whole_number = int(str(chance_of_being_infected).split('.')[0])
        for i in range(number_of_people_met):
            calculate_infection = random.randint(0, POPULATION)
            if calculate_infection < infect_chance_whole_number:
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
    infected_population = 2
    healthy_population = POPULATION
    cache = []
    infection_cache = []
    total_people_met = 0
    for day in range(DAYS):
        if day % RECOVERY_DAYS == 0 and day > 0:
            healthy_population += infection_cache[day - RECOVERY_DAYS]
            infected_population -= infection_cache[day - RECOVERY_DAYS]
        for i in range(POPULATION):
            is_infected, number_of_people_met = await Infect(infected_population)
            total_people_met += number_of_people_met
            if is_infected:
                infected_population += 1
                healthy_population -= 1
        cache.append(infected_population)
        infection_cache.append(infected_population)
        if day == 0:
            print(f'Infected today: {cache[0]}')
        else:
            print(f'Infected today: {cache[day] - cache[day -1]}, Total Infected: {cache[day]}, Total Healthy: {healthy_population}, Day: {day}')
        print(f'{total_people_met} interactions overall')
        print('---1 day passed---')
        await asyncio.sleep(1)

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(startSimulation())
    print('Total Number of Infections: ' + str(infected_population))

main()
