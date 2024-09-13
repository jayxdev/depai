import os
import subprocess

def check_outdated_packages(env_name):
	pip_path = os.path.join(env_name, 'Scripts', 'pip')
	result = subprocess.run([pip_path, 'list', '--outdated'], capture_output=True, text=True)
	print("Outdated packages:\n", result.stdout)