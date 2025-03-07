# Schedule loading, saving, and period calculations 

import json
from datetime import datetime
from constants import SCHEDULES_FILE, REGULAR_SCHEDULE, DELAY_SCHEDULE, HOMEROOM_SCHEDULE
from utils.settings_manager import SettingsManager

class ScheduleManager:
    def __init__(self, schedule_file=None):
        self.schedule_file = schedule_file or SCHEDULES_FILE
        self.schedules = self.load_schedules()
        self.settings_manager = SettingsManager()
        self.messages = self.settings_manager.get_schedule_messages()
        
        # Ensure default schedules exist with names
        defaults = {
            'schedule_1': {'name': REGULAR_SCHEDULE, 'events': []},
            'schedule_2': {'name': DELAY_SCHEDULE, 'events': []},
            'schedule_3': {'name': HOMEROOM_SCHEDULE, 'events': []}
        }
        
        for key, default in defaults.items():
            if key not in self.schedules:
                self.schedules[key] = default.copy()
            elif 'name' not in self.schedules[key]:
                self.schedules[key]['name'] = default['name']
        
    def load_schedules(self):
        with open(self.schedule_file, 'r') as f:
            return json.load(f)['southampton_high_school']
            
    def save_schedules(self, schedules):
        with open(self.schedule_file, 'w') as f:
            json.dump({'southampton_high_school': schedules}, f, indent=4)
            
    def get_current_event(self, schedule_type, current_time=None):
        """Get the current event based on the time"""
        schedule_map = {
            REGULAR_SCHEDULE: 'schedule_1',
            DELAY_SCHEDULE: 'schedule_2',
            HOMEROOM_SCHEDULE: 'schedule_3'
        }
        
        schedule_key = schedule_map.get(schedule_type)
        if not schedule_key or schedule_key not in self.schedules:
            return "Not in Session"
            
        if current_time is None:
            current_time = datetime.now()
            
        if isinstance(current_time, str):
            try:
                current_time = datetime.strptime(current_time, "%H:%M")
            except ValueError:
                return "Invalid Time Format"
            
        current_time_str = current_time.strftime("%H:%M")
        
        schedule = self.schedules[schedule_key]
        if 'events' not in schedule:
            return "Schedule Not Configured"
        
        events = schedule['events']
        if not events:
            return "No Events Defined"
        
        # Before school check
        first_event = next((e for e in events if e.get('start')), None)
        if not first_event or current_time_str < first_event['start']:
            return self.messages['before_schedule']
        
        # During event check
        for event in events:
            start = event.get('start')
            end = event.get('end')
            
            if not start or not end:
                continue
                
            if start <= current_time_str <= end:
                return self.messages['during_event'].format(event_name=event['name'])
                
        # After school check
        last_event = next((e for e in reversed(events) if e.get('end')), None)
        if last_event and current_time_str > last_event['end']:
            return self.messages['after_schedule']
        
        # Between events check
        for i in range(len(events) - 1):
            current_end = events[i].get('end')
            next_start = events[i + 1].get('start')
            if (current_end and next_start and 
                current_end <= current_time_str <= next_start):
                return self.messages['between_events'].format(
                    prev_event=events[i]['name'],
                    next_event=events[i + 1]['name']
                )
        
        return "Not in Session" 