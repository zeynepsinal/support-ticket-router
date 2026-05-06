# support-ticket-router
# Support Ticket Router

## Project Overview

This project is a simple rule-based support ticket routing system.

The application processes customer support tickets and automatically determines:

- Ticket category
- Priority level
- Assigned support team
- Reason for the classification

The system uses predefined business rules and keyword matching instead of machine learning.

---

# Features

- Automatic ticket categorization
- Priority detection
- Team assignment
- Human-readable reasoning output
- Handles incomplete or empty fields
- Case-insensitive keyword matching

---

# Classification Rules

## Categories

### Billing
Keywords:
- payment
- paid
- card
- invoice
- refund
- money

### Account
Keywords:
- login
- password
- account
- access

### Technical
Keywords:
- crash
- bug
- error
- upload
- broken
- not working

### General
Default category if no keyword matches.

---

# Priority Rules

## High Priority
A ticket becomes high priority if:

- The customer is premium
- The message contains:
  - urgent
  - asap
  - immediately
  - cannot use
  - blocked
- A billing issue includes:
  - money
  - refund
  - withdrawn

## Medium Priority
If category is:
- technical
- account

## Low Priority
All other tickets.

---

# Assigned Teams

| Category | Assigned Team |
|---|---|
| billing | payments-team |
| account | account-support |
| technical | technical-support |
| general | general-support |

---

# Project Structure

```text
support-ticket-router/
│
├── main.py
└── README.md

# Approach

## How did you break down the problem?

I divided the problem into several smaller steps:

1. Combine the ticket subject and message into one searchable text.
2. Detect the category using predefined keyword rules.
3. Determine the priority level based on customer type and urgency rules.
4. Assign the correct support team according to the category.
5. Generate a readable explanation for the result.

This structure keeps the solution simple, readable and easy to maintain.

---

## What assumptions did you make?

I assumed that:

- Keyword matching should be case-insensitive.
- Subject or message fields may sometimes be empty.
- Premium customers should always receive high priority.
- If multiple categories match, the first matching category is selected based on rule order.
- If no keyword matches exist, the ticket should be classified as general.

---

## What edge cases did you handle or intentionally ignore?

### Handled
- Empty subject or message
- Missing customerType field
- Uppercase/lowercase differences
- Tickets without matching keywords
- Invalid or incomplete ticket fields

### Ignored
- Advanced NLP or AI-based understanding
- Typo correction
- Multiple category assignment
- Sentiment analysis
- Language detection

---

## What part of your solution would you change first if requirements evolved?

If the project became larger, I would first move all classification rules and keywords into a separate configuration file such as JSON or YAML.

This would make the system easier to update without modifying the main codebase.

I would also consider:
- Adding unit tests
- Building a REST API with Flask or FastAPI
- Adding database support
- Replacing rule-based logic with machine learning

---

# How to Run

## Requirements

- Python 3.x

## Run the Project

```bash id="dz9y0q"
python main.py

The script will process the sample tickets and print the classification results.

---

# Example Output

```python
{
  "id": 1,
  "category": "billing",
  "priority": "high",
  "assignedTeam": "payments-team",
  "reason": "Billing issue from a premium customer."
}

## How Can I Test the Code?

You can test the project by editing the `tickets` list inside `main.py`.

Example test case:

```python
{
    "id": 5,
    "subject": "Urgent login issue",
    "message": "I am blocked and cannot access my account.",
    "customerType": "standard",
    "createdAt": "2026-04-29T10:20:00Z"
}

#Expected result:

Category: account
Priority: high
Assigned Team: account-support

#You can also test:

Empty messages
Premium technical issues
General questions
Multiple keyword matches
Invalid fields

###Technologies Used
Python 3
Rule-based classification
Basic string processing
Future Improvements

###Possible future improvements:

REST API support
Web interface
Database integration
AI/NLP-based classification
Multi-language support
Logging and monitoring
Unit testing
