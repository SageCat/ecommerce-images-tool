import os


def rename_files(directory):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            files_in_dir = [
                f
                for f in os.listdir(dir_path)
                if os.path.isfile(os.path.join(dir_path, f))
            ]
            if files_in_dir:
                files_in_dir.sort()
                for i, file in enumerate(files_in_dir, start=1):
                    file_name, file_ext = os.path.splitext(file)
                    new_file_name = f"{i:02d}{file_ext}"
                    old_file_path = os.path.join(dir_path, file)
                    new_file_path = os.path.join(dir_path, new_file_name)
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {old_file_path} -> {new_file_path}")


# 在当前目录下递归查找文件
current_directory = r"C:\Users\Sage\Pictures\手机壳"
rename_files(current_directory)
