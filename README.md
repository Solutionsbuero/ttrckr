# ttrckr

Tinfoil Colloquy's barcode based Train Tracking. This application sources the video-stream from the camera by using OpenCV. This way, the focus of the camera can be manually adjusted. The scanning is done using the [ZBar Library](http://zbar.sourceforge.net/).


## Installation

This program relies on the OpenCV Library. For convenience this project uses the unofficial pre-built OpenCV binaries from [opencv-python](https://pypi.org/project/opencv-python/).

_Raspberry Pi:_ You have to add the [Piwheels](https://www.piwheels.org/) Wheel Repository to your system to obtain the OpenCV Binaries for your system.

_All Systems:_ Make sure you have the ZBar library installed:

```shell script
sudo apt-get install libzbar0
```

## Usage

You can change the parameters with the constants in the `ttrckr.py` file. To determine the correct focus you can increase/decrease the focus value by five pressing i/d key in the active output window.


## A word on the barcodes

- Use a single digit number (do not use characters for the moment).
- Example for a usable [barcode generator](https://products.aspose.app/barcode/generate).
- Recommended Code Type: Code 93 Standard.
- Use a scalable image format to ensure the best output quality.
- Our barcode size (printed): 120mm x 70mm.
- Use plain white paper and a high printer resolution.
