import os

class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://playwright.dev/")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    BROWSERS = ["chromium", "firefox"]

settings = Settings()