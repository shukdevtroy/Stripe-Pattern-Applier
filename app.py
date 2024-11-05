import os
import zipfile
import streamlit as st
from PIL import Image, ImageOps
import io
import tempfile

# Load pattern images as in-memory objects
patterns = {
    1: "Barcode Pattern.jpg",  # Vertical stripes
    2: "Diagonal Stripes.jpg",  # Diagonal stripes
    3: "horizontal stripe pattern.jpg",  # Horizontal stripes
    4: "Vertical Concentrated.jpg"  # Vertical Concentrated stripes
}

# Function to apply selected pattern
def apply_pattern(image, pattern_id):
    """Apply selected stripe pattern to the given image."""
    original = image.convert("RGBA")
    pattern = Image.open(patterns[pattern_id]).convert("L")  # Convert pattern to grayscale
    
    # Create an alpha channel where white becomes transparent and black stays opaque
    transparent_pattern = Image.new("RGBA", pattern.size)
    for x in range(pattern.width):
        for y in range(pattern.height):
            pixel = pattern.getpixel((x, y))
            # If the pixel is black (0), set to opaque black; if white (255), set to transparent
            transparent_pattern.putpixel((x, y), (0, 0, 0, 255) if pixel < 128 else (0, 0, 0, 0))
    
    # Resize the transparent pattern to match the original image size
    transparent_pattern = ImageOps.fit(transparent_pattern, original.size, method=0, bleed=0.0, centering=(0.5, 0.5))
    
    # Overlay the transparent pattern on the original image
    combined = Image.alpha_composite(original, transparent_pattern)
    return combined

# Function to process and save the image with applied pattern
def process_image(image, pattern_id, image_name):
    """Apply the selected pattern to the uploaded image and save it to the output directory."""
    combined_image = apply_pattern(image, pattern_id)
    
    # Convert to RGB if saving as JPEG or PNG
    combined_image = combined_image.convert("RGB")
    
    # Save the processed image to a temporary in-memory buffer
    img_byte_arr = io.BytesIO()
    combined_image.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)  # Rewind the buffer to the beginning
    return img_byte_arr

# Function to create a ZIP file from a list of image paths
def create_zip_file(image_buffers, zip_filename):
    """Create a ZIP file from the processed images."""
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for idx, image_buffer in enumerate(image_buffers):
            # Save the image in memory with a unique name
            zipf.writestr(f"patterned_image_{idx + 1}.jpg", image_buffer.read())
    return zip_filename

# Streamlit UI
st.title("Stripe Pattern Applier")
st.write("Upload one or multiple images and apply a stripe pattern.")

# Sidebar with instructions
st.sidebar.title("Instructions")
st.sidebar.write("""
1. **Upload an Image**: Choose either a single image or multiple images by using the file uploader.
2. **Choose a Pattern**: You can either apply a **single pattern** or apply **all available patterns** to your uploaded images. 
3. **Download**: Once the images are processed, you can download the individual processed image(s) or download all processed images in a ZIP file.
4. **Pattern Options**: The available patterns include:
   - **Vertical Stripes**
   - **Diagonal Stripes**
   - **Horizontal Stripes**
   - **Vertical Concentrated Stripes**
""")

# Modal Popup for Instructions (Expander with images)
with st.expander("Learn about Stripe Pattern", expanded=False):
    st.write(
        "Stripe patterns are a versatile and dynamic design element that can significantly alter the aesthetic of an image. Whether applied as vertical, horizontal, diagonal, or concentrated vertical stripes, they introduce texture, movement, and depth to compositions. Vertical stripes often convey height and elegance, while horizontal stripes create a sense of calm and stability. Diagonal stripes add energy and dynamism, and concentrated vertical stripes offer a more dramatic, focused look. When applied to images, stripe patterns can either subtly enhance the background or become the focal point, depending on their size, contrast, and direction. They can also introduce a sense of rhythm, guide the viewer's eye, and accentuate specific elements, making them a powerful tool for adding visual interest, texture, and creativity to photographs and digital art."
    )
    
    # Example images for face filtering (You can replace these with any actual images you want to display)
    # For example, if you have sample images, you can display them here:
    st.image("Barcode Pattern.jpg", caption="Verticle Stripe Pattern", use_column_width=True)
    st.image("Diagonal Stripes.jpg", caption="Diagonal Stripe Pattern", use_column_width=True)
    st.image("horizontal stripe pattern.jpg", caption="Horizontal Stripe Pattern", use_column_width=True)
    st.image("Vertical Concentrated.jpg", caption="Vertical Concentrated Stripe Pattern", use_column_width=True)

