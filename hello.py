import json
import os

print('Content-type application/json')
print()
print(json.dumps(dict(os.environ), indent=4))
