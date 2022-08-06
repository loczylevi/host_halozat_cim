

#elso_bin --> ip cim binárisba
#n_elso_bin --> netmaszk binárisba

elso_bin = "11000000101010000000000100000000"
n_elso_bin = "11111111111111111111111100000000"
host = ""
halozat = ""

index = 0
for netmaszk in n_elso_bin:
    if netmaszk == "0":
        host = host + elso_bin[index]
        index = index + 1
    elif netmaszk == "1":
        halozat = halozat + elso_bin[index]
        index = index + 1
        
print(f"hostocska uwu: {host}")
print(f"halozatocska gg: {halozat}")




