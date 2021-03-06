from kuknos_sdk import Server

server = Server(horizon_url="https://hz1-test.kuknos.org")
account_id = "GASOCNHNNLYFNMDJYQ3XFMI7BYHIOCFW3GJEOWRPEGK2TDPGTG2E5EDW"
last_cursor = 'now'  # or load where you left off


def tx_handler(tx_response):
    print(tx_response)


for tx in server.transactions().for_account(account_id).cursor(last_cursor).stream():
    tx_handler(tx)
