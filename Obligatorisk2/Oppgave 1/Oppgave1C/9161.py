# Oppgave 1C
# 9.1.6.1

tall_listen = ["+1", "+2", "-3", "-5", "zero", "+10", "+30"]

# Funksjonen endrer tallene til pos, neg eller zero. Dette avhenger av hva de har i sign
# Input :: listen med tall som inneholder om de er positivt, negativt eller zero :: list
# Output :: listen med sign :: list
def signtall(listen):
    tall_med_pos = list(filter(lambda sign: "+" in sign, listen))
    tall_med_neg = list(filter(lambda sign: "-" in sign, listen))
    tall_med_zero = list(filter(lambda sign: "zero" in sign, listen))
    return tall_med_pos, tall_med_neg, tall_med_zero
print(signtall(tall_listen))

words = ["banana", "bean", "falafel", "leaf", "Jabir"]
# Funksjonen gjør det sånn at bare ord med fem bokstaver dukker opp
# Input :: liste med ord :: list
# Output :: liste med ord med bare 5 bokstaver :: list
def ordtell(listen):
    ord_tell = list(filter(lambda wd: len(wd) == 5, words))
    return ord_tell

print(ordtell(words))


tall = [1, 2, 10, 20, 15, 11, 12, 14]

# Funksjonen gjør det sånn at den printer ut bare tall mellom 10-20 og som er parttall
# Input :: liste med tall : list
# Output :: liste med tall 10 < num > 20, som er part tall
def evennum(listen):
    even = []
    for num in listen: 
        if 10 < num < 20 and num % 2 == 0:  
            even.append(num)  
    return even  

print(evennum(tall))



