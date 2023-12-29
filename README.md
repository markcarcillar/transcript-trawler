# TranscriptTrawler: All-Channel YouTube Subtitle Harvester

## Introduction
TranscriptTrawler is a Python tool designed to download subtitles from all videos of a specified YouTube channel. It creates organized transcripts, saving each video's subtitles in a separate text file named after the video title, stored under a directory named after the channel.

## Purpose
The primary purpose of this tool is to provide an easy way to extract and archive subtitles from YouTube videos. This can be particularly useful for content analysis, educational purposes, language learning, and accessibility enhancements.

## Use Case
An ideal use case for this tool is for researchers and educators who wish to analyze the content of a YouTube creator's videos, enabling a deeper understanding of the subject matter, linguistic usage, and content trends.

## Suggested Enhancement
It is recommended to utilize this tool alongside the OpenAI API to further enhance and refine the extracted transcripts. The OpenAI API could be used to improve the accuracy of subtitles, summarize content, or even translate them into different languages. However, due to budget constraints, this feature is not currently implemented.

## How to Use
1. **Setup**: Ensure Python is installed on your system and install the `youtube_transcript_api` and `requests` libraries.
2. **API Key**: Obtain a YouTube Data API key from the Google Cloud Console.
3. **Run**: Execute the script and input the YouTube channel ID and a name for the channel folder when prompted.
4. **Output**: The subtitles will be downloaded and saved in a directory named after the channel, with each subtitle file named after its corresponding video title.

## Requirements
- Python 3.x
- `youtube_transcript_api`
- `requests`