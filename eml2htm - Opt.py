import email
import os

def eml_to_html(eml_file):
    """Extracts HTML content from an EML file.

    Args:
        eml_file: Path to the EML file.

    Returns:
        The HTML content as bytes, or None if no HTML part is found.
        Raises an exception if there's an issue parsing the email.
    """
    try:
        with open(eml_file, 'rb') as file:  # Open in binary mode for robustness
            msg = email.message_from_binary_file(file) # Use binary file reading
            for part in msg.walk():
                if part.get_content_type() == 'text/html':
                    return part.get_payload(decode=True)
            return None
    except Exception as e:
        print(f"Error processing {eml_file}: {e}")
        return None

def process_eml_files(root_path):
    """Processes EML files in a directory (non-recursively).

    Args:
        root_path: Path to the directory containing EML files.
    """
    try:
        files = [f for f in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, f))]
        eml_files = [os.path.join(root_path, f) for f in files if f.endswith('.eml')]

        for eml_file in eml_files:
            htm_file = eml_file + ".htm"
            html_content = eml_to_html(eml_file)

            if html_content:
                try:
                    with open(htm_file, 'wb') as o:
                        o.write(html_content)
                    print(f"Successfully converted {eml_file} to {htm_file}")
                except Exception as e:
                    print(f"Error writing HTML to {htm_file}: {e}")
            else:
                print(f'No HTML content found in {eml_file}.')
    except FileNotFoundError:
        print(f"Error: Directory not found: {root_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



# Usage
root_path = r"C:/emails/"  # Use raw string to avoid backslash issues
process_eml_files(root_path)