# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'reStructuredPython'
copyright = '2025, Rihaan Meher'
author = 'Rihaan Meher'

release = '2.4.0'
html_favicon = "_static/icon.png"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "red",
        "color-brand-secondary": "blue",
        "color-brand-content": "#CC3333",
        "color-admonition-background": "orange",
        "color-background-primary": "#e3f2fd",
    },
    "dark_css_variables": {
        "color-foreground-primary": "black",
        "color-brand-secondary": "blue",
        "color-foreground-secondary": "#5a5c63",
        "color-foreground-muted": "#6b6f76",
        "color-foreground-border": "#878787",
        "color-brand-primary": "red",
        "color-brand-content": "#CC3333",
        "color-admonition-background": "orange",
        "color-background-primary": "#e3f2fd",
        "color-background-secondary": "#f8f9fb",
        "color-background-hover": "#efeff4ff",
        "color-background-border": "#eeebee"
    },
    "announcement": '''
    
    <nav class="navbar">
    <a href="/"><div class="logo">reStructuredPython</div></a>
    <ul class="nav-links">
      <li><a href="https://restructuredpython.rf.gd/playground">Playground</a></li>
      <li><a href="https://restructuredpython.rf.gd#github">Open Source</a></li>
      <li><a href="https://restructuredpython.rf.gd#features">Features</a></li>
      <li><a href="/">Docs</a></li>
      <li><a href="https://restructuredpython.rf.gd#download">Download</a></li>
      <li><a href="https://restructuredpython.rf.gd#community">Community</a></li>
    </ul>
  </nav>
  <style>
  :root {
    --blue: #3178c6;
    --light-blue: #e3f2fd;
    --dark-text: #1a1a1a;
    --gray: #f5f5f5;
}

  nav.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    background: white;
    border-bottom: 1px solid #ccc;
}

.navbar .logo {
    font-size: 22px;
    font-weight: 700;
    color: var(--blue);
}

.nav-links {
    list-style: none;
    display: flex;
    gap: 20px;
}

.nav-links a {
    color: var(--dark-text);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
}

.nav-links a:hover {
    color: var(--blue);
} 
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
</style>
  ''',
}
