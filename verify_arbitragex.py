import time
from playwright.sync_api import sync_playwright

local_url = "file:///C:/Users/Nucom/Projects/ArbitrageX/index.html"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    # Desktop 1440x900
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    print(f"Loading ArbitrageX ({local_url})...")
    page.goto(local_url, wait_until="networkidle")
    time.sleep(3)
    
    print("Page Title:", page.title())
    page.screenshot(path=r"C:\Users\Nucom\Desktop\arbitragex_live_scanner.png")
    print("1. Captured Live Scanner Screenshot")
    
    # Test Route Modal
    print("Testing Route Execution Modal...")
    page.click("button.btn-route >> nth=0")
    page.wait_for_selector("#routeModal.active", timeout=5000)
    time.sleep(1)
    page.screenshot(path=r"C:\Users\Nucom\Desktop\arbitragex_route_modal.png")
    print("2. Captured Arbitrage Route Modal Screenshot")
    page.click("#routeModal .modal-close")
    time.sleep(0.5)
    
    # Test License Key Activation to Pro
    print("Testing License Key Activation (PRO-ARBITRAGE-2026)...")
    page.click("#btnNavUpgrade")
    page.wait_for_selector("#pricingModal.active", timeout=5000)
    time.sleep(0.5)
    page.fill("#licenseKeyInput", "PRO-ARBITRAGE-2026")
    page.click("button.btn-activate")
    time.sleep(2)
    page.screenshot(path=r"C:\Users\Nucom\Desktop\arbitragex_pro_unlocked.png")
    print("3. Captured Pro Tier Unlocked Screenshot")
    
    # Mobile Test
    print("Testing Mobile Responsiveness (iPhone 14)...")
    mobile_page = browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True)
    mobile_page.goto(local_url, wait_until="networkidle")
    time.sleep(3)
    mobile_page.screenshot(path=r"C:\Users\Nucom\Desktop\arbitragex_mobile.png")
    print("4. Captured Mobile View Screenshot")
    
    browser.close()

print("\n>>> ARBITRAGEX VERIFICATION COMPLETED SUCCESSFULLY! <<<")
