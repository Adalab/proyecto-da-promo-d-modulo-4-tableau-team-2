# Guardia Datil – True Crime Analysis

A project developed by data intelligence and analysis specialists to process criminal data.

---

## Team Guardia Datil

A multidisciplinary team combining field tactics, technology, and strategic analysis to uncover hidden criminal patterns:

- **Andrea** – Special Investigation Corporal – Rural Unit of Tedin (Galicia)  
- **Cristina** – Field Operations Brigade – Criminal Intelligence Unit of Toledo  
- **Mai** – Reconnaissance Lieutenant – Strategic Analysis Unit of Jaén  
- **Elena** – Technical Support Sergeant – Technology and Records Unit of Granada  

---

## Project Objective

The objective of the project is to investigate and analyse data on serial killers on a global scale. Utilising data science, web scraping, and data visualisation techniques, our objective was to identify patterns in profiles, weapons, number of victims, motivations, and other key variables.

---

## Project Structure

### 1. Original datasets

We started from several datasets found on Kaggle containing basic information about serial killers. These files can be found in the `Primary database/` folder.

### 2. EDA and data cleaning

We performed exploratory data analysis and cleaning to:

- Remove duplicates and inconsistent records  
- Normalize categories (countries, weapons, charges...)  
- Prepare the dataset for enrichment and visualization

> Notebook: `EDA y limpieza.ipynb`

### 3. Web scraping and enrichment

We used web scraping (mainly Wikipedia) to enrich the dataset with additional details such as:

- Weapons used by each killer  
- Specific crime types (e.g., cannibalism, child abuse, sexual violence)

> Script: `web scraping 1.ipynb`

### 4. Final dataset

The final version, `Final-data/final_final.csv`, contains one row per killer per country, with all fields cleaned and enriched for further analysis.

---

## Data visualization with Tableau

The core part of our analysis was carried out in **Tableau**, where we built a set of interactive dashboards stored in the file `LibroCasiFinal_06.04 con KPI.twbx`.

We visualized key patterns through views focused on:

- Geographic distribution of killers  
- Weapons and crime typologies  
- Evolution by decade  
- Victim count vs method used

We also created a custom color palette, which was added as a default theme in Tableau to maintain consistent visual identity across all dashboards.

The result is a collection of clear and unified visualizations, accessible to both technical and non-technical audiences.

---

## Tools used

- **Python**  
  - `pandas`  
  - `numpy`  
  - `requests`  
  - `beautifulsoup4`  
- **Jupyter Notebook**  
- **VS Code**  
- **Tableau**  

---

Thank you for reviewing our work.  
Mission accomplished. Until the next case...

— Guardia Datil, because even the darkest crimes leave traces in the data



