import schedule
import subprocess
import time

def my_function():
    # کدهای برنامه
    # برای مثال، اجرای یک برنامه با استفاده از Streamlit:
    subprocess.run(['streamlit', 'run', 'app.py'])

# تعریف تابع برای اجرای برنامه هر روز ساعت ۱۲:۰۰ بعدازظهر
def run_daily():
    my_function()

# تنظیم زمان اجرای برنامه
schedule.every().day.at("12:00").do(run_daily)

# اجرای برنامه به صورت بی‌پایان
while True:
    schedule.run_pending()
    time.sleep(1)