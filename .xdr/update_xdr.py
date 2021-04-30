import os
from urllib.parse import urljoin

import requests

BASE_XDR_GITHUB_URL = (
    "https://raw.githubusercontent.com/kuknos/kuknos-core/master/src/xdr/"
)
XDR_FILES = (
    "Kuknos-SCP.x",
    "Kuknos-ledger-entries.x",
    "Kuknos-ledger.x",
    "Kuknos-overlay.x",
    "Kuknos-transaction.x",
    "Kuknos-types.x",
)
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
print("Downloading xdr files from {}".format(BASE_XDR_GITHUB_URL))
for filename in XDR_FILES:
    print("Downloading {}".format(filename))
    url = urljoin(BASE_XDR_GITHUB_URL, filename)
    file = os.path.join(BASE_DIR, filename)
    resp = requests.get(url, allow_redirects=True)
    open(file, "wb").write(resp.content)
print("Finished")
