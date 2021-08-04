import os

## on//off
colors = "on"

def sorting(files):
    global formats, names
    text = []; images = []; audio = []; videos = []; exe = []; pfiles = []; hfiles = []; anyelse = []
    for file in files:
        dots = [i+1 for i, symb in enumerate(file) if symb=='.']
        if '.' in file:
            if dots[0] == 1:
                hfiles.append(file)
            elif '.py' in file:
                pfiles.append(file)
            elif '.bmp' in file or '.tiff' in file or '.tif' in file or '.gif' in file or 'jpeg' in file or '.jpg' in file or '.png' in file or '.svg' in file or 'webp' in file:
                images.append(file)
            elif '.avi' in file or '.mpeg' in file or '.wmv' in file or '.mp4' in file or '.mov' in file or '.webm' in file:
                videos.append(file)
            elif '.wav' in file or '.ogg' in file or '.mp3' in file or '.flac' in file:
                audio.append(file)
            elif '.txt' in file or '.doc' in file or '.odt' in file or '.rtf' in file or '.html' in file or '.pdf' in file:
                text.append(file)
            elif '.exe' in file or '.apk' in file:
                exe.append(file)
            else:
                anyelse.append(file)
        else:
            anyelse.append(file)
    formats = [text, images, audio, videos, exe, pfiles, hfiles, anyelse]
    names = ['Text Docs', 'Images', 'Audio', 'Videos', 'Executables', 'Python scripts', 'Hidden files', 'Anything else']

def filesprint(form, name, color1, color2):
    if color1 == None or color2 == None:
        if form != []:
            print(f'[---{name}---]')
            for f in form:
                print(f)
    else:
        if form != []:
            print(f'{color1}[---{name}---]{color2}')
            for f in form:
                print(f'{color1}{f}{color2}')

def output():
    directory = os.getcwd()
    sorting(os.listdir(directory))
    if colors == 'off':
        print(f'Directory: {directory}')
        for format, name in zip(formats, names):
            filesprint(format, name, None, None)
    elif colors == 'on':
        g = "\033[38;5;82m{}" .format("")
        w = "\033[38;5;231m{}" .format("")
        colorsforprint = [w, "\033[38;5;11m{}" .format(""), "\033[38;5;9m{}" .format(""), "\033[38;5;208m{}" .format(""), "\033[38;5;28m{}" .format(""), "\033[38;5;30m{}" .format(""), "\033[38;5;245m{}" .format(""), "\033[38;5;69m{}" .format("")]
        print(f'{g}Directory: {directory}{w}')
        for format, name , color in zip(formats, names, colorsforprint):
            filesprint(format, name, color, w)
    else:
        raise Exception('Syntax error in line 3')

output()
