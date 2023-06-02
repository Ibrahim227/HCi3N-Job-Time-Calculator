from cx_Freeze import setup, Executable

# Set up the path to my script
script_path = "hci3n-gui-app - Copy.py"

# Create the executable
exe = Executable(
    script=script_path,
    base="Win32GUI",
    icon="images/logoHCi3N.ico",
)

options = {
    "build.exe": {
        "include": ["cx_Freeze"],
        "include_files": ["images", ".github", ".pytest_cache"],
    }
}

# Create the setup
setup(
    name="HC3N",
    version="1.0",
    description="My Application Description",
    options=options,
    executables=[exe]
)
