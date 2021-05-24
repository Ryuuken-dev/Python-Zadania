"""
Szkielet rozwiązania: https://repl.it/repls/SoftRequiredIrc
Przykładowe dane: https://repl.it/repls/SpectacularEnragedKnowledge
Korzystając z klasy Kot, stwórz małą symulację, w której jest kot idący sobie gdzieś wzdłuż korytarza. Po
drodze mija dużo pudełek z losowymi zabawkami (ale w każdym pudełku jest tylko jeden rodzaj zabawek).

Kiedy napotyka pudełko, widzi trzymane tam zabawki i losowo wybierana jest jedna z poniższych opcji:

    1. Kot przechodzi obok zabawki obojętnie,
    2. Jest zachwycony zabawką i uznaje, że ją lubi,
    3. Stwierdza, że jeśli ją lubił, to najwyższy czas ją teraz znienawidzić.

Później kot idzie dalej, znów sprawdza co tam jest i decyduje co robić. Symulacja kończy się po zadanej z
góry liczbie iteracji (np. 100). Po zakończeniu kot mówi nam, które zabawki polubił, a które nie i ile ich
było. Dla uproszczenia, zakładamy że kot napotyka pudełko na każdym kroku. Bywa, że w wielu pudełkach
są te same zabawki.

Lista zabawek jest wczytywana z pliku, który najpierw trzeba stworzyć na swoim komputerze i wypełnić
jakąś zawartością. Można zrobić swoją listę zabawek albo wykorzystać tą podaną pod linkiem podanym w
materiałach. Funkcja wczytująca plik i zwracająca listę znajdujących się tam elementów jest już gotowa w
szkielecie rozwiązania.
"""
from Cat import Cat
from Box import Box


cat = Cat()
box = Box()
box.unpack()
for _ in range(1, 6):
    box.add_toy()
    cat.verify(box)

print(cat.get_results())

