desserts = ["ရွှေရင်အေး", "ဆနွင်းမကင်း","ငှက်ပျောပူတင်း", "မုန့်ကြာစိ"]
print(desserts)
print("ပထမဆုံး အချိုပွဲ -", desserts[0])
print("ဒုတိယ အချိုပွဲ -", desserts[1])
print("နောက်ဆုံးအချိုပြွ -", desserts[-1])
desserts[0] = "မုန့်လက်ဆောင်"
print("နာမည်ပြင်ပြီးနောက် -", desserts)
desserts.append("ကျောက်ကျောပူတင်း")
print("အသစ်ထည့်ပြီးနောက်အချိုပွဲစာရင်း -", desserts )
for dessert in desserts:
    print("ဆရာ့တပည့်လေးကြိုက်တဲ့ အချိုပွဲကတော့ -", dessert)
numbers = [1,2,3,4,5]
for number in numbers:
    print( "၂ ဖြင့် မြှောက်ပြီးရသောတန်ဖိုး -",number*2)
    if number % 2 != 0:
        print("မမဂဏန်းလေးဖြစ်ပါတယ် -",number)