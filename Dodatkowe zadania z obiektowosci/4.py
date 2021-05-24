"""
Przygotuj klasę Worker. Klasa ta powinna przechowywać informację o imieniu, nazwisku oraz o stawce godzinowej pracownika.
Stawka godzinowa powinna być polem prywatnym. Dostęp do tego pola jest możliwy poprzez metody get_brutto_hourly_rate()
oraz get_netto_hourly_rate(). W przypadku netto, wartość stawki powinna być pomniejszana o 19%.
"""


class Worker:
    def __init__(self, name: str, surname: str, rate: float):
        self._rate = rate
        self.surname = surname
        self.name = name

    def get_brutto_hourly_rate(self):
        return self._rate

    def get_netto_hourly_rate(self):
        return round(self._rate - (self._rate * 0.19), 2)


def test_get_brutto_method():
    kowalski = Worker('Jan', 'Kowalski', 19.50)

    assert kowalski.get_brutto_hourly_rate() == 19.50


def test_get_netto_method():
    kowalski = Worker('Jan', 'Kowalski', 19.50)

    assert kowalski.get_netto_hourly_rate() == round(19.50 - (19.50 * 0.19), 2)
