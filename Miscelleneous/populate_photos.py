import pandas as pd
import numpy as np

data = pd.read_csv('laptops.csv', encoding='latin-1',index_col=0)

photo_urls = ["https://ssl-product-images.www8-hp.com/digmedialib/prodimg/lowres/c05975535.png",
          "https://currys-ssl.cdn.dixons.com/css/themes/ucms/category/laptop/img/2018/Lenovo-3.png",
          "https://www.jbhifi.com.au/FileLibrary/ProductResources/Images/255878-L-LO.jpg",
          "https://static-ecpa.acer.com/media/catalog/product/cache/7/small_image/300x/17f82f742ffe127f42dca9de82fb58b1/p/r/predator-helios300-ph317-51_main.png",
          "https://www.pclaptops.com/uploads/sm5newsite643792114.png",
          "http://lab-kuzniewski.pl/wp-content/uploads/2018/08/lenovo-laptop-thinkpad-x1-extreme-hero.png",
          "https://www.notebookcheck.net/uploads/tx_jppageteaser/Toshiba_updates_the_Satellite_P_Series_with_Haswell_processors_and_NVIDIA_discrete_graphics_01.jpg",
          "https://www.laptopoutlet.co.uk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/5/4/5454_112.jpg",
          "https://www.notebook.hu/notebook.hu/default/cache/images/product/800_600/y/o/yoga260_1.jpg",
          "https://cf5.s3.souqcdn.com/item/2018/01/24/30/11/18/52/item_XL_30111852_93853569.jpg",
          "https://dustinweb.azureedge.net/image/249985/400/320/lenovo-legion-y520-gtx-1050-ti.jpg",
          ]


data['photo_url'] = np.random.choice(list(photo_urls), len(data))

data.to_csv("laptops_with_Photo_URL.csv")