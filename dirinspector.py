from os import listdir as ls
from os import getcwd as gd

def main():
    directory = (gd(), ls(gd()))
    files = [[], [], [], [], [], [], [], []]
    for file in directory[1]:
        if '.' == file[0]:
            files[0].append(("Hidden", 245, file))
        elif '.py' in file or '.cpp' in file:
            files[1].append(("Code", 10, file))
        elif '.bmp' in file or '.tiff' in file or '.tif' in file or '.gif' in file or 'jpeg' in file or '.jpg' in file or '.png' in file or '.svg' in file or 'webp' in file:
            files[2].append(("Image", 226, file))
        elif '.avi' in file or '.mpeg' in file or '.wmv' in file or '.mp4' in file or '.mov' in file or '.webm' in file:
            files[3].append(("Video", 208, file))
        elif '.txt' in file or '.doc' in file or '.odt' in file or '.rtf' in file or '.html' in file or '.pdf' in file:
            files[4].append((("Text", 255, file)))
        elif '.wav' in file or '.ogg' in file or '.mp3' in file or '.flac' in file:
            files[5].append(("Audio", 124, file))
        else:
            try:
                ls(file)
                files[6].append(("Directory", 27, file))
            except NotADirectoryError:
                files[7].append(("Etc", 93, file))
            except PermissionError:
                files[7].append(("Permission denied", 93, file))
    print(f"\033[38;5;10mDirectory: {directory[0]}\033[0;0m")
    for file_type in files:
        try:
            file_type.sort()
            print(f"\033[38;5;{file_type[0][1]}m--[{file_type[0][0]}]--\033[0;0m")
            for file in file_type:
                print(f"\033[38;5;{file[1]}m{file[2]}\033[0;0m")
        except IndexError:
            pass

if __name__ == "__main__":
    main()
