from core.exceptions import AccountClosingError, BankAccountNotFoundError, TransactionError
from domain.processes.supporting.finance.bank_account import BankAccount
from domain.processes.supporting.finance.currency import Currency
from domain.processes.supporting.finance.transaction import Transaction



class AccountingDepartment:
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._transaction_history: list[Transaction] = list()
        self._accounts: list[BankAccount] = list()


    def open_account(self, account_number: str, currency: Currency) -> BankAccount:
        return BankAccount(account_number, currency)
    

    def close_account(self, account_number: str) -> None:
        for account in self._accounts:
            if account.account_number == account_number:
                if account.balance != 0: raise AccountClosingError(f"Невозможно закрыть счет: {account_number}, пока на нем есть деньги")
                self._accounts.remove(account)
        raise BankAccountNotFoundError(f"Счета {account_number} не существует")


    def process_transaction(self, transaction: Transaction) -> None:
        try:
            transaction.execute()
        except TransactionError:
            transaction.set_failed()
        finally:
            self._transaction_history.append(transaction)


    def get_account_history(self, account_number: str) -> list[Transaction]:
        bank_account: BankAccount | None = None
        for account in self._accounts:
            if account.account_number == account_number:
                bank_account = account
        
        if not bank_account: 
            raise BankAccountNotFoundError(f"Счета {account_number} не существует")
        
        account_transactions: list[Transaction] = list()
        for transaction in self._transaction_history:
            if transaction.from_account == bank_account or transaction.to_account == bank_account:
                account_transactions.append(transaction)
        return account_transactions


    def calculate_total_balance(self, currency: Currency) -> int:
        total_balance: int = 0

        for account in self._accounts:
            if account.currency == currency:
                total_balance += account.balance

        return total_balance
