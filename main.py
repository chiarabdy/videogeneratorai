import requests


def fetch_quote():
    url = 'https://stoic-quotes.com/api/quote'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def create_voice_over_elevenlabs(text, api_key, voice_id='21m00Tcm4TlvDq8ikWAM', audio_path='quote.mp3'):
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
    headers = {
        'accept': 'audio/mpeg',
        'xi-api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        with open(audio_path, 'wb') as f:
            f.write(response.content)
        print("Voice over created successfully.")
    else:
        print(f"Failed to create voice over. Status code: {response.status_code}, Response: {response.text}")


def main():
    api_key = '04fd0bce309bc27878f3fdebfa7dcf83'  # Replace with your actual API key
    quote = fetch_quote()
    if quote:
        quote_text = quote['text']
        quote_author = quote['author']
        full_text = f"{quote_text} by {quote_author}"

        # Print the quote in the terminal
        print("Fetched Quote:")
        print(full_text)

        audio_path = 'quote.mp3'
        create_voice_over_elevenlabs(full_text, api_key, audio_path=audio_path)
    else:
        print("Failed to fetch quote.")


if __name__ == "__main__":
    main()
