def obter_valor_maior(num1: int, num2: int) -> int:
    if num1 < num2:
        return num2

    return num1

   #*Outra possibilidade de fazer em apenas um linha
   #return num1 if num1>num2 else num2

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
maior = obter_valor_maior(num1, num2)

print(f"O maior valor é o {maior}.")
