#source code : https://legacy.docs.iota.org/docs/core/1.0/tutorials/python
from iota import Iota, TryteString, Address, Tag, ProposedTransaction
from pprint import pprint

# Declare an API object
api = Iota('https://nodes.devnet.iota.org:443' , testnet = True)
#api =Iota('http://zmq.devnet.iota.org:5556')

#api = Iota('https://api.lb-0.testnet.chrysalis2.com')

# Prepare custom data
my_data = TryteString.from_unicode('Hello from the Tangle')

# Generate a random address that doesn't have to belong to anyone
#my_address = Address.random(81)
#my_address = Address(b'HEQLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWOR99D')
my_address = 'ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9VEERIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDXNYVAPLZAW'
# Tag is optional here
my_tag = Tag(b'MY9FIRST9TAG')

# Prepare a transaction object
tx = ProposedTransaction(
    address = Address(my_address),
    value=0,
    #tag=my_tag,
    message=my_data
)

# Send the transaction to the network
#response = api.send_transfer([tx])
# Adjust min_weight_magnitude for Hornet node.
response = api.send_transfer([tx],depth=3 , min_weight_magnitude=9)
 
#pprint('Check your transaction on the Tangle!')
#pprint('https://utils.iota.org/transaction/%s/devnet' % response['bundle'][0].hash)
result = api.send_transfer(transfers = [tx])

print(result['bundle'].tail_transaction.hash)
