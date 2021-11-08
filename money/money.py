import random
import asyncio
import time

async def startMoney():
  money = 25000
  day = 1

  DFT_price_per_ducky = 4 # dollars
  DFT_cost_of_production = 0.5 # dollar
  DFT_cost_of_labor_per_ducky = 0.25 # workers wages, etc
  number_of_workers = 10
  worker_pay = 500 # per 2 weeks
  rent_and_utils = 25000 # per month
  max_demand = 1000
  DFT_rate_of_production = number_of_workers * 10

  sold = 0

  while day <= 121:
    print(f"Day {day}!")
    if day == 1:
    	demand = 100 #random.randint(10, max_demand + 1)
    if day % 30 == 0:
      money -= rent_and_utils
      if money > rent_and_utils:
        print("Moving to bigger factory...")
        time.sleep(1)
        rent_and_utils = 35000
        DFT_rate_of_production += int(DFT_rate_of_production * 0.5)
    if day % 14 == 0:
      money -= worker_pay * number_of_workers
    if day == 121:
      print(f"Simulation over. Total duckys sold: {sold}. Final Balance: {money}.")
      break

    produced_duckys = DFT_rate_of_production * 10

    if demand < produced_duckys:
      cost_of_production = DFT_cost_of_production
      cost_of_labor_per_ducky = DFT_cost_of_labor_per_ducky
      cost_of_produced_duckys = produced_duckys * (cost_of_production + cost_of_labor_per_ducky)
      if day == 1:
        price_per_ducky = DFT_price_per_ducky
      gross_income = demand * price_per_ducky
      net_income = gross_income - cost_of_produced_duckys
      print(f"Demand: {demand}. Gross income: {gross_income}. Net income: {net_income}. Costs: {cost_of_produced_duckys}. Price: {price_per_ducky}.")
      money += net_income
      sold += demand
      print(f"Closing Money: {money}")
      if money > rent_and_utils and price_per_ducky >= 4 and demand >= 100:
        price_per_ducky -= 0.25
        demand += int(demand * 0.1)
      elif money < rent_and_utils:
        price_per_ducky += 0.5
        cost_of_production -= 0.25
        max_demand -= int(max_demand * 0.1)
    elif demand > produced_duckys:
      number_of_workers += 2
      rate_of_production = number_of_workers * 15
      produced_duckys += rate_of_production * 1
      cost_of_production += 0.25
      cost_of_labor_per_ducky += 0.25
      price_per_ducky += 1
      cost_of_produced_duckys = produced_duckys * (cost_of_labor_per_ducky + cost_of_production)

      gross_income = demand * price_per_ducky
      net_income = gross_income - cost_of_produced_duckys

      print(f"HIGH DEMAND: {demand}. Produced: {produced_duckys}. Gross income: {gross_income}. Net income: {net_income}. Costs: {cost_of_produced_duckys}. Price: {price_per_ducky}.")
      money += net_income
      sold += produced_duckys
      print(f"Closing Money: {money}.")
      demand -= int(demand * 0.3)
      if money > rent_and_utils and price_per_ducky > 4:
        price_per_ducky -= 0.25
        max_demand += int(max_demand * 0.1)
      elif money < rent_and_utils:
        price_per_ducky += 0.5
        cost_of_production -= 0.25
        max_demand -= int(max_demand * 0.1)
    day += 1

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(startMoney())

main()
