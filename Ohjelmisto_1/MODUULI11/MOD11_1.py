class Publishing:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"The publishings name is {self.name}")

class Book(Publishing):
    def __init__(self, name, writer, pages):
        self.writer = writer
        self.pages = pages
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Written by: {self.writer}, and has {self.pages} pages.")


class Magazine(Publishing):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Edited by: {self.editor}")

publishings = []
publishings.append(Magazine("Aku Ankka", "Aki Hyyppä"))
publishings.append(Book("Hytti n:o 6", "Rosa Liksom", "200"))

for p in publishings:
    p.print_info()