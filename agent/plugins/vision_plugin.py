# vision_plugin.py
from PIL import Image

class VisionPlugin:
    def __init__(self, agent):
        self.agent = agent

    def analyze_image(self, image_path):
        """Perform a basic analysis of an image."""
        try:
            with Image.open(image_path) as img:
                print(f"Image {image_path} loaded successfully.")
                return {
                    "format": img.format,
                    "size": img.size,
                    "mode": img.mode
                }
        except Exception as e:
            print(f"Error analyzing image: {e}")
            return None

    def execute(self, image_path):
        """Execute the vision task."""
        print(f"Executing Vision task for {self.agent.name}")
        return self.analyze_image(image_path)
