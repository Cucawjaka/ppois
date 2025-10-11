from domain.processes.main_procceses.sales.Customer import Customer
from domain.processes.main_procceses.sales.Delivery import Delivery
from domain.processes.main_procceses.sales.Invoice import Invoice
from domain.processes.main_procceses.sales.Order import Order
from domain.processes.main_procceses.sales.OrderItem import OrderItem


class SalesDepartment:
    def __init__(self) -> None:
        self._customers: dict[str, Customer] = dict()
        self._orders: dict[str, Order] = dict()
        self._invoices: dict[str, Invoice] = dict()
        self._deliveries: dict[str, Delivery] = dict()

    def register_customer(self, customer: Customer) -> None:
        self._customers[customer.name] = customer

    def create_order(self, customer: Customer, items: list[OrderItem]) -> Order:
        order = Order()
        for item in items:
            order.add_item(item)
        self._orders[order.id] = order
        customer.add_order(order)
        return order

    def get_invoice(self, order: Order) -> Invoice:
        invoice = Invoice(order)
        self._invoices[invoice.id] = invoice
        return invoice

    def arrange_delivery(self, order: Order, address: str) -> Delivery:
        delivery = Delivery(order, address)
        self._deliveries[delivery._id] = delivery
        return delivery

    def get_customer_orders(self, customer: Customer) -> list[Order]:
        return customer.order_history()
