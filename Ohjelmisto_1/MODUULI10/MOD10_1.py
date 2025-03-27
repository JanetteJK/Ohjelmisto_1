#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Elevator:
    def __init__(self, first_floor, top_floor):
        self.first_floor = first_floor
        self.top_floor = top_floor
        self.current_floor = first_floor

    def move_up(self):
        self.current_floor = self.current_floor+1
        print(f"Elevator is now on floor {self.current_floor}")

    def move_down(self):
        self.current_floor = self.current_floor-1
        print(f"Elevator is now on floor {self.current_floor}")

    def move_to_floor(self, floor):
        while self.current_floor < floor:
            elevator.move_up()
        while self.current_floor > floor:
            elevator.move_down()


elevator = Elevator(1,9)
elevator.move_to_floor(5)
elevator.move_to_floor(elevator.first_floor)



