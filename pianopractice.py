#!/usr/local/bin/python3
import random


class PianoPractice:
    group : str
    exercise : str

    def __init__(self, group, exercise):
        self.group = group
        self.exercise = exercise

    def __repr__(self):
        return self.group + ': ' + self.exercise

    @staticmethod
    def exercises_to_practice() -> [str]:
        scales: [str] = [PianoPractice("Scale", "Major"), PianoPractice("Scale", "Blues (minor)"),
                         PianoPractice("Scale", "Blues (major)"), PianoPractice("Scale", "Mixolydian (dom7)")]
        hanon: [str] = [PianoPractice("Hanon", "1"), PianoPractice("Hanon", "2"), PianoPractice("Hanon", "3"),
                        PianoPractice("Hanon", "4"), PianoPractice("Hanon", "5"), PianoPractice("Hanon", "6"),
                        PianoPractice("Hanon", "7"), PianoPractice("Hanon", "8"), PianoPractice("Hanon", "9"),
                        PianoPractice("Hanon", "10"), PianoPractice("Hanon", "11"), PianoPractice("Hanon", "12"),
                        PianoPractice("Hanon", "13"), PianoPractice("Hanon", "14"), PianoPractice("Hanon", "15"),
                        PianoPractice("Hanon", "16"), PianoPractice("Hanon", "17"), PianoPractice("Hanon", "18"),
                        PianoPractice("Hanon", "19"), PianoPractice("Hanon", "20"), PianoPractice("Hanon", "21"),
                        PianoPractice("Hanon", "22"), PianoPractice("Hanon", "23"), PianoPractice("Hanon", "24"),
                        PianoPractice("Hanon", "25"), PianoPractice("Hanon", "26"), PianoPractice("Hanon", "27"),
                        PianoPractice("Hanon", "28"), PianoPractice("Hanon", "29"), PianoPractice("Hanon", "30")]
        blues_school: [str] = [PianoPractice("Blues School", "Major Blues 12-Bar Form & Harmony, The First Lesson"),
                               PianoPractice("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #1"),
                               PianoPractice("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #2"),
                               PianoPractice("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #3"),
                               PianoPractice("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #4"),
                               PianoPractice("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #5"),
                               PianoPractice("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #6"),
                               PianoPractice("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #7"),
                               PianoPractice("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #8")]
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
