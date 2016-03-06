
balance = int(raw_input('balance = '))
annualInterestRate = float(raw_input('annualInterestRate = '))



monthlyInterestRate = (annualInterestRate)/12.0
totalBalance = balance
minimumFixedMonthlyPayment = 10
while totalBalance > 0:


    for month in range(1, 13):
        monthlyUnpaidBalance = (totalBalance) - (minimumFixedMonthlyPayment)
        remainingBalance = (monthlyUnpaidBalance) +int((monthlyInterestRate * monthlyUnpaidBalance))
        totalBalance = remainingBalance
        print month,totalBalance, minimumFixedMonthlyPayment
    if totalBalance > 0:
        totalBalance = balance
    # else:
    #     break


        minimumFixedMonthlyPayment += 10



print "Lowest Payment", minimumFixedMonthlyPayment
