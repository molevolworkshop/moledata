# GitHub Actions Workflows

This repository uses automated GitHub Actions workflows to manage items in the moledata repo

## Compress PDFs in PR (`compress-pdfs.yml`)
- **Trigger Events:** Pull requests that edit any file in the format `**/*.pdf`.

Automatically compresses newly added or modified PDF files in lecture update Pull Requests using Ghostscript to reduce file size. It checks for previous automated commits to prevent infinite loops, replaces the large PDFs with compressed versions, and pushes the changes back to the PR branch.

## Process Lab Materials Issue (`process-lab-issue.yml`)
- **Trigger Events:** Issues opened or edited with the `lab-update` label.

Parses form fields from lab update issues to organize and ingest new lab materials. It automatically downloads and extracts provided archives, scripts, datasets, and markdown READMEs into a standardized directory structure (`labs/slug/`). It updates `_data/materials-registry.csv` and automatically creates a Pull Request with the structured lab files.

## Process Lecture Materials Issue (`process-lecture-issue.yml`)
- **Trigger Events:** Issues opened or edited with the `lecture-update` label.

Similar to the lab processor, this workflow parses lecture update issues. It downloads uploaded lecture presentations (like PDFs) or captures off-site URLs, creates the necessary `lectures/slug/` directories, updates `_data/materials-registry.csv`, and automatically opens a Pull Request with the new or updated lecture materials.

## Notify Website Repo on Update (`update_ping.yml`)
- **Trigger Events:** Push to the `main` branch.

Acts as a webhook to ping the primary website repository. It sends a `repository_dispatch` event (`moledata-updated`) to the `molevolworkshop.github.io` repository, triggering a site rebuild so that newly merged data and materials are immediately reflected on the live site.

## Update Issue Templates - Faculty (`update-issue-templates-faculty.yml`)
- **Trigger Events:** Manual workflow dispatch or repository dispatch (`faculty-registry-updated`, a ping is sent from the website repo when this happens).
A cross-repository synchronization tool that pulls the latest `faculty-registry.csv` from the main website repository. It dynamically updates the faculty dropdown choices in both the Lecture and Lab issue templates (`update-lecture.yml` and `update-lab.yml`), ensuring the presenter options are always up to date.

## Update Issue Templates - Lectures/Labs (`update-issue-templates-lectureslabs.yml`)
- **Trigger Events:** Push modifying `_data/materials-registry.csv` or manual workflow dispatch.
Keeps issue template dropdowns synchronized with the available materials in the repository. It parses the registry CSV to build a current list of existing lectures and labs, then automatically injects these as selectable options into the `update-lecture.yml` and `update-lab.yml` issue templates.