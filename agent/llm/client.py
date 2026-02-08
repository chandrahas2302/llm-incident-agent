import logging
import requests
from agent.config.llm_config import (
    LLM_ENABLED,
    HF_API_TOKEN,
    HF_API_URL,
    TEMPERATURE,
    MAX_NEW_TOKENS,
    TIMEOUT_SECONDS,
)

log = logging.getLogger("agent.llm")


class LLMClient:
    def __init__(self):
        # Never block app startup
        self.enabled = bool(LLM_ENABLED and HF_API_TOKEN)

        log.info(
            "LLMClient initialized | enabled=%s | endpoint=%s",
            self.enabled,
            HF_API_URL if self.enabled else "disabled"
        )

        self.headers = (
            {"Authorization": f"Bearer {HF_API_TOKEN}"}
            if self.enabled
            else {}
        )

    def ask(self, prompt: str) -> dict:
        # Hard safety gate
        if not self.enabled:
            log.warning("LLM skipped: disabled or token missing")
            return {
                "enabled": False,
                "suggested_action": None,
                "explanation": "LLM disabled or token missing"
            }

        # 🔍 LOG PROMPT (PROOF LLM IS USED)
        log.warning("LLM PROMPT >>>\n%s", prompt)

        payload = {
            "inputs": prompt,
            "parameters": {
                "temperature": TEMPERATURE,
                "max_new_tokens": MAX_NEW_TOKENS,
                "return_full_text": False
            }
        }

        try:
            response = requests.post(
                HF_API_URL,
                headers=self.headers,
                json=payload,
                timeout=TIMEOUT_SECONDS
            )

            log.info(
                "LLM HTTP response | status=%s",
                response.status_code
            )

            # Hugging Face cold-start handling
            if response.status_code == 503:
                log.warning("LLM model loading (503)")
                return {
                    "enabled": True,
                    "suggested_action": None,
                    "explanation": "Model loading on Hugging Face, retry shortly"
                }

            response.raise_for_status()
            result = response.json()

        except requests.exceptions.RequestException as e:
            log.error("LLM request failed: %s", str(e))
            return {
                "enabled": True,
                "suggested_action": None,
                "explanation": f"LLM request failed: {str(e)}"
            }

        # HF response can be list or dict
        if isinstance(result, list):
            text = result[0].get("generated_text", "")
        else:
            text = result.get("generated_text", "")

        # 🔍 LOG RAW OUTPUT
        log.warning("LLM RAW OUTPUT <<<\n%s", text.strip())

        action = self._extract_action(text)

        # 🔍 LOG FINAL DECISION
        log.warning("LLM DECISION <<< action=%s", action)

        return {
            "enabled": True,
            "suggested_action": action,
            "explanation": text.strip()
        }

    def _extract_action(self, text: str) -> str | None:
        text = text.lower()

        if "restart" in text:
            return "restart"
        if "scale" in text:
            return "scale"
        if "alert" in text:
            return "alert"

        return None
