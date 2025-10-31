class NotificationService:
    def send_email(self, customer_id: str, message: str) -> None:
        print(f"Email для клиента {customer_id}] {message}")

    def senf_notification(self, customer_id: str, message: str) -> None:
        print(f"Уведомление для клиента {customer_id}] {message}")
