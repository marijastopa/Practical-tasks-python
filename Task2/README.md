# SurveyMonkey Survey Creator and Email Notifier
This Python script allows you to create a survey on SurveyMonkey, add questions, and send the survey link to a list of recipients via email using Gmail's SMTP service. The script leverages the SurveyMonkey API for survey creation and Gmail’s SMTP server for email notifications.

## Features
- **Survey Creation:** Automatically creates a survey on SurveyMonkey with a title and set of questions from a JSON file.
- **Email Notification:** Sends the survey link via email to recipients listed in a text file.
- **SMTP Authentication:** Uses Gmail's SMTP service with an App Password for secure access.

## Prerequisites
- Make sure Python is installed on your system.
- **SurveyMonkey Account:** You need a SurveyMonkey account with an API Access Token.
- **Google Account with 2-Step Verification:** Required to use an App Password for SMTP authentication with Gmail.

## Setup Instructions
1. SurveyMonkey API Setup
- Sign up for SurveyMonkey
- Create an application in the Developer Portal

2. Google Account App Password Setup
- **Enable 2-Step Verification:** Go to your Google Account Security settings and enable 2-Step Verification.
- **Generate an App Password:** Go to App Passwords in your Google Account settings and generate a 16-character App Password.
- Copy the App Password and keep it for configuring SMTP in the script.

## Project Structure
Ensure you have the following files in the same directory as the create_survey.py script:
- create_survey.py: The main Python script.
- survey_questions.json: A JSON file containing the survey title, page, questions, and answers.
- recipients.txt: A text file with a list of email addresses to which the survey link will be sent.

### Example of survey_questions.json
```
{
  "Survey_Title": {
    "Page_One": {
      "Question1": {
        "Description": "What is your favorite color?",
        "Answers": ["Red", "Blue", "Green"]
      },
      "Question2": {
        "Description": "What is your favorite animal?",
        "Answers": ["Cat", "Dog", "Bird"]
      },
      "Question3": {
        "Description": "What is your favorite food?",
        "Answers": ["Pizza", "Sushi", "Pasta"]
      }
    }
  }
}
```

### Example of recipients.txt
```
example1@example.com
example2@example.com
example3@example.com
```

## Script Configuration
Update the following variables in create_survey.py:
- **ACCESS_TOKEN:** Replace "YOUR_ACCESS_TOKEN_HERE" with your SurveyMonkey API access token.
- **SMTP Details:**
  - smtp_server: Set as "smtp.gmail.com" for Gmail.
  - smtp_port: Set as 587 for Gmail (TLS).
  - sender_email: Replace "YOUR_EMAIL@gmail.com" with your Gmail address.
  - sender_password: Replace "YOUR_APP_PASSWORD" with your generated Gmail App Password.
 
Running the Script
Once everything is set up, run the script with:
```python3 create_survey.py```

## Script Functionalities
1. ``create_survey`` Function
This function uses the SurveyMonkey API to create a survey, add a page, and add questions.
- Parameters: ``survey_data`` (dictionary containing survey details from ``survey_questions.json``).
- Steps:
  1. **Create Survey:** Sends a POST request to SurveyMonkey’s API to create a new survey with the title from survey_questions.json.
  2. **Create Page:** Adds a page to the survey.
  3. **Add Questions:** Adds each question from the JSON file to the created page. Supports multiple-choice questions with predefined answers.
- Output: Prints the survey ID, page ID, and each question’s ID for tracking.

2. ``send_survey_via_email`` Function
This function uses Gmail’s SMTP server to send the survey link to a list of recipients.
- Parameters:
  - ``survey_id:`` The ID of the created survey, used to generate the survey link.
  - ``recipients_file:`` Path to ``recipients.txt``, which contains the list of email addresses.
- Steps:
  1. **SMTP Connection:** Connects to Gmail’s SMTP server using TLS and logs in with the App Password.
  2. **Generate Survey Link:** Constructs the survey link using the survey ID.
  3. **Send Emails:** Loops through each email in ``recipients.txt``, sending a personalized message with the survey link.
- Output: Prints a success message for each email sent or an error if there are issues with the SMTP connection.

## Error Handling
- **SurveyMonkey API Errors:** If any SurveyMonkey API request fails, the script will print an error message with the response details.
- **SMTP Authentication Errors:** If SMTP authentication fails, an error message is printed with the reason.
- **File Not Found Errors:** If ``survey_questions.json`` or ``recipients.txt`` is missing, the script will raise a file-not-found error.

## Example Output
After running the script, you should see output like this:
```
Survey Response Status: 201
Survey created with ID: 123456789
Page created with ID: 987654321
Question 'Question1' added with ID: 112233445
Question 'Question2' added with ID: 223344556
Question 'Question3' added with ID: 334455667
Invitation sent to example1@example.com
Invitation sent to example2@example.com
```
If there are any issues, the error message will be displayed.

