import requests

# Ganti dengan token akses Bitly Anda
BITLY_ACCESS_TOKEN = 'ade477d5cb443a631e28f03e2b67d278eefd5ce0'

def shorten_url(long_url):
    headers = {
        'Authorization': f'Bearer {BITLY_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'long_url': long_url
    }
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', json=data, headers=headers)
    if response.status_code == 200:
        short_url = response.json().get('link')
        return short_url
    else:
        print(f'Error: {response.status_code}')
        print(response.text)
        return None

def main():
    print('URL SHORTENER Danvertt')
    long_url = input('Masukkan URL panjang yang ingin dipendekkan: ')
    short_url = shorten_url(long_url)
    if short_url:
        print(f'URL pendek Anda: {short_url}')

if __name__ == '__main__':
    main()
