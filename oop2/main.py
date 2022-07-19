from accounts import Account


acc = Account("Shamim", "CSE", "5th", 20, 5000)
print(acc)
print(acc.waiver_amount(3.80))
print(acc.first_payment_amount())
print(acc.register(26000))
print(acc.reg_status())
