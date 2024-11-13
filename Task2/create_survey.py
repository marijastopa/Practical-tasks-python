import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up SurveyMonkey API details
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"  # Replace with your actual SurveyMonkey access token
BASE_URL = "https://api.surveymonkey.com/v3"

def create_survey(survey_data):
    survey_name = list(survey_data.keys())[0]
    page_name = list(survey_data[survey_name].keys())[0]
    questions = survey_data[survey_name][page_name]

    # Step 1: Create Survey
    survey_response = requests.post(
        f"{BASE_URL}/surveys",
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        },
        json={"title": survey_name}
    )

    print("Survey Response Status:", survey_response.status_code)
    print("Survey Response JSON:", survey_response.json())

    if survey_response.status_code == 201 and "id" in survey_response.json():
        survey_id = survey_response.json()["id"]
        print(f"Survey created with ID: {survey_id}")
    else:
        print("Error creating survey:", survey_response.json())
        return None

    # Step 2: Create Page in Survey
    page_response = requests.post(
        f"{BASE_URL}/surveys/{survey_id}/pages",
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        },
        json={"title": page_name}
    )
    page_id = page_response.json().get("id")
    print(f"Page created with ID: {page_id}")

    # Step 3: Add Questions to Page
    for question_name, question_data in questions.items():
        question_payload = {
            "headings": [{"heading": question_data["Description"]}],
            "family": "multiple_choice",
            "subtype": "vertical",
            "answers": {"choices": [{"text": ans} for ans in question_data["Answers"]]}
        }
        question_response = requests.post(
            f"{BASE_URL}/surveys/{survey_id}/pages/{page_id}/questions",
            headers={
                "Authorization": f"Bearer {ACCESS_TOKEN}",
                "Content-Type": "application/json"
            },
            json=question_payload
        )
        print(f"Question '{question_name}' added with ID: {question_response.json().get('id', 'N/A')}")

    return survey_id

def send_survey_via_email(survey_id, recipients_file):
    survey_link = f"https://www.surveymonkey.com/r/{survey_id}"

    # SMTP Configuration for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "YOUR_EMAIL@gmail.com"  # Replace
    sender_password = "YOUR_APP_PASSWORD"   # Replace

    # Read recipient emails from file
    with open(recipients_file, 'r') as f:
        emails = [line.strip() for line in f if line.strip()]

    # Connect to SMTP server and send emails
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        for recipient in emails:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = "Please participate in our survey"

            body = f"Hi,\n\nWe'd love to hear your feedback! Please participate in our survey by clicking the link below:\n{survey_link}\n\nThank you!"
            msg.attach(MIMEText(body, 'plain'))

            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"Invitation sent to {recipient}")

        server.quit()
    except Exception as e:
        print("Error sending emails:", e)

if __name__ == "__main__":
    # Load survey questions from JSON file
    with open("survey_questions.json", "r") as json_file:
        survey_data = json.load(json_file)

    # Create survey
    survey_id = create_survey(survey_data)

    # Send survey link via email
    if survey_id:
        send_survey_via_email(survey_id, "recipients.txt")

