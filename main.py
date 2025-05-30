import spacy

nlp = spacy.load("en_core_web_sm")

# Predefined actions and mappings (can be extended)
actions_map = {
    "register": "Authentication",
    "login": "Authentication",
    "upload": "File Management",
    "verify": "Admin Panel",
    "approve": "Review System",
    "reject": "Review System",
    "submit": "Form Submission",
    "create": "Content Creation"
}

def extract_entities(text):
    doc = nlp(text.lower())
    verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    nouns = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return verbs, nouns

def map_modules(verbs):
    modules = set()
    for v in verbs:
        if v in actions_map:
            modules.add(actions_map[v])
    return list(modules)

def generate_schema(nouns):
    schema = []
    for n in nouns:
        entity = n.capitalize()
        if "user" in n:
            schema.append(f"{entity}s(id, name, email, password)")
        elif "document" in n or "file" in n:
            schema.append(f"{entity}s(id, user_id, file_url, status)")
        elif "leave" in n:
            schema.append(f"{entity}s(id, user_id, from_date, to_date, reason, status)")
        else:
            schema.append(f"{entity}s(id, name, description)")
    return schema

def generate_pseudocode(verbs, nouns):
    logic_blocks = []
    if "register" in verbs:
        logic_blocks.append("""def register_user(name, email, password):\n    # Add user to database\n    pass""")
    if "login" in verbs:
        logic_blocks.append("""def login_user(email, password):\n    # Authenticate user\n    pass""")
    if "upload" in verbs and "document" in nouns:
        logic_blocks.append("""def upload_document(user_id, file):\n    # Save file and link to user\n    pass""")
    if "verify" in verbs or "approve" in verbs:
        logic_blocks.append("""def review_document(doc_id, action):\n    if action in ['approve', 'reject']:\n        # Change status\n        pass""")
    return logic_blocks

def main():
    print("\n🔍 AI Business Requirement Analyzer")
    user_input = input("Enter a high-level business requirement:\n> ")

    verbs, nouns = extract_entities(user_input)
    modules = map_modules(verbs)
    schema = generate_schema(nouns)
    pseudocode = generate_pseudocode(verbs, nouns)

    print("\n📦 Suggested Modules:")
    for m in modules:
        print(f"- {m}")

    print("\n🗃️ Suggested Database Schemas:")
    for s in schema:
        print(f"- {s}")

    print("\n📜 Suggested Pseudocode:")
    for p in pseudocode:
        print(f"\n{p}")

if __name__ == "__main__":
    main()
