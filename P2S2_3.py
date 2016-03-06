
balance = int(raw_input('balance = '))
annualInterestRate = float(raw_input('annualInterestRate = '))



monthlyInterestRate = (annualInterestRate)/12.0
totalBalance = balance
monthlyPaymentLowerBound =totalBalance/12.0
monthlyPaymentUpperBound =(totalBalance * (1 + monthlyInterestRate)**12) / 12.0
minimumFixedMonthlyPayment =(monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2 # pick the midpoint.

while totalBalance > 0:


    for month in range(1, 13):
        monthlyUnpaidBalance =(totalBalance) - (minimumFixedMonthlyPayment)
        remainingBalance =(monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)
        totalBalance =round(remainingBalance, 2)
        print month,totalBalance, round(minimumFixedMonthlyPayment, 2)
    #reset totalBalance to balance
    if totalBalance > 0:
        totalBalance = balance
        monthlyPaymentLowerBound = minimumFixedMonthlyPayment
        minimumFixedMonthlyPayment =(monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2
        #
        # if minimumFixedMonthlyPayment > (monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2:
        #     monthlyPaymentLowerBound = minimumFixedMonthlyPayment
    if totalBalance < -1: # how to decide the number(-0.01, -1??)
        totalBalance = balance
        monthlyPaymentUpperBound = minimumFixedMonthlyPayment
        minimumFixedMonthlyPayment =round((monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2, 2)

    # else:
    #         monthlyPaymentUpperBound = minimumFixedMonthlyPayment
    #
    # minimumFixedMonthlyPayment =round((monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2, 2)



print "Lowest Payment", round (minimumFixedMonthlyPayment, 2)
