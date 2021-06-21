# ambiguous calculation
# How it is O(low*high*n), it is linear i know

def ambMeasure(measuringCups, lowdiff, highdiff, low, high):
    if len(measuringCups) != 0:
        if measuringCups[-1][0] <= lowdiff and measuringCups[-1][1] <= highdiff:
            lowdiff -= measuringCups[-1][0]
            highdiff -= measuringCups[-1][1]
            return ambMeasure(measuringCups, lowdiff, highdiff, low, high)

        else:
            measuringCups.pop()
            return ambMeasure(measuringCups, lowdiff, highdiff, low, high)

    else:
        if (highdiff - lowdiff) <= (high-low):
            return True

        else:
            return False

# 2*last_cup + 1*(remaining tup cups)
measuringCups = [
    [200, 210],
    [450, 465],
    [800, 850],
]

low = 2100
high = 2300

print(ambMeasure(measuringCups, low, high, low, high))

## What is the worst case in this?