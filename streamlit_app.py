import streamlit as st
import requests
import asyncio
import aiohttp


# Asynchronous function to fetch a single job posting
async def fetch_job(session, job_id):
    job_url = f"https://hacker-news.firebaseio.com/v0/item/{job_id}.json?print=pretty"
    async with session.get(job_url) as job_response:
        if job_response.status == 200:
            return await job_response.json()
        return None


# Asynchronous function to fetch all job postings concurrently
async def fetch_jobs(job_ids):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_job(session, job_id) for job_id in job_ids]
        jobs = await asyncio.gather(*tasks)
        return [job for job in jobs if job is not None]


# Function to fetch job postings from Hacker News API
def fetch_job_postings():
    url = "https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty"
    response = requests.get(url)
    if response.status_code == 200:
        job_ids = response.json()[:25]  # Get top 25 job IDs
        jobs = asyncio.run(fetch_jobs(job_ids))
        return jobs
    else:
        return []


# Asynchronous function to fetch a single story
async def fetch_story(session, story_id):
    story_url = (
        f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty"
    )
    async with session.get(story_url) as story_response:
        if story_response.status == 200:
            return await story_response.json()
        return None


# Asynchronous function to fetch all stories concurrently
async def fetch_stories(top_ids):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_story(session, story_id) for story_id in top_ids]
        stories = await asyncio.gather(*tasks)
        return [story for story in stories if story is not None]


# Function to fetch top stories from Hacker News API
def fetch_top_stories():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    response = requests.get(url)
    if response.status_code == 200:
        top_ids = response.json()[:15]  # Get top 15 story IDs
        stories = asyncio.run(fetch_stories(top_ids))
        return stories
    else:
        return []


# Main Streamlit app
def main():
    st.title("🚀 Hacker News Dashboard")
    st.write("Welcome to the Hacker News Dashboard! Choose an option below.")

    # Button for job postings
    if st.button("💼 List Job Postings"):
        st.subheader("Job Postings")
        jobs = fetch_job_postings()
        if jobs:
            for job in jobs:
                st.markdown(f"### **{job.get('title', 'No title available')}**")
                st.markdown(f"**Link:** [View Job]({job.get('url', '#')})")
                st.markdown(
                    f"**Posted by:** {job.get('by', 'Unknown')} | **Score:** {job.get('score', 0)}"
                )
                st.markdown("---")  # Horizontal rule for separation
        else:
            st.write("No job postings available at the moment.")

    # Button for top stories
    if st.button("🔝 Find Top 15 Stories of the Day"):
        st.subheader("Top 15 Stories")
        stories = fetch_top_stories()
        if stories:
            for story in stories:
                st.write(f"**Title:** {story.get('title', 'No title available')}")
                st.write(f"**Link:** [Read More]({story.get('url', '#')})")
                st.write(
                    f"**Posted by:** {story.get('by', 'Unknown')} | **Score:** {story.get('score', 0)}"
                )
                st.write("---")
        else:
            st.write("No stories found.")
    # Footer
    st.markdown("---")
    st.write("Made with ❤️ by [Chinmay](https://linktr.ee/chinmay_kotkar)")


if __name__ == "__main__":
    main()
