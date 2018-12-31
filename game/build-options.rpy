init python:
    build.classify('game/saves/**.**', None)
    build.classify('game/cache/**.**', None)
    build.classify('game/**.rpy', None)
    build.classify('game/**.rpym', None)
    build.archive("content", "all")
    build.classify('game/**.**', 'content')
