# Autogen Agent Template

Autogen Agent Template Python-based project designed to provide advanced tools and services for data processing, analysis, and automation. The project is structured to support modular development with clear separation of concerns, including core configurations, language model integrations, service layers, and user interface components.

## Features

- Core configuration and logging utilities
- Integration with language models for advanced processing
- Modular services for application monitoring and prompt handling
- User interface components for interactive usage

## Project Structure

- `app/` - Main application package
  - `core/` - Core utilities including configuration, constants, and logging
  - `llm/` - Language model clients and agents
  - `notebooks/` - Jupyter notebooks for experimentation and analysis
  - `services/` - Application services such as monitoring and prompt handling
  - `ui/` - User interface components
  - `utils/` - Utility tools and prompts
- `exports/` - Exported files and outputs
- `README.md` - Project documentation
- `.gitignore` - Git ignore rules
- `.python-version` - Python version specification
- `pyproject.toml` - Project metadata and dependencies
- `uv.lock` - Lock file for dependencies

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd autogen-agent-template
   ```

2. Install dependencies using uv:
   ```bash
   uv install
   uv sync
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

## Usage

Run the main application UI:

```bash
chainlit run app/main.py
```
