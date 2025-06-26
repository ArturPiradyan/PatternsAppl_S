

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount): pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")

class PaymentPlatform:
    def __init__(self, method):
        self.method = method

    def checkout(self, amount):
        print("Initiating payment through platform...")
        self.method.pay(amount)

class ECommercePlatform(PaymentPlatform):
    def checkout(self, amount):
        print("E-Commerce checkout started.")
        super().checkout(amount)

class MobileAppPlatform(PaymentPlatform):
    def checkout(self, amount):
        print("Mobile App checkout started.")
        super().checkout(amount)

if __name__ == "__main__":
    cc_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()

    ecommerce = ECommercePlatform(cc_payment)
    mobile = MobileAppPlatform(paypal_payment)

    ecommerce.checkout(49.99)
    print("---")
    mobile.checkout(12.50)
