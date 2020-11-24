import requests
import json

stock = '$SPX.X'

#key for the APIs
td_consumer_key = 'YOUR_KEY_HERE'

#
# Get last trading day's data
# to calculate Pivot Point
#
def getHistQuote(s):
    endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory?&periodType={periodType}&period={period}&frequency={frequency}&frequencyType={frequencyType}'

    full_url = endpoint.format(stock_ticker=s,
        periodType = "month",
        period = 1,
        frequency = 1,
        frequencyType = "daily"
        )
    page = requests.get(url=full_url,
                    params={'apikey' : td_consumer_key})
    content = json.loads(page.content)

    return(content)
    
# calculate the pivot point

content = getHistQuote(stock)

# content['candles'][-1]

pp = (content['candles'][-1]['high'] + content['candles'][-1]['low'] + content['candles'][-1]['close']) / 3
r1 = 2 * pp - content['candles'][-1]['low']
s1 = 2 * pp - content['candles'][-1]['high']
r2 = pp + (content['candles'][-1]['high'] - content['candles'][-1]['low'])
s2 = pp - (content['candles'][-1]['high'] - content['candles'][-1]['low'])
r3 = pp + 2 * (content['candles'][-1]['high'] - content['candles'][-1]['low'])
s3 = pp - 2 * (content['candles'][-1]['high'] - content['candles'][-1]['low'])

if (content['candles'][-1]['open'] > content['candles'][-1]['close']):
  print("yesterday is down")
  X = content['candles'][-1]['high'] + content['candles'][-1]['low'] + content['candles'][-1]['close'] + content['candles'][-1]['low']
elif (content['candles'][-1]['open'] < content['candles'][-1]['close']):
  print("yesterday is up")
  X = content['candles'][-1]['high'] + content['candles'][-1]['low'] + content['candles'][-1]['close'] + content['candles'][-1]['high']
else:
  print("yesterday is even")
  X = content['candles'][-1]['high'] + content['candles'][-1]['low'] + content['candles'][-1]['close'] + content['candles'][-1]['close']

high = X/2 - content['candles'][-1]['low']
low  = X/2 - content['candles'][-1]['high']

print('last close : ', content['candles'][-1]['close'])
print('range (PP) : ', low, "-", high)
print("s3 : ", s3)
print("s2 : ", s2)
print("s1 : ", s1)
print("pp : ", pp)
print("r1 : ", r1)
print("r2 : ", r2)
print("r3 : ", r3)
