alfabet = "abcdefghijklmnopqrstuvwxyz"
alfabet_majus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def enter_a_binari(enter):
    binari = format(enter, "0b")
    return binari

def text_a_ascii(txt):
    paraules = txt.split(" ")
    for paraula in paraules:
        for char in paraula:
            if char == ",":
                print(",", end="")
            else:
                if char in alfabet:
                    index = alfabet.index(char)
                    print(enter_a_binari(index), end=" ")
                elif char in alfabet_majus:
                    index = alfabet_majus.index(char)
                    print(enter_a_binari(index), end=" ")
            if paraula.index(char) == (len(paraula) - 1):
                print("  ", end="")
        if paraules.index(paraula) == (len(paraules) - 1):
            print(" ")

while True:
    text = input("->> ")
    text_a_ascii(text)
