import os
file_name = 'transcript_test' 
file_path = os.path.join("view-res/transcript_data", file_name + '.txt')  

"""
    audio script từ phụ đề video
    -> pip install youtube-transcript-api
"""

from youtube_transcript_api import YouTubeTranscriptApi

# URL video YouTube
video_url = 'https://www.youtube.com/watch?v=W5eqxYWdQT0'  # thay 'video_id' bằng id của video

# Lấy id của video từ URL
video_id = video_url.split('v=')[1]

# Lấy transcript (phụ đề) nếu có sẵn
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['vi', 'en'])

    # In ra nội dung transcript
    with open(file_path, 'w', encoding='utf-8') as f:
        for entry in transcript:
            f.write(str(entry['start']) + ' - ' + entry['text'] + '\n\n')
            # print(f"{entry['start']} - {entry['text']}")

except Exception as e:
    print(f"Lỗi: {str(e)}")
