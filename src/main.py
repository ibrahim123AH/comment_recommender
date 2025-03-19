import streamlit as st
import base64
import io
from PIL import Image
from recommender import generate_image_response

# def encode_image_to_base64(image_bytes):
#     """Encodes image bytes to a Base64 string."""
#     return base64.b64encode(image_bytes).decode("utf-8")

# def calculate_dynamic_height(text):
#     """Calculate dynamic height for text area based on character count."""
#     return max(68, len(text) // 2)  # Min height 100, Max height 300


st.set_page_config(layout="wide")  # Set the page layout to wide
# st.title("Image and Text Processor")
# Centered title using markdown
st.markdown("""
<h1 style='text-align: center;'>Comment Recommender Tool</h1>
""", unsafe_allow_html=True)

# Define two columns with equal width, spanning full width of page
left_col, right_col = st.columns([1, 1], gap="small")  # Reducing gap between columns

with left_col:
    st.subheader("Input post and comment", divider="gray")
    
    # Model selection
    model_options = ["Gemini 2.0 Flash", "Gemini 2.0 Flash-Lite", "Gemini 2.0 Pro Experimental 02-05", "Gemini 2.0 Flash Thinking Experimental 01-21"]
    selected_model = st.radio("Select a model:", model_options)
    
    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    css = '''
    <style>
    /* Make the button larger */
    [data-testid="stFileUploaderDropzone"] {
        min-height: 200px !important;
        padding: 20px !important;
    }'''
    st.markdown(css, unsafe_allow_html=True)
    
    text_input = st.text_area("Enter comment:")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

with right_col:
    st.subheader("Output Reply Advice", divider="gray")
    extracted_text = ""
    
    if st.button("Process"):
        if uploaded_file is not None and text_input:
            image_bytes = uploaded_file.getvalue()
            encoded_image = base64.b64encode(image_bytes).decode("utf-8")
            extracted_text, sections = generate_image_response(encoded_image, text_input, selected_model)

            st.success("Processing completed!")
            # print(extracted_text)
            # print(f"\033[91m{extracted_text}\033[0m")
            # print(f"\033[91m{sections}\033[0m")
            # Display each key-value pair in a separate box
            for key, value in sections.items():
                height = max(68, len(value) // 4) 
                # st.markdown(f"**{key}:**")
                st.markdown(f"""
                <div style='margin-top: 0px; margin-bottom: 0px;'>
                    <p style='font-weight: bold; margin-bottom: 1px; margin-top: 1px;'>{key}:</p>
                """, unsafe_allow_html=True)
                st.text_area("", value, height=height, key=key, disabled=False)
                st.markdown("</div></div>", unsafe_allow_html=True)
        else:
            st.error("Please upload an image and enter text before processing.")
# if __name__ == "__main__":
#     main()




# import streamlit as st
# import base64
# import io
# from PIL import Image
# from recommender import generate_image_response

# def encode_image_to_base64(image_bytes):
#     """Encodes image bytes to a Base64 string."""
#     return base64.b64encode(image_bytes).decode("utf-8")

# def main():
#     st.title("Image and Text Processor")
    
#     # Model selection
#     model_options = ["Gemini 2.0 Flash", "Gemini 2.0 Flash-Lite", "Gemini 2.0 Pro Experimental 02-05", "Gemini 2.0 Flash Thinking Experimental 01-21"]

#     selected_model = st.radio("Select a model:", model_options)
    
#     # Upload image
#     uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], label_visibility="visible")
#     # Make file uploader larger using markdown styling
    
#     css = '''
# <style>
#     /* Adjust the width and height */
#     [data-testid="stFileUploader"] {
#         width: 1000px !important;
#         height: 400px !important;
#     }

#     /* Adjust the padding and font size */
#     [data-testid="stFileUploader"] > div {
#         padding: 20px !important;
#         font-size: 18px !important;
#     }

#     /* Make the button larger */
#     [data-testid="stFileUploaderDropzone"] {
#         min-height: 400px !important;
#         padding: 20px !important;
#     }

#     /* Style the drag and drop area */
#     [data-testid="stFileUploaderDropzone"] div {
#         font-size: 16px !important;
#         padding: 10px !important;
#     }
# </style>
# '''
#     st.markdown(css, unsafe_allow_html=True)
#     text_input = st.text_area("Enter comment:")
    
#     extracted_text = ""
    
#     if uploaded_file is not None:
#         # Display image
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image", use_container_width=True)
        
#     if st.button("Process"):
#         if uploaded_file is not None and text_input:
#             # Read image bytes and encode as Base64
#             image_bytes = uploaded_file.getvalue()
#             encoded_image = encode_image_to_base64(image_bytes)
            
#             # Process image with selected model
#             extracted_text = generate_image_response(encoded_image, text_input, selected_model)
            
#             st.success("Processing completed!")
#             st.text_area("Output:", extracted_text, height=200)
#         else:
#             st.error("Please upload an image and enter text before processing.")

# if __name__ == "__main__":
#     main()
