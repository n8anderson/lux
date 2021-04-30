import pandas as pd

def test_opacity():
    dataset = [
        {"special.char": 1, "normal": 2},
        {"special.char": 1, "normal": 2},
        {"special.char": 1, "normal": 5},
        {"special.char": 1, "normal": 2},
        {"special.char": 1, "normal": 3},
        {"special.char": 1, "normal": 2},
        {"special.char": 1, "normal": 6},
        {"special.char": 1, "normal": 2},
        {"special.char": 1, "normal": 7},
        {"special.char": 1, "normal": 2},
        {"special.char": 3, "normal": 10},
        {"special.char": 1, "normal": 1},
        {"special.char": 5, "normal": 2},
        {"special.char": 1, "normal": 2},
        {"special.char": 1, "normal": 2},
        {"special.char": 1, "normal": 2},
        {"special.char": 1, "normal": 2},
    ]
    test = pd.DataFrame(dataset)
    if len(test) >= 500:
        opacity = 0.3
    elif 150 <= len(test) < 500:
        opacity = 0.5
    elif 25 <= len(test) < 150:
        opacity = 0.7
    else:
        opacity = 1

    assert opacity == 1
