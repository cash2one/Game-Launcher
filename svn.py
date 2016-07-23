import pysvn
import os

client = pysvn.Client()


path = 'content'
if os.listdir(path) == []:
    client.checkout('http://svn.santosrp.com/svn/santosv2', 'content')
else:
    client.update('content')

