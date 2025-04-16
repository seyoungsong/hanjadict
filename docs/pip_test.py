from importlib import reload

import hanjadict

reload(hanjadict)

print(hanjadict.lookup("雪"))
