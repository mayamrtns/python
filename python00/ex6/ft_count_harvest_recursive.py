def ft_count_harvest_recursive(today=1):
    daysuntil = int(input("Days until harvest: "))
    if(today > daysuntil):
        print("Harvest time!")
    else:
        print("Day", today)
        ft_count_harvest_recursive(today + 1)
