import requests
import random
import argparse
from lxml import etree
from bs4 import BeautifulSoup
from openpyxl import Workbook


def create_parser():
    parser = argparse.ArgumentParser(
        description='Get info about curses from coursera.org')
    parser.add_argument(
        '--total',
        default=20,
        type=int,
        help='How many courses check.'
    )
    parser.add_argument(
        '--datafile',
        default='courses_info.xlsx',
        help='File for saving information about courses'
    )
    return parser


def get_content(url):
    content = requests.get(url).content
    return content


def get_random_courses_list(content, number_of_courses):
    links = etree.fromstring(content)
    urls = []
    for url in links.getchildren():
        for loc in url.getchildren():
            urls.append(loc.text)
    courses_urls_list = random.sample(urls, number_of_courses)
    return courses_urls_list


def get_courses_pages(courses_urls_list):
    courses_pages = []
    for course_url in courses_urls_list:
        courses_pages.append(requests.get(course_url).text)
    return courses_pages


def get_html_text(soup, html_tag, css_class):
    html_values = soup.find(html_tag, css_class)
    if html_values:
        return html_values.get_text()
    else:
        return None


def get_html_len(soup, html_tag, css_class):
    html_values = soup.find_all(html_tag, css_class)
    if html_values:
        return len(html_values)
    else:
        return None


def get_course_info(course):
    soup = BeautifulSoup(course, 'lxml')
    course_info = {}
    course_info['title'] = get_html_text(soup, 'h1', 'title')
    course_info['language'] = get_html_text(soup, 'div', 'rc-Language')
    course_info['startdate'] = get_html_text(soup, 'div', 'startdate')
    course_info['duration'] = get_html_len(soup, 'div', 'week-heading')
    course_info['rating'] = get_html_text(soup, 'div', 'ratings-text')
    return course_info


def get_courses_info(courses_list):
    courses_info = []
    for course in courses_list:
        courses_info.append(get_course_info(course))
    return courses_info


def output_courses_info_to_xlsx(courses_info):
    wb = Workbook()
    sheet = wb.active
    sheet.title = 'Coursera information'
    head_line = [
        'Course Title',
        'Language',
        'Start Date',
        'Duration',
        'Rating'
    ]
    sheet.append(head_line)
    for course_info in courses_info:
        sheet.append([
            course_info['title'],
            course_info['language'],
            course_info['startdate'],
            course_info['duration'],
            course_info['rating']
        ])
    return wb


def save_datafile(wb):
    try:
        datafile = wb.save(args.datafile)
        return datafile
    except PermissionError:
        print('Pls close default file or select another!!!')


if __name__ == '__main__':
    url = 'https://www.coursera.org/sitemap~www~courses.xml'
    parser = create_parser()
    args = parser.parse_args()
    content = get_content(url)
    courses_urls = get_random_courses_list(content, args.total)
    courses_pages = get_courses_pages(courses_urls)
    courses_info = get_courses_info(courses_pages)
    wb = output_courses_info_to_xlsx(courses_info)
    datafile = save_datafile(wb)








