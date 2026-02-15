# Klausmeier-Gray-Scott simulation project

A final project for `Deterministic modelling` course.
It is focused on theoretical analysis and interactive simulations of the model. 

Key features
- Scripts for theoretical and numerical analysis.
- Interactive Streamlit app with Plotly visualizations.
- Example simulation results and media in the `data/` folder.

Quick start
1. (optional) Create and activate a Python virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
2. Install dependencies from the bundled `requirements.txt`:
```powershell
pip install -r requirements.txt
```
3. Run the Streamlit app (example):
```powershell
streamlit run app\\Klausmeier_Gray_Scott_model.py
```
4. Open the URL provided by Streamlit (default: http://localhost:8501) to view the interactive app and visualizations.

Project layout (important files)
- `app/` - Streamlit application files (views and pages).
- `app/pages/` - individual Streamlit pages (tabs).
- `pipeline/` - model, solver and analysis modules.
- `data/` - simulation outputs for bif diagram (.csv), images and animations.
- `notebooks/` - notebooks on pattern gallery and bifurcation diagram.

License
- This project is licensed under the MIT License — see the `LICENSE` file for details.

Author / contact
- Jan Żurek
