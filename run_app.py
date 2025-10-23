#!/usr/bin/env python3
"""
Real Estate Analytics Platform Launcher
This script ensures the application runs without any path errors
"""

import os
import sys
import subprocess

def main():
    print("🏠 Real Estate Analytics Platform")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists('app/Home.py'):
        print("❌ Error: app/Home.py not found!")
        print("Please run this script from the project root directory:")
        print("C:\\Users\\SAMAR\\OneDrive\\Desktop\\real-estate-Main")
        input("Press Enter to exit...")
        return
    
    # Check if virtual environment exists
    if not os.path.exists('venv'):
        print("⚠️  Warning: Virtual environment not found!")
        print("Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'])
    
    # Activate virtual environment and install dependencies
    print("📦 Installing dependencies...")
    if os.name == 'nt':  # Windows
        activate_script = 'venv\\Scripts\\activate.bat'
        pip_path = 'venv\\Scripts\\pip.exe'
    else:  # Unix/Linux/Mac
        activate_script = 'venv/bin/activate'
        pip_path = 'venv/bin/pip'
    
    # Install requirements
    try:
        subprocess.run([pip_path, 'install', '-r', 'requirements.txt'], check=True)
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Error installing dependencies!")
        return
    
    # Start Streamlit
    print("🚀 Starting Real Estate Analytics Platform...")
    print("📍 Application will open in your browser at: http://localhost:8501")
    print("=" * 40)
    
    try:
        subprocess.run(['streamlit', 'run', 'app/Home.py'])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")

if __name__ == "__main__":
    main()
