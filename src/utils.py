import os
import re
import subprocess
from datetime import datetime
import platform
import signal

def start_ffmpeg_recording(output_file):
    """Starts recording the screen with ffmpeg. Adjust crop for full width and current height."""
    output_path = os.path.join(os.getcwd(), 'video', datetime.now().strftime('%Y%m%d'), output_file)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create the directory if it does not exist

    print("Path to file: ",output_path)
    # Add the screen number to the ffmpeg command
    if platform.system() == 'Linux':
        command = [
            'ffmpeg',
            '-y',
            '-video_size', '1280x720',  # Set the video size
            '-framerate', '25',  # Set the frame rate
            '-f', 'x11grab',  # Grab the X11 display
            '-i', ':99.0',  # Set the display number
            output_path
        ]
    elif platform.system() == 'Darwin':  # macOS
            command = [
        'ffmpeg',
        '-y',  # Overwrite output files without asking
        '-f', 'avfoundation',
        '-i', '2',  # Adjust this to match your screen capture device index
        '-r', '30',  # Frame rate
        '-s', '2880x1800',  # Capture size for 13-inch MacBook Pro Retina
        '-vf', 'crop=2880:1400:0:300',  # Use full width, adjust height and y offset as needed
        '-t', '15',  # Duration of recording in seconds
        output_path
    ]
            
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("FFMpeg successfully started")
    # Check if the process started correctly
    if process.poll() is not None:
        print("Error starting ffmpeg recording:", process.stderr.read())

    return process

def stop_ffmpeg_recording(process):
    """Terminates the ffmpeg recording process."""
    process.send_signal(signal.SIGINT)
    process.wait()


def format_filename_from_url(url):
    """Formats a filename from a URL, removing scheme and replacing special characters."""
    filename = re.sub(r'https?://', '', url)  # Remove scheme
    filename = re.sub(r'[^a-zA-Z0-9\-_\.]', '_', filename)  # Replace special characters
    return f"{filename}_recording"

