import sys

categories = ["Biography", "Comedy", "Detective Fiction", "Drama", "Fantasy", "Fiction", "Horror", "Nonfiction", "Romance", "Science Fiction", "Thriller"]


def display_percent(current, total, prefix=""):
    current_percent = current * 100 / total
    sys.stdout.write("\r")
    sys.stdout.write("%s[%-20s] %d%%" % (prefix, '='*int(current_percent/5), current_percent))
    sys.stdout.flush()
