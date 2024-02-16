p1 = input("Yoshingizni kiriting : ")
p2 = input("Yoshingizni kiriting : ")
p3 = input("Yoshingizni kiriting : ")

a = {
    "Jake" : int(p1),
    "Mike" : int(p2),
    "Max" : int(p3)
}
for x in p1 and p2 and p3:
    if p1 > p2 :
        print("jake mendan katta")
    if p1 == p2 :
        print("Mike meni tengdoshim ")
    if p1 < p3:
        print("Max mendan kichkina ")
