![telegram](https://img.shields.io/badge/Telegram-/json?url=https://t.me/Kobsser&style=flat&logo=telegram&color=26A5E4) ![github](https://img.shields.io/badge/Github-Jedis-/json?url=https://github.com/Kobsser/Jedis&style=flat&logo=github&color=181717) ![pypi](https://img.shields.io/badge/Pypi-/json?url=https://pypi.org/project/jedis/&style=flat&logo=pypi&color=b5b5b5)
# Jedis
>`PyJedis` is a python package for easy `json` management that have an interface similar to __redis__.

### Installation
to install with __pip__:
```
pip install jedis
```
or from **[source](https://github.com/Kobsser/Jedis)**:
```
python setup.py install
```
### Getting Started
```
from jedis import Jedis

j = Jedis("example.json")
if not j.exists("foo"):
    j.set("foo", "bar")
    
print(j.get('foo'))
```
#
