# import demoji

# text = "Hello, world! 🙂"
# text_without_emojis = demoji.replace_with_desc(text)

# print(text_without_emojis)

# import emoji
# from PIL import Image, ImageDraw, ImageFont

# def text_to_emoji_image(text, filename):
#     # Convert text to emojis
#     emoji_text = emoji.emojize(text, language='alias')

#     # Create a new image with a white background
#     img = Image.new('RGB', (500, 500), color = (255, 255, 255))

#     # Set the font and font size
#     font = ImageFont.truetype("arial.ttf", 40)

#     # Create a drawing context
#     draw = ImageDraw.Draw(img)

#     # Calculate the x and y coordinates to center the text
#     text_width, text_height = font.getsize(emoji_text)
#     x = (img.width - text_width) / 2
#     y = (img.height - text_height) / 2

#     # Draw the text on the image
#     draw.text((x, y), emoji_text, font=font, fill=(0, 0, 0))

#     # Save the image to a file
#     img.save(filename)

# # Example usage
# text = "smiling face with smiling eyes"
# filename = "emoji_image.png"
# text_to_emoji_image(text, filename)
