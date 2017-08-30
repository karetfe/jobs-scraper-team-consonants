#This is the database connection test which check if the connection is ok or not
#@input : MongoClient with ip address, port and database connection name
#@output: True or False

import unittest
import sys
import pymongo

from mock import patch
from database import *
patch('pymongo.MongoClient')

class TestDBConnection(unittest.TestCase):

	def testdbconnection(self):
		try :
			self.client = MongoClient('localhost', 27017)
			self.conn = self.client['thinkit']
		except Exception:
			print 'Database connection test!'
			return False
		return True

if __name__ == '__main__':
	unittest.main()
