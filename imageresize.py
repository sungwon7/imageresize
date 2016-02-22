#!/usr/bin/env python
# coding: utf-8
"""
    Image Resize
    ~~~~~~
    이미지믈 입력받아 사이즈 변환하는 모듈
"""

import os.path
import uuid
from PIL import Image

IMAGE_SIZE = (((320,200), (640,480), (800,600)),((200,320), (480,640), (600,800)))

def resize(file_name, outpath, result):

	"""Image resize

    Keyword arguments:
    file_name -- file full path
    outpath   -- image resize save path
    result    -- thumbnail list [ { } , ... ]

	Return:
		error  -- is error error msg (code, msg)
    """
	error    = (0, 'OK')

	if not os.path.exists( file_name ):
		return (-100, "Not Found file: {}".format(file_name))

	im = None
	try :
		im = Image.open(file_name)
	except:
		return (-200, 'Cannot identify image file')

	(x,y) = im.size

	hash_file_name = str(uuid.uuid4()).replace("-",'')
	max_length     = max(x, y)
	# print max_length, hash_file_name

	cur_image_size = IMAGE_SIZE[0]

	if x < y:
		cur_image_size = IMAGE_SIZE[1]

	if max_length > 320:
		# 320x240 or 240x320
		thumbnail     = im.resize( cur_image_size[0] )
		out_file_name = "{}_{}_{}.png".format(hash_file_name, cur_image_size[0][0], cur_image_size[0][1])
		out_full_path = os.path.join(outpath, out_file_name)
		thumbnail.save(out_full_path, "PNG")

		file_info             = {}
		file_info['width']    = cur_image_size[0][0]
		file_info['height']   = cur_image_size[0][1]
		file_info['filename'] = out_file_name
		result.append(file_info)

	if max_length > 640:
		# 640x480 or 480x640
		thumbnail     = im.resize( cur_image_size[1] )
		out_file_name = "{}_{}_{}.png".format(hash_file_name, cur_image_size[1][0], cur_image_size[1][1])
		out_full_path = os.path.join(outpath, out_file_name)
		thumbnail.save(out_full_path, "PNG")

		file_info             = {}
		file_info['width']    = cur_image_size[1][0]
		file_info['height']   = cur_image_size[1][1]
		file_info['filename'] = out_file_name
		result.append(file_info)

	if max_length > 800:
		# 800x600 or 600x800
		thumbnail     = im.resize( cur_image_size[2] )
		out_file_name = "{}_{}_{}.png".format(hash_file_name, cur_image_size[2][0], cur_image_size[2][1])
		out_full_path = os.path.join(outpath, out_file_name)
		thumbnail.save(out_full_path, "PNG")

		file_info             = {}
		file_info['width']    = cur_image_size[2][0]
		file_info['height']   = cur_image_size[2][1]
		file_info['filename'] = out_file_name
		result.append(file_info)

	return error

def main():
	# resize('./test/1024_768.png', None, None)
	print resize('./test/768_1024.jpg', "./out", None)

if __name__ == '__main__':
	main()
