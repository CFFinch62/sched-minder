# Schedule Minder Configuration Guide

## Overview
Schedule Minder can be customized through various configuration files and settings. This guide explains all available configuration options.

## Schedule Configuration

### Location
The schedule configuration file is located at:
```
data/schedules.json
```

### Format
```json
{
    "organization_name": {
        "schedule_1": {
            "name": "Regular Schedule",
            "events": [
                {
                    "name": "Warning Bell",
                    "start": "07:20",
                    "end": "07:25",
                    "minutes": 5
                },
                {
                    "name": "Period 1",
                    "start": "07:25",
                    "end": "08:11",
                    "minutes": 46
                }
            ]
        },
        "schedule_2": {
            "name": "Two Hour Delay",
            "events": []
        },
        "schedule_3": {
            "name": "Homeroom Schedule",
            "events": []
        }
    }
}
```

### Schedule Properties
- `name`: Display name for the schedule
- `events`: Array of event objects
  - `name`: Event identifier
  - `start`: Start time (HH:MM format)
  - `end`: End time (HH:MM format)
  - `minutes`: Duration in minutes

## Application Settings

### Color Configuration
Colors can be configured through the UI or directly in settings:

```json
{
    "window_bg_color": "#000000",
    "window_text_color": "#FFFFFF",
    "message_bg_color": "#000066",
    "message_text_color": "#FFFFFF"
}
```

### Window Sizes
Available window size presets:
```python
WINDOW_SIZES = {
    'small': QSize(305, 230),
    'medium': QSize(445, 355),
    'large': QSize(675, 555),
    'test_mode': QSize(385, 320)
}
```

### Admin Settings
- Default password: `chucksoft`
- Password storage: Encrypted in settings file
- Change via Tools > Change Admin Password

### Message Configuration
Messages can be configured through the UI or directly in settings:

```json
{
    "messages/before_schedule": "Before Schedule",
    "messages/during_event": "{event_name}",
    "messages/between_events": "{prev_event} → {next_event}",
    "messages/after_schedule": "After Schedule"
}
```

#### Message Placeholders
- `{event_name}`: Current event name
- `{prev_event}`: Previous event name
- `{next_event}`: Next event name

#### Default Messages
Default messages are defined in constants.py:
```python
DEFAULT_MESSAGES = {
    "before_schedule": "Before Schedule",
    "during_event": "{event_name}",
    "between_events": "{prev_event} → {next_event}",
    "after_schedule": "After Schedule"
}
```

## File Locations

### Application Data
```
data/
├── schedules.json    # Schedule definitions
└── about.json       # Application information
```

### Assets
```
assets/
├── icons/           # Application icons
├── images/          # UI images
└── test_files/      # Test schedule files
```

## Test Mode Configuration

### Test Files Format
Create text files in `assets/test_files/` with times to test:
```
07:20  # First event start
07:25  # Event transition
07:30  # Second event start
```

### Test Mode Settings
- Delay between times: 1-60 seconds
- Auto-advance option
- Manual time entry

### Tooltip Format
```
Current Time: HH:MM (MODE)
Regular: Current Event     # Changed from Current Period
2-Hour Delay: Current Event
Homeroom: Current Event
```

## System Tray Integration

### Icon Configuration
- Default: `assets/icons/clock.png`
- Custom icons supported (PNG, ICO)
- Change via Tools > Change Tray Icon

## Performance Settings

### Update Intervals
- Period check: Every 60 seconds
- UI refresh: Every 1000ms
- Test mode: User-defined

### Memory Usage
- Minimum: 50MB
- Recommended: 100MB
- Maximum: System dependent

## Backup and Recovery

### Backup Locations
```
data/backups/
├── schedules_YYYY-MM-DD.json
└── settings_YYYY-MM-DD.json
```

### Auto-save Features
- Schedule changes
- Color settings
- Window position
- Last used size

## Troubleshooting

### Configuration Reset
To reset all settings:
1. Close application
2. Delete settings file
3. Restart application

### File Permissions
Required permissions:
- Read/Write: data directory
- Read: assets directory
- Execute: main.py

## Advanced Configuration

### Environment Variables
```bash
SCHEDULE_MINDER_DEBUG=1    # Enable debug logging
SCHEDULE_MINDER_TEST=1     # Force test mode
SCHEDULE_MINDER_NO_TRAY=1  # Disable system tray
```

### Command Line Arguments
```bash
python main.py --debug     # Enable debug mode
python main.py --test      # Start in test mode
python main.py --help      # Show all options
``` 