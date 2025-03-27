class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

class Kuukausipalkkainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        super().__init__(etunimi, sukunimi)
        self.kuukausipalkka = kuukausipalkka
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'   - Kuukausipalkka on {self.kuukausipalkka}€ ') # metodin ylikirjoittaminen.

class Tuntipalkkainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = tuntipalkka
    def tulosta_tiedot(self):
            super().tulosta_tiedot()
            print(f'   - Tuntipalkka on {self.tuntipalkka}€ ')
    def tulosta_nimi(self):
        print(f'{self.etunimi} {self.sukunimi}')

työntekijät = []
työntekijät.append(Työntekijä("Viivi", "Virta"))
työntekijät.append(Työntekijä("Ahmed", "Habib"))
työntekijät.append(Kuukausipalkkainen("Pera", "Lahti", 4500.0))
työntekijät.append(Tuntipalkkainen("Liisa", "Vuori", 50.0))

työntekijät[-1].tulosta_nimi()

#for t in työntekijät:
    #t.tulosta_tiedot()
