# Stripe Pattern Applier

This Streamlit application allows users to upload one or multiple images and apply a variety of stripe patterns. The available patterns include vertical stripes, diagonal stripes, horizontal stripes, and vertical concentrated stripes. The processed images can be downloaded individually or in a ZIP file.

## Features

- **Upload Single or Multiple Images**: Users can upload one or multiple images in common formats such as PNG, JPG, JPEG, BMP, or GIF.
- **Apply Stripe Patterns**: Users can apply one or all of the following stripe patterns:
  - **Vertical Stripes**
  - **Diagonal Stripes**
  - **Horizontal Stripes**
  - **Vertical Concentrated Stripes**
- **Download Processed Images**: After applying the pattern(s), users can download:
  - A single processed image, or
  - A ZIP file containing all processed images.
  
## How to Use

1. **Upload an Image**:
   - You can choose to upload a single image or multiple images using the file uploader.
   
2. **Choose a Pattern**:
   - Once the images are uploaded, you can choose to apply one or all of the available stripe patterns. 
   - The available patterns include:
     - Vertical Stripes
     - Diagonal Stripes
     - Horizontal Stripes
     - Vertical Concentrated Stripes

3. **Download**:
   - After applying the pattern(s), you can download:
     - **A single processed image** by clicking the "Download Processed Image" button.
     - **A ZIP file** containing all processed images if you choose to apply all patterns.

4. **Instructions**:
   - A sidebar provides instructions on how to use the app, and an expander shows information about the different stripe patterns.

## Prerequisites

To run the app locally, make sure you have the following installed:

- Python 3.7+
- Streamlit
- Pillow (PIL)
- numpy==1.26.3
- zipfile36

### Installing Dependencies

To install the necessary dependencies, you can use the following command:

```bash
pip install -r requirements.txt
```

Here’s the `requirements.txt`:

```txt
streamlit
Pillow
numpy==1.26.3
zipfile36
```

## Running the App

To run the Streamlit app locally, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/shukdevtroy/Stripe-Pattern-Applier.git
    cd Stripe-Pattern-Applier
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

4. Open your browser and go to `http://localhost:8501` to use the app.

## Example Images

Here are a few examples of the stripe patterns that can be applied:

- **Vertical Stripe Pattern**  
  ![Vertical Stripe Pattern](https://github.com/shukdevtroy/Stripe-Pattern-Applier/blob/main/images/Barcode%20Pattern.jpg)

- **Diagonal Stripe Pattern**  
  ![Diagonal Stripe Pattern](https://github.com/shukdevtroy/Stripe-Pattern-Applier/blob/main/images/Diagonal%20Stripes.jpg)

- **Horizontal Stripe Pattern**  
  ![Horizontal Stripe Pattern](https://github.com/shukdevtroy/Stripe-Pattern-Applier/blob/main/images/horizontal%20stripe%20pattern.jpg)

- **Vertical Concentrated Stripe Pattern**  
  ![Vertical Concentrated Stripe Pattern](https://github.com/shukdevtroy/Stripe-Pattern-Applier/blob/main/images/Vertical%20Concentrated.jpg)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Demo App

[Click to view the demo app](https://shukdevdatta123-stripe-pattern-applier.hf.space)


