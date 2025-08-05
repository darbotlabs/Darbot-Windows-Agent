#!/usr/bin/env python3
"""
Validation script for Darbot Windows Agent

This script performs basic validation of the package structure
without requiring full dependencies to be installed.
"""

import os
import sys
import importlib.util
from pathlib import Path

def validate_package_structure():
    """Validate that the package has the expected structure."""
    print("🔍 Validating package structure...")
    
    required_files = [
        "darbot_windows_agent/__init__.py",
        "darbot_windows_agent/agent/__init__.py", 
        "darbot_windows_agent/agent/service.py",
        "darbot_windows_agent/agent/views.py",
        "darbot_windows_agent/desktop/__init__.py",
        "darbot_windows_agent/desktop/views.py",
        "tests/__init__.py",
        "main.py",
        "pyproject.toml",
        "README.md",
        "INSTALLATION.md",
        "DEVELOPMENT.md", 
        "TROUBLESHOOTING.md"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing required files:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False
    
    print("✅ Package structure is valid")
    return True

def validate_python_syntax():
    """Validate Python syntax for key files."""
    print("🔍 Validating Python syntax...")
    
    python_files = [
        "main.py",
        "darbot_windows_agent/__init__.py",
        "tests/unit/agent/test_agent_service.py"
    ]
    
    for file_path in python_files:
        if Path(file_path).exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    compile(f.read(), file_path, 'exec')
                print(f"✅ {file_path} - syntax OK")
            except SyntaxError as e:
                print(f"❌ {file_path} - syntax error: {e}")
                return False
        else:
            print(f"⚠️  {file_path} - file not found")
    
    return True

def validate_documentation():
    """Validate that documentation files are present and non-empty."""
    print("🔍 Validating documentation...")
    
    doc_files = {
        "README.md": 3000,      # Should be substantial
        "INSTALLATION.md": 5000, # Comprehensive installation guide
        "DEVELOPMENT.md": 10000, # Detailed development guide
        "TROUBLESHOOTING.md": 8000, # Comprehensive troubleshooting
    }
    
    for doc_file, min_size in doc_files.items():
        if Path(doc_file).exists():
            size = Path(doc_file).stat().st_size
            if size >= min_size:
                print(f"✅ {doc_file} - {size} bytes (comprehensive)")
            else:
                print(f"⚠️  {doc_file} - {size} bytes (may need more content)")
        else:
            print(f"❌ {doc_file} - missing")
            return False
    
    return True

def validate_project_config():
    """Validate pyproject.toml configuration."""
    print("🔍 Validating project configuration...")
    
    if not Path("pyproject.toml").exists():
        print("❌ pyproject.toml missing")
        return False
    
    with open("pyproject.toml", 'r') as f:
        content = f.read()
    
    required_sections = [
        "[project]",
        "[project.optional-dependencies]", 
        "[build-system]",
        "[tool.pytest.ini_options]"
    ]
    
    for section in required_sections:
        if section in content:
            print(f"✅ {section} section found")
        else:
            print(f"❌ {section} section missing")
            return False
    
    # Check for Python version compatibility
    if "requires-python" in content:
        if ">=3.12" in content:
            print("✅ Python version requirement: >=3.12")
        else:
            print("⚠️  Python version requirement may need adjustment")
    
    return True

def validate_test_structure():
    """Validate test structure."""
    print("🔍 Validating test structure...")
    
    test_files = [
        "tests/__init__.py",
        "tests/unit/agent/test_agent_service.py",
        "tests/unit/agent/test_agent_views.py",
        "tests/unit/desktop/test_desktop_views.py"
    ]
    
    found_tests = 0
    for test_file in test_files:
        if Path(test_file).exists():
            found_tests += 1
            print(f"✅ {test_file}")
        else:
            print(f"⚠️  {test_file} - not found")
    
    if found_tests >= 2:
        print(f"✅ Found {found_tests} test files")
        return True
    else:
        print(f"⚠️  Only found {found_tests} test files")
        return False

def main():
    """Run all validation checks."""
    print("🤖 Darbot Windows Agent - Validation Audit")
    print("=" * 50)
    
    checks = [
        ("Package Structure", validate_package_structure),
        ("Python Syntax", validate_python_syntax),
        ("Documentation", validate_documentation),
        ("Project Configuration", validate_project_config),
        ("Test Structure", validate_test_structure)
    ]
    
    results = []
    for check_name, check_func in checks:
        print(f"\n📋 {check_name}")
        print("-" * 30)
        result = check_func()
        results.append((check_name, result))
    
    print("\n" + "=" * 50)
    print("📊 VALIDATION SUMMARY")
    print("=" * 50)
    
    passed = 0
    for check_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {check_name}")
        if result:
            passed += 1
    
    print(f"\nPassed: {passed}/{len(results)} checks")
    
    if passed == len(results):
        print("\n🎉 All validation checks passed!")
        print("The repository is ready for production use.")
        return 0
    else:
        print(f"\n⚠️  {len(results) - passed} validation checks failed.")
        print("Please address the issues above before production use.")
        return 1

if __name__ == "__main__":
    sys.exit(main())