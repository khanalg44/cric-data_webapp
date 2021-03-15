# Git Repo for cric-data web application


# Deployment

Need `Procfile` and  `requirements.txt` files in the working directory.

## Directly using Heroku CLI

```
git add .
git commit -m "m"
heroku login 
heroku git:remote -a cric-data
git push -f heroku master
```

# Deployment through Git

- Push to Git using regular git push steps `git add .; git commit -m 'message'; git push -u origin master`
- Go to your app in `Heroku.com` and go to Deploy tab and then select connect to GitHub and then follow the steps therein.
