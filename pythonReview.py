def create_youtube_video(title,description):
	youtube_video={"title":title,"description":description,"likes":0,"dislikes":0,"username": {}}

	return youtube_video

def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"]+=1
	return youtube_video

def dislikes(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"]+=1
	return youtube_video

def add_comment(youtube_video,username,comment_text):
	youtube_video["username"][username]=comment_text
	return youtube_video

a = create_youtube_video("video1","very very cool video")
for i in range(495):
	like(a)
print(add_comment(a,"dror","great video!"))


