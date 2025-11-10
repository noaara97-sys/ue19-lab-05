import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        donnee = response.json()
        print(f" {donnee['setup']}")
        print(f" {donnee['punchline']}")
    else:
        print(f"Erreur lors de la requête.")

if __name__ == "__main__":
    get_joke()