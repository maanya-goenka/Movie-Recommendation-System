from csv import reader
import pandas as pd

movieData = pd.read_csv('movies.csv')
movieData2 = pd.read_csv('imdb.csv')

def extractMovieTitleAndYear(movieTitle):
    year = movieTitle[len(movieTitle)-5:len(movieTitle)-1]
    if year.isnumeric() == False:
       return movieTitle, None
    else:
        title = movieTitle[:len(movieTitle)-7]
        return title, int(year)

# uses the imdb.csv dataset
def imdbExtraction():
    movieId = []
    movieTitle = []
    movieFeatures= []
    count = 0
    with open('imdb.csv', 'r') as readObject:
        csvReader = reader(readObject)
        header = next(csvReader)
        for line in csvReader:
            count += 1
            # we are using genres, director, and cast to make recommendations
            movie_id = line[0]
            movieId.append(movie_id)
            title = line[2]
            movieTitle.append(title)
            movieGenres = line[5].replace("-", "")
            movieDirector = line[9]
            movieCast = line[12]
            movieFeatures.append(movieGenres + ' ' + movieCast + ' ' + movieDirector)

            # limiting the dataset to the first 50000 movies
            if count >= 25000:
                break

    moviesIMDB = pd.DataFrame({'Movie ID': movieId, 'Title': movieTitle, 'Features': movieFeatures})
    moviesIMDB.to_csv('movieData2.csv', header = True, index = False, sep=';', mode='a')

    return moviesIMDB

# uses the movies.csv dataset
def extractWeb():
    movieId = []
    movieTitle = []
    movieYear = []
    movieGenres = []
    count = 0
    with open('movies.csv', 'r') as readObject:
        csvReader = reader(readObject)
        header = next(csvReader)
        for line in csvReader:
            count += 1
            # we are using genres to make recommendations so if the genre is absent, we can remove that movie from the dataset
            if line[2]=="(no genres listed)":
                continue
            movieId.append(line[0])
            title, year = extractMovieTitleAndYear(line[1])
            movieTitle.append(title)
            if year == None:
                movieYear.append("N/A")
            else:
                movieYear.append(int(year))
            # replace hyphenated movie genres with non hyphenated ones
            movieGenres.append(line[2].replace("-", ""))

    movies = pd.DataFrame({'Movie ID': movieId, 'Title': movieTitle, 'Year': movieYear, 'Genre': movieGenres})
    movies.to_csv('movieData.csv', header = True, index = None, sep=';', mode='a')

    return movies
