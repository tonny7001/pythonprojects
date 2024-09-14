tienda= [('camisa', 20.00),
         ('Pantalon', 25.00),
         ('Chaqueta', 50.00),
         ('medias',10.00)]
fun_euro=lambda  datos:(datos[0],datos[1] *0.96)

fun_pesos=lambda datos:(datos[0], datos[1]*4.000)

tienda2=list(map(fun_pesos, tienda))

for i in tienda2:
    print(i)



