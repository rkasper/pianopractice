#!/usr/local/bin/python3
import random


class PianoPractice:
    @staticmethod
    def exercises_to_practice() -> [str]:
        scales: [str] = ["Scale: Major", "Scale: Blues (minor)", "Scale: Blues (major)", "Scale: Mixolydian (dom7)"]
        hanon: [str] = ["Hanon: 1", "Hanon: 2", "Hanon: 3", "Hanon: 4", "Hanon: 5",
                        "Hanon: 6", "Hanon: 7", "Hanon: 8", "Hanon: 9", "Hanon: 10",
                        "Hanon: 11", "Hanon: 12", "Hanon: 13", "Hanon: 14", "Hanon: 15",
                        "Hanon: 16", "Hanon: 17", "Hanon: 18", "Hanon: 19", "Hanon: 20",
                        "Hanon: 21", "Hanon: 22", "Hanon: 23", "Hanon: 24", "Hanon: 25",
                        "Hanon: 26", "Hanon: 27", "Hanon: 28", "Hanon: 29", "Hanon: 30"]
        blues_school: [str] = ["Blues School: Major Blues 12-Bar Form & Harmony, The First Lesson",
                               "Blues School: Major Blues 12-Bar Form & Harmony, Variation #1",
                               "Blues School: Major Blues 12-Bar Form & Harmony, Variation #2",
                               "Blues School: Major Blues 12-Bar Form & Harmony, Variation #3",
                               "Blues School: Major Blues 12-Bar Form & Harmony, Variation #4",
                               "Blues School: Major Blues 12-Bar Form & Harmony, Variation #5",
                               "Blues School: Major Blues 12-Bar Form & Harmony, Variation #6",
                               "Blues School: Major Blues 12-Bar Form & Harmony, Variation #7",
                               "Blues School: Major Blues 12-Bar Form & Harmony, Variation #8"]
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