import streamlit as st
import os

# Directory where blog images will be stored
IMAGE_DIR = 'blog_images'
os.makedirs(IMAGE_DIR, exist_ok=True)  # Create directory if it doesn't exist

# File path where blog posts will be stored
BLOG_FILE = 'blogs.txt'

# Function to read blog posts from the file
def read_blogs():
    blogs = []
    try:
        with open(BLOG_FILE, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                title, content, image_path = line.split(' | ', 2)
                blogs.append({"title": title, "content": content, "image_path": image_path})
    except FileNotFoundError:
        pass
    return blogs

# Function to add a blog post to the file
def add_blog(title, content, image_path):
    with open(BLOG_FILE, 'a') as file:
        file.write(f"{title} | {content} | {image_path}\n")

# Function to update a blog post in the file
def update_blog(old_title, new_title, new_content, new_image_path):
    blogs = read_blogs()
    with open(BLOG_FILE, 'w') as file:
        for blog in blogs:
            if blog['title'] == old_title:
                file.write(f"{new_title} | {new_content} | {new_image_path}\n")
            else:
                file.write(f"{blog['title']} | {blog['content']} | {blog['image_path']}\n")

# Function to delete a blog post from the file
def delete_blog(title):
    blogs = read_blogs()
    with open(BLOG_FILE, 'w') as file:
        for blog in blogs:
            if blog['title'] != title:
                file.write(f"{blog['title']} | {blog['content']} | {blog['image_path']}\n")

# Initialize session state for blogs
if 'blogs' not in st.session_state:
    st.session_state.blogs = read_blogs()

# Streamlit UI
st.title("Blog API")

# Add a new blog post
st.subheader("Add Blog Post")
with st.form(key='add_blog_form'):
    blog_title = st.text_input("Blog Title")
    blog_content = st.text_area("Blog Content")
    blog_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    submit_button = st.form_submit_button("Add Blog")
    
    if submit_button:
        if not blog_title.strip() or not blog_content.strip():
            st.error("Please fill in the blog title and content.")
        else:
            # Save the image if uploaded
            if blog_image is not None:
                image_path = os.path.join(IMAGE_DIR, blog_image.name)
                with open(image_path, "wb") as f:
                    f.write(blog_image.getbuffer())
            else:
                image_path = "No image uploaded"
            
            add_blog(blog_title, blog_content, image_path)
            st.success("Blog post added successfully!")
            st.session_state.blogs = read_blogs()  # Refresh blog list

# Display existing blog posts
st.subheader("Existing Blog Posts")
if st.session_state.blogs:
    for blog in st.session_state.blogs:
        # Display each blog post
        col1, col2, col3 = st.columns([3, 1, 1])

        with col1:
            st.markdown(
                f"""
                <div style="border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; border-radius: 5px;">
                    <h4>{blog['title']}</h4>
                    <p>{blog['content']}</p>
                    <p><strong>Image:</strong></p>
                    {'<img src="' + blog['image_path'] + '" width="100%" style="border-radius: 5px;" />' if blog['image_path'] != "No image uploaded" else "No image uploaded"}
                </div>
                """, unsafe_allow_html=True
            )

        with col2:
            # Update blog post button
            if st.button("Update", key=f'update_{blog["title"]}'):
                # Store the title for updating
                st.session_state.updating_title = blog['title']

                # Set the current blog data into the session state for editing
                st.session_state.update_title = blog['title']
                st.session_state.update_content = blog['content']
                st.session_state.update_image_path = blog['image_path']

        with col3:
            # Delete blog post button
            if st.button("Delete", key=f'delete_{blog["title"]}'):
                delete_blog(blog['title'])
                st.success("Blog post deleted successfully!")
                st.session_state.blogs = read_blogs()  # Refresh blog list
else:
    st.write("No blog posts available.")

# Update blog post section
if 'updating_title' in st.session_state:
    st.subheader("Update Blog Post")
    with st.form(key='update_blog_form'):
        update_title = st.text_input("New Title", value=st.session_state.update_title)
        update_content = st.text_area("New Content", value=st.session_state.update_content)
        update_image = st.file_uploader("Upload New Image", type=["png", "jpg", "jpeg"])
        update_button = st.form_submit_button("Update Blog")
        
        if update_button:
            if not update_title.strip() or not update_content.strip():
                st.error("Please fill in both the new blog title and content.")
            else:
                # Save the new image if uploaded
                if update_image is not None:
                    new_image_path = os.path.join(IMAGE_DIR, update_image.name)
                    with open(new_image_path, "wb") as f:
                        f.write(update_image.getbuffer())
                else:
                    new_image_path = st.session_state.update_image_path  # Keep old image if no new image uploaded

                update_blog(st.session_state.updating_title, update_title, update_content, new_image_path)
                st.success("Blog post updated successfully!")
                st.session_state.blogs = read_blogs()  # Refresh blog list
                del st.session_state.updating_title  # Clear the update title to stop showing update form
else:
    st.session_state.pop('update_title', None)
    st.session_state.pop('update_content', None)
    st.session_state.pop('update_image_path', None)
