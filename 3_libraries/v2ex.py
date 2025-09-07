import requests
import json

# 1. API端点（从文档获取）
url = "https://www.v2ex.com/api/topics/hot.json"

# 2. 发送GET请求（若需查询参数，可加params参数）
response = requests.get(url)

# 3. 判断请求是否成功（2xx状态码表示成功）
if response.status_code >= 200 and response.status_code < 300:
    print("请求成功！")
    # 4. 解析JSON响应（response.text是JSON字符串）
    data = json.loads(response.text)  # 转为Python列表/字典

    # 提取第3个热门主题的标题和内容（索引从0开始，索引2对应第3个）
    third_topic = data[2]
    print("第3个热门主题标题：", third_topic["title"])
    print("第3个热门主题内容：", third_topic["content"])
else:
    print(f"请求失败，状态码：{response.status_code}")