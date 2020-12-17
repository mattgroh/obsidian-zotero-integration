# Zotero Obsidian Integration

## Copy .pdfs from Zotero to Obsidian and create markdown files with .pdf metadata

Step 1 – Download a .csv of your Zotero library. Go to File>Export and export as .csv.

Step 2 – Run zotero2obsidian.py

`python zotero2obsidian.py zotero_filepath obsidian_filepath library_filepath markdown_folder`

where zotero_filepath is where the zotero .pdfs are, obsidian_filepath is where you want the .pdfs in obsidian, library_filepath is where the exported Zotero library .csv is, and markdown_folder is where you want your markdown files to live

For example, here's how I run the script on my computer.

`python zotero2obsidian.py /Users/heart/Zotero/storage/ /Users/heart/mindspace/pdfs/zotero/ library.csv /Users/heart/mindspace/zotero\ research/`

## 

