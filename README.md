
# 🧠 AI-Based Requirement Converter

## 📌 Overview

This project is a **prototype AI automation tool** that simplifies the conversion of **high-level business requirements** into **low-level technical specifications**, including:

- 📦 Functional Modules  
- 🗃️ Database Schemas  
- 📜 Pseudocode Logic  

This tool leverages Natural Language Processing (NLP) to analyze textual inputs and extract meaningful actions, actors, and entities, then maps them to logical software components.

---

## 🎯 Objective

> **"To Create an AI-based automation tool that can analyze high-level business requirements and break them down into modules, schemas, and pseudocode."**

This is aims to demonstrate the ability to design a software pipeline that bridges business understanding with system architecture.

---

## 🛠️ Features

- Accepts natural language input describing a business requirement.
- Extracts **verbs** (actions) and **nouns** (resources/roles) using `spaCy`.
- Maps actions to **modules** using a rule-based dictionary.
- Suggests basic **relational database schemas** based on key nouns.
- Outputs **pseudocode** logic blocks for important functionalities.

---

## 📂 Project Structure

```
requirement_converter/
├── main.py
└── README.md  <-- this file
```

---

## 🔧 Installation

1. Clone the repository or download the files.

2. Install Python dependencies:

```bash
pip install spacy
python -m spacy download en_core_web_sm
```

---

## ▶️ How to Run

```bash
python main.py
```

Then input a high-level requirement when prompted.

---

## 🧪 Example

### Input:

> "Create a portal where users can register, login, and upload documents which admins verify."

### Output:

```
📦 Suggested Modules:
- Authentication
- File Management
- Admin Panel

🗃️ Suggested Database Schemas:
- Users(id, name, email, password)
- Documents(id, user_id, file_url, status)

📜 Suggested Pseudocode:

def register_user(name, email, password):
    # Add user to database
    pass

def login_user(email, password):
    # Authenticate user
    pass

def upload_document(user_id, file):
    # Save file and link to user
    pass

def review_document(doc_id, action):
    if action in ['approve', 'reject']:
        # Change status
        pass
```

---

## 🧠 NLP Concepts Used

- **Tokenization** and **Lemmatization** to extract verbs and nouns.
- **Part-of-Speech Tagging** to distinguish actions from resources.
- **Rule-based Mapping** to relate verbs to system modules.

---

## ⚙️ Technology Stack

| Component | Tool         |
|----------|--------------|
| Language | Python       |
| NLP      | spaCy        |
| Input    | CLI          |
| Output   | Text Console |

---

## 💡 Future Improvements

- Use a Large Language Model (LLM) like GPT-4 for smarter mapping.
- Build a **Streamlit GUI** for better UX.
- Export output to **Markdown**, **JSON**, or **PDF** formats.
- Add support for more complex schema relationships (1:n, n:n).
- Integrate Entity-Relationship Diagrams (ERDs).

---

## 👤 Author

Internship Assessment Submission by: **Priyanshu Gupta**
