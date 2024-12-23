def calculate_total_points():
    D1, D2, D3 = map(int, input().strip().split())
    total_levels = int(input().strip())
    points = 0

    if total_levels > 0:
        level1 = min(total_levels, 3)
        points += level1 * D1
        total_levels -= level1
    
    if total_levels > 0:
        level2 = min(total_levels, 4)
        points += level2 * D2
        total_levels -= level2
    

    if total_levels > 0:
        points += total_levels * D3
    

    print(points)

calculate_total_points()