class Plant:
    def __init__(self, name, height, days_old):
        self.name = name
        self.height = height
        self.days_old = days_old
    def grow(self, height) -> None:
        self.height += height
    def age(self, days_old) -> None:
        self.days_old += days_old
    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days_old} days old")

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    initial_height = 25.0
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age(1)
        rose.show()

    growth = round(30.6 - 25.0, 1)
    print(f"Growth this week: {growth}cm")