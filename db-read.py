import json

from storage import Storage

if __name__ == '__main__':
    print('Scales: ' + json.dumps(Storage.get_scales_as_json(), indent=2))
    print('Hanon: ' + json.dumps(Storage.get_hanon_as_json(), indent=2))
    print('Blues: ' + json.dumps(Storage.get_blues_as_json(), indent=2))
