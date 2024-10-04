def calculate_water_store(hieghts_of_buildings):
    if len(hieghts_of_buildings) < 3:
        return 0
    
    left, right = 0, len(hieghts_of_buildings)-1
    left_max, right_max = hieghts_of_buildings[left], hieghts_of_buildings[right]
    water_stored = 0

    while left < right:
        if hieghts_of_buildings[left] < hieghts_of_buildings[right]:
            left += 1
            left_max = max(left_max, hieghts_of_buildings[left])
            water_stored += left_max - hieghts_of_buildings[left]
        else:
            right -= 1
            right_max = max(right_max, hieghts_of_buildings[right])
            water_stored += right_max - hieghts_of_buildings[right]
    return water_stored

heights_of_buildings = [6,2,2,3,4]
answer = calculate_water_store(heights_of_buildings)
print(f"Total Water Stored : {answer * 100} Liters")