import json

from boto.s3.key import Key

from pianopractice import PianoPractice, storage_bucket

if __name__ == '__main__':
    b = storage_bucket()

    scales = Key(b)
    scales.key = PianoPractice.STORAGE_KEY_SCALES
    content = scales.get_contents_as_string()
    exercises = json.loads(content)
    print('Scales: ' + str(exercises))

    hanon = Key(b)
    hanon.key = PianoPractice.STORAGE_KEY_HANON
    content = hanon.get_contents_as_string()
    exercises = json.loads(content)
    print('Hanon: ' + str(exercises))

    blues = Key(b)
    blues.key = PianoPractice.STORAGE_KEY_BLUES
    content = blues.get_contents_as_string()
    exercises = json.loads(content)
    print('Blues: ' + str(exercises))
