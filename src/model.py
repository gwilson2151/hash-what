from hashlib import sha256
from functools import partial

def _calc_sha256(file_path):
    sha256_hash = sha256()
    with open(file_path, 'rb') as file_desc:
        for byte_block in iter(lambda: file_desc.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def sha256_calculator(file_path):
    return partial(_calc_sha256, file_path=file_path)
