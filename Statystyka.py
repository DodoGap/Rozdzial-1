import sys
import statistics

class Statistics:
    def __init__(self, liczby):
        self.liczby = liczby

    def sprawdzenie(self):
        for liczba in self.liczby:
            if not self.is_number(liczba):
                print("Błąd: Wszystkie argumenty powinny być liczbami.")
                sys.exit(1)

    def is_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def average(self):
        return sum(self.liczby) / len(self.liczby)

    def median(self):
        posortowane_liczby = sorted(self.liczby)
        dlugosc = len(posortowane_liczby)
        if dlugosc % 2 == 0:
            srodkowa_liczba = dlugosc // 2
            return (posortowane_liczby[srodkowa_liczba - 1] + posortowane_liczby[srodkowa_liczba]) / 2
        else:
            return posortowane_liczby[dlugosc // 2]

    def minimum(self):
        return min(self.liczby)

    def maximum(self):
        return max(self.liczby)

    def standard_deviation(self):
        return statistics.stdev(self.liczby)
    
    def zamien_przecinki(self):
        for i in range(len(self.liczby)):
            if isinstance(self.liczby[i], str):
                self.liczby[i] = self.liczby[i].replace(',', '.')

def main():
    # Pobranie argumentów z linii poleceń (bez pierwszego argumentu, który jest nazwą skryptu)
    args = sys.argv[1:]

    # Powołanie klasy Statistics
    stats = Statistics(args)

    # Zamiana przecinków na kropki
    stats.zamien_przecinki()

    # Sprawdzenie czy argumenty w klasie to liczby
    stats.sprawdzenie()

    # Zamiana z string na float
    args_float = [float(arg) for arg in args]
    stats = Statistics(args_float)

    # Obliczenie i wyświetlenie statystyk
    print("Średnia:", stats.average())
    print("Mediana:", stats.median())
    print("Minimum:", stats.minimum())
    print("Maksimum:", stats.maximum())
    print("Odchylenie standardowe:", stats.standard_deviation())

main()
