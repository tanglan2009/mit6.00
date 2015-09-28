#test
# Determines remaining credit card balance after a year of making the minimum
# payment each month.

balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annualInterestRate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
miniMonthlyPaymentRate = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))

totalAmountPaid = 0
for month in range(1, 13):

    miniMonthlyPayment = round(balance * miniMonthlyPaymentRate, 2)
    interestPaid = round(annualInterestRate/12*balance, 2)
    principalPaid = round(miniMonthlyPayment - interestPaid, 2)
    remainingBalance =round(balance- principalPaid, 2)
    balance = remainingBalance
    print 'month: ', month
    print 'Minimum monthly payment: ',miniMonthlyPayment
    print 'Principle paid: ', principalPaid
    print 'Remaining balance: ', remainingBalance
    totalAmountPaid = totalAmountPaid + miniMonthlyPayment
print "RESULT"
print 'Total amount paid: ', totalAmountPaid
print 'Remaining balance: ', remainingBalance
