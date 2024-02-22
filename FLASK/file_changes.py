import json

with open('videos.json', 'r') as f:
    videos = json.load(f)


def write_changes_to_file():
    global videos
    videos = {k: v for k, v in sorted(videos.items(), key=lambda video: video[1]['uploadDate'])}
    with open('videos.json', 'w') as f:
        json.dump(videos, f)
