from os import listdir as ls
from os import getcwd as gd

def main():
	directory = (gd(), ls(gd()))
	files = [[], [], [], [], [], [], []]
	for file in directory[1]:
		if '.' == file[0]:
			files[0].append((245, file))
		elif '.bmp' in file or '.tiff' in file or '.tif' in file or '.gif' in file or 'jpeg' in file or '.jpg' in file or '.png' in file or '.svg' in file or 'webp' in file:
			files[1].append((226, file))
		elif '.avi' in file or '.mpeg' in file or '.wmv' in file or '.mp4' in file or '.mov' in file or '.webm' in file:
			files[2].append((208, file))
		elif '.txt' in file or '.doc' in file or '.odt' in file or '.rtf' in file or '.html' in file or '.pdf' in file:
			files[3].append(((255, file)))
		elif '.wav' in file or '.ogg' in file or '.mp3' in file or '.flac' in file:
			files[4].append((124, file))
		else:
			try:
				ls(file)
				files[5].append((27, file))
			except NotADirectoryError:
				files[6].append((93, file))
			except PermissionError:
				files[6].append((93, file))
	print(f"\033[38;5;10mDirectory: {directory[0]}\033[0;0m")
	for file_type in files:
		file_type.sort()
		for file in file_type:
			print(f"\033[38;5;{file[0]}m{file[1]}\033[0;0m")

if __name__ == "__main__":
	main()
