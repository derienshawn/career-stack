# Career-Stack

Career-Stack is a platform to connect IT job experience seekers with project creators in need of technical talent.
# Staging
- Configure server.py RedirectResponse URL based on your environment:
```python
    # URL for LOCAL testing -- uncomment when running locally
    return RedirectResponse(local_url)

    # URL for STAGING testing -- uncomment when running on Heroku staging
    return RedirectResponse(staging_url)
```
# Running the app locally

Run the following command inside the root directory to start the app locally:
```
uvicorn server:app --reload
```
- View the app in staging:
https://career-stack.herokuapp.com/

- View API docs:
https://career-stack.herokuapp.com/docs