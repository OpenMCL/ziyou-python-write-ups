# 簡明 Python 學習講義：習題解答集

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

國立中央大學吳維漢教授一著「[簡明 Python 學習講義](https://www.books.com.tw/products/0010811676)」的習題解答集、暨 MCL 工讀生合著紀念集。

## Build Documents

Make sure you already have a XeLaTeX complier (to write documents), and a proper Python interpreter (to write codes).

Then, clone the project first (with submodules):

```sh
git clone --recurse-submodules https://github.com/OpenMCL/ziyou-python-write-ups
```

Enter the project, and run the following command to build the document:

```sh
xelatex docs/main.tex
xelatex docs/main.tex
```

or simply run `make docs` if you have `make`.

This would output a pdf file called `main.pdf` at the project root folder.

## Contribution

We would love to accept your patches to this project. There are some guidelines
you need to follow:

### Coding Style

- Please follow [PEP8](https://peps.python.org/pep-0008/). We recommend you
  check your patch with [Flake8](https://flake8.pycqa.org/).
- In addition, please format your code with
  [Black](https://github.com/psf/black).

We recommend you use [VS Code](https://code.visualstudio.com/) to write code
with ease. You can put the following settings to
`${workspaceFolder}/.vscode/settings.json`:

```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true
}
```

### Peer Review

All submissions require review. We use GitHub (or GitLab) pull requests and
review systems to meet these requirements. See
[help](https://help.github.com/articles/about-pull-requests/) here for more
information on using GitHub pull requests.

## License

- All Python implementations are released under the [BSD-3-Clause
  License](LICENSE).
- The LaTeX template [ElegantBook](https://elegantlatex.org/) used in this
  project is released under the [LaTeX Project Public License](LICENSE.LPPL),
  v1.3c or later.
- Both fonts [源流明體](https://github.com/ButTaiwan/genryu-font) and
  [源樣黑體](https://github.com/ButTaiwan/genyog-font) used in this project
  are released under the [SIP Open Font License](LICENSE.SIL) Version 1.1.
