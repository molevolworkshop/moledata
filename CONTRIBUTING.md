# Contributing to moledata

This repository holds the **lecture slides** and **lab materials** for the Workshop on
Molecular Evolution (MOLE). This page is for faculty adding or updating their materials.

---

## How to contribute

Contributions should be done by either creating a GitHub issue or by creating a Pull Request directly.
We have GitHub issue templates for both [lecture](https://github.com/molevolworkshop/moledata/issues/new?template=update-lecture.yml) and [lab](https://github.com/molevolworkshop/moledata/issues/new?template=update-lab.yml) materials submissions, respectively.
Filling out these templates is recommended because will automatically format the data, update metadata files as needed, and submit a Pull Request on your behalf. 
If submitting a Pull Request directly, you will need to fork the [moledata repo](https://github.com/molevolworkshop/moledata) and ensure that your materials are appropriately formatted (see below).

 **Don't want to deal with GitHub?** Email your slides or lab files to the workshop
> director and they'll add them for you.


## Materials registry
We keep a registry of the current labs and lectures in [materials-registry.csv](https://github.com/molevolworkshop/moledata/blob/main/_data/materials-registry.csv).
Find or add the relevant lab/lecture for your materials. The element in the `item_id` column will be name of the folder containing your materials and will be how the website paths to and locates certain materials. 
The specific location of the materials depend on whether it is designated as a `lab` or `lecture`. For example, the materials corresponding to the IQ-Tree lab (with `item_id` `iqtree-lab`) are stored in `moledata/labs/iqtree-lab`.
If lab or lecture materials are stored off-site (e.g., on Figshare or a personal github), you should update the `material_location` in the `materials-registry.csv` with a link to the specific materials.*
If the materials are stored on-site and in the appropriate location, you should leave `material_location` blank as the site will parse this location automatically. 

## Materials formatting 

### Lectures

For a given lecture topic the specific materials should be in the appropriate folder (e.g., `/lectures/lecture_id`).
There are two things we desire in this folder:

1. **The lecture itself**: This should be a PDF with the slides for the lecture (e.g., `/lectures/lecture_id/lecture_id.pdf`). If the lecture contains multiple presentations, please create a separate topic for each segment. 
2. A **README.md** file that contains a brief overview of the topic, learning objectives, and any relevant attribution (if relevant).

Extra files that go with a talk (a script, a small dataset) go in the **same folder**.
Please see [Naming](#naming-conventions) for naming conventions.
Note that large files and PDFs are stored with Git LFS, so check [Git LFS](#one-time-setup-install-git-lfs) for more information.

### Labs

Put your files in `labs/lab_id`.
If stored on-site, lab materials folders should have this structure:

- A **README.md** that contains the actual lab itself and instructions for running thru the lab. These can use markdown formatting for 
- A **/scripts/** folder that contains any relevant scripts used in the analysis. Ideally, one should be able to perform a given analysis by directly by calling the relevant scripts without having to move move or reformat any files (requiring intermediate files from previous analyses is fine).
- A **/data/** folder that contains all relevant files needed for analyses. 
- An **/output/** that stores any generated output from the analyses ran in the **/scripts/** folder and may be pre-populated with intermediate results or pre-given sample outputs. 
- Any other files that might be relevant to the lab (additional markdowns, reading, references, related lab exercises, etc.) can be stored in additional folders or at the base directory for the lab.
The [lab GitHub issue template](https://github.com/molevolworkshop/moledata/issues/new?template=update-lab.yml) is great for automatically uploading your materials while following these conventions

---

## Naming conventions

- `item_id`'s should use slug casing, i.e., lowercase words separated by hyphens.
- Slides should be named after the item_id and stored in a folder of the same name. E.g., `lectures/intro-phylogenetics/intro-phylogenetics.pdf`
  `beerli`, `solis-lemus`).
- If giving more than one talk (or a talk is split into multiple parts, each talk should be registered on the `materials-registry.csv` and uploaded separately.
- **Hosting your slides or labs on Figshare or your own site instead?** Then don't add anything here
  in moledata. Your **link** should to the materials should be put in the `material_location` column of the `registry-materials.csv`

---

## One-time setup: install Git LFS

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
