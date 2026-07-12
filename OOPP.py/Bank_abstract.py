from abc import ABC, abstractclassmethod

class Payment(ABC):

        @abstractclassmethod
        def pay(self,amount):
            pass


class CreditCard(Payment):
      
      def pay(self, amount):
             (self, amount)
             print(f"Paid {amount} using CreditCard")

            
class UPI(Payment):
      
      def pay(self, amount):
              (amount)

              print("f Paid {amount} using UPI")

p1 = CreditCard()

p2 = UPI()

p1.pay (500)
p2.pay (500)