from binance.client import Client
import info

client = Client(info.test_api_key,
                info.test_secret_key,
                tld='us')

print('Connection to matrix: Achieved')
