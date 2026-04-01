import requests
from bs4 import BeautifulSoup

# url = "https://movie.douban.com/top250"
# response = requests.get(url)  # 发送GET请求
#
# # 查看状态码
# print("状态码：", response.status_code)

url = "https://movie.douban.com/top250"

# 自定义请求头，模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# 传入headers参数
response = requests.get(url, headers=headers)
html = response.text  # 存储HTML内容

# 验证请求是否成功
# if response.ok:
#     print("请求成功！")
#     # 获取网页源码（HTML）
#     html_content = response.text
#     print(html_content)  # 打印源码（后续将解析）
# else:
#     print("请求失败，状态码：", response.status_code)

# 创建Beautiful Soup对象
soup = BeautifulSoup(html, "html.parser")

# 查找所有class="title"的<span>标签
all_titles = soup.find_all("span", attrs={"class": "title"})

# 提取中文标题（过滤含斜杠的原版标题）
for title_tag in all_titles:
    title = title_tag.string  # 获取标签内文本
    if "/" not in title:  # 仅保留中文标题
        print(title)

# 遍历10页（start参数：0,25,50,...,225）
for start_num in range(0, 250, 25):
    # 构造每页URL
    url = f"https://movie.douban.com/top250?start={start_num}"
    response = requests.get(url, headers=headers)
    html = response.text

    # 解析当前页
    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.find_all("span", attrs={"class": "title"})

    # 提取并打印中文标题
    for title_tag in all_titles:
        title = title_tag.string
        if "/" not in title:
            print(title)