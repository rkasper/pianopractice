import unittest
import warnings

import validators as validators

from pianopractice import PianoPractice


class PianoPracticeTests(unittest.TestCase):
    def ignore_warnings(test_method):
        def test_run(self, *args, **kwargs):
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                test_method(self, *args, **kwargs)

        return test_run

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
            # group: str = oldExercise['group']
            # self.assertTrue(
            #     group.startswith("Scale") or group.startswith("Hanon") or group.startswith(
            #         "Blues School"), 'Unable to find a "Scale", "Hanon", or "Blues School".')

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

    @ignore_warnings
    def test_randomListOfKeys(self):
        keys: [str] = PianoPractice.keys_to_practice()
        self.assertEqual(12, len(keys))
        self.assertIn('A', keys)
        self.assertIn('C#/Db', keys)

        # TODO This is a bad test: it is nondeterministic - it might fail randomly. Fix that.
        keys2: [str] = PianoPractice.keys_to_practice()
        self.assertNotEqual(keys, keys2)