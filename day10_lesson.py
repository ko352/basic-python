# Day-10: ကျွန်တော့်တို့ရဲ့ ပထမဆုံး Python ကမ္ဘာ
print("မင်္ဂလာပါ ဆရာ! ကျွန်တော် Python လောကထဲကို စတင်ခြေချလိုက်ပါပြီ")
# ခေါင်းစဉ် (၃) ခုအတွက် စိတ်ကူးထဲက Variables လေးတွေ ဆောက်ကြည့်ရအောင်
data_target = "Data Analytics"
ai_target = "AI & Chatbot Development"
automation_target = "task Automation"
print(f"ကျွန်တော်ရဲ့ ရည်မှန်းချက်တွေကတော့{data_target}၊ {ai_target}၊ နဲ့ {automation_target}တို့ဖြစ်ပါတယ်။")
# ၁။ Variable မျိုးစုံကိုတည်ဆောက်ဆောက်ခြင်း
student_name = "တပည့်ကျော်ကြီး" # String
learning_day = "10"             # Integer
python_rating = 9.5           # Float
is_excited = True             # Boolean
# ၂။ အဲဒီ Variable တွေကို print ထုတ်ကြည့်ခြင်း
print("--- ကျောင်းသား အချက်အလက် ---")
print("အမည်:",student_name)
print("သင်ယူသည့်ရက်စွဲ: Day -", learning_day)
print("စိတ်ကျေနပ်မှုနှုန်း:", python_rating)
print("စိတ်လှုပ်ရှားနေသလား:", is_excited)
# စွမ်းရည်ဆန်း: တန်ဖိုးတွေကို တွက်ချက်ကြည့်ခြင်း
next_year_day = int(learning_day) + 5
print("နောက် ၅ ရက်ဆိုရင် Day -", next_year_day, "ကိုရောက်ပါပြီ။")