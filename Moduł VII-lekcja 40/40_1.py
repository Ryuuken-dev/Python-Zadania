"""
Przygotuj klasę BankDeposit, która będzie pozwalała wpłacać (deposit) i wypłacać (withdraw)
środki. Utwórz klasę konta oszczędnościowego SavingsAcoount, która będzie dziedziczyła po
BankAccount i umożliwi zwiększenie stanu konta o procent odsetek.
"""


class BankDeposit:
    def __init__(self):
        self.money = 1000

    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        if self.money < money:
            return 'Brak środków na koncie!'
        self.money -= money

    def get_account_status(self):
        return self.money


class SavingsAccount(BankDeposit):
    def __init__(self):
        super().__init__()

    def get_up(self, amount: int):
        self.money += self.money * (amount / 100)

    def get_account_status(self):
        return super(SavingsAccount, self).get_account_status()



def test_if_deposit_works_correctly():
    money = 1000

    bank = BankDeposit()
    bank.deposit(money)

    assert bank.get_account_status() == 2000


def test_if_withdraw_works_correctly():
    money = 500

    bank = BankDeposit()
    bank.withdraw(money)

    assert bank.get_account_status() == 500


def test_if_get_up_works_correctly():
    amount = 5
    money = 1000

    bank = BankDeposit()
    bank.deposit(money)
    savings = SavingsAccount()
    savings.get_up(amount)

    assert savings.get_account_status() == 1050


if __name__ == '__main__':
    bank = BankDeposit()
    bank.deposit(1000)
    bank.withdraw(500)
    savings = SavingsAccount()
    savings.get_up(5)
    print(savings.get_account_status())



