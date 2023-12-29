
from pathlib import Path

# Define the directory where the transcripts are located and where the combined files will be stored
transcripts_dir = Path('transcripts')
combined_transcripts_dir = Path('transcripts-all-in-one')

# Create the combined transcripts directory if it does not exist
combined_transcripts_dir.mkdir(exist_ok=True)

# Function to combine all transcripts of a single channel into one file
def combine_channel_transcripts(channel):
    # Check if the combined file already exists, if so, skip this channel
    combined_file_path = combined_transcripts_dir / f'{channel}-all-transcripts.txt'
    if combined_file_path.is_file():
        print(f"The file for {channel} already exists. Skipping...")
        return

    # Get the list of transcript files for the channel
    channel_dir = transcripts_dir / channel
    transcript_files = [f for f in channel_dir.iterdir() if f.is_file()]

    # Open the combined file and write the content of each transcript file into it
    with combined_file_path.open('w', encoding='utf-8') as combined_file:
        for transcript_file in transcript_files:
            with transcript_file.open('r', encoding='utf-8') as f:
                combined_file.write(f"{transcript_file.stem}\n")  # Write the title (remove file extension)
                combined_file.write(f"[{f.read()}]\n\n")  # Write the content of the transcript file


# Combine transcripts for each channel
for channel in transcripts_dir.iterdir():
    if channel.is_dir():
        combine_channel_transcripts(channel.name)
