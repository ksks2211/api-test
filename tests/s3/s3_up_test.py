from api_test.s3 import upload


filename = './tests/profile.png'
key = "images/photo.png"


upload(filename, key)