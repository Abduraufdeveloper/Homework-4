a = {
    "name" :"John",
    "notes":[7,4,1]
}
for x in a:
    d = "notes"[0]
    c = "notes"[1]
    e = "notes"[2]
    if d > c and e:
        print(f"Name:John" f"top_notes:{d}")
    if c > d and e:
        print(f"Name:John" f"top_notes:{c}")
    if e > d and c:
        print(f"Name:John" f"top_notes:{e}")
