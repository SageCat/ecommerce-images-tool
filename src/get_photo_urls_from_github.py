import requests
import globals
import transpose_urls as tu
import pandas as pd


def delete_csv_existing_rows(filename, **conditions):
    """
    :param filename:
    :param conditions:
    :return:
    """
    df = pd.read_csv(filename)
    original_rows_count = len(df)
    mask = pd.Series(True, index=df.index)
    for key, value in conditions.items():
        if value is not None:
            mask = mask & (df[key] == value)
    # 删除满足条件的行，即已有的数据
    df = df[~mask]
    current_rows_count = len(df)
    df.to_csv(filename, index=False)
    if current_rows_count < original_rows_count:
        print(f'========= {original_rows_count - current_rows_count} rows have been deleted! ==========')
    elif current_rows_count == original_rows_count:
        print(f'========= No data deleted! New data will be inserted! ==========')
    else:
        print(f'========= Unexpected value! ==========')


# GitHub Raw 地址模板
raw_url_template = (f'https://raw.githubusercontent.com/{globals.USERNAME}/{globals.IMAGES_REPOSITORY}/'
                    f'{globals.IMAGES_REPOSITORY_BRANCH}/{globals.PRODUCT_IMAGE_FOLDER_PATH}/')

# 获取文件夹内容
response = requests.get(
    f'https://api.github.com/repos/{globals.USERNAME}/{globals.IMAGES_REPOSITORY}/'
    f'contents/{globals.PRODUCT_IMAGE_FOLDER_PATH}')
data = response.json()

# 先根据条件删除已有数据
delete_csv_existing_rows(globals.CSV_FILE, ProductCategory=globals.PRODUCT_CATEGORY,
                         PhotoName=globals.PRODUCT_PHOTO_NAME, Link=globals.PRODUCT_LINK)

# 遍历文件夹内容并将新的数据写入到文件
for item in data:
    if item['type'] == 'file':
        file_name = item['name']
        if file_name.lower().endswith('.jpg'):
            # 获取图片链接
            image_link = (raw_url_template + file_name).replace(' ', '%20')
            line = globals.PRODUCT_CATEGORY + ',' + file_name + ',' + image_link
            with open(globals.CSV_FILE, 'a', encoding='utf-8') as f:
                f.writelines(line + '\n')
                print(line)

# 转置并输出数据到excel文件
tu.transpose(globals.PRODUCT_CATEGORY, globals.SINGLE_PRODUCT_PHOTO_COUNT, globals.CSV_FILE).to_excel(
    f'../excel/NIS {globals.PRODUCT_CATEGORY} Photos URL.xlsx', index=False)
