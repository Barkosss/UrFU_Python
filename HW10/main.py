import argparse
import os
import pathlib
import sys
import threading
import urllib.request
from typing import Optional
from urllib.error import URLError, HTTPError


def load_content(url: str) -> Optional[bytes]:
    try:
        return urllib.request.urlopen(url, timeout=10).read()
    except (HTTPError, URLError):
        return None


def download_image(out_dir: pathlib.Path) -> None:
    url = "https://habr.com/ru/articles/"
    response = load_content(url)
    with open(out_dir, "") as file:
        file.write(response)


def wrapper(articles: int, out_dir: pathlib.Path) -> None:
    pass


def run_scraper(threads: int, articles: int, out_dir: pathlib.Path) -> None:
    for _ in range(threads):
        thread = threading.Thread(target=wrapper, args=(articles, out_dir))
        thread.start()
        thread.join()


def main():
    script_name = os.path.basename(sys.argv[0])
    parser = argparse.ArgumentParser(
        usage=f'{script_name} [ARTICLES_NUMBER] THREAD_NUMBER OUT_DIRECTORY',
        description='Habr parser',
    )
    parser.add_argument(
        '-n', type=int, default=25, help='Number of articles to be processed',
    )
    parser.add_argument(
        'threads', type=int, help='Number of threads to be run',
    )
    parser.add_argument(
        'out_dir', type=pathlib.Path, help='Directory to download habr images',
    )
    args = parser.parse_args()

    run_scraper(args.threads, args.n, args.out_dir)


if __name__ == '__main__':
    main()