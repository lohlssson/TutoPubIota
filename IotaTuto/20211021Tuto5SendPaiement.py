#source code : https://legacy.docs.iota.org/docs/core/1.0/tutorials/python
from iota import Iota
from iota import ProposedTransaction
from iota import Address

# Replace this seed with the one that owns the address you used to get free test tokens
seed = 'JBN9ZRCOH9YRUGSWIQNZWAIFEZUBDUGTFPVRKXWPAUCEQQFS9NHPQLXCKZKRHVCCUZNF9CZZWKXRZVCWQ'

# Connect to a node
api = Iota('https://nodes.devnet.iota.org:443', seed, testnet = True)

# Define an address to which to send IOTA tokens 
address = 'ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9VEERIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDXNYVAPLZAW'
#ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9VEERIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDXNYVAPLZAW
#address = 'atoi1qz4ep7pqxuz8xhlscnzhl8meh27ymz00ctyrpxlp0ppdh6ghtrrky8079cd'

# Define an input transaction object
# that sends 1 i to the address
tx = ProposedTransaction(
    address=Address(address),
    value = 1
)

print('Sending 1 i to ',  address)

result = api.send_transfer(transfers=[tx] )

print('Bundle: ')
print(result['bundle'].hash)

