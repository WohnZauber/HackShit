import requests

# Deine Cloudflare-Details
api_token = 'KKj9A8hVIHcmUwqbuEAR6r3gKWDfSPRB5rMTFWVy'
account_id = '5246f6e1a46e56084561fd0ce9bc5420'

# Setze die E-Mail-Domain für die Erstellung von Aliassen
email_domain = 'fthemgiveways.com'

# Die URL für das Cloudflare API zum Erstellen von E-Mail-Routing-Regeln
create_routing_rule_url = f"https://api.cloudflare.com/client/v4/accounts/5246f6e1a46e56084561fd0ce9bc5420/email/routing/rules"

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

# Funktion zum Erstellen von E-Mail-Routing-Regeln
def create_email_routing_rule(local_part):
    payload = {
        "match": {
            "from": f"{local_part}@{email_domain}"
        },
        "actions": [
            {
                "type": "forward",
                "value": "bastiprohd1@gmail.com"  # Ziel-E-Mail-Adresse
            }
        ]
    }
    response = requests.post(create_routing_rule_url, headers=headers, json=payload)
    return response.json()

# Hauptfunktionsaufruf
if __name__ == '__main__':
    number_of_emails_to_create = 10  # Anzahl der zu erstellenden E-Mail-Adressen
    for i in range(number_of_emails_to_create):
        local_part = f"alias{i}"  # Lokaler Teil der E-Mail-Adresse (vor dem @)
        result = create_email_routing_rule(local_part)
        print(result)
