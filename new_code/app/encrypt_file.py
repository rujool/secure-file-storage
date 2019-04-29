import os, random, struct, hashlib
from Crypto.Cipher import AES
from werkzeug.utils import secure_filename
from flask import current_app

def encrypt_and_save_file(key, infile, file_size):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    out_filename = os.path.join(current_app.config.get('UPLOAD_FOLDER'), secure_filename(infile.filename)) + '.enc'
    chunksize = 64 * 1024
    iv = os.urandom(16)
    key = hashlib.sha256(key).digest()
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    sha512 = hashlib.sha512()

    with open(out_filename, 'wb') as outfile:
        data = None
        #keep reading until out of data
        outfile.write(struct.pack('<Q', file_size))
        print("origsize=",file_size)
        sha512.update(struct.pack('<Q',file_size))
        outfile.write(iv)
        print("iv=",iv)
        sha512.update(iv)
        infile.seek(0)
        while True:
            
            data = infile.read(chunksize)
            if len(data) == 0:
                break
            elif len(data) % 16 != 0:
                chunk += b' ' * (16 - len(data) % 16)
            sha512.update(data)
            enc_data = encryptor.encrypt(data)
            outfile.write(enc_data)
        print("sha512: {0}".format(sha512.hexdigest()))

# password = 'secret'.encode('utf-8')
# filename = 'rxd170930_Assignment1.docx'
# encrypt_file(hashlib.sha256(password).digest(),filename)