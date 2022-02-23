from boto.s3.key import Key

from pianopractice import PianoPractice, storage_bucket

if __name__ == '__main__':
    b = storage_bucket()

    scales = Key(b)
    scales.key = PianoPractice.STORAGE_KEY_SCALES
    scales.set_contents_from_string("""[{"name": "Major", "url": "https://pianoscales.org/major.html"},
{"name": "Minor", "url": "https://pianoscales.org/minor.html"},
{"name": "Blues (minor)", "url": "https://pianoscales.org/blues.html"},
{"name": "Blues (major)", "url": "https://pianoscales.org/blues.html"},
{"name": "Mixolydian (dom7)", "url": "https://pianoscales.org/mixolydian.html"},
{"name": "Chromatic", "url": "https://www.pianoscales.org/chromatic.html"}]""")

    hanon = Key(b)
    hanon.key = PianoPractice.STORAGE_KEY_HANON
    hanon.set_contents_from_string("""[{"name": "1",
              "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-1/"},
{"name": "2", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-2/"},
{"name": "3", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-3/"},
{"name": "4", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-4/"},
{"name": "5", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-5/"},
{"name": "6", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-6/"},
{"name": "7", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-7/"},
{"name": "8", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-8/"},
{"name": "9", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-9/"},
{"name": "10", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-10/"},
{"name": "11", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-11/"},
{"name": "12", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-12/"},
{"name": "13", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-13/"},
{"name": "14", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-14/"},
{"name": "15", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-15/"},
{"name": "16", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-16/"},
{"name": "17", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-17/"},
{"name": "18", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-18/"},
{"name": "19", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-19/"},
{"name": "20", "url": "https://www.hanon-online.com/the-virtuoso-pianist-part-i/hanon-exercise-n-20/"},
{"name": "21", "url": "https://galaxymusicnotes.com/products/hanon-exercise-no-21"},
{"name": "22", "url": "https://galaxymusicnotes.com/products/hanon-exercise-no-22"},
{"name": "23", "url": "https://galaxymusicnotes.com/products/hanon-exercise-no-23-from-the-virtuoso-pianist"},
{"name": "24", "url": "https://galaxymusicnotes.com/products/hanon-exercise-no-24-from-the-virtuoso-pianist-part-2"},
{"name": "25", "url": "https://galaxymusicnotes.com/products/hanon-exercise-no-25"},
{"name": "26", "url": "https://galaxymusicnotes.com/products/hanon-exercise-no-26"},
{"name": "27", "url": "https://galaxymusicnotes.com/products/hanon-exercise-no-27"},
{"name": "28", "url": "https://galaxymusicnotes.com/products/hanon-exercise-no-28"},
{"name": "29", "url": "https://galaxymusicnotes.com/products/hanon-exercise-no-29"},
{"name": "30", "url": "https://galaxymusicnotes.com/products/hanon-exercise-no-30"}]""")

    blues = Key(b)
    blues.key = PianoPractice.STORAGE_KEY_BLUES
    blues.set_contents_from_string("""[{"name": "Major Blues 12-Bar Form & Harmony, The First Lesson",
"url": "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-the-first-lesson/"},
{"name": "Major Blues 12-Bar Form & Harmony, Variation #2",
"url": "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-2/"},
{"name": "Major Blues 12-Bar Form & Harmony, Variation #3",
"url": "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-3/"},
{"name": "Major Blues 12-Bar Form & Harmony, Variation #4",
"url": "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-4/"},
{"name": "Major Blues 12-Bar Form & Harmony, Variation #5",
"url": "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-5/"},
{"name": "Major Blues 12-Bar Form & Harmony, Variation #6",
"url": "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-6/"},
{"name": "Major Blues 12-Bar Form & Harmony, Variation #7",
"url": "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-7/"},
{"name": "Major Blues 12-Bar Form & Harmony, Variation #8",
"url": "https://piano-ology.com/blues-school-major-blues-12-bar-form-harmony-variation-8/"},
{"name": "Comping Pattern #1", "url": "https://piano-ology.com/blues-school-comping-pattern-1/"},
{"name": "Comping Pattern #2", "url": "https://piano-ology.com/blues-school-comping-pattern-2/"},
{"name": "Comping Pattern #3", "url": "https://piano-ology.com/blues-school-comping-pattern-3/"}]""")
