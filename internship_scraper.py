from playwright.sync_api import sync_playwright
import agentql


QUERY = """
{
    internships[]{
        name
        link
        company
        location
    }
}"""


links= []
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    agentql_page = agentql.wrap(page)
    agentql_page.goto("https://au.gradconnection.com/internships/engineering-software/melbourne/")
    response = agentql_page.query_data(QUERY)
    
    for link in response['internships']:
        links.append(link['link'])
    print(links)

    browser.close()