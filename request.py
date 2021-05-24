import sys
import requests

# sys.stdout.write("Python %s\n" % (sys.version,))
# print(sys.path)
print(sys.executable)

r = requests.get(url="https://google.com", verify=False)
print(r.status_code)
print(r.ok)
