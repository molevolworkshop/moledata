# Contributing to moledata

This repository holds the **lecture slides** and **lab materials** for the Workshop on
Molecular Evolution (MOLE). This page is for faculty adding or updating their materials.

---

## How to contribute

Contributions should be done via pull request, so you need to fork the [moledata repo](https://github.com/molevolworkshop/moledata).

> **Don't want to deal with GitHub?** Email your slides or lab files to the workshop
> director and they'll add them for you.

1. **Find or create your folder:** `lectures/<your-last-name>/` — e.g. `lectures/beerli/`.
2. **Add your slides** as a PDF with a short, descriptive name:
   `lectures/beerli/coalescent-intro.pdf`.
   Extra files that go with a talk (a script, a small dataset) go in the **same folder**. Please see [Naming](#naming) for naming conventions. Note that large files and PDFs are stored with Git LFS, so check [Git LFS](#git-lfs) for more information.
3. **For a lab:** put your files in `labs/<lab-name>/` and update that folder's `README.md`. Please see [Naming](#naming) for naming conventions.
4. **Commit and open a pull request.** The maintainer reviews and merges.

That's the whole process. The two sections below are only if you need the details.

- [Naming — where files go and what to call them](#naming)
- [One-time setup: install Git LFS](#git-lfs)

---

## Naming conventions {#naming}

- **Slides live in your faculty folder:** `lectures/<your-last-name>/` (lowercase, e.g.
  `beerli`, `solis-lemus`).
- **Name each file for the talk**, lowercase and hyphenated, no year:
  `coalescent-intro.pdf`, `model-selection.pdf`. (The year is recorded automatically when
  the workshop's materials are archived, so you don't put it in the filename.)
- **Two talks?** Just give them different names: `coalescent-intro.pdf`,
  `coalescent-extending.pdf`.
- **Files that go with a talk** (a script, a dataset) share the slide's name so they sit
  together: `coalescent-intro.pdf` and `coalescent-intro-sim.R`.
- **Hosting your slides on Figshare or your own site instead?** Then don't add anything here
  in moledata. Your **link** goes on the schedule instead. Open a pull request on the
  **website** repo
  ([molevolworkshop.github.io](https://github.com/molevolworkshop/molevolworkshop.github.io))
  adding your link to `schedule.md` for your talk. (Or email the director the link and they'll
  add it.)

---

## One-time setup: install Git LFS {#git-lfs}

Large files (PDFs, big datasets) are stored with
[Git Large File Storage](https://git-lfs.com/), so you need it installed **before you
push**; otherwise you'd upload broken placeholder files instead of the real slides.

Install once per computer:

- **macOS:** `brew install git-lfs`
- **Windows:** installer at [git-lfs.com](https://git-lfs.com/) (or `winget install GitHub.GitLFS`)
- **Linux (Debian/Ubuntu):** `sudo apt install git-lfs`

Then, once, run:

```
git lfs install
```

That's it! From then on large files are handled automatically.

_(Or skip all of this and email your files to the director.)_
