def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    
    def count(current_day, total_days):
        if current_day > total_days:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        count(current_day + 1, total_days)
    
    count(1, days)