# Radio button for single or multiple image upload
upload_option = st.radio("Choose Upload Option", ["Upload Single Image", "Upload Multiple Images"])

# Upload single or multiple image files based on the selected option
if upload_option == "Upload Single Image":
    uploaded_files = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg", "bmp", "gif"], key="single_image")
else:
    uploaded_files = st.file_uploader("Choose image files", type=["png", "jpg", "jpeg", "bmp", "gif"], accept_multiple_files=True, key="multiple_images")

# Allow the user to select a pattern
pattern_option = st.radio(
    "Select Pattern Option",
    options=["Apply One Pattern", "Apply All Patterns"]
)

# If the user selects "Apply One Pattern", show pattern selection
if pattern_option == "Apply One Pattern":
    pattern_id = st.radio(
        "Select a stripe pattern",
        options=[1, 2, 3, 4],
        format_func=lambda x: {
            1: "Vertical Stripes",
            2: "Diagonal Stripes",
            3: "Horizontal Stripes",
            4: "Vertical Concentrated Stripes"
        }[x]
    )

# Process and display/download images based on the upload option
if uploaded_files:
    if upload_option == "Upload Single Image":
        # Process the single image
        image = Image.open(uploaded_files)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Process and provide download link for the current image
        if pattern_option == "Apply One Pattern":
            processed_image_buffer = process_image(image, pattern_id, uploaded_files.name)
            # Provide the user with a download button for the single image
            st.download_button(
                label="Download Processed Image",
                data=processed_image_buffer,
                file_name=f"patterned_{uploaded_files.name}",  # Name the file with the original name
                mime="image/jpeg"  # MIME type for JPEG. Change if using PNG or another format
            )
        else:
            # Apply all patterns to the single image and provide separate downloads
            processed_image_buffers = []
            for pattern_id in patterns:
                processed_image_buffer = process_image(image, pattern_id, uploaded_files.name)
                processed_image_buffers.append(processed_image_buffer)

            # Create a ZIP file of all the processed images
            zip_filename = "processed_images.zip"
            zip_file = create_zip_file(processed_image_buffers, zip_filename)

            # Provide the user with a download button for the ZIP file
            with open(zip_filename, "rb") as f:
                st.download_button(
                    label="Download All Processed Images as ZIP",
                    data=f,
                    file_name="processed_images.zip",
                    mime="application/zip"
                )
        
    else:
        # Create a temporary directory to store processed images
        processed_image_buffers = []
            
        # Process and save each image in the directory
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            if pattern_option == "Apply One Pattern":
                processed_image_buffer = process_image(image, pattern_id, uploaded_file.name)
                processed_image_buffers.append(processed_image_buffer)
            else:
                # Apply all patterns to the current image
                for pattern_id in patterns:
                    processed_image_buffer = process_image(image, pattern_id, uploaded_file.name)
                    processed_image_buffers.append(processed_image_buffer)
            
        # Create a ZIP file of all the processed images
        zip_filename = "processed_images.zip"
        zip_file = create_zip_file(processed_image_buffers, zip_filename)
        
        # Provide the user with a download button for the ZIP file
        with open(zip_filename, "rb") as f:
            st.download_button(
                label="Download All Processed Images as ZIP",
                data=f,
                file_name="processed_images.zip",
                mime="application/zip"
            )

else:
    st.write("Please upload one or more images to start.")