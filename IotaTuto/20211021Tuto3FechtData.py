#source code : https://legacy.docs.iota.org/docs/core/1.0/tutorials/js
from iota import Iota, Address
from iota.codecs import TrytesDecodeError

# Declare an API object
api = Iota('https://nodes.devnet.iota.org:443' , testnet=1)

# Address to fetch data from
# Replace with your random generated address from Tutorial 2. to fetch the data
# that you uploaded.
addy = 'YAOLVQPWVTHQTANVFTRHJRPKMESASZSWRPP9NFGLZE9ZNVZNXCVS9MCYPSXPDIJAZDLLE9XMWRXQVY999'

print('Fetching data from the Tangle...')
# Fetch the transaction objects of the address from the Tangle
response = api.find_transaction_objects(addresses=[addy])

if not response['transactions']:
    print('Couldn\'t find data for the given address.')
else:
    print('Found:')
    # Iterate over the fetched transaction objects
    for tx in response['transactions']:
        # data is in the signature_message_fragment attribute as trytes, we need
        # to decode it into a unicode string
        data = tx.signature_message_fragment.decode(errors='ignore')
        print(data)
