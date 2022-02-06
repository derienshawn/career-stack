# Career-Stack

Career-Stack is a platform to connect IT job experience seekers with project creators in need of technical talent.
# Staging
- Configure the following in server.py based on your environment:
```python
    # Uncomment to run redis Locally:
    # redis = redis.Redis(host= 'localhost',port= '6379')

    # Uncomment to run Redis config on staging via Heroku
    redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379')
    redis = redis.from_url(redis_url)

    # Uncomment RedirectResponse URL for LOCAL testing
    return RedirectResponse(local_url)

    # Uncomment RedirectResponse URL for STAGING testing
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