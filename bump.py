with open("version.txt", "r") as f:
    major, minor, patch = map(int, f.read().split("."))
    patch += 1
    if patch == 10:
        patch = 0
        minor += 1
    if minor == 10:
        minor = 0
        major += 1

    with open("version.txt", "w") as f:
        f.write(f"{major}.{minor}.{patch}")
