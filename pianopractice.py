#!/usr/local/bin/python3
import json
import random

#from activity import Activity

URL = 'url'

GROUP = 'group'

SCALES = [{GROUP: 'Major', URL: 'https://pianoscales.org/major.html'},
          {GROUP: 'Minor', URL: 'https://pianoscales.org/minor.html'},
          {GROUP: 'Blues (minor)', URL: 'https://pianoscales.org/blues.html'},
          {GROUP: 'Blues (major)', URL: 'https://pianoscales.org/blues.html'},
          {GROUP: 'Mixolydian (dom7)', URL: 'https://pianoscales.org/mixolydian.html'},
          {GROUP: 'Chromatic', URL: 'https://www.pianoscales.org/chromatic.html'}]

HANON_EXERCISES = [{GROUP: '1', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-1/'},
                   {GROUP: '2', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-2/'},
                   {GROUP: '3', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-3/'},
                   {GROUP: '4', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-4/'},
                   {GROUP: '5', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-5/'},
                   {GROUP: '6', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-6/'},
                   {GROUP: '7', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-7/'},
                   {GROUP: '8', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-8/'},
                   {GROUP: '9', URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-9/'},
                   {GROUP: '10',
                    URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-10/'},
                   {GROUP: '11',
                    URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-11/'},
                   {GROUP: '12',
                    URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-12/'},
                   {GROUP: '13',
                    URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-13/'},
                   {GROUP: '14',
                    URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-14/'},
                   {GROUP: '15',
                    URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-15/'},
                   {GROUP: '16',
                    URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-16/'},
                   {GROUP: '17',
                    URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-17/'},
                   {GROUP: '18',
                    URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-18/'},
                   {GROUP: '19',
                    URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-19/'},
                   {GROUP: '20',
                    URL: 'https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-20/'},
                   {GROUP: '21', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-21'},
                   {GROUP: '22', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-22'},
                   {GROUP: '23',
                    URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-23-from-the-virtuoso-pianist'},
                   {GROUP: '24',
                    URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-24-from-the-virtuoso-pianist-part-2'},
                   {GROUP: '25', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-25'},
                   {GROUP: '26', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-26'},
                   {GROUP: '27', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-27'},
                   {GROUP: '28', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-28'},
                   {GROUP: '29', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-29'},
                   {GROUP: '30', URL: 'https://galaxymusicnotes.com/products/hanon-exercise-no-30'}]

BLUES = [{GROUP: 'Major Blues 12-Bar Form & Harmony, The First Lesson',
          URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-the-first-lesson/'},
         {GROUP: 'Major Blues 12-Bar Form & Harmony, Variation #2',
          URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-2/'},
         {GROUP: 'Major Blues 12-Bar Form & Harmony, Variation #3',
          URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-3/'},
         {GROUP: 'Major Blues 12-Bar Form & Harmony, Variation #4',
          URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-4/'},
         {GROUP: 'Major Blues 12-Bar Form & Harmony, Variation #5',
          URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-5/'},
         {GROUP: 'Major Blues 12-Bar Form & Harmony, Variation #6',
          URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-6/'},
         {GROUP: 'Major Blues 12-Bar Form & Harmony, Variation #7',
          URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-7/'},
         {GROUP: 'Major Blues 12-Bar Form & Harmony, Variation #8',
          URL: 'https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-8/'},
         {GROUP: 'Comping Pattern #1',
          URL: 'https://piano-ology.com/blues-school-comping-pattern-1/'},
         {GROUP: 'Comping Pattern #2',
          URL: 'https://piano-ology.com/blues-school-comping-pattern-2/'},
         {GROUP: 'Comping Pattern #3',
          URL: 'https://piano-ology.com/blues-school-comping-pattern-3/'}]


class PianoPractice:
    @staticmethod
    def exercises_to_practice() -> []:
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
        # random_scale_activity = Activity('Scale', random_scale[GROUP], random_scale[URL])

        random_hanon = random.choice(HANON_EXERCISES)
        # random_hanon_activity = Activity('Hanon', random_hanon[GROUP], random_hanon[URL])

        random_blues_school = random.choice(BLUES)
        # random_blues_school_activity = Activity('Blues School', random_blues_school[GROUP], random_blues_school[URL])

        return [random_scale, random_hanon, random_blues_school]

    @staticmethod
    def keys_to_practice() -> [str]:
        keys: [str] = ['A', 'Bb/A#', 'B', 'C', 'C#/Db', 'D', 'Eb/D#', 'E', 'F', 'F#/Gb', 'G', 'Ab/G#']
        random.shuffle(keys)
        return keys


if __name__ == '__main__':
    print('Exercises:')
    print('\n'.join(map(str, PianoPractice.exercises_to_practice())))
    print('\nKeys:', ', '.join(map(str, PianoPractice.keys_to_practice())))
