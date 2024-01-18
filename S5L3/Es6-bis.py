def tre_numeri_piu_grandi(lista):
    if len(lista) < 3:
        print("La lista è troppo corta")
        return
    lista.sort(reverse=True)
    numeri_piu_grandi = [lista[0], lista[1], lista[2]]
    if numeri_piu_grandi[0] == numeri_piu_grandi[1] or numeri_piu_grandi[0] == numeri_piu_grandi[2] or numeri_piu_grandi[1] == numeri_piu_grandi[2]:
        print("Ci sono numeri uguali tra i primi tre")
        return

    return numeri_piu_grandi

lista = [10, 5]
risultato = tre_numeri_piu_grandi(lista)
if risultato:
    print("I tre numeri più grandi sono:", risultato)