import random
import string


def randomString(length=8):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))
