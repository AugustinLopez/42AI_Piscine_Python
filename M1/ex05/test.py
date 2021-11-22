#!/usr/bin/env python

from the_bank import Account, Bank


bank = Bank()

def p0():
    john = Account(
        'William John',
        zip='100-064',
        brother="heyhey",
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation',
        lol="hihi"
    )
    print(john)
    print(bank.fix_account(john))
    print(bank.fix_account(john))
    print(john)

def p1():
    john = Account(
        'William John',
        zip='100-064',
        rother="heyhey",
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation',
        lol="lolilol"
    )
    print(john)
    bank.fix_account(john)
    print(john)
    john = Account(
    'William John',
    zip='100-064',
    rother="heyhey",
    value=6460.0,
    ref='58ba2b9954cd278eda8a84147ca73c87',
    info=None,
    other='This is the vice president of the corporation',
    )
    print(john)
    bank.fix_account(john)
    print(john)

    bank.add(Account(
        'Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    ))

    jhon = Account(
        'Jhon',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )

    bank.add(jhon)

    print("testing a valid transfer")
    print(jhon.value)
    print(bank.transfer("Jane", "Jhon", 500))
    print(jhon.value)
    print(bank.transfer("Jane", "Jhon", 1000))
    print(jhon.value)
