from settings import *
import pandas as pd


def read_input():
    input_file = os.path.join(INPUT_PATH, 'day1.txt')
    measurements = open(input_file, 'r').read().strip().split()
    measurements = [int(m) for m in measurements if m]
    return measurements


def sol1(measurements):
    count = 0
    last = measurements[0]
    for m in measurements:
        if m > last:
            count += 1
        last = m
    return count


def sol2(measurements):
    df = pd.DataFrame({'meas': measurements})
    df.meas = df.meas.astype(int)
    df['rolling_sum'] = df.rolling(window=3).sum()
    return sol1(df.rolling_sum)


if __name__ == "__main__":
    meas = read_input()
    solution1 = sol1(meas)
    print("solution 1:", solution1)
    solution2 = sol2(meas)
    print("solution 2:", solution2)
