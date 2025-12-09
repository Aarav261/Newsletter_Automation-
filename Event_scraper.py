from playwright.sync_api import sync_playwright
import agentql



QUERY = """
{
    events[]{
        link}

}"""

def extract_meetup_links(URL_OF_MEETUP_LISTING_PAGE):
    links= []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        agentql_page = agentql.wrap(page)
        agentql_page.goto(URL_OF_MEETUP_LISTING_PAGE)
        response = agentql_page.query_data(QUERY, mode = 'fast')
        
        for link in response['events']:
            links.append(link['link'])

        browser.close()

    return links

QUERY_DETAILS = """{
    title
    link
    date
    description
    location
}"""

def extract_meetup_events(links, Limit_links=10):
    event_list = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        for link in links[:Limit_links]:
            page = browser.new_page()
            agentql_page = agentql.wrap(page)
            agentql_page.goto(link)
            response = agentql_page.query_data(QUERY_DETAILS)  # single event dict
            event_list.append(response)
            page.close()
        browser.close()
    return event_list
            
