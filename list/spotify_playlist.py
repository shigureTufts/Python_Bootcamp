playlist = {"title": "Patagonia Bus",
            "auther": "Colt",
            "songs": [
                {"title": "Afureru", "artist": ["Aru"], "album": "Aru", "added_time": "4_weeks_ago", "duration": 3.21},
                {"title": "Kimi To Coffee", "artist": ["Islet"], "album": "CYANIDE", "added_time": "3_weeks_ago", "duration": 4.02}
            ]
            }

for song in playlist["songs"]:
    print(song["title"])
