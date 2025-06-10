import hashlib
import requests

# creates SHA1 hash of user password.
def get_sha1(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

# fetches pwned/leaked passwords from Have I Been Pwned API
def fetch_pwned_data(prefix):
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'API Error: {res.status_code}')
    return res.text

# sends first 5 characters of hash to check against HIBP
def check_pwned_password(password):
    sha1 = get_sha1(password)
    prefix = sha1[:5]
    suffix = sha1[5:]
    data = fetch_pwned_data(prefix)

