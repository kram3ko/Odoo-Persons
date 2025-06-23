![odo2](https://github.com/user-attachments/assets/f41f3e62-b777-4669-84c9-e4851b3fd792)
![odo1](https://github.com/user-attachments/assets/e54bcf71-3ba3-4fb7-834d-b4898526d041)

# Odoo

Odoo is an open-source suite of web applications for business management.

## Quick Start

1. Clone the repository:

```bash
git clone https://github.com/kram3ko/Odoo-Persons.git
cd <your-project-folder>
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
