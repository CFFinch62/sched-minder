import os
from constants import TEST_FILES_DIR

class TestFileHelper:
    @staticmethod
    def get_test_file_path(file_name):
        return os.path.join(TEST_FILES_DIR, file_name)
    
    @staticmethod
    def get_available_test_files():
        """Returns a list of available test files"""
        return [f for f in os.listdir(TEST_FILES_DIR) if f.endswith('_time_test.txt')] 