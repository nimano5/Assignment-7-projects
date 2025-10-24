# A. Import the sqlite library
import sqlite3

def getAllMovies():
    try:
        # A. Connection to the database
        conn = sqlite3.connect('movies.db')

        # B. Create a workspace (aka Cursor)
        cursorObj = conn.cursor()

        # D. Run the SQL Select statement to retive the data
        cursorObj.execute('SELECT Title, YearReleased, ImageName FROM Movies;')

        # E. Tell Pyton to 'fetch' all of the records and put them in
        #     a list called allRows
        allRows = cursorObj.fetchall()  #allRows have all teh results of the table 

        movieListOfDictionaries = []

        # F. Loop through the list of records and create a dictionary for each record
        for individualRow in allRows:
            m = {"Title" : individualRow[0], 
                 "Year": individualRow[1], 
                 "Image":individualRow[2] }
            # G. Append the dictionary to the list of dictionaries
            movieListOfDictionaries.append(m)

        # H. Close the connection to the database
        if conn:
            conn.close()

        #raise Exception("This is a generic error.")

        return movieListOfDictionaries
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return [{"Title" : "Error", "Year": 0000, "Image": "error.png" }]
