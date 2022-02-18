#!/usr/local/bin/python3
import json
import random

from activity import Activity

SCALES = [["Major", "https://pianoscales.org/major.html"],
          ["Minor", "https://pianoscales.org/minor.html"],
          ["Blues (minor)", "https://pianoscales.org/blues.html"],
          ["Blues (major)", "https://pianoscales.org/blues.html"],
          ["Mixolydian (dom7)", "https://pianoscales.org/mixolydian.html"],
          ["Chromatic", "https://www.pianoscales.org/chromatic.html"]]

HANON = "Hanon"

HANON_EXERCISES = [Activity(HANON, "1", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-1/"),
                   Activity(HANON, "2", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-2/"),
                   Activity(HANON, "3", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-3/"),
                   Activity(HANON, "4", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-4/"),
                   Activity(HANON, "5", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-5/"),
                   Activity(HANON, "6", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-6/"),
                   Activity(HANON, "7", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-7/"),
                   Activity(HANON, "8", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-8/"),
                   Activity(HANON, "9", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-9/"),
                   Activity(HANON, "10",
                            "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-10/"),
                   Activity(HANON, "11",
                            "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-11/"),
                   Activity(HANON, "12",
                            "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-12/"),
                   Activity(HANON, "13",
                            "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-13/"),
                   Activity(HANON, "14",
                            "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-14/"),
                   Activity(HANON, "15",
                            "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-15/"),
                   Activity(HANON, "16",
                            "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-16/"),
                   Activity(HANON, "17",
                            "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-17/"),
                   Activity(HANON, "18",
                            "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-18/"),
                   Activity(HANON, "19",
                            "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-19/"),
                   Activity(HANON, "20",
                            "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-20/"),
                   Activity(HANON, "21", "https://galaxymusicnotes.com/products/hanon-exercise-no-21"),
                   Activity(HANON, "22", "https://galaxymusicnotes.com/products/hanon-exercise-no-22"),
                   Activity(HANON, "23",
                            "https://galaxymusicnotes.com/products/hanon-exercise-no-23-from-the-virtuoso-pianist"),
                   Activity(HANON, "24",
                            "https://galaxymusicnotes.com/products/hanon-exercise-no-24-from-the-virtuoso-pianist-part-2"),
                   Activity(HANON, "25", "https://galaxymusicnotes.com/products/hanon-exercise-no-25"),
                   Activity(HANON, "26", "https://galaxymusicnotes.com/products/hanon-exercise-no-26"),
                   Activity(HANON, "27", "https://galaxymusicnotes.com/products/hanon-exercise-no-27"),
                   Activity(HANON, "28", "https://galaxymusicnotes.com/products/hanon-exercise-no-28"),
                   Activity(HANON, "29", "https://galaxymusicnotes.com/products/hanon-exercise-no-29"),
                   Activity(HANON, "30", "https://galaxymusicnotes.com/products/hanon-exercise-no-30")]

BLUES_SCHOOL = "Blues School"

BLUES = [Activity(BLUES_SCHOOL, "Major Blues 12-Bar Form & Harmony, The First Lesson",
                  "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-the-first-lesson/"),
         Activity(BLUES_SCHOOL, "Major Blues 12-Bar Form & Harmony, Variation #2",
                  "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-2/"),
         Activity(BLUES_SCHOOL, "Major Blues 12-Bar Form & Harmony, Variation #3",
                  "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-3/"),
         Activity(BLUES_SCHOOL, "Major Blues 12-Bar Form & Harmony, Variation #4",
                  "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-4/"),
         Activity(BLUES_SCHOOL, "Major Blues 12-Bar Form & Harmony, Variation #5",
                  "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-5/"),
         Activity(BLUES_SCHOOL, "Major Blues 12-Bar Form & Harmony, Variation #6",
                  "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-6/"),
         Activity(BLUES_SCHOOL, "Major Blues 12-Bar Form & Harmony, Variation #7",
                  "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-7/"),
         Activity(BLUES_SCHOOL, "Major Blues 12-Bar Form & Harmony, Variation #8",
                  "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-8/"),
         Activity(BLUES_SCHOOL, "Comping Pattern #1",
                  "https://piano-ology.com/blues-school-comping-pattern-1/"),
         Activity(BLUES_SCHOOL, "Comping Pattern #2",
                  "https://piano-ology.com/blues-school-comping-pattern-2/"),
         Activity(BLUES_SCHOOL, "Comping Pattern #3",
                  "https://piano-ology.com/blues-school-comping-pattern-3/")]


class PianoPractice:
    @staticmethod
    def exercises_to_practice() -> [Activity]:
        # its_a_dictionary = {
        #     "Scale": [["Major", "https://pianoscales.org/major.html"], ["Minor", "https://pianoscales.org/minor.html"]],
        #     "Hanon": [["1", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-1/"],
        #               ["2", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-2/"]],
        #     "Blues School": [["Major Blues 12-Bar Form & Harmony, The First Lesson",
        #                       "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-the-first-lesson/"],
        #                      ["Major Blues 12-Bar Form & Harmony, Variation #2",
        #                       "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-2/"]]}
        # print('its_a_dictionary: ' + str(its_a_dictionary))
        # its_json = json.dumps(its_a_dictionary)
        # print('its_json: ' + its_json)
        # its_another_dictionary = json.loads(its_json)
        # print('its_another_dictionary: ' + str(its_another_dictionary))

        random_scale = random.choice(SCALES)
        random_scale_activity = Activity("Scale", random_scale[0], random_scale[1])
        print("random_scale_activity: " + str(random_scale_activity))

        hanon: [Activity] = HANON_EXERCISES
        blues_school: [Activity] = BLUES
        return [random_scale_activity, random.choice(hanon), random.choice(blues_school)]

    @staticmethod
    def keys_to_practice() -> [str]:
        keys: [str] = ["A", "Bb/A#", "B", "C", "C#/Db", "D", "Eb/D#", "E", "F", "F#/Gb", "G", "Ab/G#"]
        random.shuffle(keys)
        return keys


if __name__ == '__main__':
    print('Exercises:')
    print('\n'.join(map(str, PianoPractice.exercises_to_practice())))
    print('\nKeys:', ', '.join(map(str, PianoPractice.keys_to_practice())))
