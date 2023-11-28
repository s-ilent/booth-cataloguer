# Booth Cataloguer
This is a set of two scripts that will let you create a catalogue of your Booth library.
* The **Booth Cataloguer Extract** will convert a set of saved web pages into a JSON and CSV file that can be parsed easily.
* The **Application** will serve a web page with a searchable index of the items in the library, using the JSON.

## How do I use this?
You'll need to download your library webpages so it can parse them, and then run the extractor. After that, you can generate the catalogue.

#### Create the catalog
To run the script, you'll need `pandas`, `json`, and `BeautifulSoup`.

1. Save each page of your Booth library to a folder. 
2. Update folder_path in the extractor script to point to your folder.
3. Run the script.

Easy! In the future this process can probably be automated.

#### Generate the website
The easiest way to do things is to generate a static copy. To generate the website, you'll need `Flask`.

1. Use the extractor to save your library details to a JSON file. 
2. Update generate_catalogue.py with the location of your library's JSON file.
3. Run!
4. Move output.html to the folder with your saved library. This will allow it to load the saved thumbnail images. 


#### Start the website
Running the website live is useful for debugging. To start the website, you'll need `Flask`. The live version expects a file structure like so; run_catalogue.py on the root directory, and your downloaded pages in a subfolder with the same name as your JSON. 

1. Use the extractor to save your library details to a JSON file. 
2. Update run_catalogue.py with the location of your library's JSON file.
3. Run the script.

## Future Ideas
- Automatically downloading the library would be useful.
- It might be cool to do more with the library page.
- The CSV isn't used for anything.

## License?
MIT license.