import streamlit as st
import pandas as pd
import numpy as np
import py3Dmol
from stmol import showmol
import streamlit.components.v1 as components

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
menu = st.sidebar.radio(
    "Pages",
    ["About me", "Research Specializations", "Education"],
)

# Sections based on menu selection
#------------------------------------------------------------------------------------------------------------------------------------------------------# 
if menu == "About me":
    st.image( "linkedin-banner.png")

    st.markdown(
            """
            # About me
            Hi There, I'm David! I'm a Masters student at the University of Pretoria specialising in breast cancer genetics. I've always 
            had a passion for insight and intuition - whether it relates to my professional work, or baking sourdough bread. I've tried 
            my best to develop a keen eye for detail, along with the skills necessary to experiment and solve problems. In my free time I balance playing
            multiple musical instruments, playing DnD with friends, and I've recently taken up knitting.

            """,
            text_alignment='center'
            )
    
    st.set_page_config(layout="wide")


#----------------------------------------------------------------------------------------------------------------------------------------------#
elif menu == "Research Specializations":
    tab1, tab2 = st.tabs(["Nuclear Mechanobiology :microscope:", "Breast Cancer Genetics :dna:"])
    with tab1:
        st.markdown(
                """
                # Nuclear mechanobiology

                Most molecular biology deals with studying the chemical mechanisms that underly biological functions. This usually involves investigating how different chemical signals lead to responses by networks or proteins - ultimately leading to changes in gene expression, cell motility, cell growth etc. Mechanobiology approaches cellular biology from a different perspective entirely. This discipline is not purely biological, rather it lies at the intersection of molecular biology, engineering/mechanics, and computational science. Rather than investigating how cells respond to purely chemical stimuli, this discipline seeks to understand how cells perceive and respond to the mechanical aspects of their environment, such as different physical forces and substrate rigidity. 
                
                A further sub-domain of mechanobiology is nuclear mechanobiology. This specifically focuses on how the interface between the cytoskeleton and nucleoskeleton affects nuclear shape and function, including gene expression. In my final year of undergraduate study, I co-authored a review paper researching recent insights in this field. 
                My core contribution to this paper was reporting on recent investigations into the mechanism of nuclear rupture repair. During traumatic events in the cell due to mechanical stress or failure during cell division, part of the nucleus can rupture which could lead to anti-viral mechanisms in the cell degrading genomic DNA which can lead to catastrophic DNA damage and cell death. We found that the Barrier to Autointegration Factor (BAF) protein plays a critical role in the exposed DNA and catalysing the process of repairing the nucleus.

                Below is a PDF embed to the publication.
                """
                )
        st.divider()
        st.markdown("## Publication")
        st.pdf("VanHeerden_How_2024.pdf", height=450)
        st.caption("van Heerden D, Klima S, van den Bout I. How nuclear envelope dynamics can direct laminopathy phenotypes. Curr Opin Cell Biol. 2024 Feb;86:102290. doi: 10.1016/j.ceb.2023.102290. Epub 2023 Dec 3. PMID: 38048657.")
    with tab2:


        st.title("Breast cancer genetics")
        st.button("Reset")
        with open("p53_and_chain.pdb", 'r')as file:
            if file is not None:
                    # Read the uploaded PDB content
                with st.spinner("Loading PDB structure..."):
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
                    showmol(view, height=500, width=1200)
                st.caption("TP53 protein bound to a segment of DNA. TP53 has two domains; a major and minor binding domain. There are multiple amino acid residues that can interact with the DNA, but a single amino acid contact with the minor groove. The ability for TP53 to bind strongly to DNA, and maintain that bond, is critical to its function. Hence, any mutations that impeded this interaction could severly abrogate TP53 function i.e. DNA damage repair. (Derived from PDB structure 2AC0)")

elif menu == "Education":
    st.markdown(
            """
            # Education :mortar_board:
            ## BSc Biochemistry and Human Physiology
            I started my undergraduate studies in 2020. Beginning in UP's Biological Sciences program, I transferred to a dual-major in biochemistry and physiology. This program was largely beneficial in giving a comprehensive overview of human biology in the direction of both the micro- and macroscopic. Biochemistry gave me the opportunity to "zoom in" to structures and functions at the molecular level. Herein lies the basis of disease and drug interactions that form the basis of modern medicine. Physiology on the other hand, provided a "bottom-up" approach: allowing me to learn about each individual organ and organ system and how they interact to bring about higher order emergent physiological phenomena. 
            
            **Skills/Knowledge Acquired**
            - Understanding of principals in genetics and their applications
            - Microbiology, including bacterial and fungal
            - Nucleic acid, protein, lipid, and carbohydrate biochemistry
            - Biochemical lab experience: molecular cloning, column chromatography, SDS-PAGE, enzymology
            - Integrated physiological function

            ## BSc(Hons) Human Physiology
            My Honours year provided a window into deepening my understanding of human physiology at the molecular level - integrating the concepts I learned in undergrad. This honours program was composed of both course work along with a year-long research project. Rather than conducting a purely _in vitro_ study, I undertook a bioinformatics project analysing genomic breast cancer data to identify novel somtic mutations. This served as an exciting challenge to test the limits of my understanding of physiological function at the molecular level, but with the added challenge of analysing biological data through a different medium.
            """,
            text_alignment='center'
    )

