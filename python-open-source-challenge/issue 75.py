# ISSUE 75
#
# Problem:
# Write a program that accepts a list of movie records containing title, genre and rating and calculates the average rating for every genre.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def genre_ratings(movies):
    totals, counts = {}, {}
    for movie in movies:
        genre, rating = movie["genre"], movie["rating"]
        # TODO: Check how ratings are accumulated per genre.
        totals[genre] = totals.get(genre, 0) + rating
        counts[genre] = counts.get(genre, 0) + 1
    # TODO: Check the divisor used to calculate each genre average.
    return {genre: total / (counts[genre] + 1) for genre, total in totals.items()}

def check_solution():
    movies = [{"title":"A","genre":"comedy","rating":4},{"title":"B","genre":"comedy","rating":2},{"title":"C","genre":"drama","rating":5}]
    assert genre_ratings(movies) == {"comedy":3,"drama":5}
    assert genre_ratings([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
