from PIL import Image, ImageSequence

# 打开GIF文件
img = Image.open('smoking0man3.gif')
# 获取图像大小
width, height = img.size
# 新的画布大小
new_width = width * 3
new_height = height * 3

# 创建一个透明背景的新图像
new_img = Image.new('RGBA', (new_width, new_height), (38, 52, 76))

# 计算旧图像在新画布上的位置
offset = ((new_width - img.width) // 2, (new_height - img.height) // 2)

frames = []

# 遍历GIF的每一帧
for frame in ImageSequence.Iterator(img):
    # 创建一个透明背景的新帧
    new_frame = new_img.copy()
    # 将旧帧粘贴到新帧上
    new_frame.paste(frame, offset)
    # 从上到下的宽度的坐标，即左下角的纵坐标
    axis_width = offset[1] + width
    # 剪切图像
    cropped_frame = new_frame.crop((0, offset[0], new_height, offset[0] + width))
    frames.append(cropped_frame)

# 保存新的多帧GIF
frames[0].save('smoking0man3_with_background.gif', save_all=True, append_images=frames[1:], loop=0)
