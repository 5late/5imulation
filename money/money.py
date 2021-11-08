import random
import asyncio

async def startMoney():
  money = 15000
  day = 1

  rate_of_production = 100 # per hour
  price_per_ducky = 4 # dollars
  cost_of_production = 0.5 # dollar
  cost_of_labor_per_ducky = 0.5 # workers wages, etc
  rent_and_utils = 15000 # per month

  while day < 91:
    print(f"Day {day}!")
    demand = random.randint(0,1000)
    if day % 30 == 0:
      money -= rent_and_utils

    produced_duckys = rate_of_production * 10
    cost_of_produced_duckys = produced_duckys * (cost_of_production + cost_of_labor_per_ducky)

    if demand < produced_duckys:
      gross_income = demand * price_per_ducky
      net_income = gross_income - cost_of_produced_duckys
      print(f"Demand: {demand}. Gross income: {gross_income}. Net income: {net_income}. Costs: {cost_of_produced_duckys}.")
      money += net_income
      print(f"Closing Money: {money}")
    day += 1

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(startMoney())

main()