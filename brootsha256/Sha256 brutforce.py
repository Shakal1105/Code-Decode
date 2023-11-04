import hashlib, random
#######################data##########################
target = "87860d89fdca605c8c4f4117affbf9f68e3c5e13ea48e6f1467521cb4b24b300"
kwarg={"name":"Taras", "day":"15", "mounth":"04", "year":"98"}
###################script############################
label1 = ["day", "mounth", "year"]
passwords = []

def generate():
    name = kwarg["name"][0:3]
    listname = {}
    aaa=0
    aa = 0
    for i in name:
        listname[aaa] = [i.lower(), i.upper()]
        aaa+=1
    while aa < 42:
        a = random.choice(listname[0]) + random.choice(listname[1]) + random.choice(listname[2])
        label2 = label1.copy()
        for i in range(0, 3):
            enter = random.choice(label2)
            a = a + kwarg[enter]
            label2.remove(enter)

        if a not in passwords:
            passwords.append(a)
            aa += 1
    with open("passwords.txt", "w+") as file:
        for i in passwords:
            file.write(f"{i}\n")

generate()

for line in passwords:
    password = line.strip()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if hashed_password == target:
        print(f"Пароль найден: {password}, text = {hashed_password}")
        break

