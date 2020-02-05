from selenium import webdriver
import re


def wiki_scraper():
    final = []
    driver = webdriver.PhantomJS('/Users/garrettwilliford/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
    stop_words = ['Categories', 'Wikipedia article lists', 'Wikipedia core topics', 'Wikipedia vital articles', 'Talk', 'Contributions', \
                  'Create account', 'Log in', 'Project page', 'Talk', 'Read', 'Edit', 'View history', '', 'Main page', 'Contents', 'Featured content', \
                  'Current events', 'Random article', 'Donate to Wikipedia', 'Wikipedia store', 'Help', 'About Wikipedia', 'Community portal', 'Recent changes',\
                  'Contact page', 'What links here', 'Related changes', 'Upload file', 'Special pages', 'Permanent link', 'Page information', 'Wikidata item', \
                  'Meta-Wiki', 'Create a book', 'Download as PDF', 'Printable version', 'Asturianu', 'বাংলা', 'Deutsch', 'Ελληνικά', 'فارسی', 'Galego', '한국어', \
                  'Íslenska', '\\ עברית', 'Latviešu', '日本語', 'Русский', 'Simple English', 'کوردی', 'Suomi', 'தமிழ்', 'Татарча/tatarça', 'Türkçe', '中文', 'Edit links', \
                  'Creative Commons Attribution-ShareAlike License', '', 'Terms of Use', 'Privacy Policy', 'Wikimedia Foundation', 'Inc.', 'Privacy policy',\
                  'About Wikipedia', 'Disclaimers', 'Contact Wikipedia', 'Developers', 'Statistics', 'Cookie statement', 'Mobile view', 'Enable previews', 'edit',\
                  'Wikipedia:Vital articles', 'Jump to navigation', 'Jump to search', 'Shortcut', 'WP:VA/E/A', 'Vital articles', 'centralized watchlist', 'are labelled', \
                  'Featured articles', 'Good articles', 'Template:Icon/doc', 'User:cewbot', 'list of ten thousand articles', 'Frequently Asked Questions (FAQ) page']
    

    driver.get('https://en.wikipedia.org/wiki/Category:Wikipedia_article_lists')
    a = driver.find_elements_by_tag_name('a')
    a = [aa for aa in a if 'Vital articles' in aa.get_attribute('innerHTML')]
    for i in range(len(a)):
        driver.get('https://en.wikipedia.org/wiki/Category:Wikipedia_article_lists')
        a = driver.find_elements_by_tag_name('a')
        a = [aa for aa in a if 'Vital articles' in aa.get_attribute('innerHTML')]
        print('-----------------------------')
        print(a[i].get_attribute('innerHTML'))
        print('<><><><><><><><><><><><><><>')
        a[i].click()
        try:
            categories = driver.find_elements_by_tag_name('a')
            categories = [c.get_attribute('innerHTML') for c in categories]
            c = [re.sub('<i>', '', re.sub('</i>', '', c)) for c in categories if 'tocnumber' not in c and c not in stop_words and 'Level' not in c and '<' not in c]
            for cc in c:
                print(cc)
                final.append(cc)
        except:
            print('<<!NOT_SCRIPTABLE!>>')
    return set(final)
