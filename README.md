# lms-scripts
This script takes a list of SCORM files and replaces their broken dispatch file with a working dispatch file. It also bundles these individual files into their corresponding training style for a more organized view.

## Requirements

Python 3.x

## Usage

### Fixing Dispatch Files

1. Place the SCORM files that need their dispatch fixed into the fix_dispatch folder.
2. Run main.py.
3. Select option 1 labeled "Fix Dispatch Files".

The fixed SCORM files will be generated in the fixed_dispatch folder.

### Bundling Modules Flavors
1. Add the SCORM files that need to be bundled into the BundleFiles folder.
2. Run main.py.
3. Select option 2 labeled "Bundle Modules Flavors".

The bundled SCORM files will be generated in the bundled_modules folder.
