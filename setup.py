import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "Snake Game",
    options = {"build_exe": {"packages":["pygame"],
                             "include_files": ["Snake.Py", "biteSound.wav"]}},
    executables = executables
)