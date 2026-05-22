# Saurabh Gupta Portfolio

Django portfolio website using SQLite for local data storage.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Add local secrets in `.env.credentails` when needed.
4. Run `python manage.py migrate`.
5. Start the app with `python manage.py runserver`.
6. Import public GitHub repositories with `python manage.py import_github_repos --username dragonwolf1o1`.
7. Refresh GitHub project languages with `python manage.py sync_github_languages --username dragonwolf1o1`.

## Vercel Deployment

1. Push this project to GitHub.
2. Import the GitHub repository in Vercel.
3. Add environment variables from `.env.example` in Vercel Project Settings.
4. Keep `DJANGO_DEBUG=False` on Vercel.
5. Set `DJANGO_SUPERUSER_PASSWORD` to the admin password you want on Vercel.
6. Deploy. Vercel will detect Django from `manage.py`, use `portfolio_project/wsgi.py`, and run the static build command from `vercel.json`.

To change the deployed admin password, update `DJANGO_SUPERUSER_PASSWORD` in Vercel and redeploy.
The build log should show `Superuser admin@1o1rowc created` or `Superuser admin@1o1rowc updated`.

SQLite data is created from migrations during deployment. Admin changes made on a serverless host may not persist like a hosted database.

## Structure

`portfolio_project/` contains Django settings and root URLs.
`portfolio/` contains views, URLs, admin, models, and migrations.
`templates/` contains Django templates.
`static/` contains CSS and JavaScript assets.
