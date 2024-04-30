from PIL import Image
import os

def resize_and_center_image(image_path, output_folder, target_size):
    # 打开图像
    image = Image.open(image_path)

    # 获取图像尺寸
    width, height = image.size

    # 如果图像是正方形且尺寸符合要求，则不做任何处理
    if width == height and width == target_size[0]:
        return

    # 计算缩放比例
    scale = min(target_size[0] / width, target_size[1] / height)

    # 调整图像大小
    new_width = int(width * scale)
    new_height = int(height * scale)
    resized_image = image.resize((new_width, new_height))

    # 创建新画布
    canvas = Image.new("RGB", target_size, "white")

    # 计算图像在画布上的位置
    x = (target_size[0] - new_width) // 2
    y = (target_size[1] - new_height) // 2

    # 将调整后的图像放置在画布上
    canvas.paste(resized_image, (x, y))

    # 确保目标文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 保存调整后的图像
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    canvas.save(output_path)

# 设置目标尺寸
target_size = (660, 900)

# 遍历当前目录下的所有文件
current_directory = r"C:\Users\Sage\PycharmProjects\noon-images\images\noon\ToteBag"
output_folder = os.path.join(current_directory, 'temp')
for filename in os.listdir(current_directory):
    filepath = os.path.join(current_directory, filename)
    if os.path.isfile(filepath) and filename.lower().endswith('.jpg'):
        resize_and_center_image(filepath, output_folder, target_size)

print("图片调整完成，已保存到temp文件夹中。")
