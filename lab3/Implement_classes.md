```text

50 классов
30 ассоциаций

ClassName methods_count attribure_count:
assotiations

1. IDGenerator 2 1

2. Currency 0 3

3. UserInfo 2 4

4. Customer 4 4
   1. BankAccount
   2. Card
   3. UserInfo

5. RegistrationService 1 1
   4. IRepository

6. AccountType 0 4

7. BaseFactory 1 0

8. AccountFactory 0 2
   5. AccountType

9. AccountInfo 0 4
   6. Currency

10. CurrencyConverter 2 1

   7. dict[tuple[Currency, Currency]]
   8. ExchangeRequest

11. BankAccount 2 5

12. CurrentAccount 2 0

13. CreditAccount 4 2

14. DepositAccount 3 2

15. ForeignCurrencyAccount 2 0

16. BankAccountService 2 2
   9. BaseFactory
   10. Customer


17. CustomerRepository 3 1
   11. dict[str, Customer]

18. AccountRepository 3 1
   12. dict[str, BankAccount]

19. Money 0 2

20. TransactionRepository 3 1
   13. dict[str, Transaction]

21. ExchangeRequest 0 7

22. Receipt 1 7
   14. TransactionType

23. Transaction 6 10
   15. CurrencyConverter
   16. TransactionType

24. TransactionType 0 5

25. OperationService 7 4
   17. Money
   18. ExchangeRequest

26. Cryptography 6 0

27. CardType 0 3

28. ExpireDate 1 2

29. CardStatus 0 5

30. Card 6 9
   19. ExpireDate
   20. CardType

31. CardRepository 3 1
   21. dict[str, Card]

32. CardOrder 0 4

33. CardOrderService 2 3
   22. CardOrder

34. Denomination 0 5

35. ATM 4 6
   23. dict[Denomination, int]

36. Terminal 5 4
   24. Card

37. CreditPayment 3 6

38. CreditSchedule 1 0

39. CreditType 0 4

40. Credit 4 9
   25. list[CreditPayment]

41. NotificationService 2 0

42. CreditRepository 3 1
   26. dict[str, Credit]

43. CreditService 3 2
   27. CreditType

44. SafeBox 3 6

45. SafeBoxService 4 2
   28. BoxRepository

46. TicketStatus 0 2

47. SupportTicket 3 6

48. TicketsRepository 3 1
   29. dict[str, SupportTicket]

49. CallCenterService 4 2

50. BoxRepository 3 1
   30. dict[int, SafeBox]

100 методов
113

150 полей
157

12 исключений

1. FactoryError
2. BankAccountClosingError
3. OperationError
4. RepositoryError
5. NotFoundError
6. FrozenAccountError
7. NotEnoughMoneyError
8. DepositException
9. TransactionError
10. WrongPasswordError
11. ATMError
12. TerminalError
```
