from api_test.s3 import download


filename = './tests/download_profile.png'
key = "images/photo.png"


download(filename, key)
