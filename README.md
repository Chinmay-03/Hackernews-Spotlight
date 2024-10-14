# Hacker News Dashboard

🚀 Welcome to the Hacker News Dashboard! This is a Streamlit application that allows users to view the top stories and job postings from Hacker News.

## Features

- **Top Stories**: Fetch and display the top 15 stories of the day from Hacker News.
- **Job Postings**: Fetch and display the latest job postings from Hacker News.
- **Weekly Newsletter**: Subscribe to a weekly newsletter summarizing the top stories.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/hacker-news-dashboard.git
    cd hacker-news-dashboard
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run streamlit_app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to view the app.

## File Structure

- `streamlit_app.py`: Main Streamlit application file.
- `job.py`: Contains functions related to fetching job postings.
- `newsletter.py`: Contains functions related to the weekly newsletter.
- `test.py`, `test2.py`, `test3.py`: Test files for various functionalities.
- `test.html`: HTML file for testing purposes.

## Functions

### `streamlit_app.py`

- `fetch_job(session, job_id)`: Asynchronously fetch a single job posting.
- `fetch_jobs(job_ids)`: Asynchronously fetch all job postings concurrently.
- `fetch_job_postings()`: Fetch job postings from Hacker News API.
- `fetch_story(session, story_id)`: Asynchronously fetch a single story.
- `fetch_stories(top_ids)`: Asynchronously fetch all stories concurrently.
- `fetch_top_stories()`: Fetch top stories from Hacker News API.
- `main()`: Main function to run the Streamlit app.

### `newsletter.py`

- `fetch_top_stories()`: Fetch top stories from Hacker News.
- `summarize_stories(stories)`: Summarize the fetched stories.
- `send_newsletter(email, summary)`: Send a newsletter (demo only).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Hacker News API](https://github.com/HackerNews/API)
- Made with ❤️ by [Chinmay](https://linktr.ee/chinmay_kotkar)
