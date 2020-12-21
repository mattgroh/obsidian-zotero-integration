# Zotero Obsidian Integration

Here's an initial hack to integrate Zotero into Obsidian by (1) copying all .pdfs from Zotero into Obsidian (2) creating markdown files with metadata on. This gets some of the integration started and it's a simply, hacky Python script (as opposed to a built-in Obsidian or Zotero extension).

## Copy .pdfs from Zotero to Obsidian and create markdown files with .pdf metadata

Step 1 – Download a .csv of your Zotero library. In Zotero, go to File > Export and export as .csv.

Step 2 – Run zotero2obsidian.py

`python zotero2obsidian.py zotero_filepath obsidian_filepath library_filepath markdown_folder`

where zotero_filepath is where the zotero .pdfs are, obsidian_filepath is where you want the .pdfs in obsidian, library_filepath is where the exported Zotero library .csv is, and markdown_folder is where you want your markdown files to live

For example, here's how I run the script on my computer.

`python zotero2obsidian.py /Users/heart/Zotero/storage/ /Users/heart/mindspace/pdfs/zotero/ library.csv /Users/heart/mindspace/zotero\ research/`

## 

