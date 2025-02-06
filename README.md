---

### 📌 **README.md** (Flask API for Number Classification)  

```md
# 📊 Flask Number Classification API

This is a **Flask-based REST API** that classifies a given number based on various mathematical properties. It determines if the number is **prime, perfect, Armstrong, or odd/even** and provides a **fun fact** using the [Numbers API](http://numbersapi.com/).  

---

## 🚀 Features

- ✅ **Check if a number is prime**
- ✅ **Check if a number is perfect**
- ✅ **Identify Armstrong numbers**
- ✅ **Determine if a number is odd or even**
- ✅ **Calculate the sum of digits**
- ✅ **Fetch a fun mathematical fact using the Numbers API**
- ✅ **CORS support for cross-origin requests**
- ✅ **Deployed on [Render](https://render.com)**

---

## 📡 API Endpoint

### **🔹 GET /api/classify-number**
#### **Request Example**
```
https://hng-stage1-03as.onrender.com/api/classify-number?number=371
```

#### **Response (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### **Response (400 Bad Request)**
```json
{
    "number": "abc",
    "error": true
}
```

---

## 🛠️ **Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Kizito24/hng_stage1.git
cd hng_stage1
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run Locally**
```bash
python wsgi.py
```
API will be available at:  
```
https://hng-stage1-03as.onrender.com/api/classify-number?number=371
```
---

## 🛠 **Project Structure**
```
/flask-number-api
│── api/
│   ├── index.py  # Flask app
│── requirements.txt
│── render.yaml   # Render deployment settings
│── wsgi.py       # Gunicorn entry point
│── README.md     # Documentation
```

---

## 📜 **Tech Stack**
- **Flask** (Python Web Framework)
- **Flask-CORS** (CORS handling)
- **Gunicorn** (Production WSGI Server)
- **Requests** (API calls)
- **Render** (Deployment platform)

---

## 📧 **Contact**
If you have any issues, feel free to open an **issue** or contact me at:
- 📩 **Email:** kizitochiazor@example.com
- 🔗 **GitHub:** [Kizito24](https://github.com/Kizito24)

---

🎉 **Enjoy using the Flask Number Classification API!** 🚀
```