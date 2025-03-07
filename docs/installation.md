# Schedule Minder Installation Guide

## System Requirements

### Minimum Requirements
- Python 3.8 or higher
- 100MB free disk space
- 2GB RAM
- Display resolution: 1024x768 or higher

### Supported Operating Systems
- Windows 10/11
- Linux (Ubuntu 20.04+, Fedora 34+)
- macOS 10.15+

## Basic Installation

### Windows Installation
1. Install Python:
   - Download Python from [python.org](https://python.org)
   - Check "Add Python to PATH" during installation
   
2. Install Schedule Minder:
   ```cmd
   git clone https://github.com/your-repo/schedule-minder.git
   cd schedule-minder
   pip install PyQt6
   ```

3. Run the application:
   ```cmd
   python main.py
   ```

### Linux Installation
1. Install Python and dependencies:
   ```bash
   sudo apt update  # Ubuntu/Debian
   sudo apt install python3 python3-pip python3-venv
   ```

2. Install Schedule Minder:
   ```bash
   git clone https://github.com/your-repo/schedule-minder.git
   cd schedule-minder
   pip3 install PyQt6
   ```

3. Run the application:
   ```bash
   python3 main.py
   ```

### macOS Installation
1. Install Python:
   - Download Python from [python.org](https://python.org)
   - Or use Homebrew: `brew install python`

2. Install Schedule Minder:
   ```bash
   git clone https://github.com/your-repo/schedule-minder.git
   cd schedule-minder
   pip3 install PyQt6
   ```

3. Run the application:
   ```bash
   python3 main.py
   ```

## Development Installation

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Troubleshooting Installation

### Common Issues

1. PyQt6 Installation Fails
   ```bash
   # Windows solution
   pip install --upgrade pip
   pip install PyQt6 --force-reinstall
   
   # Linux solution
   sudo apt install python3-pyqt6
   ```

2. Permission Errors
   ```bash
   # Linux/macOS
   sudo chown -R $USER:$USER .
   chmod +x main.py
   ```

3. Missing Dependencies
   ```bash
   # Linux
   sudo apt install python3-dev build-essential
   ```

## Post-Installation Setup

1. Configure data directory:
   ```bash
   mkdir -p data
   cp example_schedules.json data/schedules.json
   ```

2. Set up logging (optional):
   ```bash
   mkdir logs
   touch logs/schedule_minder.log
   ```

## Updating Schedule Minder

1. Pull latest changes:
   ```bash
   git pull origin main
   ```

2. Update dependencies:
   ```bash
   pip install -r requirements.txt --upgrade
   ```

## Security Considerations
- Change default admin password after installation
- Set appropriate file permissions
- Back up schedule data regularly

## Getting Help
- Check the [User Guide](user_guide.md)
- Visit our [GitHub Issues](https://github.com/your-repo/schedule-minder/issues)
- Contact support@fragillidaesoftware.com 