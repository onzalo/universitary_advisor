# -*- coding: utf-8 -*-
# intente algo como
def index():
    grid = SQLFORM.grid(db.estado_academico, maxtextlength=150)
    return dict(message="hello from estado_academico.py", grid=grid)
