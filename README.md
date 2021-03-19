# Git Repo for cric-data web application


# Deployment

Need `Procfile` and  `requirements.txt` files in the working directory.

- Install `pipreqs` using `pip3 install pipreqs` to create `requirements.txt` file
- Procfile is basically a set up script. can copy and paste. `web: sh setup.sh && streamlit run app.py`

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
- For some reason the continuous deployment hasn't been working for me. So I have to deploy everytime I push my changes to git.
