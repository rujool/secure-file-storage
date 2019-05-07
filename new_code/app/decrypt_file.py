import os, random, struct, hashlib
from Crypto.Cipher import AES

def decrypt_file(key, in_filename):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    out_filename = os.path.splitext(in_filename)[0]
    chunksize = 64 * 1024

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        print("origsize=",origsize)
        iv = infile.read(16)
        print("iv=",iv)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

decrypt_file(hashlib.sha256('secret'.encode('utf-8')).digest(),'../uploaded_files/register.png.enc')
