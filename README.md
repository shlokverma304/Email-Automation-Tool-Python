# Email Automation Tool

A Python-based Email Automation Tool that reads student details from a CSV file and sends personalized emails automatically using Gmail SMTP.

## Features

* Read data from CSV file
* Send personalized emails
* Dynamic subject and message
* Gmail SMTP integration
* Bulk email sending

## Technologies Used

* Python
* CSV
* smtplib
* EmailMessage

## File Structure

```text
PROJECT
│
├── EMAIL.py
├── students.csv
└── README.md
```

## CSV Format

```csv
Name,Email
Shlok,example@gmail.com
Rahul,example2@gmail.com
```

## Run

```bash
python EMAIL.py
```


