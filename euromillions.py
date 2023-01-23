import random
import json

white_possibles = list(range(1, 51))
star_possibles = list(range(1, 13))

# tickets_per_drawing = 8_060_598
# num_drawings = 1
tickets_per_drawing: int = 2
num_drawings: int = 104

total_spent: float = 0
earnings: float = 0

times_won = {
    "5+2": 0,
    "5+1": 0,
    "5": 0,
    "4+2": 0,
    "4+1": 0,
    "4": 0,
    "3+2": 0,
    "3+1": 0,
    "3": 0,
    "2+2": 0,
    "2+1": 0,
    "2": 0,
    "1+2": 0,
    "0": 0,
}


def calc_win_amt(my_numbers: set, winning_numbers: set) -> int:
    win_amt = 0

    main_matches = len(my_numbers["whites"].intersection(winning_numbers["whites"]))
    star_matches = len(my_numbers["stars"].intersection(winning_numbers["stars"]))

    if main_matches == 5:
        if star_matches == 2:
            win_amt = 57_581_725
            times_won["5+2"] += 1
        elif star_matches == 1:
            win_amt = 267_209
            times_won["5+1"] += 1
        else:
            win_amt = 29_284
            times_won["5"] += 1
            
    elif main_matches == 4:
        if star_matches == 2:
            win_amt = 1_653
            times_won["4+2"] += 1
        elif star_matches == 1:
            win_amt = 97
            times_won["4+1"] += 1
        else:
            win_amt = 33
            times_won["4"] += 1
            
    elif main_matches == 3:
        if star_matches == 2:
            win_amt = 56
            times_won["3+2"] += 1
        elif star_matches == 1:
            win_amt = 8
            times_won["3+1"] += 1
        else:
            win_amt = 7
            times_won["3"] += 1
            
    elif main_matches == 2:
        if star_matches == 2:
            win_amt = 56
            times_won["2+2"] += 1
        elif star_matches == 1:
            win_amt = 8
            times_won["2+1"] += 1
        else:
            win_amt = 7
            times_won["2"] += 1

    elif main_matches == 1 and star_matches == 2:
        win_amt = 5
        times_won["1+2"] += 1

    else:
        times_won["0"] += 1

    return win_amt


for drawing in range(num_drawings):
    white_drawing = set(random.sample(white_possibles, k=5))
    star_drawing = set(random.sample(star_possibles, k=2))
    winning_numbers: dict = {"whites": white_drawing, "stars": star_drawing}

    for ticket in range(tickets_per_drawing):
        total_spent += 2.5
        my_whites = set(random.sample(white_possibles, k=5))
        my_stars = set(random.sample(star_possibles, k=2))
        my_numbers: dict = {"whites": my_whites, "stars": my_stars}
        
        win_amt = calc_win_amt(my_numbers, winning_numbers)
        earnings += win_amt
        
print(f"Spent: £{total_spent}")
print(f"Earnings: £{earnings}")

print(json.dumps(times_won, indent=2))
print(f"Net: £{earnings - total_spent}")