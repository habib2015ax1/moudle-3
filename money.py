def total_bill(bill,tip):
    total=(tip/100)*bill+bill
    print(total)
bill=int(input("enter the amount of bill"))
tip=int(input("enter the amount of tip"))
total_bill(bill,tip)