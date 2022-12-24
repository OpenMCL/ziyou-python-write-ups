DOCS_MAIN_TEX := docs/main.tex

.PHONY: docs lint

docs: $(DOCS_MAIN_TEX)
	xelatex $(DOCS_MAIN_TEX)
	xelatex $(DOCS_MAIN_TEX)

lint:
	flake8 src
