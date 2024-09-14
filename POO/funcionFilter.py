amigos=[("Juan", 22),
        ("Maria", 19),
        ("Pedro",25),
        ("Laura", 17),
        ("Carlos", 20),
        ("Sofia", 16)]
edad= lambda datos:datos[1] >=18

amigos1=list(filter(edad,amigos))
for i in amigos1:
    print(i)
