import json
from constants import ABOUT_FILE

class AboutManager:
    def __init__(self):
        self.about_info = self.load_about_info()
        
    def load_about_info(self):
        """Load about information from JSON file"""
        try:
            with open(ABOUT_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading about info: {e}")
            # Return default values if file can't be loaded
            return {
                "app_name": "Schedule Minder",
                "version": "1.05",
                "company": "Fragillidae Software",
                "author": "Chuck Finch",
                "website": "www.fragillidaesoftware.com",
                "logo_file": "schedule_minder.jpg"
            } 