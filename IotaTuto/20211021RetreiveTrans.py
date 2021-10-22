from iota import Iota
api = Iota('https://nodes.devnet.iota.org:443', testnet = True)
tail_transaction_hash = 'HGJHUCFTFDFVRNFQWUGESLYNEZXDWPQUUQOAYZGPNPKKHVEKJAZJNSJEIWUMQRZIWDZDOZ9OJQSNNK999'
bundle = api.get_bundles(tail_transaction_hash)
message = bundle['bundles'][0].tail_transaction.signature_message_fragment
print(message.decode())