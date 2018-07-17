#! /usr/bin/python
# -*- coding: utf-8 -8*-

from urllib import request
import ssl
import gzip
import io


urlHeaders = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'uuid_tt_dd=1115283672701812903_20180324; '
          'ADHOC_MEMBERSHIP_CLIENT_ID1.0=95f738d9-2b08-d3ee-cbf3-45ce9d3fa2e3; '
          'kd_user_id=af814ab8-1b67-4d82-8568-6c7b12052f50; '
          'UN=hlmlalala; '
          '__yadk_uid=xUWplkJm6YkBw7WqvMXuPvrRsXFrpTMQ; '
          '__utma=17226283.413198308.1524739533.1524739533.1524739533.1; '
          '__utmz=17226283.1524739533.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); '
          'CloudGuest=cVqkFaCQHGv2FtdDP4oA2p90GhBoVm2n4zq3+bDFeKP/zuYBY6JufKiD7M+pagPcMnF0imlHxs/+21Su5+HvkcuXWHgzrJRow1drf7sz9OZ7sWfEpRR8EeQ72s+NbfZgvw3e3ANAda7l39DBZLSio8veTomBcH7DAD3OSgprLDfaEL+dwy80LvPHlSfNBZU6; '
          'smidV2=20180613150521dd9db90f14184be176279bb3a3e2b7db0071ea43350799a10; '
          'UserName=hlmlalala; '
          'UserInfo=NaCHMDHN1hZHCAXUN0pB11TPAhfkRqej3rFWNfLWdyKfaXaht99p%2BbOEJkOYVG%2BdYt%2FR02E9VtBDB5ckTmYJqdLjoxly1p4RycNjY38FEojJuTCIx0%2FbIFcBJ7zUMCG8; '
          'UserNick=%E6%98%8E%E6%98%8E%E5%93%A5er; '
          'AU=B82; '
          'BT=1531556210402; '
          'UserToken=NaCHMDHN1hZHCAXUN0pB11TPAhfkRqej3rFWNfLWdyKfaXaht99p%2BbOEJkOYVG%2BdYt%2FR02E9VtBDB5ckTmYJqdLjoxly1p4RycNjY38FEog6uqS4jecVt3s56SnybcgL7OCn31lBwTWnkFU404z6WUtFRI%2FgRrIZi9uh2CGjt3WKDLavKbqvsPTY90MYYpuQ; '
          'dc_session_id=10_1531568320928.106241; '
          'TY_SESSION_ID=581bce84-dbd3-4260-83ed-88a74dbe53e7; '
          'dc_tos=pbw12l; '
          'Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1531556039,1531568321,1531568354,1531624557; '
          'Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1531624557',
'Host': 'blog.csdn.net',
'Upgrade-Insecure-Requests': 1,
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
urlImgHeaders = {
'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
'cookie': 'uuid_tt_dd=1115283672701812903_20180324; kd_user_id=af814ab8-1b67-4d82-8568-6c7b12052f50; UN=hlmlalala; __utma=17226283.413198308.1524739533.1524739533.1524739533.1; __utmz=17226283.1524739533.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); CloudGuest=cVqkFaCQHGv2FtdDP4oA2p90GhBoVm2n4zq3+bDFeKP/zuYBY6JufKiD7M+pagPcMnF0imlHxs/+21Su5+HvkcuXWHgzrJRow1drf7sz9OZ7sWfEpRR8EeQ72s+NbfZgvw3e3ANAda7l39DBZLSio8veTomBcH7DAD3OSgprLDfaEL+dwy80LvPHlSfNBZU6; smidV2=20180613150521dd9db90f14184be176279bb3a3e2b7db0071ea43350799a10; UserName=hlmlalala; UserInfo=NaCHMDHN1hZHCAXUN0pB11TPAhfkRqej3rFWNfLWdyKfaXaht99p%2BbOEJkOYVG%2BdYt%2FR02E9VtBDB5ckTmYJqdLjoxly1p4RycNjY38FEojJuTCIx0%2FbIFcBJ7zUMCG8; UserNick=%E6%98%8E%E6%98%8E%E5%93%A5er; AU=B82; BT=1531556210402; UserToken=NaCHMDHN1hZHCAXUN0pB11TPAhfkRqej3rFWNfLWdyKfaXaht99p%2BbOEJkOYVG%2BdYt%2FR02E9VtBDB5ckTmYJqdLjoxly1p4RycNjY38FEog6uqS4jecVt3s56SnybcgL7OCn31lBwTWnkFU404z6WUtFRI%2FgRrIZi9uh2CGjt3WKDLavKbqvsPTY90MYYpuQ; dc_session_id=10_1531568320928.106241; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1531554852,1531556039,1531568321,1531568354; dc_tos=pbuucf; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1531569184',
'referer': 'https://blog.csdn.net/babybabyup/article/details/81044277',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


class MyUrlOpen(object):

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.context = ssl._create_unverified_context()
        self.headers = urlHeaders


    def my_UrlOpen(self):
        req = request.Request(self.url, headers=self.headers)
        res = request.urlopen(req,context=self.context)
        if res.info()['Content-Encoding'] == 'gzip':
            buf = io.BytesIO(res.read())
            gf = gzip.GzipFile(fileobj=buf)
            content = gf.read()
            #print(content)
        else:
            print('编码方式未知，请联系作者添加')
            content = None
        return content


class MyImgUrlOpen(MyUrlOpen):

    def __init__(self, url):
        super().__init__(url)
        self.headers = urlImgHeaders

    def my_UrlOpen(self):
        req = request.Request(self.url, headers=self.headers)
        res = request.urlopen(req, context=self.context)
        context = res.read()
        return context
