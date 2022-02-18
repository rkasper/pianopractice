#!/usr/local/bin/python3
import json
import random

from activity import Activity

SCALES = [{'group': 'Major', 'url': 'https://pianoscales.org/major.html'},
          {'group': 'Minor', 'url': 'https://pianoscales.org/minor.html'},
          {'group': 'Blues (minor)', 'url': 'https://pianoscales.org/blues.html'},
          {'group': 'Blues (major)', 'url': 'https://pianoscales.org/blues.html'},
          {'group': 'Mixolydian (dom7)', 'url': 'https://pianoscales.org/mixolydian.html'},
          {'group': 'Chromatic', 'url': 'https://www.pianoscales.org/chromatic.html'}]

HANON_EXERCISES = [{'group': '1', 'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-1/'},
                   {'group': '2', 'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-2/'},
                   {'group': '3', 'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-3/'},
                   {'group': '4', 'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-4/'},
                   {'group': '5', 'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-5/'},
                   {'group': '6', 'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-6/'},
                   {'group': '7', 'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-7/'},
                   {'group': '8', 'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-8/'},
                   {'group': '9', 'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-9/'},
                   {'group': '10',
                            'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-10/'},
                   {'group': '11',
                            'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-11/'},
                   {'group': '12',
                            'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-12/'},
                   {'group': '13',
                            'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-13/'},
                   {'group': '14',
                            'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-14/'},
                   {'group': '15',
                            'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-15/'},
                   {'group': '16',
                            'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-16/'},
                   {'group': '17',
                            'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-17/'},
                   {'group': '18',
                            'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-18/'},
                   {'group': '19',
                            'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-19/'},
                   {'group': '20',
                            'url': 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-20/'},
                   {'group': '21', 'url': 'https://galaxymusicnotes.com/products/hanon-exercise-no-21'},
                   {'group': '22', 'url': 'https://galaxymusicnotes.com/products/hanon-exercise-no-22'},
                   {'group': '23',
                            'url': 'https://galaxymusicnotes.com/products/hanon-exercise-no-23-from-the-virtuoso-pianist'},
                   {'group': '24',
                            'url': 'https://galaxymusicnotes.com/products/hanon-exercise-no-24-from-the-virtuoso-pianist-part-2'},
                   {'group': '25', 'url': 'https://galaxymusicnotes.com/products/hanon-exercise-no-25'},
                   {'group': '26', 'url': 'https://galaxymusicnotes.com/products/hanon-exercise-no-26'},
                   {'group': '27', 'url': 'https://galaxymusicnotes.com/products/hanon-exercise-no-27'},
                   {'group': '28', 'url': 'https://galaxymusicnotes.com/products/hanon-exercise-no-28'},
                   {'group': '29', 'url': 'https://galaxymusicnotes.com/products/hanon-exercise-no-29'},
                   {'group': '30', 'url': 'https://galaxymusicnotes.com/products/hanon-exercise-no-30'}]

BLUES_SCHOOL = 'Blues School'

BLUES = [{'group': 'Major Blues 12-Bar Form & Harmony, The First Lesson',
                  'url': 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-the-first-lesson/'},
         {'group': 'Major Blues 12-Bar Form & Harmony, Variation #2',
                  'url': 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-2/'},
         {'group': 'Major Blues 12-Bar Form & Harmony, Variation #3',
                  'url': 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-3/'},
         {'group': 'Major Blues 12-Bar Form & Harmony, Variation #4',
                  'url': 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-4/'},
         {'group': 'Major Blues 12-Bar Form & Harmony, Variation #5',
                  'url': 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-5/'},
         {'group': 'Major Blues 12-Bar Form & Harmony, Variation #6',
                  'url': 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-6/'},
         {'group': 'Major Blues 12-Bar Form & Harmony, Variation #7',
                  'url': 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-7/'},
         {'group': 'Major Blues 12-Bar Form & Harmony, Variation #8',
                  'url': 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-8/'},
         {'group': 'Comping Pattern #1',
                  'url': 'https://piano-ology.com/blues-school-comping-pattern-1/'},
         {'group': 'Comping Pattern #2',
                  'url': 'https://piano-ology.com/blues-school-comping-pattern-2/'},
         {'group': 'Comping Pattern #3',
                  'url': 'https://piano-ology.com/blues-school-comping-pattern-3/'}]


class PianoPractice:
    @staticmethod
    def exercises_to_practice() -> [Activity]:
        # its_a_dictionary = {
        #     'Scale': [['Major', 'https://pianoscales.org/major.html'], ['Minor', 'https://pianoscales.org/minor.html']],
        #     'Hanon': [['1', 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-1/'],
        #               ['2', 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-2/']],
        #     'Blues School': [['Major Blues 12-Bar Form & Harmony, The First Lesson',
        #                       'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-the-first-lesson/'],
        #                      ['Major Blues 12-Bar Form & Harmony, Variation #2',
        #                       'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-2/']]}
        # print('its_a_dictionary: ' + str(its_a_dictionary))
        # its_json = json.dumps(its_a_dictionary)
        # print('its_json: ' + its_json)
        # its_another_dictionary = json.loads(its_json)
        # print('its_another_dictionary: ' + str(its_another_dictionary))

        random_scale = random.choice(SCALES)
        random_scale_activity = Activity('Scale', random_scale['group'], random_scale['url'])

        random_hanon = random.choice(HANON_EXERCISES)
        random_hanon_activity = Activity('Hanon', random_hanon['group'], random_hanon['url'])

        random_blues_school = random.choice(BLUES)
        random_blues_school_activity = Activity('Blues School', random_blues_school['group'], random_blues_school['url'])

        return [random_scale_activity, random_hanon_activity, random_blues_school_activity]

    @staticmethod
    def keys_to_practice() -> [str]:
        keys: [str] = ['A', 'Bb/A#', 'B', 'C', 'C#/Db', 'D', 'Eb/D#', 'E', 'F', 'F#/Gb', 'G', 'Ab/G#']
        random.shuffle(keys)
        return keys


if __name__ == '__main__':
    print('Exercises:')
    print('\n'.join(map(str, PianoPractice.exercises_to_practice())))
    print('\nKeys:', ', '.join(map(str, PianoPractice.keys_to_practice())))
