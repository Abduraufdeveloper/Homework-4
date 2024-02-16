a = int(input("enter the cost_price : "))
b = int(input("enter the sell_price : "))
c = int(input("enter the inventory : "))
d = {
    "cost_price":a,
    "sell_price":b,
    "inventory":c
}
for x in d:
    e = a + b + c
    s = round(e)
    print(s)