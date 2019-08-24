from driver.docker import Docker
import os
BASE_DATE_DIR = '/www/gpanel'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ssn!@*9jaaa4pjn@@l&trp_5iy0^djkvxzofuh%16ny(mbt#_('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

CONFIG_DIR = os.path.join(BASE_DATE_DIR, 'configs')
WWW_DIR = os.path.join(BASE_DATE_DIR, 'wwwroot')
DATABASE_DIR = os.path.join(BASE_DATE_DIR, 'database')
DRIVER = Docker
GATEWAY = '172.17.0.1'


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录,创建目录操作函数
        '''
        os.mkdir(path)与os.makedirs(path)的区别是,当父目录不存在的时候os.mkdir(path)不会创建，os.makedirs(path)则会创建父目录
        '''
        os.makedirs(path)
        # print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path + ' 目录已存在')
        return True
mkdir(CONFIG_DIR)
mkdir(WWW_DIR)


def mkfile(path, value, rewrite=False):
    if rewrite:
        try:
            f = open(path, 'w')
            f.write(value)
            f.close()
        except Exception as e:
            return False
        return True
    try:
        f = open(path, 'r')
    except Exception as e:
        f = open(path, 'w')
        f.write(value)
    finally:
        f.close()
    return True

EMAIL = 'admin@admin.com'


def rmfile(path):
    if os.path.exists(path):
        # 删除文件，可使用以下两种方法。
        os.remove(path)
        # os.unlink(path)
    else:
        print('no such file:%s' % path)
    return True
