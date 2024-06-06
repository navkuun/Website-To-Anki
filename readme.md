# Website to Anki Flashcards

This project allows you to input a website URL, scrape the text content from the linked pages, and generate Anki flashcards using a language model (LLM). The flashcards are created in a format suitable for importing into Anki.

## Project Structure

- `main.py`: This script handles fetching links from a given URL, allowing the user to select which links to scrape, and saving the scraped text.
- `file_to_anki.py`: This script uses a language model to generate flashcards from the scraped text and saves them in a format compatible with Anki.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `curses` library (usually included with Python)
- `pydantic` library
- `openai` library
- `instructor` library

You can install the required libraries using pip:

sh
pip install requests beautifulsoup4 pydantic openai instructor


## Usage

1. **Run the main script**:

sh
python main.py


2. **Enter the website URL** when prompted.

3. **Select the links** you want to scrape using the arrow keys and space bar. Press Enter to confirm your selection.

4. The script will scrape the text from the selected links and save them in the `scraped_texts` folder.

5. **Generate Anki flashcards**:
    - The `file_to_anki.py` script will automatically generate flashcards from the scraped text and save them in `flashcards.txt`.

## Example

Here is an example of how the flashcards are formatted in `flashcards.txt`:

<h2 class="card-question-text" itemprop="name text">What is the nature of sunlight?</h2> <h3 class="card-answer-text" itemprop="text">Sunlight is a form of electromagnetic radiation and the visible light we see is a small subset of the electromagnetic spectrum.</h3>
<h2 class="card-question-text" itemprop="name text">Who were the key figures that demonstrated light as a wave in the early 1800's?</h2> <h3 class="card-answer-text" itemprop="text">Thomas Young, François Arago, and Augustin Jean Fresnel.</h3>



## Detailed Description of Files

### `main.py`

This script performs the following tasks:
- Fetches all links from the provided URL.
- Displays the links in a terminal interface for selection.
- Scrapes text content from the selected links.
- Saves the scraped text in the `scraped_texts` folder.

### `file_to_anki.py`

This script performs the following tasks:
- Defines a `Flashcard` model using `pydantic`.
- Uses a language model to generate flashcards from the scraped text.
- Saves the flashcards in a tab-separated format suitable for Anki.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or find any bugs.

## License

This project is licensed under the MIT License.