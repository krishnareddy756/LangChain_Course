# Contribution Guidelines

These guidelines outline the workflow for creating and publishing new chapters
to the course.

## Creating a Chapter

We create a new chapter by adding a new directory, providing a complete
venv via `uv`, and adding the relevant learning material. Let's work through
an example chapter called `example-chapter`.

```
# first we create our new chapter directory and project env (from project root)
uv init example-chapter --python 3.12.7
# navigate into the new chapter directory
cd example-chapter
# delete unecessary hello.py file
rm hello.py
# add jupyter notebook support (if needed)
uv add ipykernel
# add required libraries, for example:
uv add numpy transformers
# confirm all functional and syncronized
uv sync
# open your project in an editor
cursor .  # run via Cursor
code .    # run via VS Code
```