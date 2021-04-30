from kuknos_sdk import Keypair, Server, TransactionBuilder, Network, Asset

server = Server(horizon_url="https://hz1-test.kuknos.org/")
source_keypair = Keypair.from_secret("SA6XHAH4GNLRWWWF6TEVEWNS44CBNFAJWHWOPZCVZOUXSQA7BOYN7XHC")

source_account = server.load_account(account_id=source_keypair.public_key)

path = [
    Asset("USD", "GBBM6BKZPEHWYO3E3YKREDPQXMS4VK35YLNU7NFBRI26RAN7GI5POFBB"),
    Asset("EUR", "GDTNXRLOJD2YEBPKK7KCMR7J33AAG5VZXHAJTHIG736D6LVEFLLLKPDL")
]
transaction = TransactionBuilder(
    source_account=source_account, network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE, base_fee=100) \
    .append_path_payment_strict_receive_op(destination="GBBM6BKZPEHWYO3E3YKREDPQXMS4VK35YLNU7NFBRI26RAN7GI5POFBB",
                            send_code="PMN", send_issuer=None, send_max="1000", dest_code="GBP",
                            dest_issuer="GASOCNHNNLYFNMDJYQ3XFMI7BYHIOCFW3GJEOWRPEGK2TDPGTG2E5EDW",
                            dest_amount="5.50", path=path) \
    .set_timeout(30) \
    .build()
transaction.sign(source_keypair)
response = server.submit_transaction(transaction)
