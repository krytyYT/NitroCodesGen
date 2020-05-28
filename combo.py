import os
import sys
import string
import pyfiglet
import random

def save(code):
    file = open("combo.txt", 'a')
    write_code = code + "\n"
    file.write(write_code)
    file.close()

os.system("cls")
result = pyfiglet.figlet_format("Discord Combo Maker", font = "slant") 
print(result)
print("\n         github.com/krytyYT/NitroCodesGen\n\n")
option = str(input("    [?] Generate codes with links? (Y/n): "))
option2 = int(input("    [?] How many?: "))
for x in range(option2):
    if option == "y":
        print("tak to dziala xD")
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        code = "https://discord.gift/" + code
        save(code)
        print("Generated: " + code)
    else:
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        save(code)
        print("Generated: " + code)
option3 = str(option2)
print("Saved " + option3 + " codes to combo.txt file!")
os.system("pause")