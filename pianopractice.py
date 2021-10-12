#!/usr/local/bin/python3
import random

from activity import Activity


class PianoPractice:
    @staticmethod
    def exercises_to_practice() -> [str]:
        scales: [str] = [Activity("Scale", "Major", "https://pianoscales.org/major.html"),
                         Activity("Scale", "Blues (minor)", "https://pianoscales.org/blues.html"),
                         Activity("Scale", "Blues (major)", "https://pianoscales.org/blues.html"),
                         Activity("Scale", "Mixolydian (dom7)", "https://pianoscales.org/mixolydian.html")]
        hanon: [str] = [Activity("Hanon", "1", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-1/"),
                        Activity("Hanon", "2", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-2/"),
                        Activity("Hanon", "3", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-3/"),
                        Activity("Hanon", "4", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-4/"),
                        Activity("Hanon", "5", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-5/"),
                        Activity("Hanon", "6", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-6/"),
                        Activity("Hanon", "7", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-7/"),
                        Activity("Hanon", "8", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-8/"),
                        Activity("Hanon", "9", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-9/"),
                        Activity("Hanon", "10", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-10/"),
                        Activity("Hanon", "11", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-11/"),
                        Activity("Hanon", "12", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-12/"),
                        Activity("Hanon", "13", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-13/"),
                        Activity("Hanon", "14", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-14/"),
                        Activity("Hanon", "15", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-15/"),
                        Activity("Hanon", "16", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-16/"),
                        Activity("Hanon", "17", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-17/"),
                        Activity("Hanon", "18", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-18/"),
                        Activity("Hanon", "19", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-19/"),
                        Activity("Hanon", "20", "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-20/"),
                        Activity("Hanon", "21", "https://galaxymusicnotes.com/products/hanon-exercise-no-21"),
                        Activity("Hanon", "22", "https://galaxymusicnotes.com/products/hanon-exercise-no-22"),
                        Activity("Hanon", "23", "https://galaxymusicnotes.com/products/hanon-exercise-no-23-from-the-virtuoso-pianist"),
                        Activity("Hanon", "24", "https://galaxymusicnotes.com/products/hanon-exercise-no-24-from-the-virtuoso-pianist-part-2"),
                        Activity("Hanon", "25", "https://galaxymusicnotes.com/products/hanon-exercise-no-25"),
                        Activity("Hanon", "26", "https://galaxymusicnotes.com/products/hanon-exercise-no-26"),
                        Activity("Hanon", "27", "https://galaxymusicnotes.com/products/hanon-exercise-no-27"),
                        Activity("Hanon", "28", "https://galaxymusicnotes.com/products/hanon-exercise-no-28"),
                        Activity("Hanon", "29", "https://galaxymusicnotes.com/products/hanon-exercise-no-29"),
                        Activity("Hanon", "30", "https://galaxymusicnotes.com/products/hanon-exercise-no-30")]
        blues_school: [str] = [Activity("Blues School", "Major Blues 12-Bar Form & Harmony, The First Lesson", "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-the-first-lesson/"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #2", "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-2/"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #3", "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-3/"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #4", "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-4/"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #5", "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-5/"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #6", "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-6/"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #7", "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-7/"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #8", "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-8/")]
        return [random.choice(scales), random.choice(hanon), random.choice(blues_school)]

    @staticmethod
    def keys_to_practice() -> [str]:
        keys: [str] = ["A", "Bb/A#", "B", "C", "C#/Db", "D", "Eb/D#", "E", "F", "F#/Gb", "G", "Ab/G#"]
        random.shuffle(keys)
        return keys


if __name__ == '__main__':
    print('Exercises:')
    print('\n'.join(map(str, PianoPractice.exercises_to_practice())))
    print('\nKeys:', ', '.join(map(str, PianoPractice.keys_to_practice())))
