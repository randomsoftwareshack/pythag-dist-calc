import math

def distCalculation(coord1, coord2, roundPlaces = None):
    if len(coord1) != len(coord2):
        raise Exception("Error; the two coordinates have a different number of dimensions")

    total = 0

    for i in range(len(coord1)):
        total += calcDifSq(coord1[i], coord2[i])

    return math.sqrt(total) if roundPlaces is None else round(math.sqrt(total), roundPlaces)
            


def calcDifSq(coord1, coord2):
    return (coord1 - coord2) ** 2
    

