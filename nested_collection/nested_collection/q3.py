songs = [
    {"id": 1, "title": "Mayajalam", "spotify_listen_count": 12000, "yt_music": 15000, "downloads": 5000},
    {"id": 2, "title": "Neon Nights", "spotify_listen_count": 850000, "yt_music": 1200000, "downloads": 45000},
    {"id": 3, "title": "Midnight Coffee", "spotify_listen_count": 45000, "yt_music": 32000, "downloads": 1200},
    {"id": 4, "title": "Velvet Sky", "spotify_listen_count": 1200400, "yt_music": 980000, "downloads": 150000},
    {"id": 5, "title": "Echoes of You", "spotify_listen_count": 3100, "yt_music": 4500, "downloads": 200},
    {"id": 6, "title": "Rush Hour", "spotify_listen_count": 560000, "yt_music": 610000, "downloads": 88000},
    {"id": 7, "title": "Quiet Storm", "spotify_listen_count": 150000, "yt_music": 145000, "downloads": 12000}
]

all_title=[di.get("title") for di in songs]
print(all_title)
all_downloads=[di.get("downloads")for di in songs]
print(all_downloads)

all_download_count={di.get("title"):di.get("downloads") for di in songs}
max_downloads=[[v,k] for k,v in all_download_count.items() ]
print(sorted(max_downloads,reverse=True)[0])


yt_max=max([di.get("yt_music") for di in songs])
most_yt_music=[di.get("title") for di in songs if di.get("yt_music")==yt_max]
print(most_yt_music)


