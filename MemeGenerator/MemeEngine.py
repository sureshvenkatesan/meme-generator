from PIL import Image , ImageDraw, ImageFont
import os
import pkg_resources


class MemeEngine:
    def __init__(self, tmp_path: str, font_name: str = 'LilitaOne-Regular.ttf'):
        """Initialize a MemeEngine object with a temporary directory path and font name.

        Args:
            tmp_path (str): The path of the temporary directory to use for storing memes.
            font_name (str, optional): The name of the font file to use for text in memes.
                Defaults to 'LilitaOne-Regular.ttf'.
        """
        self.meme_path = tmp_path
        self.font_path = pkg_resources.resource_filename(__name__, f'fonts/{font_name}')

    def make_meme(self, img_path: str, text: str, author: str, new_width: int = 500) -> str:
        """Create a meme by adding text and author to an image.

        Args:
            img_path (str): The file path of the image to use.
            text (str): The text to add to the image.
            author (str): The author name to add to the image.
            new_width (int, optional): The new width of the image in pixels. Defaults to 500.

        Returns:
            str: The file path of the newly created meme.

        Raises:
            Exception: If the image cannot be processed due to an error.
        """
        # Resize the image so the width is at most 500px
        if new_width > 500:
            new_width = 500
        try:
            #load the image
            with Image.open(img_path) as img:
                # Get the original size of the image
                width1, height1 = img.size
                # Resize the image
                # Calculate the new height of the image based on the aspect ratio
                new_height = int((float(height1) / float(width1)) * new_width)
                # Resize the image while maintaining the aspect ratio
                img = img.resize((new_width, new_height), Image.NEAREST)

                # Add the quote body and quote author to the image
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(self.font_path, 30)

                # Determine the size of the text
                text_width, text_height = draw.textsize(text, font)
                author_width, author_height = draw.textsize(f'  - {author}', font=font)

                # Determine the position to draw the text
                x = (img.width - text_width) /2
                y = (img.height - text_height - author_height) / 2

                # Draw the text on the image
                draw.text((x, y), text, font=font, fill='white')
                draw.text((x, y+text_height), f'  - {author}', font=font, fill='white')

                # Save the meme ( the manipulated image)
                # split the original image pathname into the root path and the file extension.
                root, ext = os.path.splitext(img_path)
                # get the filename of the original image without the directory path, and we append '_meme'
                # and the extension to it to get the filename of the new meme.
                filename = os.path.basename(root) + '_meme' + ext
                # dir_path = os.path.dirname(self.meme_path)
                os.makedirs(self.meme_path, exist_ok=True)
                new_path = os.path.join(self.meme_path, filename)
                img.save(new_path)

                return new_path
        except Exception as e:
            print(f"Error: Could not process image {img_path}. Error: {e}")

        return ''