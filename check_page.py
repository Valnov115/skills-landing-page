from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.goto("file:///D:/Claude Playground/Skills Landing Page/index.html")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="/tmp/landing_full.png", full_page=True)
    print("Title:", page.title())
    print("Page content length:", len(page.content()))
    # Check for any console errors
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    page.reload()
    page.wait_for_load_state("networkidle")
    page.screenshot(path="C:/Users/User/AppData/Local/Temp/landing_full.png", full_page=True)
    print("Console errors:", errors)
    browser.close()
