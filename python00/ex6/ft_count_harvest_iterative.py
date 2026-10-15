def ft_count_harvest_iterative():
    daysuntil = int(input("Days until harvest: "))
    today = 1
    while (today <= daysuntil):
        print("Day", today)
        today += 1
    print("Harvest time!")
