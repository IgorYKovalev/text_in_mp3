import os
import gtts
import pyttsx3
from pathlib import Path
import pdfplumber
from playsound import playsound


# Устанавливаем библиотеки
# pip install gtts pyttsx3 pdfplumber playsound

# gtts этой библиотеки нужен интернет
# text = input('Введите любой текст: ')
# tts = gtts.gTTS(text, lang='ru')
# tts.save('hello.mp3') # просто сохранили
# playsound('hello.mp3') # если хотим сразу послушать файл
# os.remove('hello.mp3') # если не хотим сохранять файл
#
# # pyttsx3 этой библиотеке интернет не нужен
# engine = pyttsx3.init()
# engine.setProperty('rate', 180)
# engine.setProperty('volume', 0.9)
# engine.say(text)
# engine.runAndWait()


def pdf_to_mp3(file_path='text.pdf', language='ru'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', ' ')
        my_audio = gtts.gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        return f'{file_name}.mp3 конвертацию закончил...'
    return 'Файл не существует!!!'


def main():
    file_path = input('Введите путь к файлу: ')
    # /Users/kovalevigor/PycharmProjects/text_in_mp3/test.pdf
    language = input('Введите язык ru или en: ')
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()


