uvicorn app.main:app --host 103.250.149.54 --port 8090 --reload
uvicorn app.main:app --port 8090 --reload
alembic revision --autogenerate -m "Added tables"

# New User Create
{
  "username": "smit@gmail.com",
  "password": "smit@123"
}
{
  "id": 1,
  "username": "smit@gmail.com",
  "email": "smit@gmail.com",
  "password": "smit@123",
  "f_name": "Smit",
  "l_name": "Patel",
  "gender": "MALE",
  "dob": "2000-01-01",
  "branch": 1
}
----
{
  "username": "hitesh@gmail.com",
  "password": "hitesh@123"
}
{
  "id": 2,
  "username": "hitesh@gmail.com",
  "email": "hitesh@gmail.com",
  "f_name": "Hitesh",
  "l_name": "Zala",
  "gender": "MALE",
  "dob": "2000-01-01",
  "branch": 1
}

# Treatments Create
{
  "name": "Hair Removal",
  "treatments_picture": ""
}
{
  "name": "Carbon Facial",
  "treatments_picture": ""
}
{
  "name": "Body Shaping",
  "treatments_picture": ""
}

# Sub Treatments Create
{
  "name": "Upper Lips",
  "treatments_picture": "",
  "price": 1200,
  "mrp": 1500,
  "discount": 20,
  "description": "Upper Lips desc . . . .",
  "treatment_time": "2024-02-18",
  "treatment_id": 1
}
{
  "name": "Full Face",
  "treatments_picture": "",
  "price": 1700,
  "mrp": 2000,
  "discount": 15,
  "description": "Full Face desc . . . .",
  "treatment_time": "2024-02-18",
  "treatment_id": 1
}

# Appointments
{
  "user_id": 1,
  "sub_treatment_id": 1,
  "appointment_time": "2024-02-18T19:25:47.267Z",
  "status": "Pending"
}


