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

def extract_internship_links(URL_OF_INTERNSHIP_LISTING_PAGE):
    links= []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        agentql_page = agentql.wrap(page)
        agentql_page.goto(URL_OF_INTERNSHIP_LISTING_PAGE)
        response = agentql_page.query_data(QUERY)
        
        for link in response['internships']:
            links.append(link['link'])

        browser.close()
    return links