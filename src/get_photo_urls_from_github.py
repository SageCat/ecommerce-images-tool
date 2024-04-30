import requests
import globals


# GitHub Raw 地址模板
raw_url_template = (f'https://raw.githubusercontent.com/{globals.USERNAME}/{globals.IMAGES_REPOSITORY}/'
                    f'{globals.IMAGES_REPOSITORY_BRANCH}/{globals.PRODUCT_IMAGE_FOLDER_PATH}/')

# 获取文件夹内容
response = requests.get(
    f'https://api.github.com/repos/{globals.USERNAME}/{globals.IMAGES_REPOSITORY}/'
    f'contents/{globals.PRODUCT_IMAGE_FOLDER_PATH}')
data = response.json()

# 遍历文件夹内容
for item in data:
    if item['type'] == 'file':
        file_name = item['name']
        if file_name.lower().endswith('.jpg'):
            # 获取图片链接
            image_link = (raw_url_template + file_name).replace(' ', '%20')
            line = globals.PRODUCT_CATEGORY + ',' + file_name + ',' + image_link
            with open(globals.CSV_FILE, 'a') as f:
                f.writelines(line + '\n')
                print(line)
