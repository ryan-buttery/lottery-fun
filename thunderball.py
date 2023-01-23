import random
import json

white_possibles = list(range(1, 40))
thunderball_possibles = list(range(1, 15))

tickets_per_drawing = 4
num_drawings = 52

total_spent = 0
earnings = 0

times_won = {
    "5+P": 0,
    "5": 0,
    "4+P": 0,
    "4": 0,
    "3+P": 0,
    "3": 0,
    "2+P": 0,
    "1+P": 0,
    "P": 0,
    "0": 0,
}


def calc_win_amt(my_numbers: set, winning_numbers: set) -> int:
    win_amt = 0

    white_matches = len(my_numbers["whites"].intersection(winning_numbers["whites"]))
    power_match = my_numbers["thunderball"] == winning_numbers["thunderball"]

    if white_matches == 5:
        if power_match:
            win_amt = 500_000
            times_won["5+P"] += 1
        else:
            win_amt = 5_000
            times_won["5"] += 1

    elif white_matches == 4:
        if power_match:
            win_amt = 250
            times_won["4+P"] += 1
        else:
            win_amt = 100
            times_won["4"] += 1

    elif white_matches == 3:
        if power_match:
            win_amt = 20
            times_won["3+P"] += 1
        else:
            win_amt = 10
            times_won["3"] += 1

    elif white_matches == 2 and power_match:
        win_amt = 10
        times_won["2+P"] += 1

    elif white_matches == 1 and power_match:
        win_amt = 5
        times_won["1+P"] += 1

    elif power_match:
        win_amt = 3
        times_won["P"] += 1

    else:
        times_won["0"] += 1

    return win_amt


for drawing in range(num_drawings):
    white_drawing = set(random.sample(white_possibles, k=5))
    red_drawing = random.choice(thunderball_possibles)
    winning_numbers = {"whites": white_drawing, "thunderball": red_drawing}

    for ticket in range(tickets_per_drawing):
        total_spent += 1
        my_whites = set(random.sample(white_possibles, k=5))
        my_red = random.choice(thunderball_possibles)
        my_numbers = {"whites": my_whites, "thunderball": my_red}
        win_amt = calc_win_amt(my_numbers, winning_numbers)
        earnings += win_amt

print(f"Spent: £{total_spent}")
print(f"Earnings: £{earnings}")

print(json.dumps(times_won, indent=2))
print(f"Net: £{earnings - total_spent}")
