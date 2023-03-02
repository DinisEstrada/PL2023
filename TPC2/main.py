import sys

on = True
total = 0
numbers = ""

print("Insira o texto desejado: ")
print("[Para terminar, carregue Ctrl + D]")
line = sys.stdin.read().upper()

for i in range(0,len(line)):
    if on and line[i].isdigit():
        numbers += line[i] 
    elif on and numbers != "":
        total += int(numbers)
        numbers = ""
    if line[i] == "=":
        print(f"A soma total é {total}")
    elif line[:3] == "OFF":
        on = False
    elif line[:2] == "ON":
        on = True