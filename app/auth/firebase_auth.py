import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyDQ4-z7nEqX0cMzj-5vMWxkLvEpfZIRQlM",
  "authDomain": "neno-63e45.firebaseapp.com",
  "projectId": "neno-63e45",
  "storageBucket": "neno-63e45.appspot.com",
  "messagingSenderId": "573746413201",
  "appId": "1:573746413201:web:6d3bc02b0d46ec2f7e4930",
  "measurementId": "G-TXV7TB02B1",
  "databaseURL": "https://neno-63e45-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
# storage = firebase.storage()
database = firebase.database()

def Users():
  extract_user = database.child("users").get()
  # extract_user = auth.get_account_info(id_token="eyJhbGciOiJSUzI1NiIsImtpZCI6IjY5NjI5NzU5NmJiNWQ4N2NjOTc2Y2E2YmY0Mzc3NGE3YWE5OTMxMjkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbmVuby02M2U0NSIsImF1ZCI6Im5lbm8tNjNlNDUiLCJhdXRoX3RpbWUiOjE3MDY5MzYzMzcsInVzZXJfaWQiOiJ3UkVNb2Rtb0JyWERYY1lNR2IycHpZMDI4VFUyIiwic3ViIjoid1JFTW9kbW9CclhEWGNZTUdiMnB6WTAyOFRVMiIsImlhdCI6MTcwNjkzNjMzNywiZXhwIjoxNzA2OTM5OTM3LCJlbWFpbCI6ImRheGFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImRheGFAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.HTcR7jiPPghgZ6ZBJbbHeqF5qsAdxGG7T8QeWiiCsuO9wceckELwlFbBLpcI7UsGe8MnZnw1gMM4VTGjfh9LotJIVpjtq7UHEErx8TovxMZxEUNxtYWAamzFJFnWbaXgAcTjtiASbleo8KagmsDZ7ddjEb_Ma2WOmv6BVT97sKd1DgVj2zi2DEywHH4dDTpcX5CMEyA-lmvER9R7LwIu-5c2RH8UcO4dd5M-3Ut6gYRIyvgfgBhvW9hYap8sY7vShx0wYzh6CwfdJImFK6dTbXSWRcmSVfreay04fHoNjd3hnzXjs7psSdMWfIYPhbOCrNwL64E1_yA0dgO1YiBq_Q")
  print(" ------------- start ------------- ")
  
  # Get the Firebase authentication users
  # users = auth.get_users()
  # print(" ------------- ")

  # # Extract user data from the response
  # user_list = [user.to_dict() for user in users]
  # print(f" --- user {user_list}")
  # return user_list

def signUp(email, password):
  try:  
    auth.create_user_with_email_and_password(email, password)
    return {"data": "success"}

  except:
    return {"data": "Invalid user or password. Try again. "}

    
def signIn(email, password):
  try:
    data = auth.sign_in_with_email_and_password(email, password)
    return {"data": data, "msg": "success"}
  except:
    return {"data": "Invalid user or password. Try again. "}

