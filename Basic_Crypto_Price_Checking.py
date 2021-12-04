import requests
import time

print("QUEL COIN TU VEUX CHECKER MON BRO ? ")

coin = input().lower()
r1 = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=" + coin + "&vs_currencies=EUR")
price2=r1.json()[coin]["eur"]
print("TOUT LES COMBIEN DE SECONDES BB ?")
intervalle = int(input())
while True:
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=" + coin + "&vs_currencies=EUR")
    price = r.json()[coin]["eur"]
    print(price,"€")
    print(((price-price2)/price2)*100,"%")
    price2 = price
    print()
    time.sleep(intervalle)