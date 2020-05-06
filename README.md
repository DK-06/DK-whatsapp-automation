# DK-whatsapp-automation
# It's not a auto reply bot. It's used to send a message to specific person at a specified time 
# Eg: send a birthday wishes at midnight is possible using this
# pip install python3
# pip install selenium
# Download chrome driver using this link: https://chromedriver.chromium.org/
# stable version (recomended)
# first time you must need to scan qr code and then it didn't ask you for scanning the qr code. so that you must need to set the cache
# In windows, it's located in C:/Users/"system name"/AppData/Local/Google/Chrome/User Data/Default
# This is link for os user data dir:  https://chromium.googlesource.com/chromium/src.git/+/62.0.3202.58/docs/user_data_dir.md
check it for yours

# set the chromedriver path in that line in python file. driver=webdriver.Chrome(executable_path='path of chromedriver', options=options)
# set the time in this place(///"hour"///, ///"minute"///). if (time.localtime(time.time()).tm_hour == ///"hour"/// and time.localtime(time.time()).tm_min == ///"minute"///)
# give the name of the person whom did you want to send a message. username_list = ['XXX', 'YYY', 'ZZZ']
Note: how did you save that name in your contact. (Like arun Dosthu, venki frd, Friend, Crush, Priya drlng) Uppercase, Lowercase included
# Type a message in this place.   message.send_keys('Hi!!!') 
