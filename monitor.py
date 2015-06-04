#!/usr/bin/python

import hashlib
import os
import time

dropbox_path = os.path.expanduser("~/Dropbox")
input_path = dropbox_path + "/jarvis/input.txt"
output_path = dropbox_path + "/jarvis/output.txt"

def get_hash():
    sha512 = hashlib.sha512()
    input_file = open(input_path)
    sha512.update(input_file.read())
    input_file.close()
    return sha512.hexdigest()

def monitor():
    new_hash = get_hash()
    while 1:
        time.sleep(10)
        old_hash = new_hash
        new_hash = get_hash()
        if old_hash != new_hash:
            print "File changed!"

            input_file = open(input_path)
            data = input_file.read().splitlines()
            input_file.close()

            operation = data.pop(0)

            # do stuff based on operation

if __name__ == "__main__":
    print "Monitoring for changes..."
    monitor()
