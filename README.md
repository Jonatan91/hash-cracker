# Password Hash Cracker (Educational)

A simple, dictionary-based password hash cracker written in Python.  
Supports **MD5**, **SHA1**, and **SHA256** using the standard `hashlib` library.

> **Educational use only.** Do not attempt to crack credentials you do not own or lack explicit permission to test.

---

## Features
- Dictionary (wordlist) cracking for MD5 / SHA1 / SHA256.
- Clean CLI with `argparse` (algorithm selection, wordlist path, line cap).
- Fast and dependency-free (only Python standard library).
- Clear result and elapsed time.

---

## Requirements
- Python 3.x  
- No external dependencies (uses `hashlib`).

Project structure (example):

---

## Usage

### General syntax
```bash
python3 src/main.py --hash <HEX_DIGEST> --algo <md5|sha1|sha256> --wordlist <PATH> [--max-lines N] [--quiet]
```

---

## Crack MD5 of "password"
# MD5('password') = 5f4dcc3b5aa765d61d8327deb882cf99
python3 src/main.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --algo md5 --wordlist wordlists/dict.txt

---

## Crack SHA1 of "password"
# SHA1('password') = 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
python3 src/main.py --hash 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8 --algo sha1 --wordlist wordlists/dict.txt

---

## Limit the number of candidates read from the wordlist
python3 src/main.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --algo md5 --wordlist wordlists/dict.txt --max-lines 1000

---

## How it works (short version)

- The tool does not decrypt hashes.

- It reads candidates from a wordlist and, for each one, computes the selected algorithm (MD5/SHA1/SHA256) and compares the hex digest with the target.

- If a match is found, it prints the original password.

---

## About “algo” and differences

--algo means hash algorithm:

MD5 (128-bit, 32 hex chars) — obsolete; fast and easy to crack.

SHA1 (160-bit, 40 hex chars) — stronger than MD5 but also deprecated due to collisions.

SHA256 (256-bit, 64 hex chars) — stronger, still fast to compute; weak passwords remain crackable by dictionary/bruteforce.

For real systems, use slow, salted password hash schemes such as bcrypt, scrypt, or Argon2.

## Limitations

- Dictionary-based only (no rules/masks/charset combinatorics here).

- No salts, no slow KDFs (it’s intentionally simple for learning    purposes).

- Success depends entirely on whether the correct password is present in the wordlist.

---

## Roadmap (nice-to-have)

- Add support for salted formats and slow KDFs (bcrypt/scrypt/Argon2).

- Add mask-based or hybrid attacks.

- Multi-process support for larger wordlists.

## Ethical Notice

This project is for training in a controlled environment.
Cracking credentials you do not own or are not authorized to test may be illegal and unethical.