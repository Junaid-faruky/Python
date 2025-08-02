import os

project_name = input("Project name: ")
description = input("Short description: ")
author = input("Author: ")

template = f"""# {project_name}

{description}

## Install

```bash
pip install -r requirements.txt
