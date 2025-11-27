A poorly written animation

# A Silly Animation

She was never alone

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Clone the Repository](#clone-the-repository)
3. [Set Up Conda Environment](#set-up-conda-environment)
4. [Installation](#install-ffmpeg)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Running Tests](#running-tests)
8. [Contributing](#contributing)
9. [License](#license)

---

## Prerequisites
Make sure you have the following installed on your system:

- [Git](https://git-scm.com/)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution)
- Python >= 3.x (if not using Conda environment)


---

## Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/samdong2101/A-Silly-Animation.git
cd A-Silly-Animation
```
---
## Set up conda environment
```bash
conda env create -f environment.yml
conda activate silly-animation
```
## Install ffmpeg 
```bash
cd $HOME
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar -xvf ffmpeg-release-amd64-static.tar.xz
export PATH=$HOME/ffmpeg-{YOUR_VERSION}-static:$PATH
```



