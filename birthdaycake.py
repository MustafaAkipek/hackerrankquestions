# int candles[n]: the candle that are tallest

def birthdayCakeCandles(candles):
    tallestcandle = 0
    x = max(candles)
    
    for i in candles:
        if i == x:
            tallestcandle += 1
            
    return tallestcandle