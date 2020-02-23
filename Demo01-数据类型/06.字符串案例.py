"""
    猫眼top100的网址
    第一页：https://maoyan.com/board/4?offset=0
    第二页：https://maoyan.com/board/4?offset=10
    第三页：https://maoyan.com/board/4?offset=20
    ....
    第十页：https://maoyan.com/board/4?offset=90

    请分别使用三种字符串构建的方法创建所有的请求地址
"""

# format
base_url = 'https://maoyan.com/board/4?offset={page}'
for page in range(10):
    print(base_url.format(page=page))

# %
base_url = 'https://maoyan.com/board/4?offset=%s'
for page in range(10):
    print(base_url % page)

# f
for page in range(10):
    print(f'https://maoyan.com/board/4?offset={page}')
