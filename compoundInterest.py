def calculateCompoundInterest():
    interestFormula()
    print("---")
    interestFormula()
    print("---")
    interestFormula()


def interestFormula():
    client_principle = float(input("Principle (amount): "))
    client_time = float(input("Time:               "))
    client_rate = float(input("Rate:               "))
    total_amount = client_principle * ((1 + (client_rate / 100)) ** client_time)
    compInterest = (total_amount - client_principle)
    print("Compound Interest: "+ str(round(compInterest,2)))
 

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
