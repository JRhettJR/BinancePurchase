from binance.client import Client
import info

client = Client(info.TEST_API_KEY,
                info.TEST_SECRET_KEY,
                tld='us')

print('Connection to matrix: Achieved')
