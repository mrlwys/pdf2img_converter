# 📄 PDF to Image Converter

A simple **drag-and-drop** PDF to PNG converter.

---

## ⚡ Quick Start

### **1️⃣ Install Python & Dependencies**
Make sure you have **Python 3.10+** installed. If not, [download here](https://www.python.org/downloads/).

Then, install the required package:
```bash
pip install pdf2image
```

### **2️⃣ Download and Install Poppler**

**Windows:**  
Run the following script **as Admin**:
```sh
install_poppler.bat
```

**Linux/macOS:**  
Run the script:
```sh
chmod +x install_poppler.sh
./install_poppler.sh
```

### **3️⃣ Convert PDFs to Images**
1. Place your **PDF files** inside the `pdfs` folder.
2. Run the conversion script:
```sh
python converter.py
```
3. Your images will be saved in the `images` folder. ✅

---

## 🔧 **For Advanced Users (Optional Virtual Environment)**
To keep dependencies isolated, use a **virtual environment**:

```bash
python -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate

pip install -r requirements.txt
```

---

## 📂 **Project Structure**
```
/pdf-to-image-converter
├── pdfs/                # Place your PDFs here
├── images/              # Output folder for images
├── poppler/             # Poppler installation folder
├── install_poppler.bat  # Windows installation script
├── install_poppler.sh   # Linux/macOS installation script
├── requirements.txt     # Dependencies
├── converter.py         # Conversion script
└── README.md            # This file
```

---

## 🚀 **Features**
- ✅ Converts **multiple PDFs** to PNG automatically.
- ✅ **Cross-platform**: Works on **Windows, Linux, and macOS**.
- ✅ **No manual configuration** needed—just **run the script**!
- ✅ Supports **virtual environments** for dependency management.

---

## ❓ **Troubleshooting**
### **Poppler not found?**
Make sure Poppler is installed and extracted correctly in the `poppler` folder.

To check if Poppler is working, run:
```sh
poppler/poppler-24.08.0/Library/bin/pdftoppm.exe -v  # Windows
pdftoppm -v  # Linux/macOS
```

If there's an issue, **reinstall Poppler** using the provided scripts.

---

## 📜 License
This project is open-source under the **MIT License**.
