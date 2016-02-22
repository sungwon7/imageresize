#!/usr/bin/env python
# coding: utf-8

import unittest
import imageresize

class TestImageResize(unittest.TestCase):

	def test_nofile(self):
		""" 파일이 없는 경우 test """
		error = imageresize.resize('nofile', './upload', [])
		self.assertEqual(error[0], -100)

	def test_noimagefile(self):
		""" 이미지 파일이 아닌 경우 test """
		error = imageresize.resize('test.py', './upload', [])
		self.assertEqual(error[0], -200)

	def test_split(self):
  		""" image resize test """
 		result = []
  		error = imageresize.resize('./test/1024_768.png', './upload', result)
		self.assertEqual(error[0], 0)  		

if __name__ == '__main__':
    unittest.main()