import botslib.bots_api as ba

bots_platform = ba.BEM_API('https://signal.revenyou.io/paper/api/signal/v2/')
BOT_NAME = 'Ptest2'
BOT_KEY = 'UDJOULULA0HRIHJQ'

order = ba.OrderParameters(signalProvider=BOT_NAME,
                                 signalProviderKey=BOT_KEY,
                                 baseAsset='ETH',
                                 quoteAsset='USDT',
                                 exchange='binance')
order.extId = 'order_9'
order.type = 'limit'
order.side = 'sell'
order.limitPrice = '120'
order.qtyPct = '99'
order.ttlType = 'gtc'
order.responseType = 'FULL'
order.ttlSecs= None
order.stopPrice = None

response = bots_platform.placeOrder(order)
response

request = ba.PositionRequest(signalProvider = BOT_NAME, signalProviderKey=BOT_KEY, exchange = 'binance', baseAsset = 'USDT')
response = bots_platform.getBotAssetsPct(request)




