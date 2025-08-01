# 🔗 LinkedIn Profile Outreach Automation

A professional Python-based automation script to send personalized connection requests to a list of LinkedIn profiles stored in an Excel file.

## 🎯 Project Objective

Automate LinkedIn outreach by reading profile URLs from an Excel sheet and sending a personalized message to each one using Selenium WebDriver.

---

## 📂 Folder Structure

```
.
├── linkedin_outreach_automation.py
├── linkedin_profiles.xlsx
├── credentials.env
└── README.md
```

---

## 📥 Input Files

- **linkedin_profiles.xlsx**: An Excel file with a column named **"Profile URL"** containing LinkedIn profile URLs.
- **credentials.env**: A file containing your LinkedIn login credentials in the following format:

```
LINKEDIN_EMAIL=your_email@example.com
LINKEDIN_PASSWORD=your_secure_password
```

> ⚠️ **Never share or hardcode your credentials directly in the Python file.** Always use environment variables.

---

## 🔧 Setup Instructions

1. **Install Dependencies**:

```bash
pip install pandas selenium python-dotenv openpyxl
```

2. **Update Excel File**:

Make sure your `linkedin_profiles.xlsx` contains a sheet with a column named:

```
| Profile URL                |
|----------------------------|
| https://linkedin.com/in/...|
```

3. **Add Your Credentials**:

Create a `credentials.env` file and add:

```
LINKEDIN_EMAIL=your_email
LINKEDIN_PASSWORD=your_password
```

4. **Adjust Chrome Profile Path (if needed)**:

In the script, modify this line if you're on Windows or Mac:

```python
profile_path = os.path.expanduser("~/.config/google-chrome/Default")
```

- For **Windows**: use something like `C:/Users/YourName/AppData/Local/Google/Chrome/User Data/Default`
- For **Mac**: use `~/Library/Application Support/Google/Chrome/Default`

5. **Run the Script**:

```bash
python linkedin_outreach_automation.py
```

> The script logs into LinkedIn, opens each profile URL, sends a personalized invite message, and updates the Excel file with the status.

---

## 💬 Message Template

```python
MESSAGE_TEMPLATE = "Hi {name}, I’m reaching out to invite you to join our Scoreazy community. Let’s connect!"
```

You can customize this template as needed. `{name}` will be automatically extracted from the profile URL.

---

## ✅ Output

The Excel file is updated with a new column called `Status` containing:

- `Success` – if message sent
- `Already Connected or Button Not Found` – if already connected or unable to find the button
- `Error: ...` – any unexpected errors

---

## 🔐 Ethical Disclaimer

This project is for educational/demonstration purposes only. Automated actions on LinkedIn may violate their terms of service. Use responsibly.

---

## 📌 Internship-Ready Notes

- Clean modular code following best practices
- Environment-based credential handling
- Excel and web automation integrated professionally
- Ideal for showcasing Python automation skills in interviews

