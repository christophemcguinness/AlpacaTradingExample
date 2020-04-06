import requests
from config import *
from prettyResponse import *

r = requests.get(ACCOUNT, headers=headers)

# Print Account Details
prettyJsonResponseToText(r.content)
