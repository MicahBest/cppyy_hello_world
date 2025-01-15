import cppyy
import os

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the paths to the header and library relative to this script
header_path = os.path.join(script_dir, "../src/hello.hpp")
library_path = os.path.join(script_dir, "../build/hello")

# Load the C++ header file
cppyy.include(header_path)

# Import the compiled C++ library
cppyy.load_library(library_path)

# Use the class from C++
HelloWorld = cppyy.gbl.HelloWorld
instance = HelloWorld()
instance.print()
