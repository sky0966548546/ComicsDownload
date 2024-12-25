# Manga Downloader

Use Python web scraping to download manga from [nhentai.net](https://nhentai.net) and save it to a specified folder.

## Features

**1. Web Scraping**
  - Utilizes `requests` and `BeautifulSoup` to scrape manga content.
  - Retrieves high-quality images from nhentai.net while maintaining the correct page order.

**2. Download Management**
  - Downloads manga content as images to a user-defined directory using multithreading for faster performance.

## Installation Instructions

### 1. Install Dependencies

To install the necessary Python libraries, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

This command will install required packages like `requests` and `beautifulsoup4`.

### 2. Access the Repository

You can either download the Manga Downloader from [GitHub](https://github.com/sky9154/MangaDownloader) or clone the repository using Git:

```bash
git clone https://github.com/sky9154/MangaDownloader.git
```

This will clone the repository to your local machine, and you’ll be able to run the manga downloader script.

### 3. Use the Executable File

Alternatively, you can download the latest executable file from the [Releases](https://github.com/sky9154/MangaDownloader/releases) page and run it directly without needing to install dependencies.

## How to Use

Run the following command:

```bash
python app.py
```

You can configure the settings using the `setting.ini` file:

```ini
[Download]
max_workers = 3
delay = 1
```

This allows you to set the maximum number of threads (`max_workers`) and the delay between each request (`delay`).

## Notes

- Future updates will include functionality for converting the downloaded manga into PDF format.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.