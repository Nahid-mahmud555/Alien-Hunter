import requests

def check_username(username, platforms):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; UsernameChecker/1.0)"
    }
    for name, url in platforms.items():
        full_url = url.replace("{username}", username)
        try:
            response = requests.get(full_url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"[+] Found on {name}: {full_url}")
            elif response.status_code == 404:
                print(f"[-] Not Found on {name}")
            else:
                print(f"[?] Status {response.status_code} on {name}")
        except requests.RequestException as e:
            print(f"[!] Error checking {name}: {e}")

username = input("Enter username: ")

platforms = {
    "Facebook": "https://facebook.com/{username}",
    "Instagram": "https://instagram.com/{username}",
    "GitHub": "https://github.com/{username}",
    "Twitter": "https://twitter.com/{username}",
    "LinkedIn": "https://www.linkedin.com/in/{username}",
    "TikTok": "https://www.tiktok.com/@{username}",
    "Pinterest": "https://www.pinterest.com/{username}",
    "Reddit": "https://www.reddit.com/user/{username}",
    "Snapchat": "https://www.snapchat.com/add/{username}",
    "Tumblr": "https://{username}.tumblr.com",
    "Discord": "https://discord.com/users/{username}",
    "Twitch": "https://www.twitch.tv/{username}",
    "Medium": "https://medium.com/@{username}",
    "Quora": "https://www.quora.com/profile/{username}",
    "Vimeo": "https://vimeo.com/{username}",
    "Clubhouse": "https://www.clubhouse.com/@{username}",
    "Behance": "https://www.behance.net/{username}",
    "Dribbble": "https://dribbble.com/{username}",
    "Stack Overflow": "https://stackoverflow.com/users/{username}",
    "SoundCloud": "https://soundcloud.com/{username}",
    "Spotify": "https://open.spotify.com/user/{username}",
    "Goodreads": "https://www.goodreads.com/{username}",
}

check_username(username, platforms)
