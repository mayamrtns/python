def ft_plant_age():
    cycles = int(input("Enter plant age in days: "))
    if cycles > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
    return cycles * 60
