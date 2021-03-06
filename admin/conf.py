# -*- coding: utf-8 -*-
exec(open("../conf.py").read())
# -- General -------------------------------------------------------------------
project = '%s Administrator Guide' % product_name

# -- Options for HTML output ---------------------------------------------------
html_title = "%s (%s)" % (project, release)

# -- Options for LaTeX output --------------------------------------------------
latex_elements = {
    'figure_align': 'H'}

latex_documents = [
    ('index', '%s-admin.tex' % product_key, project, project_author, 'manual'),
]

# -- Options for Epub output ----------------------------------------------
epub_title = project
