import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
	req = urllib.request.urlopen(img_url)

	img_content = req.read()

	with open(img_name, "wb") as f:
		f.write(img_content)

def main():
	gevent.joinall([
	        gevent.spawn(downloader, "3.jpg", "https://rpic.douyucdn.cn/appCovers/2017/09/22/1760931_20170922133718_big.jpg"),
	        gevent.spawn(downloader, "4.jpg", "https://rpic.douyucdn.cn/appCovers/2017/09/17/2308890_20170917232900_big.jpg"),
			gevent.spawn(downloader, "5.jpg", "https://apic.douyucdn.cn/upload/avatar_v3/201902/2f1a25e9680c41d48a3cda738b69296d_big.jpg"),

	])


if __name__ == '__main__':
	main()