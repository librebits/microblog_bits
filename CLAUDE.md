# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask microblog application based on Miguel Grinberg's Flask Mega-Tutorial (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). The project is in early development stages, currently implementing the foundational Flask application structure.

## Architecture

The application follows Flask's application factory pattern:

- `microblog.py` - Application entry point that imports the Flask app instance
- `app/__init__.py` - Creates the Flask application instance and imports routes
- `app/routes.py` - (To be created) Contains route handlers and views
- `venv/` - Python virtual environment (excluded from git)

The circular import pattern used here is a standard Flask idiom: `app/__init__.py` imports from `app.routes` at the bottom of the file to avoid circular dependencies.

## Development Commands

### Running the Application

```bash
# Activate virtual environment
source venv/bin/activate

# Set Flask application entry point
export FLASK_APP=microblog.py

# Run development server
flask run
```

### Environment Setup

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask
```

## Current Issues

See `BUGS.org` for tracked issues. The main known issue is a missing `app/routes.py` file causing an ImportError on startup.

## Tutorial Reference

This project follows the Flask Mega-Tutorial series. See `README.md` for the complete list of tutorial chapters (23 chapters total covering topics from basics to deployment, APIs, background jobs, etc.).
