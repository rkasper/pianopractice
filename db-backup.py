from storage import Storage

if __name__ == '__main__':
    scales = Storage.get_scales_as_string()
    hanon = Storage.get_hanon_as_string()
    blues = Storage.get_blues_as_string()
    data = {Storage.STORAGE_KEY_SCALES: scales, Storage.STORAGE_KEY_HANON: hanon, Storage.STORAGE_KEY_BLUES: blues}
    with open("backup.txt", "x") as f:
        print(data, file=f)
