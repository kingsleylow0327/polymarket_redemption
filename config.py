import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Settings:
    rpc_urls: list[str] = os.getenv("RPC_URLS", "").split(",")
    metamask_address: str = os.getenv("METAMASK_ADDRESS", "")
    funder: str = os.getenv("POLYMARKET_FUNDER", "")
    ctf_address: str = os.getenv("CTF_ADDRESS", "")
    usdc_address: str = os.getenv("USDC_ADDRESS", "")

def load_settings() -> Settings:
    return Settings()
