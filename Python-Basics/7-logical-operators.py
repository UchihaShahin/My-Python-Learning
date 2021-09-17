# if applicant has high income and good credit, he is eligible for loan

has_high_income = True
good_credit = True
has_criminal_record= False


#! AND: all conditions must be true...
if has_high_income and good_credit:
    print("He is Eligible (and)")

#! OR: one (must) or more conditions should be true...
if has_high_income or good_credit:
    print("He is Eligible (or)")

#! NOT:
if has_high_income and not has_criminal_record:
    print("He is Eligible (NOT)")
