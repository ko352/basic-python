try:
    number = int(input("ကိန်းးဏန်းတစ်ခု ရိုက်ထည့်ပါ: "))
    result = 10 / number
    print(f"ရလဒ်ကတော့: {result} ဖြစ်ပါတယ်။")
except ZeroDivisionError:
    print("⚠ Error: သုည (0) နဲ့စားလို့မရပါဘူး တပည့်ကြီးရဲ့။")
except ValueError:
    print("⚠ Error: ကျေးဇူးပြုပြီး စာသားတွေမရိုက်ပါနဲ့၊ ဂဏန်းပဲရိုက်ပေးပါ။")