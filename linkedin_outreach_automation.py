import pandas as pd
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv("credentials.env")
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

EXCEL_FILE = "linkedin_profiles.xlsx"
MESSAGE_TEMPLATE = "Hi {name}, I’m reaching out to invite you to join our Scoreazy community. Let’s connect!"

def setup_driver():
    options = Options()
    profile_path = os.path.expanduser("~/.config/google-chrome/Default")  # Adjust based on OS
    if os.path.exists(profile_path):
        options.add_argument(f"user-data-dir={os.path.dirname(profile_path)}")
    else:
        print("⚠️ Chrome user profile not found, proceeding without it.")

    # Optional: run headless
    # options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    return driver

def login_to_linkedin(driver):
    try:
        driver.get("https://www.linkedin.com/login")
        time.sleep(2)

        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        username_field.send_keys(EMAIL)
        password_field.send_keys(PASSWORD + Keys.RETURN)
        time.sleep(3)
        print("✅ Logged in via credentials")
    except Exception as e:
        print("⚠️ Auto-login failed. Please login manually.")
        driver.get("https://www.linkedin.com/login")
        input("🔐 After manual login, press ENTER to continue...")

def extract_name_from_url(url):
    parts = url.rstrip("/").split("/")
    return parts[-1].replace("-", " ").title()

def send_connection_request(driver, profile_url, message):
    driver.get(profile_url)
    time.sleep(3)

    try:
        connect_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Connect')]")
        connect_button.click()
        time.sleep(2)

        add_note_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add a note')]")
        add_note_button.click()
        time.sleep(1)

        message_box = driver.find_element(By.ID, "custom-message")
        message_box.send_keys(message)
        time.sleep(1)

        send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send')]")
        send_button.click()
        return "Success"

    except NoSuchElementException:
        return "Already Connected or Button Not Found"
    except Exception as e:
        return f"Error: {str(e)}"

def run_automation():
    df = pd.read_excel(EXCEL_FILE)
    if "Status" not in df.columns:
        df["Status"] = ""

    driver = setup_driver()
    login_to_linkedin(driver)

    for index, row in df.iterrows():
        url = row['Profile URL']
        if pd.notna(row.get("Status")) and row["Status"].strip() != "":
            continue

        name = extract_name_from_url(url)
        personalized_msg = MESSAGE_TEMPLATE.format(name=name)
        status = send_connection_request(driver, url, personalized_msg)
        print(f"{url} => {status}")

        df.at[index, "Status"] = status
        time.sleep(5)

    driver.quit()
    df.to_excel(EXCEL_FILE, index=False)
    print("✅ Outreach completed and saved.")

if __name__ == "__main__":
    run_automation()
