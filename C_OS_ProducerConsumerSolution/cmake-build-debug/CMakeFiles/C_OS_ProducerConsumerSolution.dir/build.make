# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2021.1.2\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2021.1.2\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/C_OS_ProducerConsumerSolution.dir/depend.make
# Include the progress variables for this target.
include CMakeFiles/C_OS_ProducerConsumerSolution.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/C_OS_ProducerConsumerSolution.dir/flags.make

CMakeFiles/C_OS_ProducerConsumerSolution.dir/main.c.obj: CMakeFiles/C_OS_ProducerConsumerSolution.dir/flags.make
CMakeFiles/C_OS_ProducerConsumerSolution.dir/main.c.obj: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/C_OS_ProducerConsumerSolution.dir/main.c.obj"
	C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\C_OS_ProducerConsumerSolution.dir\main.c.obj -c C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution\main.c

CMakeFiles/C_OS_ProducerConsumerSolution.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/C_OS_ProducerConsumerSolution.dir/main.c.i"
	C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution\main.c > CMakeFiles\C_OS_ProducerConsumerSolution.dir\main.c.i

CMakeFiles/C_OS_ProducerConsumerSolution.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/C_OS_ProducerConsumerSolution.dir/main.c.s"
	C:\MinGW\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution\main.c -o CMakeFiles\C_OS_ProducerConsumerSolution.dir\main.c.s

# Object files for target C_OS_ProducerConsumerSolution
C_OS_ProducerConsumerSolution_OBJECTS = \
"CMakeFiles/C_OS_ProducerConsumerSolution.dir/main.c.obj"

# External object files for target C_OS_ProducerConsumerSolution
C_OS_ProducerConsumerSolution_EXTERNAL_OBJECTS =

C_OS_ProducerConsumerSolution.exe: CMakeFiles/C_OS_ProducerConsumerSolution.dir/main.c.obj
C_OS_ProducerConsumerSolution.exe: CMakeFiles/C_OS_ProducerConsumerSolution.dir/build.make
C_OS_ProducerConsumerSolution.exe: CMakeFiles/C_OS_ProducerConsumerSolution.dir/linklibs.rsp
C_OS_ProducerConsumerSolution.exe: CMakeFiles/C_OS_ProducerConsumerSolution.dir/objects1.rsp
C_OS_ProducerConsumerSolution.exe: CMakeFiles/C_OS_ProducerConsumerSolution.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable C_OS_ProducerConsumerSolution.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\C_OS_ProducerConsumerSolution.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/C_OS_ProducerConsumerSolution.dir/build: C_OS_ProducerConsumerSolution.exe
.PHONY : CMakeFiles/C_OS_ProducerConsumerSolution.dir/build

CMakeFiles/C_OS_ProducerConsumerSolution.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\C_OS_ProducerConsumerSolution.dir\cmake_clean.cmake
.PHONY : CMakeFiles/C_OS_ProducerConsumerSolution.dir/clean

CMakeFiles/C_OS_ProducerConsumerSolution.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution\cmake-build-debug C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution\cmake-build-debug C:\Programming\DSA\OS\C_OS_ProducerConsumerSolution\cmake-build-debug\CMakeFiles\C_OS_ProducerConsumerSolution.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/C_OS_ProducerConsumerSolution.dir/depend

