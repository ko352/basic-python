try:
    number = int(input("ဂဏန်းတစ်ခုရိုက်ထည့်ပါ: "))
    result = 10 / number
    print(f"ရလဒ်ကတော့ {result} ပါ။")
except ZeroDivisionError:
    print("သတိပြုရန်: 0 နဲ့စားလို့မရပါဘူး ခင်ဗျာ။")
except ValueError:
    print("သတိပြုရန်: ဂဏန်ူပဲ ရိုက်ထည့်ပေးပါနော်။")
except Exception as e:
    print(f"မမျှော်လင့်ထားတဲ့ အမှားတစ်ခုခုဖြစ်သွားပါတယ်: {e}")