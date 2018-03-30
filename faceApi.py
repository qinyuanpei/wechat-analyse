#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
import TencentYoutuyun

class FaceAPI:

    def __init__(self):
        appid = 'xxxxxxx'
        userId = 'xxxxxxx'
        secretId = 'xxxxxxx'
        secretKey = 'xxxxxxx'
        endPoint = TencentYoutuyun.conf.API_YOUTU_END_POINT
        self.youtu = TencentYoutuyun.YouTu(appid, secretId, secretKey, userId, endPoint)

    def detectFace(self,image):
        try:
            retocr = self.youtu.DetectFace(image)
            return len(retocr['face'])>0
        except Exception as e:
            return false
    
    def extractTags(self,image):
        try:
            retocr = self.youtu.imagetag(image)
            return retocr['tags']
        except Exception as e:
            return None
