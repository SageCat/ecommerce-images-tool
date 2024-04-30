import requests

# GitHub 用户名
username = 'SageCat'
# 仓库名
repository = 'noon-images'
# 分支名
branch = 'main'  # 或者其他分支名称
# 文件夹路径和产品类别
folder_path = 'images/noon/ToteBag/production'
product_category = 'Tote Bag'

# GitHub Raw 地址模板
raw_url_template = f'https://raw.githubusercontent.com/{username}/{repository}/{branch}/{folder_path}/'

# 获取文件夹内容
response = requests.get(f'https://api.github.com/repos/{username}/{repository}/contents/{folder_path}')
data = response.json()

# 遍历文件夹内容
for item in data:
    if item['type'] == 'file':
        file_name = item['name']
        if file_name.lower().endswith('.jpg'):
            # 获取图片链接
            image_link = (raw_url_template + file_name).replace(' ', '%20')
            line = product_category + ',' + file_name + ',' + image_link
            with open('share_links.csv', 'a') as f:
                f.writelines(line + '\n')
                print(line)
