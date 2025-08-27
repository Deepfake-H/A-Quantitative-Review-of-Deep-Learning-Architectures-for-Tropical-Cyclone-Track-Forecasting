# A-Quantitative-Review-of-Deep-Learning-Architectures-for-Tropical-Cyclone-Track-Forecasting

# UGDE Calculator (GUI Version)

A lightweight graphical tool for calculating **Unified Ground Distance Error (UGDE)** from latitude and longitude errors in degrees.  
Supports both **MAE** and **RMSE** input modes.

> UGDE = combined great-circle distance error, useful for evaluating spatial accuracy in geoscience and meteorological prediction tasks.



## Features

- Cross-platform GUI (macOS `.app` / Windows `.exe`/ Linux)
- Supports MAE and RMSE modes
- Real-time distance calculation in kilometers
- Clean and simple user interface
- No Python installation required (precompiled executables)



## Downloads

| Platform | Format |     Download        |
|----------|--------|---------------------|
| macOS    | .app   | ugde_gui_mac.zip    | 
| Linux    |  N/A   | ugde_gui_Linux.zip  |
| Windows  | .exe   | ugde_gui_windows.zip|

> You can also clone the source code and build the executable using Python + PyInstaller.



## How to Use

### 1. Launch the Application

- **macOS**: Double-click `ugde_gui.app` (may require right-click > Open on first launch)
- **Windows**: Double-click `ugde_gui.exe` (click “More info” > “Run anyway” if SmartScreen appears)
- **Linux**: chmod +x dist/ugde_gui_linux && ./dist/ugde_gui_linux 

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


## If you need to use code or tool, please cite the paper "Beyond the Backbone: A Quantitative Review of Deep-Learning Architectures for Tropical Cyclone Track Forecasting".
