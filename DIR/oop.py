class Table:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

    def __str__(self):
        return f"Table(name='{self.name}', quality='{self.quality}')"

    def test(self):
        print(f"The table is {self.name}")

table1 = Table("Wood", "GOOD")
print(table1)
