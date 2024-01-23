import os
import gtts
from pathlib import Path
import pdfplumber
from playsound import playsound

# text = "Юзабилити — это показатель того, насколько легко и удобно пользователю взаимодействовать с интерфейсом сайта."
# tts = gtts.gTTS(text=text, lang='ru')  # меняем язык на тот, который хотим услышать
# tts.save("welcome.mp3")   # сохранили файл
# playsound("welcome.mp3")  # если хотим сразу прослушать файл
# os.remove('welcome.mp3')  # если не хотим сохранять файл


def pdf_to_mp3(file_path='text.pdf', language='ru'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'{Path(file_path).name}')

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
    print('PDF >> to >> MP3')
    file_path = input('Введите путь к файлу: ')
    # /Users/kovalevigor/PycharmProjects/text_in_mp3/test.pdf
    language = input('Введите язык ru или en: ')
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
