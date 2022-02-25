import json
import unittest

# I want this tool to tell me which old exercise to practice, and the sequence of keys to practice them in.
from os import environ

import validators as validators

from pianopractice import PianoPractice
from storage import Storage


class BizLogicTests(unittest.TestCase):
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

    def test_randomListOfKeys(self):
        keys: [str] = PianoPractice.keys_to_practice()
        self.assertEqual(12, len(keys))
        self.assertIn('A', keys)
        self.assertIn('C#/Db', keys)

        # TODO This is a bad test: it is nondeterministic - it might fail randomly. Fix that.
        keys2: [str] = PianoPractice.keys_to_practice()
        self.assertNotEqual(keys, keys2)


class StorageTests(unittest.TestCase):
    def test_canGetScalesFromStorage(self):
        content_as_string = Storage.get_scales_as_string()
        self.assertTrue(len(content_as_string) > 0)

        content_as_json = Storage.get_scales_as_json()
        self.assertTrue(len(content_as_json) > 0)

        self.assertEqual(json.loads(content_as_string), content_as_json)

    def test_canGetHanonFromStorage(self):
        content_as_string = Storage.get_hanon_as_string()
        self.assertTrue(len(content_as_string) > 0)

        content_as_json = Storage.get_hanon_as_json()
        self.assertTrue(len(content_as_json) > 0)

        self.assertEqual(json.loads(content_as_string), content_as_json)

    def test_canGetBluesFromStorage(self):
        content_as_string = Storage.get_blues_as_string()
        self.assertTrue(len(content_as_string) > 0)

        content_as_json = Storage.get_blues_as_json()
        self.assertTrue(len(content_as_json) > 0)

        self.assertEqual(json.loads(content_as_string), content_as_json)

    @unittest.skipUnless(environ.get('MOCK_DB'), "Only test with mock DB - don't break the production DB.")
    def test_canSetScalesToStorage(self):
        original_content = Storage.get_scales_as_string()
        new_content = '["poop"]'
        Storage.set_scales_from_string(new_content)
        self.assertEqual(new_content, Storage.get_scales_as_string())
        Storage.set_scales_from_string(original_content)

    @unittest.skipUnless(environ.get('MOCK_DB'), "Only test with mock DB - don't break the production DB.")
    def test_canSetHanonToStorage(self):
        original_content = Storage.get_hanon_as_string()
        new_content = '["poop"]'
        Storage.set_hanon_from_string(new_content)
        self.assertEqual(new_content, Storage.get_hanon_as_string())
        Storage.set_hanon_from_string(original_content)

    @unittest.skipUnless(environ.get('MOCK_DB'), "Only test with mock DB - don't break the production DB.")
    def test_canSetBluesToStorage(self):
        original_content = Storage.get_blues_as_string()
        new_content = '["poop"]'
        Storage.set_blues_from_string(new_content)
        self.assertEqual(new_content, Storage.get_blues_as_string())
        Storage.set_blues_from_string(original_content)


# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(PianoPracticeTests())
#     return suite


if __name__ == '__main__':
    unittest.main()
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
