def convertCelToFar(tempCel):
    tempFar = tempCel * (9/5) + 32
    return tempFar

    

def convertFarToCel(tempFar):
    tempCel = (tempFar - 32) * (5 / 9)
    return tempCel

tempFar = input('Write temp in F:')
tempCel = convertFarToCel(float(tempFar))

print(f'{tempFar} degrees F = {tempCel:.2f} degress C')


tempCel = input('Write temp in C:')
tempFar = convertCelToFar(float(tempCel))

print(f'{tempCel} degrees C = {tempFar:.2f} degrees F')
