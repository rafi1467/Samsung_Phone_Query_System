# Samsung Phone Query and Review System

## Project Overview

This project is an intelligent Samsung smartphone information system that collects phone specifications from GSMArena, stores them in MySQL, and provides query and review services through a FastAPI API.

## Features

### Data Scraping
- Scrapes Samsung smartphone specifications from GSMArena
- Collects:
  - Phone Name
  - Display Size
  - Chipset
  - Storage
  - Battery
  - Charging Information

### Database
- MySQL Database
- Structured phone information storage

### Query System
- Search Samsung phones by name
- Retrieve specifications instantly

### Multi-Agent Review System
- Specification Retrieval Agent
- Review Generation Agent

### REST API
- FastAPI based API
- JSON responses

---

## Project Structure

```text
Samsung_Phone_Query_System/
│
├── scraper/
│   └── scrape.py
│
├── database/
│   └── load_to_mysql.py
│
├── rag/
│   ├── db.py
│   ├── search_phone.py
│   └── chatbot.py
│
├── agents/
│   └── review_agent.py
│
├── api.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- BeautifulSoup
- Requests
- MySQL
- FastAPI
- Uvicorn

---

## Database Setup

Create Database:

```sql
CREATE DATABASE samsung_phones;
```

Create Table:

```sql
CREATE TABLE phones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    display_size TEXT,
    chipset TEXT,
    storage TEXT,
    battery TEXT,
    charging TEXT
);
```

---

## Installation

Clone Repository

```bash
git clone YOUR_GITHUB_LINK
```

Go to Project Folder

```bash
cd Samsung_Phone_Query_System
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Scraper

```bash
python scraper/scrape.py
```

---

## Load Data to MySQL

```bash
python database/load_to_mysql.py
```

---

## Run API

```bash
uvicorn api:app --reload
```

---

## API Endpoints

### Home

```http
GET /
```

### Get Phone Information

```http
GET /phone/S24
```

### Generate Review

```http
GET /review/S24
```

---

## API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Sample Output

```json
{
  "name": "Samsung Galaxy S24 Ultra",
  "battery": "Li-Ion 5000 mAh",
  "chipset": "Snapdragon 8 Gen 3"
}
```

---

## Author

Riajul Haque Rafi

B.Sc. in Computer Science and Engineering

Daffodil International University