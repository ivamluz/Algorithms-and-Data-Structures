def birthdayCakeCandles(candles_heights):
    if not candles_heights:
        return 0

    sorted_candle_heights = sorted(candles_heights, reverse=True)

    highest = sorted_candle_heights[0]
    candles = 0

    for i in range(len(sorted_candle_heights)):
        if sorted_candle_heights[i] == highest:
            candles += 1
        else:
            break

    return candles
