import random

from app.storage import Storage


class PianoPractice:
    NAME = 'name'
    URL = 'url'

    @staticmethod
    def exercises_to_practice() -> []:
        scales = Storage.get_scales_as_json()
        hanon = Storage.get_hanon_as_json()
        blues = Storage.get_blues_as_json()

        random_hanon = (random.choice(hanon))
        random_start_octave = random.randint(0, 6)
        random_end_octave = random.randint(random_start_octave + 1, 8)
        random_hanon[PianoPractice.NAME] = random_hanon[PianoPractice.NAME] + ' (octaves ' + str(random_start_octave)\
                                           + '-' + str(random_end_octave) + ')'

        return [(random.choice(scales)), random_hanon, (random.choice(blues))]

    @staticmethod
    def keys_to_practice() -> [str]:
        keys: [str] = ['A', 'Bb/A#', 'B', 'C', 'C#/Db', 'D', 'Eb/D#', 'E', 'F', 'F#/Gb', 'G', 'Ab/G#']
        random.shuffle(keys)
        return keys


if __name__ == '__main__':
    print('Exercises:')
    print('\n'.join(map(str, PianoPractice.exercises_to_practice())))
    print('\nKeys:', ', '.join(map(str, PianoPractice.keys_to_practice())))
