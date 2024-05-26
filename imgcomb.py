from moviepy.editor import ImageClip, concatenate_videoclips

def create_video_from_images(image_paths, output_path='quote_video.mp4'):
    clips = [ImageClip(img).set_duration(5) for img in image_paths]
    video = concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_path, fps=24)

# Example usage
create_video_from_images(['quote.png'])
