## SimpleSMSAPI
Simple API to send SMS using twilio account.

#### How to use?
Example
`curl -u user:password http://localhost:8000/api1/send_sms -d "code=+1" -d "number=7888774455" -d "text=hello there"`

#### Users
Users and account configuration is managed via django admin (/admin)
Only the first twilio account is going to be used and registered phone numbers are going to be randomly chosen