# website_to_anki/main.py
import requests
from bs4 import BeautifulSoup
import curses
import os
from urllib.parse import urljoin


def fetch_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = [urljoin(url, a["href"]) for a in soup.find_all("a", href=True)]
    return links


def display_links(stdscr, links):
    selected = [True] * len(links)
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        for idx, link in enumerate(links):
            if idx < height - 1:  # Leave space for the status bar
                if selected[idx]:
                    stdscr.addstr(idx, 0, f"* {link[:width-2]}")
                else:
                    stdscr.addstr(idx, 0, f"  {link[:width-2]}")

        stdscr.addstr(
            height - 1,
            0,
            "Use arrow keys to navigate, space to select, Enter to confirm",
        )

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(links) - 1:
            current_row += 1
        elif key == ord(" "):
            selected[current_row] = not selected[current_row]
        elif key == ord("\n"):
            break

        stdscr.move(current_row, 0)

    return [link for idx, link in enumerate(links) if selected[idx]]


def select_links(links):
    return curses.wrapper(display_links, links)


def scrape_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()


def save_texts(links, folder="scraped_texts"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for idx, link in enumerate(links):
        text = scrape_text(link)
        with open(
            os.path.join(folder, f"website_{idx}.txt"), "w", encoding="utf-8"
        ) as f:
            f.write(text)


def main():
    url = input("Enter the website URL: ")
    links = fetch_links(url)
    selected_links = select_links(links)
    save_texts(selected_links)


if __name__ == "__main__":
    main()
