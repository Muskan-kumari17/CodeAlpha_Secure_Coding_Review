# CodeAlpha Secure Coding Review

## CodeAlpha Cyber Security Internship – Task 3

### Project Title
Secure Coding Review

### Prepared By
**Muskan Kumari**  
B.Tech CSE – Cyber Security  
Rungta College of Engineering and Technology, Bhilai

## About the Project

This project is part of the CodeAlpha Cyber Security Internship – Task 3.

The project demonstrates a basic secure coding review by identifying security
weaknesses in a Python login program and improving the code to follow safer
coding practices.

## Vulnerabilities Identified

### 1. SQL Injection
The vulnerable program directly combines user input with an SQL query.

**Risk:** Malicious input could modify the SQL query.

**Improvement:** Parameterized SQL queries are used in the secure version.

### 2. Insecure Password Handling
The vulnerable program directly uses the entered password in the database query.

**Risk:** Sensitive authentication information may be handled insecurely.

**Improvement:** The secure version hashes the password before using it.

### 3. Missing Input Validation
The vulnerable program does not check whether the username and password are
empty.

**Risk:** Invalid or unexpected input can be processed.

**Improvement:** Basic input validation is added.

## Files

- `vulnerable_code.py` – Original code containing security weaknesses.
- `secure_code.py` – Improved version with security controls.
- `security_review.txt` – Security vulnerability analysis.
- `README.md` – Project documentation.

## Security Improvements

The secure version demonstrates:

- Parameterized SQL queries
- Basic input validation
- Password hashing
- Improved authentication handling

## Learning Outcome

This project helps demonstrate the importance of identifying security
vulnerabilities during code review and applying secure coding practices to
reduce security risks.

## Internship Details

**Organization:** CodeAlpha  
**Domain:** Cyber Security  
**Task:** Task 3 – Secure Coding Review