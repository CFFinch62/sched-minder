# Contributing to Schedule Minder

Thank you for your interest in contributing to Schedule Minder! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Use welcoming and inclusive language
- Be collaborative
- Accept constructive criticism gracefully

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/schedule-minder.git
   cd schedule-minder
   ```

3. Set up development environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements-dev.txt
   ```

## Development Process

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Code Style Guidelines
- Follow PEP 8 conventions
- Use meaningful variable and function names
- Add docstrings to all classes and methods
- Include type hints where appropriate
- Keep functions focused and small
- Comment complex logic

### 3. Testing
- Write tests for new features
- Update existing tests if needed
- Ensure all tests pass:
  ```bash
  python -m pytest tests/
  ```
- Check code coverage:
  ```bash
  python -m pytest --cov=src tests/
  ```

### 4. Documentation
- Update relevant documentation
- Add docstrings to new code
- Include examples where helpful
- Update README.md if needed

## Pull Request Process

1. Update your branch:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. Run quality checks:
   ```bash
   # Run tests
   python -m pytest tests/
   
   # Check code style
   flake8 .
   
   # Check type hints
   mypy .
   ```

3. Create pull request:
   - Use clear, descriptive title
   - Reference any related issues
   - Describe changes in detail
   - List any dependencies added

4. PR Checklist:
   - [ ] Tests added/updated
   - [ ] Documentation updated
   - [ ] Code follows style guidelines
   - [ ] All tests passing
   - [ ] No merge conflicts

## Reporting Issues

### Bug Reports
Include:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- System information
- Screenshots if relevant

### Feature Requests
Include:
- Clear description of feature
- Use case and benefits
- Possible implementation approach
- Any relevant examples

## Development Environment

### Recommended Tools
- VS Code or PyCharm
- Python 3.8+
- Git
- flake8
- mypy
- pytest

### VS Code Settings
```json
{
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.testing.pytestEnabled": true,
    "editor.rulers": [80],
    "editor.formatOnSave": true
}
```

## Project Structure
```
schedule-minder/
├── main.py              # Entry point
├── constants.py         # Global constants
├── windows/            # Window classes
├── dialogs/            # Dialog classes
├── utils/              # Utility classes
├── tests/              # Test files
└── docs/               # Documentation
```

## Common Tasks

### Adding a New Feature
1. Create feature branch
2. Add tests first (TDD)
3. Implement feature
4. Update documentation
5. Submit PR

### Fixing a Bug
1. Create fix branch
2. Add test to reproduce bug
3. Fix the bug
4. Verify fix with test
5. Submit PR

## Getting Help
- Check existing documentation
- Search closed issues
- Ask in discussions
- Contact maintainers

## License
By contributing, you agree that your contributions will be licensed under the project's MIT License. 