# Password Strength Checker

A Python tool that checks password strength using regex.

## Features
- Checks length
- Uppercase, lowercase, digits, special characters
- Gives feedback

## Run
python3 password_checker.py

## Sample Output

Enter password: Hello123  
Password Strength: Medium  

Suggestions:
- Add special characters

## How it Works

The program evaluates password strength based on:
- Length (>= 8)
- Lowercase letters
- Uppercase letters
- Numbers
- Special characters

Each condition adds to a score which determines strength.