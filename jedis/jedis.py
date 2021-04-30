import json
import os.path
from helpers.FileHelper import load, dump
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

class Jedis:
    """
            make instance this class to Preparation Jedis

            example :
                from Jedis import Jedis

                j = Jedis("JSONFile.json")

                ...

            """

    def __init__(self, path="myJedis.json"):
        """
        make instance this class to Preparation Jedis

        example :
            from Jedis import Jedis

            j = Jedis("JSONFile.json")

            ...

        :param path: str

        """

        self._path = path
        if path[::-1][:5][::-1] != ".json":
            raise Exception('\nThe path to the json file is incorrect. (The "path" should be .json file)')
        if os.path.exists(path):
            if "{" not in open(path).read():
                with open(path, "w") as f:
                    f.write("{")
                    f.close()
            if "}" not in open(path).read():
                with open(path, "a+") as f:
                    f.write("}")
                    f.close()
            else:
                open(path).close()
        else:
            with open(path, "w") as f:
                f.write("{}")
                f.close()

    # INFO: set - Set or change Key:Value
    def set(self, name, value):
        """
        Set the value at key ``name`` to ``value``

        example:
            import jedis
            j = jedis.Jedis("myJsonFile.json")

            j.set("age", 22)
        """
        path = self._path
        fdata = load(path)
        fdata[name] = value
        dump(path, fdata)

    # INFO: get - Get value of a key
    def get(self, name):
        """
        Return the value at key ``name``, or None if the key doesn't exist

        example:
            import jedis
            j = jedis.Jedis("myJsonFile.json")

            j.get("age")
        """
        path = self._path
        fdata = load(path)
        try:
            return fdata[name]
        except KeyError as e:
            return None

    # INFO: delete - Delete a key from json
    def delete(self, *names):
        """Delete one or more keys specified by ``names``"""
        path = self._path
        fdata = load(path)
        for i in names:
            try:
                del fdata[i]
            except KeyError as e:
                raise KeyError(f'Key "{e.args[0]}" not found!')
        dump(path, fdata)

    # INFO: dset - Set value of a key in a dictionary
    def dset(self, name, key=None, value=None, mapping=None):
        """
        Set ``key`` to ``value`` within dict ``name``,
        ``mapping`` accepts a dict of key/value pairs that that will be
        added to dict ``name``.
        :param name: str
        :param key: str
        :param value: Any
        :param mapping: dict
        :return: None
        """
        path = self._path
        fdata = load(path)
        try:
            fdata[name]
        except KeyError as e:
            fdata[name] = dict()
        if key is None and value is None:
            if mapping is not None:
                if type(mapping) is dict:
                    if len(list(mapping.keys())) == 1:
                        fdata[name][list(mapping.keys())[0]] = mapping[list(mapping.keys())[0]]
                        dump(path, fdata)
                        return
                    else:
                        raise Exception("wrong number of arguments for 'dset'")
                else:
                    raise TypeError("mapping value should be a dictionary")
            else:
                raise ValueError("'dset' with no key value pairs")
        else:
            if mapping is not None:
                raise Exception("wrong number of arguments for 'dset'")
            else:
                fdata[name][key] = value
                dump(path, fdata)

    # INFO: dget - Get value of a key in a dictionary
    def dget(self, name, key):
        """
        Return the value of ``key`` within the dict ``name``
        :param name: str
        :param key: str
        :return: Any
        """
        path = self._path
        fdata = load(path)
        try:
            return fdata[name][key]
        except KeyError as e:
            return None

    # INFO: ddel - Delete "keys" in a dictionary
    def ddel(self, name, *keys):
        """
        Delete ``keys`` from dict ``name``
        :param name: str
        :param keys: str
        :return: None
        """
        path = self._path
        fdata = load(path)
        try:
            for key in keys:
                del fdata[name][key]
            if fdata[name] == {}:
                del fdata[name]
        except KeyError as e:
            raise KeyError(f'Key "{e.args[0]}" not found!')
        dump(path, fdata)

    # INFO: dkeys - Return the list of keys within dictionary name
    def dkeys(self, name):
        """
        Return the list of keys within dict ``name``
        :param name: str
        :return: list
        """
        path = self._path
        fdata = load(path)
        try:
            return list(fdata[name].keys())
        except KeyError as e:
            raise KeyError(f'Key "{e.args[0]}" not found!')

    # INFO: dlen - Return the length of keys within dictionary name
    def dlen(self, name):
        """
        Return the number of elements in dict ``name``
        :param name: str
        :return: int
        """
        path = self._path
        fdata = load(path)
        try:
            return len(list(fdata[name].keys()))
        except KeyError as e:
            raise KeyError(f'Key "{e.args[0]}" not found!')

    # INFO: dgetall - Return the dictionary with its name
    def dgetall(self, name):
        """
        Return a Python dict of the dict's name/value pairs
        :param name: str
        :return: dict
        """
        path = self._path
        fdata = load(path)
        try:
            return fdata[name]
        except KeyError as e:
            return None

    # INFO: dexists - Return True if key of the dict exists
    def dexists(self, name, key):
        """
        Returns a boolean indicating if ``key`` exists within dict ``name``
        :param name: str
        :param key: str
        :return: boolean
        """
        path = self._path
        fdata = load(path)
        try:
            fdata[name][key]
            return True
        except KeyError as e:
            return False

    # INFO: type - Return type of the name
    def type(self, name):
        """
        Returns the type of key ``name``
        :param name: str
        :return: type
        """
        path = self._path
        fdata = load(path)
        try:
            return type(fdata[name])
        except KeyError as e:
            raise KeyError(f'Key "{e.args[0]}" not found!')

    # INFO: exists - Return True if 'name' exists
    def exists(self, name):
        """
        Returns a boolean indicating if ``name`` exists
        :param name: str
        :return: boolean
        """
        path = self._path
        fdata = load(path)
        try:
            fdata[name]
            return True
        except KeyError as e:
            return False

    # INFO: lpush - insert 'values' to the top of list within 'name'
    def lpush(self, name, *values):
        """
        Push ``values`` onto the head of the list ``name``
        :param name: str
        :param values: Any
        :return: None
        """
        path = self._path
        fdata = load(path)
        try:
            fdata[name]
        except KeyError as e:
            fdata[name] = list()
        fdata[name] = list(values) + fdata[name]
        dump(path, fdata)

    # INFO: lpush - insert 'values' to the end of list within 'name'
    def rpush(self, name, *values):
        """
        Push ``values`` onto the tail of the list ``name``
        :param name: str
        :param values: Any
        :return: None
        """
        path = self._path
        fdata = load(path)
        try:
            fdata[name]
        except KeyError as e:
            fdata[name] = list()
        fdata[name] = fdata[name] + list(values)
        dump(path, fdata)

    # INFO: lrange - Return a list elements, in range 'start' - 'end'
    def lrange(self, name, start=0, end=-1):
        """
        Return a slice of the list ``name`` between
        position ``start`` and ``end``

        < Returns the entire list by default >

        ``start`` and ``end`` can be negative numbers just like
        Python slicing notation
        :param name: str
        :param start: int
        :param end: int
        :return: list
        """
        path = self._path
        fdata = load(path)
        try:
            if type(fdata[name]) is list:
                if end < 0:
                    if end == -1:
                        return list(fdata[name][start: end]) + [fdata[name][-1]]
                    else:
                        return fdata[name][start: end + 1]
                else:
                    return fdata[name][start: end + 1]
            else:
                raise TypeError(f'"{name}" is not list!')
        except KeyError as e:
            raise KeyError(f'Name "{e.args[0]}" not found!')

    # INFO: llen - Return the length of the list name
    def llen(self, name):
        """
        Return the length of the list ``name``
        :param name: str
        :return: int
        """
        path = self._path
        fdata = load(path)
        try:
            if type(fdata[name]) is list:
                return len(fdata[name])
            else:
                raise TypeError(f'"{name}" is not list!')
        except KeyError as e:
            raise KeyError(f'Name "{e.args[0]}" not found!')

    # INFO: lset - set list[index] to value, within list ``name``
    def lset(self, name, index: int, value):
        """
        Set ``position`` of list ``name`` to ``value``
        :param name: str
        :param index: int
        :param value: Any
        :return: None
        """
        path = self._path
        fdata = load(path)
        try:
            if type(fdata[name]) is list:
                fdata[name][index] = value
                dump(path, fdata)
            else:
                raise TypeError(f'"{name}" is not list!')
        except KeyError as e:
            raise KeyError(f'Name "{e.args[0]}" not found!')

    # INFO: lindex - Return the item from list ``name`` at position ``index``
    def lindex(self, name, index: int):
        """
        Return the item from list ``name`` at position ``index``

        Negative indexes are supported and will return an item at the
        end of the list

        :param name: str
        :param index: int
        :return: Any
        """
        path = self._path
        fdata = load(path)
        try:
            if type(fdata[name]) is list:
                return fdata[name][index]
            else:
                raise TypeError(f'"{name}" is not list!')
        except KeyError as e:
            raise KeyError(f'Name "{e.args[0]}" not found!')

    def lrem(self, name, count, value):
        """
        Remove the first ``count`` occurrences of elements equal to ``value``
        from the list stored at ``name``.

        The count argument influences the operation in the following ways:
            count > 0: Remove elements equal to value moving from head to tail.
            count < 0: Remove elements equal to value moving from tail to head.
            count = 0: Remove all elements equal to value.

        :param name: str
        :param count: int
        :param value: Any
        :return: int
        """

        path = self._path
        fdata = load(path)
        try:
            if type(fdata[name]) is list:

                if count > 0:  # info: count ( + )
                    x = 0
                    while value in fdata[name]:
                        fdata[name].remove(value)
                        x += 1
                        if x == count:
                            break
                    dump(path, fdata)
                    return x

                elif count == 0:  # info: count ( 0 )
                    _oldl = len(fdata[name])
                    fdata[name] = list(filter(lambda a: a != value, fdata[name]))
                    dump(path, fdata)
                    return _oldl - len(fdata[name])

                else:  # info: count ( - )
                    count = count * -1
                    x = 0
                    fdata[name] = fdata[name][::-1]
                    while value in fdata[name]:
                        fdata[name].remove(value)
                        x += 1
                        if x == count:
                            break
                    fdata[name] = fdata[name][::-1]
                    dump(path, fdata)
                    return x

            else:
                raise TypeError(f'"{name}" is not list!')
        except KeyError as e:
            raise KeyError(f'Name "{e.args[0]}" not found!')
