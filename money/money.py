import random
import asyncio
import time

async def useExtra(extra, demand):
  if extra > demand:
    extra = int(extra - demand)
  else:
    extra = extra
  cost = 0
  return extra, cost

async def human(money):
  return '{:0,.2f}'.format(money)

async def mess():
  count = random.randint(0, 20)
  if count == 1:
    return True
  return False

async def startMoney():
  DFT_money = 30000
  money = DFT_money
  day = 1

  DFT_price_per_ducky = 4 # dollars
  DFT_cost_of_production = 0.5 # dollar
  DFT_cost_of_labor_per_ducky = 0.25 # workers wages, etc
  number_of_workers = 10
  worker_pay = 1000 # per 2 weeks
  rent_and_utils = 25000 # per month
  max_demand = 1000
  DFT_rate_of_production = number_of_workers * 10

  sold = 0
  extra = 0
  paychecks = []

  while day <= 181:
    print(f"Day {day}!")
    if day == 1:
    	demand = 100 #random.randint(10, max_demand + 1)
    if day % 30 == 0:
      money -= rent_and_utils
      if money > rent_and_utils:
        print("Moving to bigger factory...")
        if await mess():
          print("Catastrophe occured while moving, demand drops to 0, workers quit, rate of production suffers!")
          time.sleep(2)
          DFT_rate_of_production -= int(DFT_rate_of_production * 0.25)
          number_of_workers -= int(number_of_workers * 0.2)
          demand = 0
        else:
          time.sleep(1)
          rent_and_utils += 10000
          DFT_rate_of_production += int(DFT_rate_of_production * 0.5)
          number_of_workers += int(number_of_workers * 0.5)
    if day % 14 == 0:
      money -= worker_pay * number_of_workers
      paychecks.append(worker_pay * number_of_workers)
    if day % 60 == 0:
      new_cost = int(input("Please set a new price: "))
      if new_cost > (price_per_ducky * 2):
        demand = int(demand * 0.45)
      elif new_cost > (price_per_ducky * 3):
        demand = int(demand * 0.75)
      price_per_ducky = new_cost
    if day == 181:
      print(f"Simulation over. Total duckys sold: {sold}. Extra Produced: {extra}. Final Balance: ${await human(money)}.")
      print(f"Paid {await human(len(paychecks))} paychecks to {number_of_workers} workers, totalling ${await human(sum(paychecks))}.")
      print(f"${await human(money - DFT_money)} total profit gained.")
      break

    if day == 1:
      rate_of_production = DFT_rate_of_production

    produced_duckys = rate_of_production * 8

    if demand < produced_duckys:
      if extra > demand:
        extrafunc, cost = await useExtra(extra, demand)
        extra = extrafunc
        cost_of_produced_duckys = cost
      else:
        extra += (produced_duckys - demand)
        cost_of_produced_duckys = int(produced_duckys * (DFT_cost_of_production + DFT_cost_of_labor_per_ducky))
      rate_of_production = (demand // number_of_workers) + (demand * 0.1)
      cost_of_production = DFT_cost_of_production
      cost_of_labor_per_ducky = DFT_cost_of_labor_per_ducky
      #cost_of_produced_duckys = int(produced_duckys * (cost_of_production + cost_of_labor_per_ducky))
      if day == 1:
        price_per_ducky = DFT_price_per_ducky
      gross_income = demand * price_per_ducky
      net_income = int(gross_income - cost_of_produced_duckys)
      print(f"Demand: {demand}. Gross income: {await human(gross_income)}. Net income: {await human(net_income)}. Costs: {await human(cost_of_produced_duckys)}. Price: {price_per_ducky}.")
      money += net_income
      sold += demand
      print(f"Closing Money: {await human(money)}")

      if money > rent_and_utils and price_per_ducky >= 4 and demand >= 250:
        price_per_ducky += int(price_per_ducky * 0.25)
        cost_of_production += int(cost_of_production * 0.3)
        demand -= int(demand * 0.25)
      elif money < rent_and_utils and price_per_ducky >= 4:
        price_per_ducky -= 0.5
        cost_of_production -= 0.25
        demand += int(demand * 0.25)

    elif demand > produced_duckys:
      extra += int(produced_duckys - demand)
      number_of_workers += 5
      rate_of_production = int(number_of_workers * 15)
      produced_duckys += rate_of_production * 1
      cost_of_production += 0.25
      cost_of_labor_per_ducky += 0.25
      price_per_ducky += 1
      cost_of_produced_duckys = int(produced_duckys * (cost_of_labor_per_ducky + cost_of_production))

      gross_income = demand * price_per_ducky
      net_income = gross_income - cost_of_produced_duckys

      print(f"HIGH DEMAND: {demand}. Produced: {produced_duckys}. Gross income: {await human(gross_income)}. Net income: {await human(net_income)}. Costs: {await human(cost_of_produced_duckys)}. Price: {await human(price_per_ducky)}.")

      money += net_income
      sold += produced_duckys
      print(f"Closing Money: {await human(money)}.")
      demand -= int(demand * 0.3)
      if money > rent_and_utils and price_per_ducky > 4 and demand >= 100:
        price_per_ducky += int(price_per_ducky * 0.25)
        demand -= int(demand * 0.25)
      elif money < rent_and_utils:
        price_per_ducky -= int(price_per_ducky * 0.25)
        cost_of_production -= 0.25
        demand += int(demand * 0.25)
    demand += int(random.randint(0, int(demand // 8)) + 5)
    day += 1

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(startMoney())

main()
