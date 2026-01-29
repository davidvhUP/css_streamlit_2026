#!/usr/bin/env python3

import streamlit as st
import py3Dmol
from stmol import showmol

st.title("Interactive 3D PDB Viewer")

with open("p53_and_chain.pdb", 'r')as file:

    if file is not None:
        # Read the uploaded PDB content
        pdb_string = file.read()
        
        view = py3Dmol.view(width=800, height=500)
        view.addModel(pdb_string, "pdb")
        protein_sel = {'chain': 'A'}          
        nucleic_sel = {'chain': 'B'}
        view.setStyle({'cartoon': {'color': 'spectrum'}})      
        view.addSurface(
            py3Dmol.VDW,                      
            {'opacity': 0.6, 'color': 'white'},  
            protein_sel                                
        )
        view.setStyle(nucleic_sel, {
            'cartoon': {'radius': 0.2, 'colorscheme': 'Jmol'}  # Jmol colors: A=green, C=red, G=orange, T/U=blue
        })
        view.rotate(58, 'z')
        view.zoomTo()
        view.spin('vy', speed=0.25)
        showmol(view, height=600, width=1200)

    else:
        st.info("Upload a PDB file or enter a PDB ID above.")
