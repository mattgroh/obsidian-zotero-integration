import os
import shutil
import re
import sys
import pandas as pd

def collect_pdfs(zotero_filepath, obsidian_filepath):
    pdfs_source = []
    pdfs_destination = []
    for root, dirs, files in os.walk(zotero_filepath):
        for f in files:
            if f[-4:]==".pdf":
                pdfs_source.append(os.path.join(root,f))
                pdfs_destination.append(re.sub(" ", "_", re.sub(".*/","",re.sub(zotero_filepath,obsidian_filepath,os.path.join(root,f)))))
    df = pd.DataFrame({"source": pdfs_source, "destination":pdfs_destination})
    return df

if __name__ == "__main__":
    print("starting")
    # zotero_filepath = "/Users/heart/Zotero/storage/"
    # obsidian_filepath = "/Users/heart/mindspace/pdfs/zotero/"
    # library_filepath = "library.csv"
    # markdown_folder = "/Users/heart/mindspace/zotero research/"
    zotero_filepath = sys.argv[1]
    obsidian_filepath = sys.argv[2]
    library_filepath = sys.argv[3]
    markdown_folder = sys.argv[4]

    # Step 1 - Collect all .pdfs in Zotero directory and copy to Obsidian directory
    filepath_map = collect_pdfs(zotero_filepath, obsidian_filepath)
    for index, i in enumerate(filepath_map.source):
        print("Copying pdf #{}".format(index))
        shutil.copyfile("{}".format(i),"{}{}".format(obsidian_filepath,filepath_map.destination[index]))

    # Step 2  - Create markdown files in Obsidian with metadata from all Zotero pdfs

    df = pd.read_csv(library_filepath)
    df = df[["Key",'Author',"Date","Title","Short Title","Url",'File Attachments','Automatic Tags']]
    df.columns = ["key","authors","date","title","publication_title","url","zotero_filepath","tags"]
    df["obsidian_filepath"] = df.zotero_filepath.str.replace(zotero_filepath, '', regex=True)
    df["obsidian_filepath"] = df.obsidian_filepath.str.replace(".*/", '', regex=True)
    df["obsidian_filepath"] = df.obsidian_filepath.str.replace(" ", '_', regex=True)
    print(os.listdir(markdown_folder))
    for index, row in df.iterrows():
        row["title"] = re.sub("/","",row["title"])
        if "{}.md".format(row["title"]) not in os.listdir(markdown_folder):
            f = open("{}{}.md".format(markdown_folder, row["title"]), "w")
            f.write("""
    Title: [{}](pdfs/zotero/{})\n
    Authors: {}\n
    Notes:
            """.format(row["title"],row["obsidian_filepath"],row["authors"],))
            f.close()
    print("done")

