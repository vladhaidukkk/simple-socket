def index() -> str:
    with open("views/index.html") as view:
        return view.read()


def blog() -> str:
    with open("views/blog.html") as view:
        return view.read()
