import json
import urllib.request
import os
# download raw json object
url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=20&mkt=en-US"
data = urllib.request.urlopen(url).read().decode()
obj = json.loads(data)
for i in range(0, 1):
	print(i)
	url_image="https://www.bing.com/"+obj["images"][i]["url"]
	print(url_image)
	path_image=os.getcwd() + "/img_"+obj["images"][i]["hsh"]+".jpg"
	path_image_last=os.getcwd() + "/img_last.jpg"
	urllib.request.urlretrieve(url_image, path_image)
	urllib.request.urlretrieve(url_image, path_image_last)
	print(path_image)
	os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+ path_image_last)
