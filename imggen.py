from PIL import Image, ImageDraw, ImageFont

from main import quote


def create_image_from_text(text, author, image_path='quote.png'):
    # Create a blank image with white background
    img = Image.new('RGB', (800, 400), color='white')
    d = ImageDraw.Draw(img)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()

    # Add text to image
    message = f"\"{text}\"\n\n- {author}"
    d.text((10,10), message, fill=(0,0,0), font=font)

    # Save the image
    img.save(image_path)

# Example usage
quote_text = quote['text']
quote_author = quote['author']
create_image_from_text(quote_text, quote_author)
