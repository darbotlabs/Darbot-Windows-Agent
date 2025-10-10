# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **GitHub Pages Documentation Site** - Comprehensive interactive documentation with retro cyber modern fluent design
  - Responsive design with mobile support
  - Interactive terminal animations and code examples
  - Searchable FAQ section with accordion UI
  - Complete API reference with all tools documented
  - Live demo videos with UI grounding examples
  - Architecture diagrams showing system design
  - AutoGen 2.0 (ag2ai) principles integration
  - Copy-to-clipboard functionality for code snippets
- GitHub Actions workflow for automatic documentation deployment
- Jekyll configuration for GitHub Pages
- Enhanced README with link to documentation site
- ENHANCEMENTS.md documenting improvements and best practices
- Comprehensive documentation suite (INSTALLATION.md, DEVELOPMENT.md, TROUBLESHOOTING.md)
- Enhanced README with professional polish and structure
- FAQ section with common questions and answers
- Robust main.py with graceful dependency checking and user guidance
- Development tooling configuration (pytest, ruff, mypy, black)
- .gitignore file for proper repository management
- Validation script for end-to-end functionality testing

### Changed
- Python version requirement updated from 3.13+ to 3.12+ for broader compatibility
- README structure enhanced with table of contents and clear sections
- Project metadata and branding improved for production use
- Error handling in main.py improved with helpful user messages
- Badge styling updated for consistent visual presentation

### Fixed
- Dependency issues with live-inspect package removed
- Emoji encoding issues in README resolved
- Build configuration updated for proper package management

### Removed
- live-inspect dependency that was causing installation failures

## [0.5.0] - Previous Release

### Added
- Initial agent implementation with LangChain integration
- Desktop automation capabilities using UI Automation
- Support for multiple LLM providers (Google Gemini, OpenAI, Groq, Ollama)
- Basic testing infrastructure
- Core agent tools for Windows automation

### Features
- GUI-level Windows interaction without computer vision dependencies
- Fast response times (1.5-2.3 seconds per action)
- Extensible tool system for custom automation
- Integration with popular LLM providers
- MIT license for commercial use

---

## Release Notes Format

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security improvements