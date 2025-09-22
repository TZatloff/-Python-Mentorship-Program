# A Encapsulation task
class BankAccount:
    def __init__(self, owner: str, starting_balance: float = 0.0):
        self.owner = owner
        self._balance = float(starting_balance)  # treat as "internal"

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be possitive. ")
        if amount > self._balance:
            raise ValueError("Insufficient funds for this withdrawal.")

    def transfer_to(self, other_account, amount: float) -> None:
        self.withdraw(amount)
        other_account.deposit(amount)


if __name__ == "__main__":
    acct = BankAccount("Alex", 100)
    print(acct.balance)  # 100.0
    acct.deposit(50)
    print(acct.balance)  # 150.0

# B Abstraction task
import datetime


class PaymentProcessor:
    def __init__(self):
        self._transaction_log = []

    def pay(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if self._charge_card(amount):
            print(f"Payment of ${amount} on success.")
        else:
            print("Payment failed.")

    def _charge_card(self, amount: float) -> bool:
        return True


if __name__ == "__main__":
    p = PaymentProcessor()
    try:
        p.pay(100)
        p.pay(0)
    except ValueError as e:
        print(e)


# C Inheritance task

class Vehicle:
    def __init__(self, name: str):
        self.name = name

    def move(self) -> None:
        print(f"{self.name} moves forward.")


class Car(Vehicle):
    def __init__(self, name: str, doors: int, fuel=100):
        super().__init__(name)
        self.doors = doors
        self.fuel = fuel

    def lock_doors(self) -> None:
        print(f"{self.name}'s {self.doors} doors are locked.")

    def unlock_doors(self) -> None:
        print(f"{self.name}'s {self.doors} doors are unlocked.")

    def move(self):
        if self.fuel <= 0:
            print(f"{self.name} cannot move, out of fuel!")
        else:
            self.fuel -= 10
            print(f"{self.name} moves forward. Fuel left: {self.fuel}")


class Bike(Vehicle):
    def __init__(self, name: str, type_of_bike: str):
        super().__init__(name)
        self.type_of_bike = type_of_bike

    def ring_bell(self) -> None:
        print(f"{self.name} the {self.type_of_bike} bike rings its bell!")


if __name__ == "__main__":
    my_car = Car("Toyota", 4)
    my_car.move()
    my_car.lock_doors()
    my_car.unlock_doors()

    my_bike = Bike("Giant", "mountain")
    my_bike.move()
    my_bike.ring_bell()


# D Polymorphism task

class Notifier:
    def send(self, message: str) -> None:
        raise NotImplementedError("Subclasses must implement this method.")


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending : {message}")


class SMSNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending: {message}")


class PushNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending : {message}")


def send_all(notifiers: list[Notifier], message: str) -> None:
    for n in notifiers:
        n.send(message)


class SlackNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Slack : {message}")


if __name__ == "__main__":
    email = EmailNotifier()
    sms = SMSNotifier()
    send_all([email, sms], "Hello!")
    print("Done.")
    send_all([email, sms, PushNotifier(), SlackNotifier()], "Opa pa!")
