import os
import re
from icmplib import ping, Host, exceptions

address = "google"

try:
    host = ping(address, 2, .2, 1)
except exceptions.NameLookupError:
    host = ping(f"{address}.com", 2, .2, 1)
print(host)
