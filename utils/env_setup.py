import os
import subprocess
import sys

def create_virtualenv(env_name):
	subprocess.run([sys.executable, '-m', 'venv', env_name])

def install_dependencies(env_name, requirements_file):
	pip_path = os.path.join(env_name, 'Scripts', 'pip')
	subprocess.run([pip_path, 'install', '-r', requirements_file])