import sys
sys.path.append('/home/rohan/newenv/lib/python3.6/site-packages')
import json
from urllib.request import Request, urlopen
from PIL import Image
from colorthief import ColorThief
from io import BytesIO
from ItemAPI import LocationRecommendation

def get_dominant_colors(company, location, company_type):

    company = company.lower()
    headers = {
      'Content-Type': 'image/png; charset=utf-8'
    }
    request = Request('https://api.ritekit.com/v1/images/logo?domain=' + company + '.com&client_id=c3a8350984d9f9547d0e438a7668a78ffc5f26b4b5f2', headers=headers)
    response_body = urlopen(request).read()
    im = Image.open(BytesIO(response_body))
    rgb_im = im.convert('RGB')
    rgb_im.save('company_img.png')
    image = 'company_img.png'

    rec_dict = LocationRecommendation.location_similarity(location, company_type)
    print(rec_dict)


    color_thief = ColorThief(image)
    palette = color_thief.get_palette(color_count=2, quality=1)
    colors = []
    for color in palette[:2]:
        colors.append('#%02x%02x%02x' % color)

    final_dict = {"primary_color":colors[0],
                "secondary_color":colors[1],
                "recommendations":rec_dict}
    
    return final_dict

