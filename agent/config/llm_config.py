"""
LLM configuration loaded from environment.

This module reads values from environment variables (and attempts to load
`agent/.env` via python-dotenv if available). Defaults match the previous
hard-coded values. Do NOT commit real tokens to public repositories.
"""

import os
import pathlib

try:
	# Load agent/.env if python-dotenv is installed
	from dotenv import load_dotenv  # type: ignore
	env_path = pathlib.Path(__file__).resolve().parent.parent / ".env"
	load_dotenv(dotenv_path=str(env_path))
except Exception:
	# dotenv is optional; we'll fall back to existing environment variables
	pass


def _as_bool(value, default=False):
	if value is None:
		return default
	return str(value).strip().lower() in ("1", "true", "yes", "y", "on")


# Core flags
LLM_ENABLED = _as_bool(os.getenv("LLM_ENABLED"), default=True)

# Hugging Face / model settings
HF_API_TOKEN = os.getenv("HF_API_TOKEN", "")
HF_MODEL = os.getenv("HF_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")
HF_API_URL = os.getenv(
	"HF_API_URL", f"https://api-inference.huggingface.co/models/{HF_MODEL}"
)

# Generation parameters
try:
	TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))
except ValueError:
	TEMPERATURE = 0.2

try:
	MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", "200"))
except ValueError:
	MAX_NEW_TOKENS = 200

try:
	TIMEOUT_SECONDS = int(os.getenv("TIMEOUT_SECONDS", "60"))
except ValueError:
	TIMEOUT_SECONDS = 60

