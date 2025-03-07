# Schedule Minder User Guide

## Overview
Schedule Minder is a desktop application that helps you track multiple schedules in real-time. It's particularly useful for schools, businesses, or any organization that needs to monitor different schedule types simultaneously.

## Main Window
![Main Window](images/main_window.png)

The main window displays three schedule types:
- Regular Schedule
- Two Hour Delay
- Homeroom Schedule

Each schedule shows the current period or status (e.g., "Period 1", "Before School", "After School").

## Basic Features

### System Tray
- The application runs in the system tray for easy access
- Click the tray icon to show/hide the window
- Hover over the tray icon to see current schedule status
- Right-click for quick menu options

### Window Sizes
Three window sizes are available:
- Small (305x230)
- Medium (445x355)
- Large (675x555)

## Admin Features
Access these features through the Tools menu (password required).

### Schedule Editor
1. Go to Tools > Schedule Editor
2. Enter admin password
3. Select a schedule to edit
4. Modify schedule properties:
   - Schedule name
   - Period names
   - Start/end times
5. Click Save to apply changes

### Color Settings
1. Go to Tools > Color Settings
2. Customize:
   - Window Background
   - Window Text
   - Message Background
   - Message Text
3. Use "Reset to Default" to restore original colors

### Test Mode
1. Go to Tools > Enable Test Mode
2. Enter admin password
3. Features available:
   - Manual time setting
   - Test file loading
   - Automated time progression
   - Adjustable delay between times

### Message Customization
Schedule Minder allows you to customize the messages displayed for different schedule situations:

#### Accessing Message Settings
1. Go to Tools > Message Settings
2. You can customize messages for:
   - Before Schedule
   - During Event
   - Between Events
   - After Schedule

#### Message Placeholders
When customizing messages, you can use these placeholders:
- During Event: Use `{event_name}` to show the current event name
- Between Events: Use `{prev_event}` and `{next_event}` to show the transitioning events

#### Example Messages
- Before Schedule: "School starts soon"
- During Event: "Now in {event_name}"
- Between Events: "Moving from {prev_event} to {next_event}"
- After Schedule: "School day complete"

#### Resetting Messages
Click "Reset to Default" in the Message Settings dialog to restore the original messages:
- Before Schedule: "Before Schedule"
- During Event: "{event_name}"
- Between Events: "{prev_event} → {next_event}"
- After Schedule: "After Schedule"

## Keyboard Shortcuts
- `Alt+F4`: Exit application
- `Esc`: Minimize to tray

## Troubleshooting

### Common Issues
1. Window not appearing
   - Check system tray
   - Click tray icon to show

2. Schedule not updating
   - Check if test mode is enabled
   - Verify schedule times in editor

3. Colors reset unexpectedly
   - Check write permissions
   - Try running as administrator

### Error Messages
- "Invalid Time": Enter time in HH:MM format
- "Incorrect Password": Verify admin password
- "Failed to save schedules": Check file permissions

## Best Practices
1. Regular backups of schedule data
2. Test schedule changes before implementation
3. Use descriptive event names
4. Maintain consistent time formats (HH:MM)

## Support
For additional support:
- Check documentation
- Contact system administrator
- Email info@fragillidaesoftware.com 