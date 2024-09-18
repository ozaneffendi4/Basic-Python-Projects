has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income or has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible")
# Logical operators ==> Or(at least one condition must be true) & ==> And(Both conditions must be true)