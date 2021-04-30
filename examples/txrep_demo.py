from kuknos_sdk.sep.txrep import from_txrep, to_txrep
from kuknos_sdk import Keypair, TransactionBuilder, Network, Account

source_secret_key = "SBFZCHU5645DOKRWYBXVOXY2ELGJKFRX6VGGPRYUWHQ7PMXXJNDZFMKD"

source_keypair = Keypair.from_secret(source_secret_key)
source_public_key = source_keypair.public_key

receiver_public_key = "GA7YNBW5CBTJZ3ZZOWX3ZNBKD6OE7A7IHUQVWMY62W2ZBG2SGZVOOPVH"
source_account = Account(source_public_key, 12345)


transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100,
    )
    .add_text_memo("Hello, Kuknos!")
    .append_payment_op(receiver_public_key, "350.1234567", "PMN")
    .set_timeout(30)
    .build()
)

transaction.sign(source_keypair)

# convert transaction to txrep
txrep = to_txrep(transaction)
print(f"txrep: \n{txrep}")
# convert txrep to transaction
tx = from_txrep(txrep, Network.TESTNET_NETWORK_PASSPHRASE)
