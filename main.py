from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# 载入服务账号凭据
creds = Credentials.from_service_account_file('credentials.json')

# 创建 Google Drive 服务
drive_service = build('drive', 'v3', credentials=creds)

# 要获取链接的文件夹的 ID
folder_id = '1HjDT-yHnGB39-eINi0P2tJhR_YHShabr'

# 获取文件夹内的所有文件
results = drive_service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name)").execute()
files = results.get('files', [])

# 遍历文件并获取分享链接
for file in files:
    file_id = file.get('id')
    file_name = file.get('name')
    # 获取文件的分享链接
    response = drive_service.files().get(fileId=file_id, fields='webViewLink').execute()
    link = response.get('webViewLink')
    print(f"File Name: {file_name}, Share Link: {link}")
