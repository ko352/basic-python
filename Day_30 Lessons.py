def make_coffee(cup_size, sugar_level="Normal"):
    return f" သောက်မည့်အရွက်အစားက {cup_size} ဖြစ်ပြီး, သကြားဓါတ်ကတော့ {sugar_level}! "
print(make_coffee("Large"))
print(make_coffee("Medium","Less Sugure"))

def sum_numbers(number_list):
    total = 0
    for num in number_list:
        total += num
    return total
scores = [10, 20, 30, 40, 50]
result = sum_numbers(scores)
print("ရရှိလာတဲ့ စုစုပေါင်းရလဒ်ကတော့:", result)