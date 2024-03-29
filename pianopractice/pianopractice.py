import random

from pianopractice.storage import Storage


class PianoPractice:
    NAME = 'name'
    URL = 'url'

    @staticmethod
    def exercises_to_practice() -> []:
        scales = Storage.get_scales_as_json()
        hanon = Storage.get_hanon_as_json()
        blues = Storage.get_blues_as_json()

        random_hanon = (random.choice(hanon))
        random_lh_start_octave = random.randint(0, 4)
        random_lh_end_octave = random.randint(random_lh_start_octave + 2, 6)
        random_hanon[PianoPractice.NAME] = random_hanon[PianoPractice.NAME] \
            + ' (LH octaves ' + str(random_lh_start_octave) + '-' + str(random_lh_end_octave) \
            + ', RH octaves ' + str(1 + random_lh_start_octave) + '-' + str(1 + random_lh_end_octave) + ')'

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
