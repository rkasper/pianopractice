import random

from storage import Storage


class PianoPractice:
    NAME = 'name'
    URL = 'url'

    @staticmethod
    def exercises_to_practice() -> []:
        scales = Storage.get_scales_as_json()
        hanon = Storage.get_hanon_as_json()
        blues = Storage.get_blues_as_json()
        return [(random.choice(scales)), (random.choice(hanon)), (random.choice(blues))]

    @staticmethod
    def keys_to_practice() -> [str]:
        keys: [str] = ['A', 'Bb/A#', 'B', 'C', 'C#/Db', 'D', 'Eb/D#', 'E', 'F', 'F#/Gb', 'G', 'Ab/G#']
        random.shuffle(keys)
        return keys


if __name__ == '__main__':
    print('Exercises:')
    print('\n'.join(map(str, PianoPractice.exercises_to_practice())))
    print('\nKeys:', ', '.join(map(str, PianoPractice.keys_to_practice())))
