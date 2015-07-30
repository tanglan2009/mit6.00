__author__ = 'tanglan'
balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annaulRate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
minMonthRate = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))

totalAmountPaid = 0
for month in range(1, 13):

    miniMonthlyPayment = round(balance * minMonthRate, 2)
    interestPaid = round(annaulRate/12*balance, 2)
    principalPaid = round(miniMonthlyPayment - interestPaid, 2)
    remainingBalance =round(balance- principalPaid, 2)
    balance = round(remainingBalance,2)
    # print 'month: ', month
    # print 'Minimum monthly payment: ',miniMonthlyPayment
    # print 'Principle paid: ', principalPaid
    # print 'Remaining balance: ', remainingBalance
    totalAmountPaid = totalAmountPaid + miniMonthlyPayment
print 'Total amount paid: ', totalAmountPaid
print 'Remaining balance: ', remainingBalance