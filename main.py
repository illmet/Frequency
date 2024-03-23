from processing import process_data

def get_data():
    posts = process_data("data/posts", "content")
    comms = process_data("data/comments", "body")
    al = posts + comms
    return al

