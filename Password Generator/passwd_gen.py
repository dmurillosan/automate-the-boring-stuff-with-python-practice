# CLI Password Generator for secure passwords
# Made by David Murillo Santiago

# Start of Program:
import secrets
import string
import logging
import argparse
import sys
import random

logging.basicConfig(level=logging.DEBUG, format="\n%(funcName)s - line %(lineno)d: %(message)s")
logging.disable(logging.CRITICAL)

def help_page():
    help_text = """
Password Generator - Generate cryptographically secure passwords

Usage: python passwd.py [-l LENGTH | -len LENGTH | --length LENGTH] [-h | --help]

Options:
  -h, -help, --help       Show this help message and exit
  -l, --len               Password length (default: 16, min: 8, max: 512)
                          Example: -l 64 generates a 64-character password

Description:
  Generates a secure random password using cryptographically strong
  randomness. Passwords include uppercase letters, lowercase letters,
  numbers, and symbols.

  Default length: 16 characters (CISA recommended minimum)
  Minimum length: 8 characters
  Maximum length: 512 characters (Inspired by SHA-512's key size)

Examples:
  python passwd.py              Generate 16-character password (default)
  python passwd.py -l 32        Generate 32-character password
  python passwd.py --length 128 Generate 128-character password
  python passwd.py -len 64      Generate 64-character password

Note:
  The generated password is output to stdout only and is not stored,
  logged, or persisted anywhere. Use a password manager to securely
  store your generated passwords.
"""
    print(help_text)

def parse_flag():
    parser = argparse.ArgumentParser(description="Generate cryptographically secure passwords", add_help=False)

    parser.add_argument('-l', '--len',
                               required=False,
                               type=int,
                               default=16,)

    parser.add_argument('-h', '--help',
                               required=False,
                               action="store_true")
    args = parser.parse_args()
    logging.debug(f"flag length: {args.len}")
    if args.help:
        help_page()
        sys.exit()
    elif not (args.len >= 8 and args.len <= 512):
        print(f"ERROR: invalid parameter length -- '{args.len}' \nTry '--help' for help page")
        sys.exit()
    else:
        logging.debug(f"final flag length check: {args.len}")
        return args.len

def character_list():
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    sym = list(string.punctuation)
    num = list(string.digits)
    return lower, upper, sym, num

def required_password_characters():
    lower_case, upper_case, symbols, numbers = character_list()
    wordbank = lower_case + upper_case + symbols + numbers
    logging.debug(f"alphabet: {wordbank}")
    character_requirements = (secrets.choice(lower_case) + secrets.choice(upper_case) +
                              secrets.choice(symbols) + secrets.choice(numbers))
    logging.debug(f"password required characters: {character_requirements}")
    return character_requirements, wordbank

def generate_passwd():
    password_prereq, wordbank = required_password_characters()
    password_prereq = list(password_prereq)
    password_length = parse_flag()
    password = []

    for i in range((password_length - 4)):
        password.append(secrets.choice(wordbank))
    password = password + password_prereq
    password = random.sample(password, len(password))
    password = ''.join(password)
    logging.debug(f"password: {password} + length: {len(password)} + type: {type(password)}")
    return password

if __name__ == "__main__":
    print(generate_passwd())