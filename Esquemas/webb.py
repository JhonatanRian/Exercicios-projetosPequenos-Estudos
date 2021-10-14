from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://unite.nike.com/oauth.html?client_id=QLegGiUU042XMAUWE4qWL3fPUIrpQTnq&redirect_uri=https%3A%2F%2Fwww.nike.com.br%2Fapi%2Fv2%2Fauth%2Fnike-unite%2Fset&response_type=code&locale=pt_BR&state=%2F")
    page.click('text=Login')
    page.fill('input[name="emailAddress"]', "jhonatanrian.jr@gmail.com")
    page.fill('input[name="password"]', "j1f5e3o3")
    page.click('text=Submit')
    browser.close()