# A-Quantitative-Review-of-Deep-Learning-Architectures-for-Tropical-Cyclone-Track-Forecasting

# UGDE Calculator (GUI Version)

A lightweight graphical tool for calculating **Unified Ground Distance Error (UGDE)** from latitude and longitude errors in degrees.  
Supports both **MAE** and **RMSE** input modes.

> UGDE = combined great-circle distance error, useful for evaluating spatial accuracy in geoscience and meteorological prediction tasks.



## Features

- Cross-platform GUI (macOS `.app` / Windows `.exe`/ Ubuntu)
- Supports MAE and RMSE modes
- Real-time distance calculation in kilometers
- Clean and simple user interface
- No Python installation required (precompiled executables)



## Downloads

| Platform | Format |     Download        |
|----------|--------|---------------------|
| macOS    | .app   | ugde_gui_mac.zip    | 
| Ubuntu   |  N/A   | ugde_gui_ubuntu.zip |
| Windows  | .exe   | [Coming soon](#)    |

> You can also clone the source code and build the executable using Python + PyInstaller.



## How to Use

### 1. Launch the Application

- **macOS**: Double-click `ugde_gui.app` (may require right-click > Open on first launch)
- **Windows**: Double-click `ugde_gui.exe` (click “More info” > “Run anyway” if SmartScreen appears)
- **Ubuntu**: chmod +x dist/ugde_gui and then Double-click `ugde_gui` 

### 2. Enter the following values:

 **Error Type** : Select either MAE or RMSE 
 **Latitude Error (°)** : The error in latitude direction 
 **Longitude Error (°)** : The error in longitude direction 
 **Reference Latitude (°)** : Used to convert degree to km (cosine scaling) 

Then click **"Calculate UGDE"**.



### Example

Input:
- Error Type: `MAE`
- Latitude Error: `0.3`
- Longitude Error: `0.4`
- Reference Latitude: `15.0`

Output:
