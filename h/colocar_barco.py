def colocar_barco():
    n_barcos = 0
    while n_barcos not in range(1, 6):
        try:
            n_barcos = int(input("¿Con cuántos barcos quiere jugar? [1,5]: "))
        except ValueError:
            n_barcos = 0
        if n_barcos not in range(1, 6):
            print("Por favor, introduzca un número entre 1 y 5.")

    posicion_barcos = []
    letras = "abcdefghijklmnop"
    numeros = [str(num) for num in range(1, 17)]

    for len_barco in range(2, n_barcos+2):
        cond_0, cond_1, cond_2, cond_3, cond_4 = False, False, False, False, True

        while not all((cond_0, cond_1, cond_2, cond_3, cond_4)):
            
            cond_0, cond_1, cond_2, cond_3, cond_4 = False, False, False, False, True

            prov = input(f"Introduzca la posición del barco de longitud {len_barco} (ejemplo: 'a4 a7', extremos incluidos): ").split()

            if len(prov) == 2 and len(prov[0]) in (2,3) and len(prov[1]) in (2,3):
                cond_0 = True

                if prov[0][0] in letras and prov[0][1:] in numeros:
                    cond_1 = True
                else:
                    cond_1 = False

                if prov[1][0] in letras and prov[1][1:] in numeros:
                    cond_2 = True
                else:
                    cond_2 = False

                if cond_1 and cond_2:
                    if prov[0][0] == prov[1][0] and abs(int(prov[0][1:])-int(prov[1][1:]))+1 == len_barco:
                        cond_3 = True
                        horizontal = True
                    elif prov[0][1:] == prov[1][1:] and abs(letras.find(prov[0][0])-letras.find(prov[1][0]))+1 == len_barco:
                        cond_3 = True
                        horizontal = False
                    else:
                        cond_3 = False

                    if cond_3:
                        if horizontal:
                            barco = tuple([f"{prov[0][0]}{num}" for num in range(int(prov[0][1:]), int(prov[1][1:])+1)])
                        else:
                            barco = tuple([f"{letter}{prov[0][1:]}" for letter in letras[letras.find(prov[0][0]):letras.find(prov[1][0])+1]])

                        for barco_antiguo in posicion_barcos:
                            if not all(coord not in barco_antiguo for coord in barco):
                                cond_4 = False

            else:
                cond_0 = False

            if not all((cond_0, cond_1, cond_2, cond_3, cond_4)):
                print("\nPor favor, introduzca un valor de inicio y uno de fin de posición de barco adecuados.\n")
            
        posicion_barcos.append(barco)

    return posicion_barcos
