<div align="center">

# 🔐 Project 1 — Password Strength Checker

![Project](https://img.shields.io/badge/Project-01-blue)
![Status](https://img.shields.io/badge/Status-Completed-green)
![Language](https://img.shields.io/badge/Language-Python3-blue?logo=python)
![Track](https://img.shields.io/badge/Track-Cybersecurity-red)

</div>

---

## 📌 About
This is **Project 1** of the DecodeLabs Cybersecurity Internship.
A Python program that checks whether a password is
**Weak**, **Medium**, or **Strong** based on real security rules.

---

## 🎯 Goal
> Build a program that evaluates risk through pure
> string handling and conditional logic.

---

## 🔑 How It Works

| Check | Rule | Result if Failed |
|-------|------|-----------------|
| Length | Minimum 8 characters | WEAK |
| Uppercase | At least one A-Z | Score -1 |
| Numbers | At least one 0-9 | Score -1 |
| Symbols | At least one !@#$% | Score -1 |

### Scoring System
```
Score 3/3  →  STRONG
Score 2/3  →  MEDIUM
Score 1/3  →  WEAK
```

---

## 💻 How to Run

```bash
python3 password_checker.py
```

---

## 🧪 Test Cases

| Password | Length | Upper | Number | Symbol | Result |
|----------|--------|-------|--------|--------|--------|
| hello | 5 | ❌ | ❌ | ❌ | WEAK |
| helloworld | 10 | ❌ | ❌ | ❌ | WEAK |
| Helloworld1 | 11 | ✅ | ✅ | ❌ | MEDIUM |
| Hello@world1 | 12 | ✅ | ✅ | ✅ | STRONG |

---

## 🧠 Key Concepts Learned
- String handling in Python
- Conditional logic and scoring
- Security basics and password entropy
- Pythonic approach using `any()`

---

## 📂 File Structure
```
project-1-password-checker/
├── password_checker.py
└── README.md
```

---

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/kuyilini-thiyagarajah-687755281)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/kuyilinithiyagarajah/Decodelabs-cybersecurity)

Made with 💙 by Kuyilini Thiyagarajah | Powered by DecodeLabs 🔐

</div>
