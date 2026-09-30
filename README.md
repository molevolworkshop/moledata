# mole-terials
Year-to-year lecture materials, tutorials, and reproducible software environment for the Workshop on Molecular Evolution at MBL, Woods Hole.

## Repository Structure
- **[`lectures/`](lectures/)**: Slide decks and overviews for workshop lectures.
- **[`labs/`](labs/)**: Tutorial data, code scripts, output examples, and lab walkthroughs.
- **[`_data/materials-registry.csv`](_data/materials-registry.csv)**: Registry mapping each item ID, title, category, presenter, and material location.
- **[`CONTRIBUTING.md`](CONTRIBUTING.md)**: Instructions for workshop faculty and contributors on adding and updating materials.

## Git Large File Storage (LFS)
To reduce repository size, this repo uses [Git Large File Storage (LFS)](https://git-lfs.com/) for PDFs, zipped archives, and large dataset binaries.
Before pushing changes, ensure Git LFS is installed and initialized on your system:
```bash
git lfs install
```
The [`.gitattributes`](.gitattributes) file specifies all file patterns managed by Git LFS.

## Progress & Roadmap
- [x] Metadata registry for lectures and labs (`_data/materials-registry.csv`)
- [x] Automated GitHub Issue templates & workflows for lecture and lab submission
- [x] Lab walkthroughs, datasets, and README documentation
- [ ] Track traffic and download data
- [ ] Publish archived release packages for each workshop year
- [ ] Scraper / synchronization for off-site materials (Figshare, external GitHub repos)

