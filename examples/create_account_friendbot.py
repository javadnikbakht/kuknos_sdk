import requests

from kuknos_sdk import Keypair

keypair = Keypair.random()

print("Public Key: " + keypair.public_key)
print("Secret Seed: " + keypair.secret)

url = 'https://friendbot.kuknos.org'
url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': keypair.public_key})
print(response)
