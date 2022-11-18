import unittest

import validators as validators

from app.pianopractice import PianoPractice
from shared_test_code import ignore_warnings


class PianoPracticeTests(unittest.TestCase):
    def test_unittestsRunProperly(self):
        self.assertTrue(True)

    @ignore_warnings
    def test_tellsMeWhichOldExercisesToPracticeToday(self):
        # There are 3 old exercise to practice.
        exercises_to_practice = PianoPractice.exercises_to_practice()
        self.assertEqual(3, len(exercises_to_practice))

    @ignore_warnings
    def test_exerciseAreTheRightType(self):
        # The old exercises or scales, Hanon, or Blues School.
        exercises_to_practice = PianoPractice.exercises_to_practice()
        for oldExercise in exercises_to_practice:
            exercise: str = oldExercise[PianoPractice.NAME]
            self.assertTrue(len(exercise) > 0)
            self.assertTrue(validators.url(oldExercise[PianoPractice.URL]))

    # TODO This is a bad test: it is nondeterministic - it might fail randomly. Fix that.
    @ignore_warnings
    def test_exerciseListIsRandom(self):
        # It's pretty much impossible for two consecutive sets of exercises to be the same. And if they are the same,
        # try again. But don't try more than 100 times.
        exercises_to_practice = PianoPractice.exercises_to_practice()
        exercises_to_practice2 = PianoPractice.exercises_to_practice()
        self.assertNotEqual(exercises_to_practice, exercises_to_practice2)

    @ignore_warnings
    def test_thereIsExactlyOneOfEachTypeOfExercise(self):
        exercises_to_practice = PianoPractice.exercises_to_practice()
        self.assertTrue('scale' in exercises_to_practice[0]['url'])
        self.assertTrue('hanon' in exercises_to_practice[1]['url'])
        self.assertTrue('blues' in exercises_to_practice[2]['url'])

    def test_hanonExercisesTellMeWhatRangeOfOctavesToPractice(self):
        hanon = PianoPractice.exercises_to_practice()[1]
        self.assertTrue('(LH octaves ' in hanon['name'])
        self.assertTrue(', RH octaves ' in hanon['name'])

    @ignore_warnings
    def test_randomListOfKeys(self):
        keys: [str] = PianoPractice.keys_to_practice()
        self.assertEqual(12, len(keys))
        self.assertIn('A', keys)
        self.assertIn('C#/Db', keys)

        # TODO This is a bad test: it is nondeterministic - it might fail randomly. Fix that.
        keys2: [str] = PianoPractice.keys_to_practice()
        self.assertNotEqual(keys, keys2)
