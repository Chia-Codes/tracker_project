# TrackHer — Menstrual Cycle Tracker

**TrackHer** is a full-stack Django web app that lets users log menstrual cycles and symptoms via a calendar-based interface. It supports personalized cycle tracking and offers optional export to Google Sheets.

---

The live link can be found here: [View the live project here](https://trackher-c1d90b82fba4.herokuapp.com/)

---

![Mock Up](docs/readme_images/mockup.png) 

## Table of Contents

* [TrackHer](#trackher)

  * [Table of Contents](#table-of-contents)
* [User-Experience-Design](#user-experience-design)

  * [The-Strategy-Plane](#the-strategy-plane)

    * [Site-Goals](#site-goals)
    * [Agile-Planning](#agile-planning)

      * [Epics](#epics)
      * [User-Stories](#user-stories)
  * [The-Scope-Plane](#the-scope-plane)
  * [The-Structure-Plane](#the-structure-plane)

    * [Features](#features)
    * [Features-Left-To-Implement](#features-left-to-implement)
  * [The-Skeleton-Plane](#the-skeleton-plane)

    * [Wireframes](#wireframes)
    * [Database-Design](#database-design)
    * [Security](#security)
  * [The-Surface-Plane](#the-surface-plane)

    * [Design](#design)
    * [Colour-Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Imagery](#imagery)
  * [Technolgies](#technolgies)
  * [Testing](#testing)
  * [Deployment](#deployment)

    * [Version-Control](#version-control)
    * [Heroku-Deployment](#heroku-deployment)
    * [Run-Locally](#run-locally)
    * [Fork-Project](#fork-project)
  * [Credits](#credits)

# User-Experience-Design

## The-Strategy-Plane

### Site-Goals

TrackHer helps users:

* Quickly log period flow and symptoms on a monthly calendar.
* View a history of past cycles and notes.
* Optionally export logs to Google Sheets for analysis or backup.
* Maintain privacy and control of their data (per-user visibility only).

Secondary goals for the site owner:

* Keep the UX lightweight and mobile-first.
* Provide a stable, secure Django backend with a simple deployment pipeline.

### Agile-Planning

This project was developed using agile practices with small features shipped in incremental sprints (3 sprints over ~4 weeks).

All user stories were grouped into epics and prioritized using MoSCoW (Must/Should/Could). “Must have” stories were delivered first to ensure a usable MVP.

A Kanban board was created using GitHub Projects and can be located here: [Kanban Board Link](https://github.com/users/Chia-Codes/projects/9).

![Kanban image](docs/readme_images/kanban.png) 

#### Epics

**EPIC 1 – Base Setup**

Set up the Django project, apps, base templates, static handling, and initial models. This unlocks the rest of the feature work.

**EPIC 2 – Calendar & Logging**

Implement a responsive calendar view, daily log create/edit/delete, and per-day notes. Ensure one log per user per day.

**EPIC 3 – Authentication**

User registration, login, logout, and profile ownership checks so users see only their own data.

**EPIC 4 – Data Export (Google Sheets)**

Add optional export of day logs to a shared Google Sheet using a service account (or OAuth). Make this configurable via environment variables.

**EPIC 5 – Analytics (MVP)**

Basic summaries (e.g., count of period days per month; average cycle length if cycle start/end captured).

**EPIC 6 – Deployment**

Automate deployment to Heroku; configure static files, environment variables, and database.

**EPIC 7 – Documentation & Testing**

Write README, testing notes, and usage docs; document environment setup and deployment steps.

#### User-Stories

**EPIC 1 – Base Setup**

* As a developer, I want a `base.html` layout so other templates can extend a consistent UI.
* As a developer, I want static files (CSS/JS) configured locally and in production.
* As a developer, I want initial models and migrations to create the schema for daily logs and symptoms.

**EPIC 2 – Calendar & Logging**

* As a user, I want to log my period flow for a given date on a calendar.
* As a user, I want to add symptoms and a short note for that date.
* As a user, I want to edit or delete a day’s log.
* As a user, I want visual feedback (toasts) after actions.
* As a user, I want to quickly jump to today’s date and see what’s already logged.

**EPIC 3 – Authentication**

* As a user, I want to sign up, sign in, and sign out securely.
* As a user, I want to ensure only I can see and manage my logs.

**EPIC 4 – Data Export (Google Sheets)**

* As a user, I want an optional export of my logs to Google Sheets so I can analyze them elsewhere.

**EPIC 5 – Analytics (MVP)**

* As a user, I want a simple summary of the number of period days this month and basic cycle stats.

**EPIC 6 – Deployment**

* As a developer, I want an automated deployment to Heroku with static files served via WhiteNoise.

**EPIC 7 – Documentation & Testing**

* As a developer, I want comprehensive docs and a TESTING.md capturing manual test cases.

## The-Scope-Plane

* Mobile-first responsive UI
* Calendar month view for logging
* CRUD for day logs (create, view, update, delete)
* Per-user data isolation
* Optional Google Sheets export (service account)
* Basic analytics summary (MVP)

## The-Structure-Plane

### Features

`USER STORY – As a user, I want to log my period flow on a calendar`

**Calendar View**

Users can view the current month’s calendar with indicators for days that have been logged. Clicking a day opens the log form.

![Calendar View](docs/readme_images/calendar-view.png)
`USER STORY – As a user, I want to add symptoms and notes for a day`

**Daily Log Form**

A simple form captures:

* Date (defaults to selected day)
* Flow intensity (None, Spotting, Light, Medium, Heavy)
* Symptoms (multi-select)
* Optional notes (short text)

![Daily Log Form](docs/readme_images/daily-log-form.png)
`USER STORY – As a user, I want to edit or delete a day’s log`

**Manage Day Logs**

From the calendar or a list view, users can open a day’s entry to edit fields or delete the log with confirmation.

![Manage Logs](docs/readme_images/manage-logs.png)-----------------------------------------------------------------------------------------------------------------------------------------

`USER STORY – As a user, I want visual feedback after actions`

**Toasts**

Success and error toasts are displayed after create/update/delete so users get immediate feedback.

![Toasts](docs/readme_images/toasts.png) 

`USER STORY – As a user, I want to export my logs to Google Sheets`

### Features Left To Implement
* Manage Logs
* Cycle detection and prediction (estimate fertile window, next period)
* Push/email reminders for logging and expected start date
* Charts for trends (symptoms vs. cycle phases)
* PWA offline support
* Import from/export to CSV

## The-Skeleton-Plane

### Wireframes

* Login View

![Calendar Wireframe](docs/wireframes/01_login.png)

* Register View

![Calendar Wireframe](docs/wireframes/02_register.png)

* Dashboard View

![Calendar Wireframe](docs/wireframes/03_dashboard.png)

* Calendar View

![Calendar Wireframe](docs/wireframes/04_calendar.png)

* Daily Log

![Daily Log Wireframe](docs/wireframes/05_cycle_log_form.png)

* History / Insights

![Analytics Wireframe](docs/wireframes/06_insights.png)

* Settings 

![Export Wireframe](docs/wireframes/07_profile_settings.png)

* Log form

![Export Wireframe](docs/wireframes/08_quick_log_form.png)

### Database-Design

## Database Schema

![ERD](docs/readme_images/erdiagram.png)

## Submission Flow 

![System Flow](docs/readme_images/system_flow.png)

TrackHer uses Django’s auth `User` and three core models:

* **Symptom** – catalog of selectable symptoms.

  * `id`, `name` (unique), `category` (optional), `is_active` (bool), `created_at`.
* **DayLog** – one per user per date.

  * `id`, `user` (FK → `auth.User`), `date` (unique with user), `flow` (choice: NONE/SPOTTING/LIGHT/MEDIUM/HEAVY), `notes` (text, optional), `created_at`, `updated_at`.
  * Relationship: many-to-many to `Symptom` (through table `DayLogSymptoms`).
    
* **DayLogSymptoms** – join table (implicit if using Django M2M) to store which symptoms were selected for each `DayLog`.

**Constraints & Indexes**

* Unique constraint (`user`, `date`) on `DayLog` to prevent duplicates.
* Index on (`user`, `date`) for fast lookups.

**Example**

![Entity Relationship Diagram](docs/readme_images/erd.png)

### Security

* **Authentication & Authorization**: Django auth; views require login; queryset filtering ensures users only access their own `DayLog` rows.
* **CSRF**: Enabled by default on form posts.
* **Environment Variables**: Secrets are stored in `.env` locally and Heroku Config Vars in production. Never commit secrets.
* **Google Service Account**: Use a base64-encoded JSON key file (e.g. `sa.json.b64`) or an environment variable for credentials. Share the destination Google Sheet with the service account email.
* **Privacy**: Data is personal; avoid storing more than necessary. Provide a way to delete account data on request.

## The-Surface-Plane

### Design

Clean, friendly UI emphasizing readability and quick daily input. Calendar highlights logged days; forms are compact with touch-friendly controls.

## Technolgies

* **HTML** – Structure and templates
* **CSS** – Custom styles, Bootstrap utilities
* **JavaScript** – Calendar interactions (date selection), form enhancements
* **Python** – Django backend
* **Visual Studio Code** – Development IDE
* **GitHub** – Source control hosting
* **Git** – Version control
* **Font Awesome** – Icons (optional)
* **Canva** – For branding assets
* **TinyPNG** – Asset compression

**Python/Django**

* Django class-based views (ListView, CreateView, UpdateView, DeleteView)
* Mixins (`LoginRequiredMixin`) for auth-protected views
* `messages` framework for toasts
* `timezone`, `date` utilities for calendar logic

**External Python Modules** ![Requirements](docs/readme_images/requirements.txt.png) 

* `Django` (4.x)
* `gspread` – Google Sheets API client
* `google-auth` – Service account credentials
* `python-dotenv` – Local env file loading
* `dj-database-url` – Parse `DATABASE_URL`
* `whitenoise` – Static file serving on Heroku
* `gunicorn` – WSGI server
* `psycopg2`/`psycopg2-binary` – PostgreSQL driver (Heroku)

## Testing

Test cases and results can be found in the [TESTING](tests.md) file.

# Pytest

**File:** `tests/test_smoke.py`
```python
def test_smoke():
    assert True
```

Run locally:
```bash
pytest -q
```

If you see “no tests ran”, ensure the file path is `tests/test_smoke.py` and `pytest` is installed.

---


Manual testing covered:

* Registration/login/logout flows
* Calendar navigation and day selection
* Create/edit/delete of `DayLog`
* Validation preventing duplicate day entries
* (If configured) Sheets export appends to the expected worksheet

---

### Unfixed Bugs

#### Issue #1: Static files occasionally 500 (manifest entry missing)

 - Symptoms: ValueError: Missing staticfiles manifest entry for 'js/trackher.js' (or other assets) and 500s on error pages/favicons.

 - Status: Intermittent in production when a file is renamed or added without re-collecting.

 - Workaround: Run python manage.py collectstatic --noinput locally and redeploy; on Heroku ensure DISABLE_COLLECTSTATIC is not set and STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage".

 - #### Fix planned: Add a CI step to fail the build if collectstatic errors; keep all asset paths in templates in sync with /static/....

### Issue #2: Calendar “Submit Log” vs “Log Flow” toggle not applying on the site

 - Symptoms: The Submit Log button never hides and Log Flow never shows even when multiple days are selected.

 - Status: JS unit tests pass, but the behavior isn’t wired in the live template.

 - Workaround: Ensure the page loads the correct file name (trackher.js) via {% load static %} and <script src="{% static 'js/trackher.js' %}"></script> after the calendar HTML.

 -  #### Fix planned: Keep the production file name in sync with tests, and re-run collectstatic after every JS change.

### Issue #3: Multiple-date logging only partially saved

 - Symptoms: Selecting multiple days then logging saves only one (or none) of the selected dates.

 - Status: Backend expects ISO dates but template posted human-readable values.

 - Workaround: In the calendar checkbox value, use value="{{ day|date:'Y-m-d' }}". In the view, call request.POST.getlist('log_days') and parse with datetime.strptime(ds, '%Y-%m-%d').

 - #### Fix planned: Keep the ISO value in the template and centralize parsing in the submit view.

### Issue #4: Flow selection UX inconsistent

 - Symptoms: Previous “Log Flow” button behavior changed; user wants to pick Light/Medium/Heavy under the calendar and auto-save for the selected day(s).

 - Status: In progress (JS/UI refactor).

 - Workaround: None (feature change).

 - #### Fix planned: Attach click handlers to the flow buttons that (1) read selected dates, (2) post { dates: [...], flow: 'LIGHT|MEDIUM|HEAVY' } to submit_log, and (3) toast success. Hide Submit Log when ≥2 dates are selected.

### Issue #5: Journey page notice missing

 - Symptoms: No message informing users that journey tracking unlocks after ~30 days of logs.

 - Status: Not yet implemented.

 - Workaround: N/A.

 - #### Fix planned: In journey.html, conditionally render an alert if user_log_count < 30: “Journey tracking becomes available after one month of logging.”

### Issue #6: Signup and Symptom pages not centered

 - Symptoms: Forms are left-aligned on wide screens.

 - Status: UI polish needed.

 - Workaround: Wrap forms with Bootstrap grid utilities, e.g. <div class="row justify-content-center"><div class="col-12 col-md-8 col-lg-6">...</div></div>.

 - #### Fix planned: Apply the same container layout to both templates.

### Issue #7: Blog images not showing / placeholders

 - Symptoms: Blog posts render without images or with broken links.

 - Status: Paths/placeholders need updating.

 - Workaround: Keep image placeholders in /static/img/blog/ and reference via {% static %}; ensure images are committed (not generated).

 - #### Fix planned: Add a “featured_image” field and default fallback image at render time.

### Issue #8: Google Sheets: sorting/reading cycle logs not reliable

 - Symptoms: Service account can’t list/sort logs; 404/permission errors; ordering inconsistent.

 - Status: External dependency friction (sheet ID/permissions/rate limits).

 - Workaround (current): Use the Resources page inside the app to present reference sources and summaries instead of live-sorted Sheets.

 - #### Fix planned: Migrate to database-first logging (PostgreSQL) and use Sheets only for exports; if keeping Sheets, ensure the service account email has Editor access and the correct Sheet ID/tab name are set via env vars.

### Issue #9: Error pages loading static files (recursive 500)

 - Symptoms: Visiting /boom-500/ or hitting a 404 causes the error template to try to load missing CSS/JS, which itself errors.

 - Status: Known pitfall with ManifestStaticFilesStorage.

 - Workaround: Keep error templates minimal (inline critical styles, avoid {% static %} where possible).

 - #### Fix planned: Ship a tiny inline CSS block for 403/404/500 pages and remove external asset references there.

 ### Issue #10: CSV export edge cases

 - Symptoms: Export includes stale or unsorted entries.

 - Status: Minor.

 - Workaround: Order queryset by -date in the export view; ensure timezone-aware formatting.

 - #### Fix planned: Add server-side ordering and column headers consistent with on-screen labels.

# Recently Fixed 

 - Static path mismatch (trackher.js vs tracker.js): Verified the template points to js/trackher.js.

 - Collectstatic not run after asset rename: Added steps to deployment docs; keep an eye out for regressions.

 - Duplicate calendar HTML IDs/classes: Consolidated selectors used by Jest and the live page.
---

## Deployment

### Version-Control

The site was developed in VS Code and pushed to GitHub in the `tracker_project` repository.

Common git commands used during development:

```bash
git add <file>
git commit -m "commit message"
git push
```

### Heroku-Deployment

1. Create a Heroku app.
2. Add **Heroku Postgres** (Hobby Dev) from the Resources tab.
3. In **Settings → Config Vars**, set:

   * `SECRET_KEY` – your Django secret
   * `DATABASE_URL` – populated by the Postgres add-on
   * `DEBUG` – `False`
   * `GOOGLE_SHEETS_CREDENTIALS_B64` – base64-encoded service account JSON
   * `GOOGLE_SHEET_ID` – ID of the target Google Sheet
4. Configure static files via **WhiteNoise** (already in `MIDDLEWARE` for production).
5. Connect to GitHub and deploy the `main` branch.

The live link can be found here: [Live Site](https://trackher-c1d90b82fba4.herokuapp.com/)

## A) Create an admin (site owner) account

**Local (your laptop)**
```bash
# from the repo root with your venv active
python manage.py createsuperuser
# follow the prompts for email/username/password
```

**Heroku (production)**
```bash
# replace <your-app-name> with your Heroku app
heroku run python manage.py createsuperuser --app trackher
```

> If `heroku` isn’t installed: https://devcenter.heroku.com/articles/heroku-cli

## B) Sign in to Django Admin

- **Local:** open http://127.0.0.1:8000/admin/  
- **Heroku:** open `https://trackher-c1d90b82fba4.herokuapp.com/admin/`  
- Log in with the superuser credentials you created above.

> Tip: If `/admin/` 404s, confirm `django.contrib.admin` is in `INSTALLED_APPS` and that  **root urls.py** includes:
> ```python
> from django.contrib import admin
> from django.urls import path, include
> urlpatterns = [
>     path("admin/", admin.site.urls),
>     # path("", include("..."))  
> ]
> ```

## C) Edit / publish a blog post (via Django Admin)

1. In the left sidebar, click **Blog** → **Posts** (the model name may be `Post`).
2. To create: click **Add Post**. To edit: click an existing post’s title.
3. Fill out the fields (typical):
   - **Title** – the post title
   - **Slug** – URL slug (often auto-filled from title)
   - **Content/Body** – main text (Markdown/HTML depending on your model)
   - **Status** – choose **Published** to make it live (or **Draft** to hide)
   - **Published/Created/Updated** – dates (if present)
4. Click **Save** (or **Save and continue editing**).

> Don’t see “Posts”? Register your model in `blog/admin.py`:
> ```python
> from django.contrib import admin
> from .models import Post
> 
> @admin.register(Post)
> class PostAdmin(admin.ModelAdmin):
>     list_display = ("title", "status", "created", "updated")
>     list_filter = ("status", "created")
>     search_fields = ("title", "content")
>     prepopulated_fields = {"slug": ("title",)}
> ```


### Run-Locally

```bash
git clone <your-repo-url>
cd tracker_project
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env    
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

**.env example** 

```
SECRET_KEY=63f4945d921d599f27ae4fdf5bada3f2
DEBUG=True
# Optional way for Google Sheets export
GOOGLE_SHEETS_CREDENTIALS_B64=ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAidHJhY2toZXItNDczMjEzIiwKICAicHJpdmF0ZV9rZXlfaWQiOiAiOWNjOGJjYWZiNzc5ZmRhZGJjYzJlNGFhMGUxZDNiOTg1NDIzYjM4MiIsCiAgInByaXZhdGVfa2V5IjogIi0tLS0tQkVHSU4gUFJJVkFURSBLRVktLS0tLVxuTUlJRXZnSUJBREFOQmdrcWhraUc5dzBCQVFFRkFBU0NCS2d3Z2dTa0FnRUFBb0lCQVFEbmR0U1RlTE1VWXlHL1xuTEhKL2ZaREhybjZIOWd6UVFjcVpvNEs2eHVtLzBLZ2c0d3FvVGZOMzlodEFxb084MGs1OVE5NzR4OGpXdjRaNFxub0tQUUdOZTRRNzZHL3E2MXlVZHE0Q3ZEd2ZHeW4yN1NudWM0cE9Ub2JIb091Mk83Z1UrVnQxYVVUWHhGQUd2M1xuOWdNTWFHMmVVSTZOWWpoY3Y2MTdVY29iTytlLzZVaC95dEpHQ1VnTUhscW1YSDhHby9UQnNCWVN5VHIyTlZYY1xuYmg0aFhIMFk5SHVLQlhZTVJlbERUQ2pxUGJuNVQzdGFVaHdKUi9rbVFnU3huOFRhc1N1b1dkZXV1L0lGc0dnbFxuVzhMUDVxYnc4N3JmQnRTNDlEd21wNXhTemwycVJyZlp5VHZjRmV6NTZTcnp1ZDhKc3Z4SmIwQk5qckFiSVZKTFxuK0dFbzRxMVpBZ01CQUFFQ2dnRUFCV3UvS2dhRVJDeVhybDFsUDViaVlJalZ5Z3VoVEhIVUE4SGtkb2tnMFpjYVxuanUyZVV1ZURkWnBvRkQxQ0dWYWdFN2MybGtOQWtRWDZpV0h5d0RXS3ZOUXFWc2xKY0hTNnRWWXpkREhiUGlTVlxuZ1AyTGV3UkNuNjVscytsZjJqVDZ0dzRNaXl2ZTVwTk9WQWY1RlkzdkRrdUM4U3o5RnEvL0NVRzJ2dWxKNGREU1xuazRGb2lPK0ZYMTgrY0l4QStKVXFtV2V4TE9jNnFUQTR5NTdJSFJNc2pvK2IwRXU1azlSWWJFWWk1cWN4am5nWFxuR1U3NlJPUkZ1SFlEUVllZ0dXMDM0MDFkYXVCckpUK3NIbm9VV0N6cVJndjdGYTluUS9VMkRhQURsZUxWTWllRlxucWNVTXJQeW9HRkRpRG0wUXUzMXhoQk1HN0dVWVBPVS9DTHF0a0tCdHdRS0JnUUQ2d1NIQlRZaHY0cnludmwzL1xuaVBZaW0xbDVWemlUeWxOWng5MnVTdkF1ZDBCZnNINVBOVHpCV2JpY0xkRzlxNlFndXl6Q0JXWUVXdWFTRWtQdlxuWEZmLzYzTDZjR0tqTnExL21aSk9RNUZGSVVxZVlhaXpyMTZOamJhNDRaM2ozV1c0Z2pUYUIvVXRWVjJZYURYRFxueFVLdzJaZmg4eCttckhUTytCTGErWmFXd1FLQmdRRHNUbVN0RnhtSHBDNXIvai9BUU15SzBKVEU5RjlnaDMxL1xuUStZRjZLNGdCRVRjVndlMFdlcFNCd3ZoS3BIdnp3MWFHTE9NQ0N1b2ZjTHlHc2dKbXp1emRYbGFBTVRDQXM4UFxuSWYwbDNWN1Z3YkQ0V2kxZlZkcFFVNVpaZTVYcFVsWU5Fd2tmWU1lYmJ1MGZuaDBSTUMrcHUyNWdHTUh6VUVkK1xuRHA5OGdIdVVtUUtCZ1FDRnNub0w5Z244RmZtZXVycWxwK0lNbTZYK000b2dDcTJjWGh1TmRibFFIUmMrcmZ6Nlxud0pqdlFxWlM1MzlBVVFjR3lLWFpvVVUrcHpUdXh6eGZvRzN2THh1eitqNHRaZGJtQlB6a0s5U0Y5blV4czBKZVxuNCs5WExDc3pzbUFjQVl6ZDd0YTlOYWI5RDlvQ2kvVzJ0ek9TMWNITW9IUE15NERRWmFhd0NJbkpRUUtCZ1FEYlxuY2kyaVpJcEw0ZGRPYU0xUlA1dno2YUhPaWRZczhZWkU4b3dodnFROWpWbFplZVRvd251TmM0ZS9zZVhXMnVSZVxuWUFRVkxkMUZXb3o0Z3BCMEExbmMzV0kxaC9NdzdLVFhPOHc0SnEwVU93eWFoandPaGM3NHU3Y3JJRTdtWDVVVVxuRFRKeWxsQ244c3A0aTBBWkh6T1VIMEJ3TTIyaUJGSndLU3BJMTVSc09RS0JnSEZ5R0tvMjNrUmpwclAweUI3NFxudTVRU0dSZkpTbDUzMTlSK3NTaEtNbVlGOE54RFpmaTFIeE5pTEFObVhUSGN5VWlPVW9LbHFDY055blFHMVhOTlxuaGVIdmZmOVpEQ04wbzN3ZXpnZk95SHRFc01DeGpMcXRUN2FrRnRObUF5WEh2ZjhuRE9jeXhvbDBsRk5aSHZjcFxuTmFpYnZIVVVwUDFFUEVWanRIQWlybG81XG4tLS0tLUVORCBQUklWQVRFIEtFWS0tLS0tXG4iLAogICJjbGllbnRfZW1haWwiOiAiY3JlZHMtNTI3QHRyYWNraGVyLTQ3MzIxMy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgImNsaWVudF9pZCI6ICIxMTM1Nzg1MzA3NTYyNzIzMTA3MDYiLAogICJhdXRoX3VyaSI6ICJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20vby9vYXV0aDIvYXV0aCIsCiAgInRva2VuX3VyaSI6ICJodHRwczovL29hdXRoMi5nb29nbGVhcGlzLmNvbS90b2tlbiIsCiAgImF1dGhfcHJvdmlkZXJfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9vYXV0aDIvdjEvY2VydHMiLAogICJjbGllbnRfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9yb2JvdC92MS9tZXRhZGF0YS94NTA5L2NyZWRzLTUyNyU0MHRyYWNraGVyLTQ3MzIxMy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQo=
GOOGLE_SHEET_ID=1iwVbcSA6SAub8gbXlgeUODxArwJAaDZAVWXNfkIzneQ
```

### Fork-Project

Most commonly, forks are used to either propose changes to someone else’s project or to use someone else’s project as a starting point for your own idea.

* Navigate to the GitHub repository you want to fork.
* Click **Fork** in the top-right corner.
* This will create a copy of the project in your GitHub account.

## Credits

- [Django](https://www.djangoproject.com/) – Web framework for models, views, templates, auth, admin.  
  Live link: https://www.djangoproject.com/

- [django-allauth](https://django-allauth.readthedocs.io/) – Registration, login, account management.  
  Live link: https://django-allauth.readthedocs.io/

- [Bootstrap 5](https://getbootstrap.com/) – Layout, grid, components, responsive utilities.  
  Live link: https://getbootstrap.com/

- [Font Awesome](https://fontawesome.com/) – Iconography across navigation and UI.  
  Live link: https://fontawesome.com/

- [Google Fonts](https://fonts.google.com/) – Site typography.  
  Live link: https://fonts.google.com/

- [WhiteNoise](https://whitenoise.evans.io/en/stable/) – Serve static files in production (hashed manifests).  
  Live link: https://whitenoise.evans.io/en/stable/

- [Gunicorn](https://gunicorn.org/) – WSGI server for production.  
  Live link: https://gunicorn.org/

- [Heroku](https://www.heroku.com/) – App hosting and deployment.  
  Live link: https://www.heroku.com/

- [PostgreSQL](https://www.postgresql.org/) & [psycopg2](https://www.psycopg.org/) – Production DB and Python driver.  
  Live links: https://www.postgresql.org/ | https://www.psycopg.org/

- [Google Sheets API](https://developers.google.com/sheets/api) & [gspread](https://docs.gspread.org/) – Read/write Sheets for resources/logs.  
  Live links: https://developers.google.com/sheets/api | https://docs.gspread.org/

- [Jest](https://jestjs.io/) & [jsdom](https://github.com/jsdom/jsdom) – Front-end unit tests for calendar interactions.  
  Live links: https://jestjs.io/ | https://github.com/jsdom/jsdom

- [GitHub Actions](https://github.com/features/actions) – CI for tests and static analysis.  
  Live link: https://github.com/features/actions

- [TinyPNG](https://tinypng.com/) – Image compression to improve load performance.  
  Live link: https://tinypng.com/

- [Pexels](https://www.pexels.com/) – Royalty-free images (credited in captions).  
  Live link: https://www.pexels.com/

- [Canva](https://www.canva.com/) – Logo and simple graphics.  
  Live link: https://www.canva.com/

- [Favicon.io](https://favicon.io/) – Favicon generation.  
  Live link: https://favicon.io/

- [MDN Web Docs](https://developer.mozilla.org/) – HTML/CSS/JS and browser API references.  
  Live link: https://developer.mozilla.org/

- [Stack Overflow](https://stackoverflow.com/) – Debugging references (linked in code comments).  
  Live link: https://stackoverflow.com/

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) & [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) – Performance/accessibility audits; JS/network debugging.  
  Live links: https://developer.chrome.com/docs/devtools/ | https://developer.chrome.com/docs/lighthouse/overview/

- [W3Schools](https://www.w3schools.com/) – Quick HTML/CSS/JS lookups during prototyping.  
  Live link: https://www.w3schools.com/

- [Code Institute](https://codeinstitute.net/) – Learning resources and mentor guidance.  
  Live link: https://codeinstitute.net/


---

> **Notes for Maintainers**
>
> * If using a service account for Sheets, remember to share the target sheet with the service account email and verify the worksheet name expected by your export function.
> * Review privacy language if distributing publicly (GDPR/UK GDPR considerations).











