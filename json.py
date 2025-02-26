import json

# Function to validate email input
def get_valid_email():
    while True:
        email = input("Sisestage oma isiklik e-mail address: ")
        if "@" in email and "." in email:  # Basic validation
            return email
        else:
            print("Vigane e-mail! Palun sisestage korrektne e-mail aadress.")

# User Input
company_name = input("Sisestage oma firma nimi: ")
contact_email = get_valid_email()
data_collection_type = input("Millised andmed salvestame: ")
data_usage = input("Kuidas andmed kasutatakse: ")
data_storage_limit = input("Kui kaua andmed salvestatakse: ")
cookies_preference = input("Kas sa soovid salvestada küpsiseid? (Jah/Ei): ")

# Dictionary for Privacy Data
privacy_data = {
    "company_name": company_name,
    "contact_email": contact_email,
    "data_collection_type": data_collection_type,
    "data_usage": data_usage,
    "data_storage_limit": data_storage_limit,
    "cookies_preference": cookies_preference
}

# Save to JSON file
with open("privacy_template.json", "w", encoding="utf-8") as file:
    json.dump(privacy_data, file, indent=4)
    print("Kõik oli edukalt salvestatud!")

# HTML Template
html_template = """ 
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Privaatsuspoliitika</title>
</head>
<body>
    <h1>Poliitika pühendatud ettevõttele - {company_name}</h1>
    <p><strong>Kontakt:</strong> {contact_email}</p>
    
    <h2>Millised andmed kogume?</h2>
    <p>{data_collection_type}</p>
    
    <h2>Kuidas andmed kasutatakse?</h2>
    <p>{data_usage}</p>
    
    <h2>Kui kaua andmed salvestatakse?</h2>
    <p>{data_storage_limit}</p>

    <h2>Kas sa soovid salvestada küpsiseid?</h2>
    <p>{cookies_preference}</p>
</body>
</html>
"""

# Format HTML with the user-provided data
privacy_policy = html_template.format(**privacy_data)

# Save to HTML file
with open("privacy_template.html", "w", encoding="utf-8") as file:
    file.write(privacy_policy)

print("HTML fail oli genereeritud edukalt!")

