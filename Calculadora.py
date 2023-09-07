# Uma simples calculadora
# Função para somar dois números 
def add(num1, num2):
    return num1 + num2

# Função para subtração 
def subtract(num1, num2):
    return num1 - num2

# Função para multiplica dois números
def multiply(num1, num2):
    return num1 * num2

# Função para divisão
def divide(num1, num2):
    return num1 / num2

print("Selecione uma operação -\n" \
        "1. Soma\n" \
        "2. Subtração\n" \
        "3. Multiplicação\n" \
        "4. Divisão\n")

# Obtendo entradas do usuário
select = int(input("Selecione a operação 1, 2, 3, 4 :")) 

number_1 = int(input("Entre com o primeiro número: "))
number_2 = int(input("Entre com o segundo número: "))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2)) 

elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2)) 

elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
else:
    print("Entrada inválida")

