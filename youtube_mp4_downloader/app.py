from pytube import YouTube

def download_song(url: str, output_path: str) -> None:
    try:
        data = YouTube(url)
        audio_data = data.streams.filter(only_audio=True).first()
        audio_title = audio_data.title
        audio_data.download(output_path)
        print(f'Successfully downloaded audio: {audio_title} to {output_path}')
    except Exception as e:
        print(f'Error: {e}')

url: str = input()
output_path: str = 'Songs/'
download_song(url, output_path)
