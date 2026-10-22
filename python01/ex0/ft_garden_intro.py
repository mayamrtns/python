def ft_garden_intro(plant_name: str, plant_height: int, plant_age: int):
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant_name}")
    print(f"Height: {plant_height}cm")
    print(f"Age: {plant_age} days\n")
    print("=== End of Program ===")

if __name__ == "__main__":
    plant_name = "Rose"
    plant_height = 25
    plant_age = 30
    ft_garden_intro(plant_name, plant_height, plant_age)
