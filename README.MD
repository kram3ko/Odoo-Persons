# Odoo

Odoo is an open-source suite of web applications for business management.

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/kram3ko/Odoo-Persons.git
cd <project-folder>
```

2. Install dependencies using [uv](https://github.com/astral-sh/uv):

```bash
pip install uv
uv sync
```

3. Start the project with Docker Compose:

```bash
docker compose up --build
```

4. Open your browser and go to [http://127.0.0.1:8069](http://127.0.0.1:8069)
   - Create a new database following the instructions on the page.

5. After the database is created, go to the Apps menu and install the "Persons" app.

6. You will then be able to access the persons management module at [http://127.0.0.1:8069/persons](http://127.0.0.1:8069/persons)

## Description

- The `addons/persons` directory contains the app for managing persons.

---

> Make sure you have Docker and Python 3.12+ installed for proper operation.
