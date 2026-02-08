import logging
import uvicorn

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    uvicorn.run(
        "agent.ingestion.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
