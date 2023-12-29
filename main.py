import os
import re

import requests

from datetime import datetime

from youtube_transcript_api import YouTubeTranscriptApi


def create_directory(channel_name):
    path = os.path.join('transcripts', channel_name)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_yearly_monthly_directory(base_path, date_posted):
    # Convert the date string to a datetime object
    date = datetime.strptime(date_posted[:-1], '%Y-%m-%dT%H:%M:%S')  # Remove the 'Z' from the ISO format and parse
    
    # Create the year directory
    year_path = os.path.join(base_path, str(date.year))
    if not os.path.exists(year_path):
        os.makedirs(year_path)
    
    # Create the month directory within the year directory
    month_path = os.path.join(year_path, date.strftime('%b'))
    if not os.path.exists(month_path):
        os.makedirs(month_path)
    
    return month_path


def sanitize_filename(title):
    return re.sub(r'[\\/*?:"<>|]', '', title)


def download_subtitles(video_id, video_title, channel_path, date_posted):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en'])
        subtitles = transcript.fetch()

        # Use the new function to create/get the monthly directory
        path = create_yearly_monthly_directory(channel_path, date_posted)

        safe_title = sanitize_filename(video_title)
        file_name = f"{path}/{safe_title}.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            # Write the title and date before the subtitles
            file.write(f"Title: {video_title} - Date Posted: {date_posted}\n\n")
            for line in subtitles:
                file.write(f"{line['text']}\n")

        print(f"Subtitles saved to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_channel_videos(channel_id, api_key):
    base_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'channelId': channel_id,
        'maxResults': 50,
        'type': 'video',
        'key': api_key
    }
    
    video_info = []
    while True:
        response = requests.get(base_url, params=params)
        videos = response.json()

        for item in videos.get('items', []):
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            date_posted = item['snippet']['publishedAt']  # Extract the date posted
            video_info.append((video_id, video_title, date_posted))  # Add date_posted to the tuple

        if 'nextPageToken' in videos:
            params['pageToken'] = videos['nextPageToken']
        else:
            break

    return video_info


def main():
    channel_id = input("Enter YouTube channel ID: ")
    api_key = os.getenv('YT_API_KEY')
    if api_key is None:
        input("Can't find API Key from environment variables. Enter it here: ")
    channel_name = input("Enter a name for the channel folder: ")
    channel_path = create_directory(channel_name)
    
    videos = get_channel_videos(channel_id, api_key)
    print('Total Videos:', len(videos))

    for video_id, video_title, date_posted in videos:
        print(f"Downloading subtitles for video: {video_title}")
        download_subtitles(video_id, video_title, channel_path, date_posted)


if __name__ == "__main__":
    main()
