from os import listdir as ls
from os import getcwd as gd

f_code = ['.py', '.cpp']
f_image = ['.bmp', '.tiff', '.tif', '.gif', 'jpeg', '.jpg', '.png', '.svg', '.webp']
f_video = ['.avi', '.mpeg', '.wmv', '.mp4', '.mov', '.webm']
f_document = ['.txt', '.doc', '.odt', '.rtf', '.html', '.pdf', '.ppt', '.pptx', '.xlsx']
f_audio = ['.wav', '.ogg', '.mp3', '.flac']
f_archive = ['.7z', '.cab', '.deb', '.gz', '.gz', '.jar', '.rar', '.rpm', '.tar', '.tar-gz', '.tgz', '.zip', '.zipx']

def check_for_format(file: str, formats: list) -> bool:
    for form in formats:
        if form in file:
            return True
    return False

def main():
    directory = (gd(), ls(gd()))
    files = [[], [], [], [], [], [], [], [], []]
    for file in directory[1]:
        if '.' == file[0]:
            files[0].append(("Hidden", 245, file))
        elif check_for_format(file, f_code):
            files[1].append(("Code", 10, file))
        elif check_for_format(file, f_image):
            files[2].append(("Image", 226, file))
        elif check_for_format(file, f_video):
            files[3].append(("Video", 208, file))
        elif check_for_format(file, f_document):
            files[4].append(("Text", 255, file))
        elif check_for_format(file, f_audio):
            files[5].append(("Audio", 124, file))
        elif check_for_format(file, f_archive):
            files[6].append(("Archive", 81, file))
        else:
            try:
                ls(file)
                files[7].append(("Directory", 27, file))
            except NotADirectoryError:
                files[8].append(("Etc", 93, file))
            except PermissionError:
                files[8].append(("Permission denied", 93, file))
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
