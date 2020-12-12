#Create an array class that has a name attribute (★★☆)
#普通のクラスと何が違うのかわからん
import numpy as np
class Name(object):
    def __init__(self,name):
        self.name = name

Z = Name("akita")
print (Z.name)