import yaml
import argparse

def validate_config(config_path):
    """Validates the YAML configuration file."""
    try:
        with open(config_path, 'r') as f:
            yaml.safe_load(f)
        print(f"Configuration file {config_path} is valid.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate a YAML configuration file.")
    parser.add_argument("--config", required=True, help="Path to the configuration file.")
    args = parser.parse_args()
    validate_config(args.config)
