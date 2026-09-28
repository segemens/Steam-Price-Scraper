import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk

cookies = {'birthtime': '283993201', 'lastagecheckage': '1-January-1979'}
headers = {'User-Agent': 'Mozilla/5.0'}

def FindLink(game_name):
    search_url = f'https://store.steampowered.com/search/?term={game_name}'
    
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    first_result = soup.find('a', {'class': 'search_result_row'})

    if first_result:
        return first_result['href']
    else:
        return None

def MainProgram(search_box, game_name_label, game_price_label):
    game_name_inp = search_box.get().strip()
    print(f"'{game_name_inp}' aranıyor...\n")

    found_url = FindLink(game_name_inp)

    if found_url:
        print('Oyun bulundu! Sayfasına gidiliyor...\n')

        try:
            response = requests.get(url=found_url, headers=headers, cookies=cookies)
            soup = BeautifulSoup(response.content, 'html.parser')

            game_name = soup.find('div', {'id': 'appHubAppName'}).text.strip()
            purchase_block = soup.find('div', {'id': re.compile('^game_area_purchase_section_add_to_cart_')})

            if purchase_block:
                price_tag = purchase_block.find('div', {'class': 'discount_final_price'})

                if not price_tag:
                    price_tag = purchase_block.find('div', {'class': 'game_purchase_price'})

                if price_tag:
                    game_name_label.config(text=f'Oyun: {game_name}')
                    game_price_label.config(text=f'Fiyat: {price_tag.text.strip()}')
                else:
                    print('Fiyat etiketi bulunamadı (Ön sipariş, ücretsiz veya demo olabilir).')
            else:
                print('Satın alma bloğu bulunamadı.')
            
        except Exception as e:
            print(f'Fiyat çekilirken hata oluştu: {e}')

    else:
        print('Böyle bir oyun yok. İsmi doğru yazdığınızdan emin olun...')

def MakeWindow():
    window = tk.Tk()
    window.title("Steam Fiyat Bulucu")
    window.geometry("400x450")
    window.configure(bg="#1b2838") 
    window.resizable(False, False)

    font_header = ("Arial", 11, "bold")
    font_normal = ("Arial", 10)
    font_result = ("Arial", 12, "bold")

    header_label = tk.Label(window, text="Aranacak Oyunu Girin", bg="#1b2838", fg="#66c0f4", font=font_header)
    header_label.pack(pady=(30, 10))

    search_box = tk.Entry(window, width=30, font=("Arial", 12), bg="#2a475e", fg="white", insertbackground="white", relief="flat")
    search_box.pack(pady=5, ipady=5)

    result_panel = tk.Frame(window, bg="#171a21", width=340, height=180)
    result_panel.pack(pady=10)
    result_panel.pack_propagate(False)

    status_label = tk.Label(result_panel, text="> Sistem hazır.", bg="#171a21", fg="gray", font=font_normal, anchor="w")
    status_label.pack(fill="x", padx=15, pady=(15, 10))

    game_name_label = tk.Label(result_panel, text="Oyun: -", bg="#171a21", fg="#66c0f4", font=font_result, anchor="w")
    game_name_label.pack(fill="x", padx=15, pady=5)

    game_price_label = tk.Label(result_panel, text="Fiyat: -", bg="#171a21", fg="white", font=font_result, anchor="w")
    game_price_label.pack(fill="x", padx=15, pady=5)

    search_button = tk.Button(window, text="FİYATI SORGULA", bg="#5c7e10", fg="white", font=font_header, relief="flat", activebackground="#739e15", activeforeground="white", command=lambda: MainProgram(search_box, game_name_label, game_price_label))
    search_button.pack(pady=20, ipadx=10, ipady=5)

    window.mainloop()

MakeWindow()