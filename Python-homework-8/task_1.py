# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
list = [i for i in range(10)]
print(list)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for i in list:
    if i % 2 == 0:
        print(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i+=1

# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {
    "name": "John",
    "age": 35,
    "city": "New York"
}
for key, value  in person.items():
    print (key, value)

# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix = [[2,3,4], [5,6,7], [8,9,10]]
for row in matrix:
    for num in row:
        print(f"{num}")
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
for i in range(1,8,2):
    print(i)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
fruit_list = ["banana","apples","cherries", "kiwi"]
for i, fruit in enumerate(fruit_list):
    print(i, fruit)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
names = ["John","Nick","Kyle"]
ages = [45,25,35]
for name, age in zip(names, ages):
    print (name, age)
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
num_list = [i for i in range(10)]
print(num_list)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
i = 1
while i > 50:
    print(num_list[i])
    num_list = [i + 1 for i in range(len(num_list))]
    
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
number_list = [i for i in range(100)]
print(number_list)
number_list = [i**2 for i in range(len(number_list))]
print(number_list)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(11):
    print(i * 7)
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
lista_de_liste = [[2,3], [4,5], [1,2]]
for i,j in lista_de_liste:
    print(i,j)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
rinduri = int(input("Introduceti numarul de rinduri: "))
coloane = int(input("Introduceti numarul de coloane: "))
for i in range(rinduri):
    for j in range(coloane):
        print("*", end="")
    print()

# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(7):
    for j in range(i):
        print(j+1, end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(5):  
    for j in range(i,5):
        print(5-j, end="")
    print()   
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
for i in range(7):
    for j in "abcdefg":
        print(j, end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
