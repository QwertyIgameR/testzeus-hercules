import os
from testzeus_hercules.config import get_global_conf
from dotenv import load_dotenv

# Force load .env manually first to see if that works
print("--- Manually loading .env ---")
load_dotenv(".env", verbose=True, override=True)
print(f"AGENTS_LLM_CONFIG_FILE from os.environ: {os.environ.get('AGENTS_LLM_CONFIG_FILE')}")

print("\n--- Using testzeus_hercules.config ---")
conf = get_global_conf()
config_file = conf.get("AGENTS_LLM_CONFIG_FILE")
print(f"AGENTS_LLM_CONFIG_FILE from config: {config_file}")

if config_file:
    print(f"File exists check: {os.path.exists(config_file)}")
    if os.path.exists(config_file):
        print(f"Absolute path: {os.path.abspath(config_file)}")
else:
    print("Config file var is None or Empty")
