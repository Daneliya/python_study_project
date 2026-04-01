import os
from urllib.request import urlretrieve

import requests


def download_images(base_url, num, start, end):
    # 确保存储目录存在
    save_dir = num
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i in range(start, end + 1):
        # 动态拼接图片URL
        img_name = f'{num}jp-{i}.jpg'
        # full_img_url = urljoin(base_url + num + '/', img_name)
        full_img_url = base_url + num + img_name
        print(full_img_url)

        try:
            # 发送HTTP请求获取页面内容
            response = requests.get(full_img_url, stream=True)
            response.raise_for_status()  # 检查请求是否成功

            # 下载图片到指定目录
            # img_path = os.path.join(save_dir, img_name)
            img_path = save_dir + img_name
            urlretrieve(full_img_url, img_path)
            print(f'Successfully downloaded {img_name}')
        except requests.RequestException as e:
            print(f'Failed to download {img_name}: {e}')

        # try:
        #     # 发送HTTP请求获取页面内容
        #     response = requests.get(full_img_url, stream=True)
        #     response.raise_for_status()  # 检查请求是否成功
        #
        #     # 下载图片到指定目录
        #     img_path = os.path.join(save_dir, img_name)
        #     with open(img_path, 'wb') as f:
        #         f.write(response.content)
        #     print(f'Successfully downloaded {img_name}')
        # except requests.RequestException as e:
        #     print(f'Failed to download {img_name}: {e}')


if __name__ == '__main__':
    # 基础链接和编号
    # https://pics.dmm.co.jp/digital/video/juq00688/juq00688jp-3.jpg
    base_url = 'https://pics.dmm.co.jp/digital/video'
    # num = '/juq00688'
    # num = '/juq00757'
    num = '/ipzz00428'

    # 循环拼接链接并下载图片，这里是从1到10
    download_images(base_url, num, 1, 10)
