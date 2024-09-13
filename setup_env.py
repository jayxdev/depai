import os
import yaml
import logging
from utils.env_setup import create_virtualenv, install_dependencies
from utils.dependency_checker import check_outdated_packages
from utils.ai_dependency_resolver import resolve_conflicts, suggest_dependency_versions

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config('config/config.yaml')
    requirements_file = config['requirements_file']
    env_name = config['env_name']

    if not os.path.exists(requirements_file):
        logging.error("%s not found.", requirements_file)
        return

    create_virtualenv(env_name)
    install_dependencies(env_name, requirements_file)
    resolve_conflicts(env_name)
    check_outdated_packages(env_name)

if __name__ == "__main__":
    main()