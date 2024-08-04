# Text-Detection-and-Recognition-with-EasyOCR
This project demonstrates how to use EasyOCR with OpenCV and Matplotlib to detect and recognize text in an image. The code utilizes the GPU if available, providing a faster processing speed.

Here's a sample README file for your code, including a section for the license. This README provides an overview of the project, setup instructions, usage guidelines, and the license information.

---

# Text Detection and Recognition with EasyOCR

This project demonstrates how to use EasyOCR with OpenCV and Matplotlib to detect and recognize text in an image. The code utilizes the GPU if available, providing a faster processing speed.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

To run this code, you'll need to install the following Python packages:

- [OpenCV](https://opencv.org/)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [Matplotlib](https://matplotlib.org/)
- [PyTorch](https://pytorch.org/) (with CUDA support if you have a compatible GPU)

### Installing Required Packages

You can install the required packages using the following command:

```bash
pip install opencv-python-headless easyocr matplotlib torch torchvision torchaudio
```

Ensure that you have the CUDA toolkit and appropriate drivers installed if you plan to use a GPU.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Replace the Image Path:**
   Edit the `image_path` variable in the script with the path to your image file.

3. **Run the Script:**
   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the name of your Python script file.

## License
This project is licensed under the MIT License.

## Contributing

Feel free to fork this repository and submit pull requests for any enhancements or bug fixes.

