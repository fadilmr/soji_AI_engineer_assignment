import requests
from bs4 import BeautifulSoup
from pathlib import Path

def download_ad(url, ad_name):
    folder = Path(f"ad_data/{ad_name}")
    folder.mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    
    text = soup.get_text()
    with open(folder / "content.txt", "w") as f:
        f.write(text)

    pdf_links = soup.find_all('a', href=True)
    pdf_count = 0
    
    for link in pdf_links:
        href = link['href']
        if '.pdf' in href.lower():
            if href.startswith('http'):
                pdf_url = href
            else:
                pdf_url = f"https://ad.easa.europa.eu{href}"
            pdf_response = requests.get(pdf_url)
            pdf_count += 1
            
            pdf_file = folder / f"document_{pdf_count}.pdf"
            with open(pdf_file, "wb") as f:
                f.write(pdf_response.content)

if __name__ == "__main__":
    ads = [
        ("https://ad.easa.europa.eu/ad/US-2025-23-53", "FAA-2025-23-53"),
        ("https://ad.easa.europa.eu/ad/2025-0254", "EASA-2025-0254")
    ]
    
    for url, name in ads:
        download_ad(url, name)
