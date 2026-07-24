# 🛒 Smart Retail AI Checkout System

An AI-powered retail checkout system that automates product detection, billing, inventory management, and receipt generation using **YOLOv8**, **OpenCV**, **Streamlit**, and **SQLite**.

The application detects products from camera input, calculates bills automatically, updates inventory in real time, and generates downloadable PDF receipts, providing a fast and contactless checkout experience.

---

## 🚀 Features

- 🤖 Real-time product detection using YOLOv8
- 📷 Camera-based product scanning
- 🛍️ Automatic shopping cart generation
- 💳 AI-powered billing system
- 📦 Real-time inventory management
- 🗄️ SQLite database integration
- 📄 Automatic PDF receipt generation
- 🎨 Interactive Streamlit dashboard
- ⚡ Fast inference with optimized YOLOv8 model
- 🔄 Automatic stock quantity updates after every purchase

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python 3.10+ |
| AI Model | YOLOv8 (Ultralytics) |
| Computer Vision | OpenCV |
| Web Interface | Streamlit |
| Database | SQLite |
| Image Processing | Pillow, NumPy |
| PDF Generation | ReportLab |
| Data Handling | Pandas |
| Model Framework | Ultralytics |

---

## 📂 Project Structure

```text
Smart-Retail-AI/
│
├── app.py                 # Main Streamlit application
├── detect.py              # YOLO object detection
├── database.py            # SQLite operations
├── billing.py             # Billing module
├── receipt.py             # PDF receipt generator
├── products.db            # Product database
├── yolov8n.pt             # YOLO model weights
├── requirements.txt
├── receipts/
└── README.md
```

---

# ⚙️ Workflow

1. Launch Streamlit application.
2. Capture product image using camera.
3. YOLOv8 detects products automatically.
4. Detected items are added to the shopping cart.
5. Bill is generated automatically.
6. Inventory quantity is updated.
7. PDF receipt is generated and saved.
8. Customer completes checkout.

---

# 📊 Project Statistics

| Metric | Value |
|---------|-------|
| AI Model | YOLOv8 Nano |
| Programming Language | Python |
| Database | SQLite |
| User Interface | Streamlit |
| Object Detection Confidence | ≥ 50% |
| Receipt Format | PDF |
| Inventory Update | Real-Time |
| Camera Support | Yes |
| Supported Modules | 3 |
| Core Python Files | 6+ |
| Database Tables | 1 |
| Generated Receipts | Unlimited |

---

# 📦 Modules

## 📷 AI Product Scanner
- Detects products using YOLOv8.
- Captures images directly from camera.
- Draws bounding boxes around detected products.
- Automatically counts detected items.

---

## 💳 Billing System

- Creates shopping cart automatically.
- Calculates subtotal.
- Calculates grand total.
- Supports multiple products in one transaction.

---

## 📦 Inventory Management

- Displays available products.
- Shows current stock.
- Automatically deducts sold quantity.
- Prevents manual inventory tracking.

---

## 📄 Receipt Generation

- Generates professional PDF receipts.
- Includes:
  - Product Name
  - Quantity
  - Price
  - Total
  - Grand Total
- Stores receipts automatically.

---

# 💾 Database Schema

| Field | Type |
|--------|------|
| id | INTEGER |
| name | TEXT |
| price | REAL |
| quantity | INTEGER |

---

# 📈 Future Enhancements

- Barcode & QR Code Support
- Customer Login
- Payment Gateway Integration
- Multi-Camera Support
- Cloud Database
- Sales Analytics Dashboard
- Admin Authentication
- GST Invoice Generation
- Voice Assistant
- Mobile Application

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/khushbumeena-4/Smart-Retail-AI.git
```

Move into project

```bash
cd Smart-Retail-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Screenshots

<img width="1536" height="1024" alt="retail" src="https://github.com/user-attachments/assets/7a4f3b58-0ff9-498e-910c-07bb6d1b507e" />


---

# 👩‍💻 Author

**Khushbu Meena**

B.Tech Computer Science Engineering

GitHub:
https://github.com/khushbumeena-4

---

## ⭐ If you found this project useful, consider giving it a Star.
