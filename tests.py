import unittest

# I want this tool to tell me which old exercise to practice, and the sequence of keys to practice them in.

import validators as validators

from pianopractice import PianoPractice


class MyTestCase(unittest.TestCase):
    def test_unittestsRunProperly(self):
        self.assertTrue(True)

    def test_tellsMeWhichOldExercisesToPracticeToday(self):
        # There are 3 old exercise to practice.
        exercises_to_practice = PianoPractice.exercises_to_practice()
        self.assertEqual(3, len(exercises_to_practice))

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
    def test_exerciseListIsRandom(self):
        # It's pretty much impossible for two consecutive sets of exercises to be the same. And if they are the same,
        # try again. But don't try more than 100 times.
        exercises_to_practice = PianoPractice.exercises_to_practice()
        exercises_to_practice2 = PianoPractice.exercises_to_practice()
        self.assertNotEqual(exercises_to_practice, exercises_to_practice2)

    def test_thereIsExactlyOneOfEachTypeOfExercise(self):
        exercises_to_practice = PianoPractice.exercises_to_practice()
        self.assertTrue('scale' in exercises_to_practice[0]['url'])
        self.assertTrue('hanon' in exercises_to_practice[1]['url'])
        self.assertTrue('blues' in exercises_to_practice[2]['url'])

    def test_rand_list_of_keys(self):
        keys: [str] = PianoPractice.keys_to_practice()
        self.assertEqual(12, len(keys))
        self.assertIn('A', keys)
        self.assertIn('C#/Db', keys)

        # TODO This is a bad test: it is nondeterministic - it might fail randomly. Fix that.
        keys2: [str] = PianoPractice.keys_to_practice()
        self.assertNotEqual(keys, keys2)


if __name__ == '__main__':
    unittest.main()
