#!/usr/bin/env python

import os
import sys
import json
import random
import string
import requests
import pyperclip
import subprocess
from Crypto.Random import get_random_bytes

binary_7z = '/usr/local/bin/7z'

class FileIO:

    BASE_URL = 'https://file.io'

    def uploadEphemeralFile(self, file):
        http = HttpInterface()
        response = http.uploadFile(self.BASE_URL, file)
        if response['success'] == True:
            pyperclip.copy(response['link'])
            url = pyperclip.paste()
            subprocess.run(['osascript', '-e', 'display notification "File was successfully uploaded to file.io" with title "Fie.io uploader" sound name "default"'])
        else:
            subprocess.run(['osascript', '-e', 'display notification "Error: {0}" with title "Fie.io uploader" sound name "default"'.format(response['message'])])


class PrepareFile:

    def generate_key(self, length):
        key = get_random_bytes(length)
        return key.hex()

    def get_random_filename(self, letters_count, digits_count):
        sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
        sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

        sample_list = list(sample_str)
        random.shuffle(sample_list)
        final_string = ''.join(sample_list)
        return final_string

    def prepare_compressed_file(self, files):
        key = self.generate_key(32)
        filename = self.get_random_filename(5, 3)
        rc = subprocess.call([binary_7z, 'a', '-p{0}'.format(key), '-y', '/tmp/{0}.zip'.format(filename)] + files)
        return filename, key

    def delete_file(self, file):
        os.remove(file)

class HttpInterface:

    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050',
    }

    def uploadFile(self, url, file):
        files = {'file': open(file, 'rb')}
        r = requests.post(url, files=files, proxies=self.proxies)
        return r.json()

if __name__ == '__main__':
    fileio = FileIO()
    prepare_file = PrepareFile()
    files = json.loads(sys.argv[1])
    filename, key = prepare_file.prepare_compressed_file(files)
    fileio.uploadEphemeralFile('/tmp/{0}.zip'.format(filename))
    prepare_file.delete_file('/tmp/{0}.zip'.format(filename))

    subprocess.run(['osascript', '-e', 'tell application "TextEdit" to make new document with properties {text:"Key: ' + key + '"}'])
