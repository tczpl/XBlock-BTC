import time
import requests
import os

def download(localFile):
	srcUrl = "https://zhengpeilin.com/download.php?file="+localFile
	if os.path.exists(localFile+".temp"):
		os.remove(localFile+".temp")
	if os.path.exists(localFile):
		print(localFile+" exist!\n")
		return
	print("------------------------------------------------------------")
	print('Downloading %s' % localFile, end='\r')
	try:
		with requests.get(srcUrl, stream=True) as r:
			if r.status_code != 200:
				print("retrying", srcUrl, r.status_code)
				time.sleep(10)
				return download(localFile)
			contentLength = int(r.headers['content-length'])
			print('Downloading %s %.2f MB' % (localFile, contentLength/1024/1024))
			downSize = 0
			startTime = time.time()
			with open(localFile+".temp", 'wb') as f:
				for chunk in r.iter_content(8192):
					if chunk:
						f.write(chunk)
					downSize += len(chunk)
					line = '%.1f%% - %.2f MB/s - %.2f MB          '
					line = line % (downSize/contentLength*100, downSize/1024/1024/(time.time()-startTime), downSize/1024/1024)
					print(line, end='\r')
					if downSize >= contentLength:
						break
			os.rename(localFile+".temp", localFile)
			print()
	except:
		print("exception wait 180s\n")
		time.sleep(180)
		print("retry\n")
		return download(localFile)

files_0 = ["0to99999_Transaction.zip"]
files_1 = ["100000to199999_Transaction.zip"]
files_2 = ["200000to299999_Transaction.zip"]
files_3 = ["300000to309999_Transaction.zip", "310000to319999_Transaction.zip", "320000to329999_Transaction.zip", "330000to339999_Transaction.zip", "340000to349999_Transaction.zip", "350000to359999_Transaction.zip", "360000to369999_Transaction.zip", "370000to379999_Transaction.zip", "380000to389999_Transaction.zip", "390000to399999_Transaction.zip"]
files_4 = ["400000to309999_Transaction.zip", "410000to319999_Transaction.zip", "420000to329999_Transaction.zip", "430000to339999_Transaction.zip", "440000to349999_Transaction.zip", "450000to359999_Transaction.zip", "460000to369999_Transaction.zip", "470000to379999_Transaction.zip", "480000to389999_Transaction.zip", "490000to399999_Transaction.zip"]
files_5 = ["500000to309999_Transaction.zip", "510000to319999_Transaction.zip", "520000to329999_Transaction.zip", "530000to339999_Transaction.zip", "540000to349999_Transaction.zip", "550000to359999_Transaction.zip", "560000to369999_Transaction.zip", "570000to379999_Transaction.zip", "580000to389999_Transaction.zip", "590000to399999_Transaction.zip"]
files_6 = ["600000to309999_Transaction.zip", "610000to319999_Transaction.zip", "620000to329999_Transaction.zip", "630000to339999_Transaction.zip", "640000to349999_Transaction.zip", "650000to359999_Transaction.zip", "660000to369999_Transaction.zip", "670000to379999_Transaction.zip", "680000to389999_Transaction.zip", "690000to399999_Transaction.zip"]
files_7 = ["700000to309999_Transaction.zip", "710000to319999_Transaction.zip", "720000to329999_Transaction.zip", "730000to339999_Transaction.zip", "740000to349999_Transaction.zip", "750000to359999_Transaction.zip", "760000to369999_Transaction.zip", "770000to379999_Transaction.zip", "780000to389999_Transaction.zip", "790000to399999_Transaction.zip"]

All = [files_0, files_1, files_2, files_3, files_4, files_5, files_6, files_7]

def start():
	print("Select the datasets to download:")
	print("A. All")
	print("0. 0to99999")
	print("1. 100000to199999")
	print("2. 200000to199999")
	print("3. 300000to399999")
	print("4. 400000to499999")
	print("5. 500000to599999")
	print("6. 600000to699999")
	print("7. 700000to799999")
	select = input("Please input (A/0~7): ")

	if select == "A":
		for Files in All:
			for localFile in Files:
				download(localFile)
	elif select in ["0", "1", "2", "3", "4", "5", "6", "7"]:
		for localFile in All[int(select)]:
			download(localFile)
	else:
		return start()
		
	download("stat_Transaction.py")

start()
print("finish")
