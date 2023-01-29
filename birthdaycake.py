candles = [5,5,5,5,7]
candle = []
max_candle = 0
result = 0
for i in range(len(candles)):
    candle.append(candles[i])
    
max_candle = max(candle)
    
for i in range(len(candle)):
    if max_candle == candle[i]:
        result += 1
    else:
        continue
            
print(result)