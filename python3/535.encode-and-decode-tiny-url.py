#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
import base64
import hashlib

class Codec:
    def __init__(self):
        self.data = {}
    def encode(self, longUrl: str) -> str:
        code = base64.b64encode(hashlib.sha1(longUrl.encode()).digest()).decode("utf-8")
        self.data['http://tinyurl.com/' + code] = longUrl
        return 'http://tinyurl.com/' + code

    def decode(self, shortUrl: str) -> str:
        return self.data[shortUrl]

import random
class Codec:
    def __init__(self):
        self.data = {}
        self.index = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
    def encode(self, longUrl: str) -> str:
        code = ''
        for i in range(6):
            code += self.index[random.randint(0, 61)]
        self.data['http://tinyurl.com/' + code] = longUrl
        return 'http://tinyurl.com/' + code

    def decode(self, shortUrl: str) -> str:
        print(shortUrl)
        return self.data[shortUrl]       

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

