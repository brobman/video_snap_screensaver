from distutils.core import setup
import py2exe

opencv_lib_src = os.path.join(os.path.dirname(cv2.__file__), "..", "opencv_python.libs")
opencv_lib_dst = os.path.join("lib", "opencv_python.libs")
build_exe_options = {
    "packages": ["os"],
    "excludes": [],
    "include_files": [(opencv_lib_src, opencv_lib_dst)],
}

setup(
    name="VideoSnapScreensaver",
    console=["main.py"],
    options={
        "py2exe": {"packages": ["sys", "os", "random", "cv2", "numpy"]},
        "include_files": [(opencv_lib_src, opencv_lib_dst)],
        "add_to_path": True,
    },
)


## > cxfreeze -c main.py --target-dir dist
