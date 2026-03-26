cadeia = input("Digite uma sequência binária:")

estado = "q0"

for algarismo in cadeia:
    if algarismo in ["0", "1"]:
        cadeia = True
    else:
        cadeia = False
        print("Cadeia inválida, use apenas 0 ou 1")

while cadeia == True:
 if estado == "q0":
    if algarismo == "0":
        estado = "q0"
    elif algarismo == "1":
        estado = "q1"

 if estado == "q1":
    if algarismo == "0":
        estado = "q0"
    elif algarismo == "1":
        estado = "q1"

 if estado == "q1":
   print("Estado final:" ,estado)
   print("Cadeia válida")
 else:
   print("Estado final:" ,estado)
   print("Cadeia inválida")
 break