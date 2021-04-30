from kuknos_sdk import TransactionBuilder, Network, Keypair, Account

root_keypair = Keypair.from_secret("SA6XHAH4GNLRWWWF6TEVEWNS44CBNFAJWHWOPZCVZOUXSQA7BOYN7XHC")
# Create an Account object from an address and sequence number.
root_account = Account(account_id=root_keypair.public_key, sequence=1)

transaction = TransactionBuilder(source_account=root_account, network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
                                 base_fee=100).add_text_memo("Happy birthday!").append_payment_op(
    destination="GASOCNHNNLYFNMDJYQ3XFMI7BYHIOCFW3GJEOWRPEGK2TDPGTG2E5EDW", amount="2000",
    asset_code="PMN").set_timeout(30).build()
