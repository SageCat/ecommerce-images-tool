import os
import shutil


def copy_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # 获取所有层的目录名（从下一级目录开始）
            dirs_path = root.split(os.path.sep)[1:]
            # 构建新文件名
            new_file_name = "_".join(dirs_path[4:] + [file])
            new_file_path = os.path.join(directory, new_file_name)
            # 复制文件
            shutil.copyfile(file_path, new_file_path)
            print(f"Copied: {file_path} -> {new_file_path}")


# 在当前目录下递归查找文件并复制到当前目录
current_directory = r"C:\Users\Sage\Pictures\手机壳"
copy_files(current_directory)
