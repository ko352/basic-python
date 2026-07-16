def check_result(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"
my_score = 45
result = check_result(my_score)
print(result)