import os
import subprocess
import logging
import joblib
import pandas as pd
from utils.env_setup import create_virtualenv, install_dependencies
from utils.dependency_checker import check_outdated_packages
from utils.ai_dependency_resolver import resolve_conflicts, suggest_dependency_versions


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the trained model
model = joblib.load('dependency_resolver_model.pkl')

def resolve_conflicts(env_name):
	pip_path = os.path.join(env_name, 'Scripts', 'pip')
	result = subprocess.run([pip_path, 'check'], capture_output=True, text=True)
	conflicts = result.stdout

	if conflicts:
		logging.info("Dependency conflicts detected:\n%s", conflicts)
		# Extract dependencies and conflicts
		conflicts_list = conflicts.split('\n')
		for conflict in conflicts_list:
			if conflict:
				dep, conf = conflict.split(' ', 1)
				suggestion = suggest_dependency_versions(dep, conf)
				if suggestion:
					logging.info("Suggested resolution: %s", suggestion)
					subprocess.run([pip_path, 'install', suggestion])
				else:
					logging.warning("No known resolution found. Please resolve manually.")
	else:
		logging.info("No dependency conflicts detected.")

def suggest_dependency_versions(dependency, conflict):
	# Prepare the input data
	input_data = pd.DataFrame([[dependency + ' ' + conflict]], columns=['combined'])
	
	# Predict the resolution
	resolution = model.predict(input_data)
	return resolution[0] if resolution else None

def main():
	env_name = 'env'
	requirements_file = 'requirements.txt'

	if not os.path.exists(requirements_file):
		logging.error("%s not found.", requirements_file)
		return

	create_virtualenv(env_name)
	install_dependencies(env_name, requirements_file)
	resolve_conflicts(env_name)
	check_outdated_packages(env_name)

if __name__ == "__main__":
	main()