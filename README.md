# 🔗 Serverless URL Shortener (AWS Lambda + API Gateway + DynamoDB)

A lightweight serverless URL shortener built using **AWS Lambda**, **API Gateway**, and **DynamoDB** — fully serverless, pay-per-use, and free-tier optimized 💸.

---

## ⚙️ Features

- Shortens any long URL into a 6-char unique shortcode 🔐
- Redirects users to original URL using `/shortcode` route 🌐
- Fully serverless using AWS Lambda + API Gateway
- Stores mappings in DynamoDB
- 301 redirect support for SEO friendliness 📈

---

---

## 🚀 Usage

### 🔹 1. Shorten a URL

**Endpoint:**  
`POST /shorten`  
**Body:**
```json
{
  "url": "https://<Some long url u need to Shorten>.com"
}
```

**Response:**
```json
{
  "shortcode": "a1b2c3",
  "short_url": "https://your-api-url/a1b2c3"
}
```

---

### 🔹 2. Redirect

Access the shortened URL:  
`GET /a1b2c3` 
➡️ Redirects to `https://<Some long url u need to Shorten>.com`

---

## 🛠️ Tech Stack

- AWS Lambda (Python 3.13) 
- Amazon API Gateway 
- Amazon DynamoDB - to store the actual and shortened URL
- CloudWatch Logs - for the logs monotoring(minimal for free-tier optimization)
- Deployed in **Asia Pacific (Mumbai)** region

---

## 📂 Project Structure

```
📁 url-shortener/
├── shorten_url.py        # Lambda: shorten handler
├── redirect_url.py       # Lambda: redirect handler
├── test_request.http     # Test requests for REST clients
├── architecture.png      # Diagram of architecture
└── README.md             # You’re here!
```

---

## 💡 Future Ideas

- Add a frontend UI for input
- Custom shortcode input
- Analytics for clicks 🔍
- Expiry system for links

---

## 👤 Author

**Sahithyan M**  
🔗 [GitHub](https://github.com/Sahithyan04)  
🔗 [LinkedIn](https://linkedin.com/in/sahithyanm)

---


