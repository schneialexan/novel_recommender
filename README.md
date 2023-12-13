<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br></h1>
<h3>Novel Recommender (novelupdates.com)</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat-square&logo=Streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white" alt="scikitlearn" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat-square&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat-square&logo=Jinja&logoColor=white" alt="Jinja" />
<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=flat-square&logo=SciPy&logoColor=white" alt="SciPy" />

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat-square&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON" />
</p>
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running ](#-running-)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

► https://novel-recommender.streamlit.app/)

---

## 📦 Features

► Make a Persona and get Novel based recommendations

► Make a Persona based history to then get recommendations based on that history

---


## 📂 Repository Structure

```sh
└── /
    ├── .devcontainer/
    │   └── devcontainer.json
    ├── book_recommendations_tfidf.py
    ├── data_exploration.ipynb
    ├── data_scraper/
    │   ├── create_graph.ipynb
    │   ├── requirements.txt
    │   ├── scraper.py
    │   └── utils.py
    ├── helper/
    │   └── preprocessing.py
    ├── recommender_evaluation.py
    ├── user_book_history_recommender.py.py
    ├── user_book_similarity_recommender.py
    └── user_gen/
        ├── helper/
        │   └── preprocessing.py
        ├── requirements.txt
        └── synthetic_user_gen.py

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                               | Summary       |
| ---                                                | ---           |
| [book_recommendations_tfidf.py]({file_path})       | ► pure content-based |
| [data_exploration.ipynb]({file_path})              | ► Exploration |
| [recommender_evaluation.py]({file_path})           | ► Evaluation & Testing |
| [user_book_history_recommender.py.py]({file_path}) | ► Test the Synthetic Gen |
| [user_book_similarity_recommender.py]({file_path}) | ► Collaborative Filtering tests |
| [create_graph.ipynb]({file_path})                  | ► Creating the fancy Graph |
| [scraper.py]({file_path})                          | ► To scrap the data from the website |
| [utils.py]({file_path})                            | ► helper functions |
| [preprocessing.py]({file_path})                    | ► Make access to the scrapped data easier |
| [requirements.txt]({file_path})                    | ► For installations |
| [synthetic_user_gen.py]({file_path})               | ► Final Streamlit App |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

- ℹ️ python = 3.9 (this was only tested on 3.9)

### 🔧 Installation

1. Clone the  repository:
```sh
git clone git@github.com:schneialexan/novel_recommender.git
```

2. Change to the project directory:
```sh
cd novel_recommender
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running 

```sh
python synthetic_user_gen.py
```


---


## 🛣 Project Roadmap

> - [X] `ℹ️  Task 1: Content-Based Filtering
> - [X] `ℹ️  Task 2: Synthetic Persona-based history generation
> - [ ] `ℹ️  Task 3: Collaborative Filtering (with synthetic user-item generation)


---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/local//blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/local//discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/local//issues)**: Submit bugs found or log feature requests for LOCAL.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>


[**Return**](#Top)

---

