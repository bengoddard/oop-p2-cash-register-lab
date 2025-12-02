#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self._discount = 0
    self.total = 0
    self.items = []
    self.previous_transactions = []

    self.discount = discount

  @property
  def discount(self):
    return self._discount
  @discount.setter
  def discount(self, value):
    if type(value) is int and 0 < value < 100:
      self._discount = value
    else:
      print("Not valid discount")
      self._discount = 0

  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(item)
    prev_trans = {
      "item": item,
      "price": price,
      "quantity": quantity
    }
    self.previous_transactions.append(prev_trans)

  def apply_discount(self):
    if self._discount > 0:
      discount = (self._discount / 100) * self.total
      self.total -= discount
      print(f"After the discount, the total comes to ${self.total:.0f}.")
    else:
      print('There is no discount to apply.')

  def void_last_transaction(self):
    if not self.previous_transactions:
      print("No transactions to void.")
      return
    last_trans = self.previous_transactions.pop()
    void_price = last_trans["price"] * last_trans["quantity"]
    void_item_name = last_trans["item"]
    self.total -= void_price
    if self.items and self.items[-1] == void_item_name:
      self.items.pop()
    print(f"Voided last transaction {void_item_name}. Current total: {self.total}")
