Django To-Do App (CI/CD with Jenkins, Docker & Trivy)

A simple Django-based To-Do application containerized with Docker and deployed through a Jenkins CI/CD pipeline. The pipeline builds, tests, runs, and scans the Docker image for vulnerabilities using Trivy.

Features

✅ Add, update, toggle, and delete tasks

✅ Django + SQLite lightweight backend

✅ CI/CD pipeline with Jenkins

✅ Containerized using Docker

✅ Security scanning using Trivy

Project Structure

Django_To-Do_App_CI_CD/
│── todo/                 # Django app (models, views, urls, templates)
│── todoproject/          # Django project configs
│── templates/            # HTML templates
│── requirements.txt      # Python dependencies
│── Dockerfile            # Docker image definition
│── entrypoint.sh         # Entrypoint script for migrations
│── Jenkinsfile           # Jenkins CI/CD pipeline
│── README.md             # Documentation

Jenkins Pipeline

This project includes a Jenkinsfile with the following stages:

Code → Pulls latest code from GitHub

Build → Builds Docker image of Django app

Test → Runs Django unit tests (python manage.py test)

Scan → Runs Trivy scan on built Docker image

Run → Runs container if tests & scans pass
<img width="1842" height="733" alt="Screenshot from 2025-08-21 03-24-39" src="https://github.com/user-attachments/assets/cc21cfc7-b705-4e7f-bbdc-632fe645e048" />

<img width="1914" height="1076" alt="Screenshot from 2025-08-21 03-24-09" src="https://github.com/user-attachments/assets/3bcf95be-7a37-4c02-bc4f-cb0fcb02cb89" />


