#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 浙江政务服务网域名
SITEURL = 'http://www.zjzwfw.gov.cn'

# 添加浙江省各市URL
cityUrl = {
    'hangzhou': 'http://www.zjzwfw.gov.cn/zjzw/punish/frontpunish/searchall_list.do?areacode=330101&xzcf_code=&pageNo=1',
    'wenzhou': 'http://www.zjzwfw.gov.cn/zjzw/punish/frontpunish/searchall_list.do?areacode=330301&xzcf_code=&pageNo=1'
}

# 浏览器标识
HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/73.0.3683.86 Safari/537.36'
}
