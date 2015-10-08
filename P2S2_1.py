balance = float(raw_input('balance = '))
annualInterestRate = round(float(raw_input('annualInterestRate = ')), 1)
monthlyPaymentRate = round(float(raw_input('monthlyPaymentRate = ')), 2)

monthlyInterestRate = (annualInterestRate)/12.0

totalPaid = 0
for month in range(1, 13):
    minimumMonthlyPayment = round((monthlyPaymentRate)*(balance), 2)
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    remainingBalance = round((monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance), 2)
    balance = remainingBalance
    totalPaid = totalPaid + minimumMonthlyPayment
    print "month: ", month
    print "Minimum monthly payment: ", minimumMonthlyPayment
    print "Remaining balance: ", remainingBalance
print "Total paid: ", totalPaid
print "Remaining balance: ", remainingBalance