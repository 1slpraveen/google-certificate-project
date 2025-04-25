import random
from weasyprint import HTML
from datetime import datetime

# Example dictionary with static data
certificate_data = {
    "name": "Jane Doe",
    "course_title": "Google Cloud Fundamentals",
    "date": "April 25, 2025",
    "navbar": "📘 Google Academy",
    "title": "Certificate of Completion",
    "subtitle": "This is to proudly recognize",
    "text": "for the successful completion of",
    "footer": "© 2025 Google Academy · This certificate is digitally issued",
    "signature_line_width": 200
}

# List of predefined signatures (you can add more names to the list)
signatures = ["John Smith", "Jane Doe", "Peter Johnson", "Mary Evans"]

# Function to generate a random signature from the predefined list
def generate_random_signature():
    return random.choice(signatures)

def generate_certificate_from_data(data, output_path="google_certificate.pdf"):
    # Extract values from the data dictionary
    name = data.get('name', 'Unknown')
    course_title = data.get('course_title', 'Unknown Course')
    date_str = data.get('date', datetime.today().strftime('%B %d, %Y'))
    navbar = data.get('navbar', "Google Academy")
    title = data.get('title', "Certificate of Completion")
    subtitle = data.get('subtitle', "This is to proudly recognize")
    text = data.get('text', "for the successful completion of")
    footer = data.get('footer', "This certificate is digitally issued")
    signature_line_width = data.get('signature_line_width', 200)

    # Generate a random signature
    signature = generate_random_signature()  # Randomly select a signature

    # HTML content for the certificate using the data dictionary
    html_content = f"""
    <html>
    <head>
        <style>
            @page {{
                size: A4 landscape;
                margin: 0;
            }}
            body {{
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #f0f8ff, #add8e6); /* Soft gradient background */
                font-family: 'Georgia', serif;
            }}
            .certificate-wrapper {{
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
                height: 100%;
                padding: 20px;
                box-sizing: border-box;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
            .certificate {{
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                align-items: center;
                width: 100%;
                max-width: 850px;
                border: 8px solid #4285F4; /* Slightly thinner blue border */
                border-radius: 10px;
                padding: 40px 60px;
                background-color: #ffffff;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Soft shadow for the certificate box */
                text-align: center;
            }}
            .navbar {{
                width: 100%;
                background-color: #4285F4;
                color: white;
                padding: 16px;
                font-size: 20px;
                font-weight: bold;
                text-align: left;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }}
            .title {{
                font-size: 50px;
                font-weight: bold;
                color: #0b5394;
                text-transform: uppercase;
                margin-bottom: 20px;
                text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Adding subtle shadow to the title */
            }}
            .subtitle {{
                font-size: 24px;
                color: #2c3e50;
                margin-bottom: 10px;
                font-style: italic;
            }}
            .name {{
                font-size: 40px;
                font-weight: bold;
                color: #154360;
                margin: 20px 0;
                text-transform: uppercase;
            }}
            .text {{
                font-size: 20px;
                color: #34495e;
                margin-bottom: 20px;
            }}
            .course {{
                font-size: 26px;
                font-weight: 600;
                color: #1f618d;
                margin-bottom: 40px;
            }}
            .date {{
                font-size: 18px;
                color: #566573;
                font-style: italic;
                margin-top: 20px;
            }}
            .signature {{
                width: 100%;
                text-align: center;
                position: relative;
                margin-top: 40px;
           
            }}
            .signature-text {{
                font-size: 16px;
                color: #34495e;
                font-weight: bold;
            }}
            .footer {{
                font-size: 12px;
                color: #95a5a6;
                margin-top: 20px;
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <div class="certificate-wrapper">
            <div class="certificate">
                <div class="navbar">{navbar}</div>

                <div class="title">{title}</div>
                <div class="subtitle">{subtitle}</div>
                <div class="name">{name}</div>
                <div class="text">{text}</div>
                <div class="course">"{course_title}"</div>
                <div class="date">Issued on {date_str}</div>

                <div class="signature">
                    <div class="signature-line"></div>
                    <div class="signature-text">{signature}</div>  <!-- This will now show a random signature -->
                </div>

                <div class="footer">{footer}</div>
            </div>
        </div>
    </body>
    </html>
    """

    # Generate PDF from HTML content and save to the specified output path
    try:
        HTML(string=html_content).write_pdf(output_path)
        print(f"✅ Certificate saved to: {output_path}")
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")

# Example usage with the Python dictionary data:
generate_certificate_from_data(certificate_data, "google_certificate.pdf")
