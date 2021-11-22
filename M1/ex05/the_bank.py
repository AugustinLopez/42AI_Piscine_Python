from inspect import ismethod


class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        if not hasattr(self, "value"):
            self.value = 0
        elif not (isinstance(self.value, float)
                  or isinstance(self.value, int)):
            raise TypeError("Wrong attribute Type. Expected float/int. Got "
                            + str(type(self.value)))
        elif not (isinstance(amount, float)
                  or isinstance(amount, int)):
            raise TypeError("Expected float/int. Got " + str(type(amount)))
        self.value += amount

    def __repr__(self):
        return (str(self.__dict__))


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        if not isinstance(account, Account):
            raise TypeError("Expected Account. Got " + str(type(account)))
        self.account.append(account)

    def __get_account_validity(self, account) -> dict:
        ret = {"odd": False, "no_b": True,
               "zipc": False, "value": False,
               "name": False, "id": False, "valid": True}
        i = 0
        for att in dir(account):
            if (att.startswith("__")
                    or ismethod(getattr(account, att))
                    or att == "ID_COUNT"):
                continue
            i += 1
            if (att.startswith('b')):
                ret["no_b"] = False
            elif (att == "zip" or att == "addr"):
                ret["zipc"] = True
            elif (att == "name"):
                ret["name"] = True
            elif (att == "id"):
                ret["id"] = True
            elif (att == "value"):
                if isinstance(account.value, int) \
                        or isinstance(account.value, float):
                    ret["value"] = True
        if (i % 2):
            ret["odd"] = True
        for item in ret.values():
            if item is False:
                ret["valid"] = False
                break
        ret['count'] = i
        print(ret)
        return ret

    def __fix_account(self, account, id):
        test = self.__get_account_validity(account)
        if test["valid"]:
            return True
        if test["no_b"] is False:
            for att in list(dir(account)):
                if (ismethod(getattr(account, att))):
                    continue
                if att.startswith('b'):
                    delattr(account, att)
                    test['count'] -= 1
        if test['name'] is False:
            account.name = None
            test['count'] += 1
        if test['id'] is False:
            account.id = id
            test['count'] += 1
        if test['value'] is False:
            account.value = 0
            test['count'] += 1
        if test['zipc'] is False:
            account.zip = None
            test['count'] += 1
        if test['count'] % 2 == 0:
            if not(hasattr(account, "zip")):
                account.zip = None
            elif not (hasattr(account, "addr")):
                account.addr = None
            else:
                j = 0
                while True:
                    if not (hasattr(account, "dummy" + str(j))):
                        setattr(account, "dummy" + str(j), None)
                        break
            test['count'] += 1
            test['odd'] = True
        return True

    def __find_valid_account(self, account):
        ret = None
        if isinstance(account, Account):
            ret = account
        elif isinstance(account, int):
            i = account
            if (i >= len(self.account) or i < 0):
                return False
            ret = self.account[i]
        elif isinstance(account, str):
            for i, elem in enumerate(self.account):
                if hasattr(elem, "name"):
                    if elem.name == account:
                        ret = elem
                        break
        if ret is None:
            return None
        dic = self.__get_account_validity(ret)
        if dic['valid'] is False:
            return None
        return ret

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        ori = self.__find_valid_account(origin)
        if ori is None:
            return False
        des = self.__find_valid_account(dest)
        if des is None:
            return False

        if not (isinstance(des.value, int) or isinstance(des.value, float)):
            return False
        if not (isinstance(ori.value, int) or isinstance(ori.value, float)):
            return False
        if not (isinstance(amount, int) or isinstance(amount, float)):
            return False
        if amount < 0:
            return False
        if amount > ori.value:
            return False
        ori.value -= amount
        des.value += amount
        return True

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        acc = None
        if isinstance(account, Account):
            acc = account
            i = -1
        elif isinstance(account, int):
            i = account
            if (i >= len(self.account) or i < 0):
                # raise IndexError("Index is invalid")
                return False
            acc = self.account[i]
        elif isinstance(account, str):
            for i, elem in enumerate(self.account):
                if hasattr(elem, "name"):
                    if elem.name == account:
                        acc = elem
                        break
        else:
            # raise TypeError("Expected int or str. Got " + str(type(account)))
            return False
        if acc is None:
            return False
        print(acc)
        return self.__fix_account(acc, i)
