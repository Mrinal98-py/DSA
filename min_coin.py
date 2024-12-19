price = 12

coin1 = 1 
coin2 = 2
coin3 = 5

demand_coin1 = 0
demand_coin2 = 0
demand_coin3 = 0

while price > 0:
    if price >= coin3:
        req_coin3 = price // coin3
        remain_price = price - (coin3 * req_coin3)
        price = remain_price
        demand_coin3 = req_coin3
    elif price >= coin2:
        req_coin2 = price // coin2
        remain_price = price - (coin2 * req_coin2)
        price = remain_price
        demand_coin2 = req_coin2

    elif price >= coin1:
        req_coin1 = price // coin1
        remain_price = price - (coin1 * req_coin1)
        price = remain_price
        demand_coin1 = req_coin1
        
    else:
        break

print(coin1,"demand:",demand_coin1,",cost:",demand_coin1*1 )
print(coin2,"demand:",demand_coin2,",cost:",demand_coin2*2)
print(coin3,"demand:",demand_coin3,",cost:",demand_coin3*5)

print("Total no of coin req:",demand_coin1+demand_coin2+demand_coin3)
print("Total price:",demand_coin1*1+demand_coin2*2+demand_coin3*5)


    