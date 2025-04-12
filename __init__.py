import pdfkit

def convert_html_to_pdf(input_html, output_pdf):
    # Set path to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=r'E:\UserDev\wkhtmltopdf\bin\wkhtmltopdf.exe')

    # Configuration options
    options = {
        "no-images": "",  # Disable images if necessary
        "page-size": "A4",  # Set page size
        "viewport-size": "1280x1024",  # Custom viewport size
        "disable-smart-shrinking": "",  # Prevent automatic shrinking of content
        "encoding": "UTF-8",  # Ensure proper encoding
        "print-media-type": "",  # Use media styles for printing
    }

    # Convert HTML file to PDF
    pdfkit.from_file(input_html, output_pdf, configuration=config, options=options)

# Define paths
input_html = r"C:\Users\simi\Desktop\OneDrive\AAAMemory\test\AAC--Japanese.html"
output_pdf = r"C:\Users\simi\Desktop\DevProjects\simi-py\output_full.pdf"

# Convert the HTML to PDF
convert_html_to_pdf(input_html, output_pdf)
