#!/usr/local/bin/python3
import random


class Activity:
    group : str
    exercise : str

    def __init__(self, group, exercise):
        self.group = group
        self.exercise = exercise

    def __repr__(self):
        return self.group + ': ' + self.exercise

class PianoPractice:
    @staticmethod
    def exercises_to_practice() -> [str]:
        scales: [str] = [Activity("Scale", "Major"), Activity("Scale", "Blues (minor)"),
                         Activity("Scale", "Blues (major)"), Activity("Scale", "Mixolydian (dom7)")]
        hanon: [str] = [Activity("Hanon", "1"), Activity("Hanon", "2"), Activity("Hanon", "3"),
                        Activity("Hanon", "4"), Activity("Hanon", "5"), Activity("Hanon", "6"),
                        Activity("Hanon", "7"), Activity("Hanon", "8"), Activity("Hanon", "9"),
                        Activity("Hanon", "10"), Activity("Hanon", "11"), Activity("Hanon", "12"),
                        Activity("Hanon", "13"), Activity("Hanon", "14"), Activity("Hanon", "15"),
                        Activity("Hanon", "16"), Activity("Hanon", "17"), Activity("Hanon", "18"),
                        Activity("Hanon", "19"), Activity("Hanon", "20"), Activity("Hanon", "21"),
                        Activity("Hanon", "22"), Activity("Hanon", "23"), Activity("Hanon", "24"),
                        Activity("Hanon", "25"), Activity("Hanon", "26"), Activity("Hanon", "27"),
                        Activity("Hanon", "28"), Activity("Hanon", "29"), Activity("Hanon", "30")]
        blues_school: [str] = [Activity("Blues School", "Major Blues 12-Bar Form & Harmony, The First Lesson"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #1"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #2"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #3"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #4"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #5"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #6"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #7"),
                               Activity("Blues School", "Major Blues 12-Bar Form & Harmony, Variation #8")]
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
