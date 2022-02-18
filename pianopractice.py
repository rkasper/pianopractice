#!/usr/local/bin/python3
import json
import random

# Notes for future JSON work:
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


class PianoPractice:
    NAME = 'name'

    URL = 'url'

    SCALES = [{NAME: 'Major', URL: 'https://pianoscales.org/major.html'},
              {NAME: 'Minor', URL: 'https://pianoscales.org/minor.html'},
              {NAME: 'Blues (minor)', URL: 'https://pianoscales.org/blues.html'},
              {NAME: 'Blues (major)', URL: 'https://pianoscales.org/blues.html'},
              {NAME: 'Mixolydian (dom7)', URL: 'https://pianoscales.org/mixolydian.html'},
              {NAME: 'Chromatic', URL: 'https://www.pianoscales.org/chromatic.html'}]

    HANON = [{NAME: '1', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-1/'},
             {NAME: '2', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-2/'},
             {NAME: '3', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-3/'},
             {NAME: '4', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-4/'},
             {NAME: '5', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-5/'},
             {NAME: '6', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-6/'},
             {NAME: '7', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-7/'},
             {NAME: '8', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-8/'},
             {NAME: '9', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-9/'},
             {NAME: '10',
                        URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-10/'},
             {NAME: '11',
                        URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-11/'},
             {NAME: '12',
                        URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-12/'},
             {NAME: '13',
                        URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-13/'},
             {NAME: '14',
                        URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-14/'},
             {NAME: '15',
                        URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-15/'},
             {NAME: '16',
                        URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-16/'},
             {NAME: '17',
                        URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-17/'},
             {NAME: '18',
                        URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-18/'},
             {NAME: '19',
                        URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-19/'},
             {NAME: '20',
                        URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-20/'},
             {NAME: '21', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-21'},
             {NAME: '22', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-22'},
             {NAME: '23',
                        URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-23-from-the-virtuoso-pianist'},
             {NAME: '24',
                        URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-24-from-the-virtuoso-pianist-part-2'},
             {NAME: '25', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-25'},
             {NAME: '26', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-26'},
             {NAME: '27', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-27'},
             {NAME: '28', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-28'},
             {NAME: '29', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-29'},
             {NAME: '30', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-30'}]

    BLUES = [{NAME: 'Major Blues 12-Bar Form & Harmony, The First Lesson',
              URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-the-first-lesson/'},
             {NAME: 'Major Blues 12-Bar Form & Harmony, Variation #2',
              URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-2/'},
             {NAME: 'Major Blues 12-Bar Form & Harmony, Variation #3',
              URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-3/'},
             {NAME: 'Major Blues 12-Bar Form & Harmony, Variation #4',
              URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-4/'},
             {NAME: 'Major Blues 12-Bar Form & Harmony, Variation #5',
              URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-5/'},
             {NAME: 'Major Blues 12-Bar Form & Harmony, Variation #6',
              URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-6/'},
             {NAME: 'Major Blues 12-Bar Form & Harmony, Variation #7',
              URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-7/'},
             {NAME: 'Major Blues 12-Bar Form & Harmony, Variation #8',
              URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-8/'},
             {NAME: 'Comping Pattern #1',
              URL: 'https://piano-ology.com/blues-school-comping-pattern-1/'},
             {NAME: 'Comping Pattern #2',
              URL: 'https://piano-ology.com/blues-school-comping-pattern-2/'},
             {NAME: 'Comping Pattern #3',
              URL: 'https://piano-ology.com/blues-school-comping-pattern-3/'}]

    @staticmethod
    def exercises_to_practice() -> []:
        return [(random.choice(PianoPractice.SCALES)), (random.choice(PianoPractice.HANON)),
                (random.choice(PianoPractice.BLUES))]

    @staticmethod
    def keys_to_practice() -> [str]:
        keys: [str] = ['A', 'Bb/A#', 'B', 'C', 'C#/Db', 'D', 'Eb/D#', 'E', 'F', 'F#/Gb', 'G', 'Ab/G#']
        random.shuffle(keys)
        return keys


if __name__ == '__main__':
    print('Exercises:')
    print('\n'.join(map(str, PianoPractice.exercises_to_practice())))
    print('\nKeys:', ', '.join(map(str, PianoPractice.keys_to_practice())))
