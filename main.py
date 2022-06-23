from pytube import YouTube

url = input("Enter URL : ")

video = YouTube(url)

print(video.title)
print(video.thumbnail_url)
video.streams.get_highest_resolution().download()
print('downloaded')
