import math
from collections import deque

# buffer para estabilidade
historico = deque(maxlen=5)

def suavizar_saida(gesto):
    historico.append(gesto)
    if historico.count(gesto) >= 3:
        return gesto
    return None

def gestos(lm):
    margem = 0.015  # 🔥 tolerância (ajuste fino aqui)

    indicadory = [lm[8].y, lm[7].y, lm[6].y, lm[5].y] 
    indicadorx = [lm[8].x, lm[7].x, lm[6].x, lm[5].x]

    medioy = [lm[12].y, lm[11].y, lm[10].y, lm[9].y] 
    mediox = [lm[12].x, lm[11].x, lm[10].x, lm[9].x] 

    anelary = [lm[16].y, lm[15].y, lm[14].y, lm[13].y] 
    mindinhoy = [lm[20].y, lm[19].y, lm[18].y, lm[17].y] 

    dedaoy = [lm[4].y, lm[3].y, lm[2].y, lm[1].y] 
    dedaox = [lm[4].x, lm[3].x, lm[2].x, lm[1].x]   

    # distância (mantida igual, só mais estável)
    distancia = math.sqrt((lm[8].x - lm[4].x) ** 2 + (lm[8].y - lm[4].y) ** 2)

    # 🔥 helpers com margem (mesma lógica, só mais tolerante)
    def menor(a, b): return a < b - margem
    def maior(a, b): return a > b + margem

    # ------------------------
    # GESTOS (mesma lógica)
    # ------------------------

    if (
        menor(indicadory[0], indicadory[2]) and
        maior(medioy[0], medioy[2]) and
        maior(anelary[0], anelary[2]) and
        maior(mindinhoy[0], mindinhoy[2]) and
        menor(dedaox[0], dedaox[1])
    ):
        return suavizar_saida("onlyindex")

    elif (
        menor(indicadory[0], indicadory[2]) and
        menor(medioy[0], medioy[2]) and
        maior(anelary[0], anelary[2]) and
        maior(mindinhoy[0], mindinhoy[2]) and
        menor(dedaox[0], dedaox[1])
    ):
        return suavizar_saida("index_middle")

    elif (
        menor(indicadory[0], indicadory[2]) and
        menor(medioy[0], medioy[2]) and
        menor(anelary[0], anelary[2]) and
        maior(mindinhoy[0], mindinhoy[2]) and
        menor(dedaox[0], dedaox[1])
    ):
        return suavizar_saida("index_middle_ring")

    elif (
        menor(indicadory[0], indicadory[2]) and
        menor(medioy[0], medioy[2]) and
        menor(anelary[0], anelary[2]) and
        menor(mindinhoy[0], mindinhoy[2]) and
        maior(dedaox[0], dedaox[1])
    ):
        return suavizar_saida("all_fingers")

    elif (
        maior(indicadorx[0], indicadorx[1]) and
        maior(indicadorx[1], indicadorx[2]) and
        maior(indicadorx[2], indicadorx[3]) and

        maior(dedaox[0], dedaox[1]) and
        maior(dedaox[1], dedaox[2]) and
        maior(dedaox[2], dedaox[3]) and

        maior(mediox[0], mediox[1]) and
        maior(mediox[1], mediox[2]) and
        maior(mediox[2], mediox[3]) and

        maior(anelary[0], anelary[2]) and
        maior(mindinhoy[0], mindinhoy[2]) and
        distancia > 0.05
    ):
        return suavizar_saida("diminuir_volume")

    elif (
        maior(indicadorx[0], indicadorx[1]) and
        maior(indicadorx[1], indicadorx[2]) and
        maior(indicadorx[2], indicadorx[3]) and

        maior(dedaox[0], dedaox[1]) and
        maior(dedaox[1], dedaox[2]) and
        maior(dedaox[2], dedaox[3]) and

        maior(medioy[0], medioy[2]) and
        maior(anelary[0], anelary[2]) and
        maior(mindinhoy[0], mindinhoy[2]) and
        distancia > 0.05
    ):
        return suavizar_saida("aumentar_volume")

    else:
        return None