#!/usr/bin/python
"compute aws s3 etag"

import hashlib


def compute_s3_etag(file_path, chunk_size=8 * 1024 * 1024):
    "compute aws s3 etag"

    md5s = []

    with open(file_path, 'rb') as fp:
        while True:
            data = fp.read(chunk_size)
            if not data:
                break
            md5s.append(hashlib.md5(data))

    if len(md5s) == 1:
        return '"{}"'.format(md5s[0].hexdigest())

    digests = b''.join(m.digest() for m in md5s)
    digests_md5 = hashlib.md5(digests)
    return '"{}-{}"'.format(digests_md5.hexdigest(), len(md5s))

if __name__ == "__main__":

    print compute_s3_etag('./vep86.tgz')
