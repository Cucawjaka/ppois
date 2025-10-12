```text
1. EmailAccount 3

2. EmployeeTask 2
   Status

3. Status

4. Employee 3
   Permission,
   EmailAccount,
   EmployeeTask

5. Permission

6. Team 3
   Employee

7. HRDepartment 3
   IDGenerator
   Employee
   Permission,
   EmailAccount,

8. Budget 6

9. Currency

10. BankAccount 3
    Currency

11. Receipt

12. CurrencyConverter 1
    Currency

13. Transaction 6
    BankAccount
    CurrencyConverter

14. AccountingDepartment 5
    BankAccount
    Currency
    Transaction

15. Country

16. Advertisement

17. AdvertidingChannel 6
    Advertisement
18. MarketingCampaign 7
    Budget
    Country
    AdvertisingChannel

19. CampaignReport

20. MarketingDepatment 2
    MarketingCampaign
    Budget

21. WareHouse 5
    Country
    Material
    Product
    Cargo

22. Cargo
    Material | Product

23. Product

24. Material

25. LogisticsCenter 5
    Country
    Cargo
    WareHouse
    CargoSortingPlan
    Material | Product

26. CargoSortingPlan
    WareHouse
    Material | Product

27. IDGenerator 2

28. TechnologicalCard
    Product

29. ProductionOrder 2
    TechnologicalCard
    Product

30. ProductionUnit 6
    Product

31. ProductionLine 4
    ProductionUnit
    ProductionOrder
    Product

32. ProductionPlan 2
    ProductionOrder
    Product | Material

33. Factory 5
    WareHouse
    ProductionLine
    ProductionPlan
    ProductionOrder

34. Route 1
    LogisticsCenter

35. VehicleType

36. WeightMap 2
    Product | Material

37. Vehicle 3
    VehicleType
    Cargo

38. Carrier 4
    Vehicle
    Shipment

39. Shipment 2
    Cargo
    Route
    Vehicle

40. LogisticsDepartment 5
    Country
    LogisticsCenter
    Carrier
    Shipment
    Cargo
    Route

41. OrderItem
    Product

42. Order 4
    OrderItem

43. Invoice 1
    Order

44. Delivery 2
    Order

45. Customer 2
    Order

46. SalesDepartment 5
    Customer
    Order
    Invoice
    Delivery
    OrderItem

47. Supplier 2
    Country
    Material | Product
    PurchaseOrder

48. Contract 1
    Supplier
    Material | Product

49. PurchaseOrder 4
    Material | Product

50. ProcurementDepartment 4
    Supplier
    Contract
    PurchaseOrder
    Material | Product

123
```
