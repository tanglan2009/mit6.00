__author__ = 'tanglan'

totalBalance = float(raw_input('Enter the outstanding balance on your credit card:'))
r = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

minimumMontlyPaid = int(totalBalance) / 12 -int(totalBalance)/12%10
balance = totalBalance
while balance > 0:
    for month in range(1,13):
        currentBalance = balance *(1 + r/12) - minimumMontlyPaid
        balance = currentBalance
        if balance <= 0:
            break
    if balance <= 0:
        break
    minimumMontlyPaid += 10
    balance = totalBalance



print 'Monthly payment to pay off debt in 1 year: ', minimumMontlyPaid
print 'Number of months needed: ', month
print 'Balance: ', balance
