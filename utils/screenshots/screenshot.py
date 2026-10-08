import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCREENSHOT_DIR = Path(
    os.getenv("SCREENSHOT_DIR", PROJECT_ROOT / "artifacts" / "screenshots")
)


async def take_screenshot(page, name: str) -> Path:
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    path = SCREENSHOT_DIR / f"{name}.png"
    await page.screenshot(path=str(path))
    return path