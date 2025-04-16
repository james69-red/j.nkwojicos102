P = float(input("Enter Principal Amount: "))
R = float(input("Enter Interest Rate (in %): "))
T = float(input("Enter Time (in years): "))
n = int(input("Enter Compounding Frequency (e.g., 1 for yearly, 4 for quarterly, etc.): "))
PMT = float(input("Enter Payment per Period (for Annuity): "))


def simple_interest(P, R, T):
    """Calculate Simple Interest"""
    A = P * (1 + (R / 100) * T)
    return A

def compound_interest(P, R, n, t):
    """Calculate Compound Interest""" 
    A = P * (1 + (R / n))**(n * t)
    return A

def annuity_plan(PMT, R, n, t):
    """Calculate Annuity Plan"""
    rate = R / n
    A = PMT * ((1 + rate)**(n * t) - 1) / rate
    return A
print("Simple Interest:", simple_interest(P, R, T))
print("Compound Interest:", compound_interest(P, R, n, T))
print("Annuity Plan:", annuity_plan(PMT, R, n, T))