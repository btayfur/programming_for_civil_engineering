"""
Deprem Veri Görselleştirme - Infografik Oluşturma
=================================================
Bu uygulama USGS (ABD Jeoloji Araştırmaları Kurumu) API'sinden
son bir aydaki M4.5+ depremleri çeker ve profesyonel bir
infografik oluşturur.

Kaynak: https://earthquake.usgs.gov/fdsnws/event/1/
"""

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')
import matplotlib.dates as mdates

# Türkçe karakter desteği için
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


def fetch_earthquake_data():
    """
    USGS API'sinden son bir aydaki M4.5+ depremleri çeker.
    
    Returns:
        pd.DataFrame: Deprem verileri
    """
    # Son bir ay için tarih aralığı
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    
    # USGS API URL'si
    base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": start_date.strftime("%Y-%m-%d"),
        "endtime": end_date.strftime("%Y-%m-%d"),
        "minmagnitude": 4.5,
        "orderby": "time"
    }
    
    print("=" * 60)
    print("[*] USGS Deprem Verileri Cekiliyor...")
    print(f"[>] Tarih Araligi: {start_date.strftime('%d.%m.%Y')} - {end_date.strftime('%d.%m.%Y')}")
    print(f"[>] Minimum Buyukluk: M4.5+")
    print("=" * 60)
    
    try:
        response = requests.get(base_url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        # GeoJSON formatından DataFrame'e çevirme
        earthquakes = []
        for feature in data['features']:
            props = feature['properties']
            coords = feature['geometry']['coordinates']
            
            # Unix timestamp'i datetime'a çevir
            time = datetime.fromtimestamp(props['time'] / 1000)
            
            earthquakes.append({
                'time': time,
                'date': time.date(),
                'hour': time.hour,
                'day_of_week': time.strftime('%A'),
                'magnitude': props['mag'],
                'depth': coords[2],  # km cinsinden derinlik
                'longitude': coords[0],
                'latitude': coords[1],
                'place': props['place'],
                'type': props.get('type', 'earthquake'),
                'tsunami': props.get('tsunami', 0),
                'felt': props.get('felt', 0),
                'significance': props.get('sig', 0)
            })
        
        df = pd.DataFrame(earthquakes)
        print(f"[OK] {len(df)} adet deprem verisi basariyla cekildi!")
        print("=" * 60)
        
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"[HATA] API Hatasi: {e}")
        return None


def get_magnitude_category(mag):
    """Deprem büyüklüğüne göre kategori belirler."""
    if mag >= 7.0:
        return "Büyük (M7.0+)"
    elif mag >= 6.0:
        return "Güçlü (M6.0-6.9)"
    elif mag >= 5.0:
        return "Orta (M5.0-5.9)"
    else:
        return "Hafif (M4.5-4.9)"


def get_depth_category(depth):
    """Deprem derinliğine göre kategori belirler."""
    if depth < 70:
        return "Sığ (0-70 km)"
    elif depth < 300:
        return "Orta (70-300 km)"
    else:
        return "Derin (300+ km)"


def create_color_palette():
    """Profesyonel renk paleti döndürür."""
    return {
        'background': '#0a0e27',        # Koyu lacivert
        'card_bg': '#13183a',            # Kart arka planı
        'card_border': '#2a3f7a',        # Kart kenarlığı
        'primary': '#00d4ff',            # Ana renk (cyan)
        'secondary': '#ff6b6b',          # İkincil renk (kırmızı)
        'accent': '#ffd93d',             # Vurgu rengi (sarı)
        'success': '#6bcb77',            # Yeşil
        'text_primary': '#ffffff',       # Ana metin
        'text_secondary': '#8892b0',     # İkincil metin
        'grid': '#1e2a5e',               # Grid çizgileri
        
        # Büyüklük renkleri
        'mag_light': '#6bcb77',          # Hafif
        'mag_moderate': '#ffd93d',       # Orta
        'mag_strong': '#ff9f43',         # Güçlü
        'mag_major': '#ff6b6b',          # Büyük
        
        # Gradient renkleri
        'gradient_start': '#667eea',
        'gradient_end': '#764ba2'
    }


def plot_magnitude_distribution(ax, df, colors):
    """Büyüklük dağılımı histogramı."""
    ax.set_facecolor(colors['card_bg'])
    
    # Histogram
    bins = np.arange(4.5, df['magnitude'].max() + 0.5, 0.25)
    n, bins_edges, patches = ax.hist(df['magnitude'], bins=bins, 
                                      edgecolor='white', linewidth=0.5, alpha=0.9)
    
    # Renklendirme
    for i, patch in enumerate(patches):
        mag = (bins_edges[i] + bins_edges[i+1]) / 2
        if mag >= 7.0:
            patch.set_facecolor(colors['mag_major'])
        elif mag >= 6.0:
            patch.set_facecolor(colors['mag_strong'])
        elif mag >= 5.0:
            patch.set_facecolor(colors['mag_moderate'])
        else:
            patch.set_facecolor(colors['mag_light'])
    
    ax.set_xlabel('Büyüklük (M)', fontsize=11, color=colors['text_primary'], fontweight='bold')
    ax.set_ylabel('Deprem Sayısı', fontsize=11, color=colors['text_primary'], fontweight='bold')
    ax.set_title('Buyukluk Dagilimi', fontsize=14, color=colors['primary'], 
                 fontweight='bold', pad=15)
    
    # Stil ayarları
    ax.tick_params(colors=colors['text_secondary'])
    ax.spines['bottom'].set_color(colors['card_border'])
    ax.spines['left'].set_color(colors['card_border'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.2, color=colors['grid'], linestyle='--')


def plot_depth_distribution(ax, df, colors):
    """Derinlik dağılımı."""
    ax.set_facecolor(colors['card_bg'])
    
    # Derinlik kategorileri
    df['depth_cat'] = df['depth'].apply(get_depth_category)
    depth_counts = df['depth_cat'].value_counts()
    
    # Sıralama
    order = ["Sığ (0-70 km)", "Orta (70-300 km)", "Derin (300+ km)"]
    depth_counts = depth_counts.reindex([o for o in order if o in depth_counts.index])
    
    # Renk paleti
    bar_colors = [colors['success'], colors['accent'], colors['secondary']][:len(depth_counts)]
    
    bars = ax.barh(range(len(depth_counts)), depth_counts.values, 
                   color=bar_colors, edgecolor='white', linewidth=0.5)
    
    ax.set_yticks(range(len(depth_counts)))
    ax.set_yticklabels(depth_counts.index, fontsize=10, color=colors['text_primary'])
    ax.set_xlabel('Deprem Sayısı', fontsize=11, color=colors['text_primary'], fontweight='bold')
    ax.set_title('Derinlik Dagilimi', fontsize=14, color=colors['primary'], 
                 fontweight='bold', pad=15)
    
    # Değerleri barlara ekle
    for bar, val in zip(bars, depth_counts.values):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
               f'{int(val)}', ha='left', va='center', fontsize=10, 
               color=colors['text_primary'], fontweight='bold')
    
    ax.tick_params(colors=colors['text_secondary'])
    ax.spines['bottom'].set_color(colors['card_border'])
    ax.spines['left'].set_color(colors['card_border'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.2, color=colors['grid'], linestyle='--', axis='x')


def plot_daily_timeline(ax, df, colors):
    """Günlük deprem zaman çizelgesi."""
    ax.set_facecolor(colors['card_bg'])
    
    daily_counts = df.groupby('date').size()
    dates = pd.to_datetime(daily_counts.index)
    
    # Alan grafiği
    ax.fill_between(dates, daily_counts.values, alpha=0.3, color=colors['primary'])
    ax.plot(dates, daily_counts.values, color=colors['primary'], linewidth=2.5, marker='o', 
            markersize=4, markerfacecolor=colors['accent'], markeredgecolor='white')
    
    # Ortalama çizgisi
    mean_val = daily_counts.mean()
    ax.axhline(y=mean_val, color=colors['secondary'], linestyle='--', linewidth=1.5, 
               label=f'Ortalama: {mean_val:.1f}')
    
    ax.set_xlabel('Tarih', fontsize=11, color=colors['text_primary'], fontweight='bold')
    ax.set_ylabel('Deprem Sayısı', fontsize=11, color=colors['text_primary'], fontweight='bold')
    ax.set_title('Günlük Deprem Sayisi', fontsize=14, color=colors['primary'], 
                 fontweight='bold', pad=15)
    
    ax.legend(loc='upper right', facecolor=colors['card_bg'], edgecolor=colors['card_border'],
              labelcolor=colors['text_primary'])
    
    # X ekseni formatı - daha iyi tarih gösterimi
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=4))  # Her 4 günde bir
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))
    ax.tick_params(colors=colors['text_secondary'], labelrotation=30, labelsize=9)
    ax.spines['bottom'].set_color(colors['card_border'])
    ax.spines['left'].set_color(colors['card_border'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.2, color=colors['grid'], linestyle='--')


def plot_world_map(ax, df, colors):
    """Dünya haritası üzerinde deprem lokasyonları."""
    ax.set_facecolor('#0d1b2a')  # Okyanus rengi
    
    # Kıta sınırları (basitleştirilmiş)
    ax.axhline(y=0, color=colors['grid'], linewidth=0.5, alpha=0.3)
    ax.axvline(x=0, color=colors['grid'], linewidth=0.5, alpha=0.3)
    
    # Harita ızgarası
    for lat in range(-60, 90, 30):
        ax.axhline(y=lat, color=colors['grid'], linewidth=0.3, alpha=0.2, linestyle=':')
    for lon in range(-180, 180, 60):
        ax.axvline(x=lon, color=colors['grid'], linewidth=0.3, alpha=0.2, linestyle=':')
    
    # Deprem noktaları
    sizes = (df['magnitude'] ** 2.5) * 3
    
    # Renk haritası
    scatter = ax.scatter(df['longitude'], df['latitude'], 
                        s=sizes, c=df['magnitude'], 
                        cmap='YlOrRd', alpha=0.7, 
                        edgecolors='white', linewidth=0.3)
    
    ax.set_xlim(-180, 180)
    ax.set_ylim(-90, 90)
    ax.set_xlabel('Boylam', fontsize=11, color=colors['text_primary'], fontweight='bold')
    ax.set_ylabel('Enlem', fontsize=11, color=colors['text_primary'], fontweight='bold')
    ax.set_title('Dünya Haritasi Uzerinde Depremler', fontsize=14, 
                color=colors['primary'], fontweight='bold', pad=15)
    
    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax, shrink=0.8, pad=0.02)
    cbar.set_label('Büyüklük', fontsize=10, color=colors['text_primary'])
    cbar.ax.yaxis.set_tick_params(color=colors['text_secondary'])
    cbar.outline.set_edgecolor(colors['card_border'])
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color=colors['text_secondary'])
    
    ax.tick_params(colors=colors['text_secondary'])
    ax.spines['bottom'].set_color(colors['card_border'])
    ax.spines['left'].set_color(colors['card_border'])
    ax.spines['top'].set_color(colors['card_border'])
    ax.spines['right'].set_color(colors['card_border'])


def plot_hourly_distribution(ax, df, colors):
    """Saatlik deprem dağılımı (radar/polar chart)."""
    ax.set_facecolor(colors['card_bg'])
    
    hourly = df.groupby('hour').size()
    hours = list(range(24))
    values = [hourly.get(h, 0) for h in hours]
    
    # Polar koordinatlar
    angles = np.linspace(0, 2*np.pi, 24, endpoint=False).tolist()
    values_closed = values + [values[0]]
    angles_closed = angles + [angles[0]]
    
    ax_polar = plt.subplot(ax.get_gridspec()[ax.get_subplotspec().rowspan, 
                                              ax.get_subplotspec().colspan], 
                          projection='polar', facecolor=colors['card_bg'])
    ax.remove()
    
    ax_polar.set_facecolor(colors['card_bg'])
    ax_polar.fill(angles_closed, values_closed, alpha=0.3, color=colors['primary'])
    ax_polar.plot(angles_closed, values_closed, color=colors['primary'], linewidth=2)
    ax_polar.scatter(angles, values, color=colors['accent'], s=40, zorder=5, edgecolors='white')
    
    # Saat etiketleri
    ax_polar.set_xticks(angles)
    ax_polar.set_xticklabels([f'{h:02d}:00' for h in hours], fontsize=8, 
                              color=colors['text_secondary'])
    ax_polar.set_title('Saatlik Dagilim (UTC)', fontsize=14, color=colors['primary'], 
                       fontweight='bold', pad=20)
    
    ax_polar.tick_params(colors=colors['text_secondary'])
    ax_polar.spines['polar'].set_color(colors['card_border'])
    ax_polar.grid(True, alpha=0.3, color=colors['grid'])
    
    return ax_polar


def plot_magnitude_vs_depth(ax, df, colors):
    """Büyüklük vs Derinlik scatter plot."""
    ax.set_facecolor(colors['card_bg'])
    
    sizes = (df['magnitude'] ** 2) * 8
    scatter = ax.scatter(df['magnitude'], df['depth'], 
                        s=sizes, c=df['significance'], 
                        cmap='plasma', alpha=0.7,
                        edgecolors='white', linewidth=0.3)
    
    ax.set_xlabel('Büyüklük (M)', fontsize=11, color=colors['text_primary'], fontweight='bold')
    ax.set_ylabel('Derinlik (km)', fontsize=11, color=colors['text_primary'], fontweight='bold')
    ax.set_title('Buyukluk vs Derinlik', fontsize=14, color=colors['primary'], 
                 fontweight='bold', pad=15)
    ax.invert_yaxis()
    
    cbar = plt.colorbar(scatter, ax=ax, shrink=0.7, pad=0.03)
    cbar.set_label('Önem Skoru', fontsize=10, color=colors['text_primary'])
    cbar.ax.yaxis.set_tick_params(color=colors['text_secondary'])
    cbar.outline.set_edgecolor(colors['card_border'])
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color=colors['text_secondary'])
    
    ax.tick_params(colors=colors['text_secondary'])
    ax.spines['bottom'].set_color(colors['card_border'])
    ax.spines['left'].set_color(colors['card_border'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.2, color=colors['grid'], linestyle='--')


def plot_top_earthquakes(ax, df, colors):
    """En büyük 10 deprem tablosu."""
    ax.set_facecolor(colors['card_bg'])
    ax.axis('off')
    
    top10 = df.nlargest(10, 'magnitude')[['time', 'magnitude', 'depth', 'place']].reset_index(drop=True)
    
    # Tablo başlığı
    ax.text(0.5, 0.95, 'EN BÜYÜK 10 DEPREM', fontsize=14, color=colors['primary'],
            fontweight='bold', ha='center', va='top', transform=ax.transAxes)
    
    # Tablo başlıkları
    headers = ['#', 'Tarih', 'M', 'Derinlik', 'Konum']
    col_positions = [0.02, 0.10, 0.30, 0.40, 0.55]
    
    y_start = 0.92
    y_step = 0.085  # Satır aralığını artırdık
    
    for i, (header, pos) in enumerate(zip(headers, col_positions)):
        ax.text(pos, y_start, header, fontsize=10, color=colors['accent'],
               fontweight='bold', ha='left', va='top', transform=ax.transAxes)
    
    # Ayırıcı çizgi (plot ile çünkü axhline transform desteklemiyor)
    ax.plot([0.02, 0.98], [y_start - 0.02, y_start - 0.02], 
            color=colors['card_border'], linewidth=1, transform=ax.transAxes)
    
    # Veriler
    for idx, row in top10.iterrows():
        y_pos = y_start - (idx + 1) * y_step
        
        # Sıra
        ax.text(col_positions[0], y_pos, f'{idx+1}', fontsize=9, 
               color=colors['text_primary'], ha='left', va='top', transform=ax.transAxes)
        
        # Tarih
        date_str = row['time'].strftime('%d.%m %H:%M')
        ax.text(col_positions[1], y_pos, date_str, fontsize=9, 
               color=colors['text_secondary'], ha='left', va='top', transform=ax.transAxes)
        
        # Büyüklük - renkli
        mag = row['magnitude']
        if mag >= 7.0:
            mag_color = colors['mag_major']
        elif mag >= 6.0:
            mag_color = colors['mag_strong']
        else:
            mag_color = colors['mag_moderate']
        ax.text(col_positions[2], y_pos, f'{mag:.1f}', fontsize=10, 
               color=mag_color, ha='left', va='top', fontweight='bold', transform=ax.transAxes)
        
        # Derinlik
        ax.text(col_positions[3], y_pos, f'{row["depth"]:.0f}km', fontsize=9, 
               color=colors['text_secondary'], ha='left', va='top', transform=ax.transAxes)
        
        # Konum (kısaltılmış)
        place = str(row['place'])[:40] + '...' if len(str(row['place'])) > 40 else str(row['place'])
        ax.text(col_positions[4], y_pos, place, fontsize=9, 
               color=colors['text_secondary'], ha='left', va='top', transform=ax.transAxes)


def create_stat_card(ax, value, label, icon, colors, value_color=None):
    """İstatistik kartı oluşturur."""
    ax.set_facecolor(colors['card_bg'])
    ax.axis('off')
    
    if value_color is None:
        value_color = colors['primary']
    
    # İkon ve değer
    ax.text(0.5, 0.7, icon, fontsize=28, ha='center', va='center', transform=ax.transAxes)
    ax.text(0.5, 0.35, str(value), fontsize=24, color=value_color, 
            fontweight='bold', ha='center', va='center', transform=ax.transAxes)
    ax.text(0.5, 0.1, label, fontsize=10, color=colors['text_secondary'], 
            ha='center', va='center', transform=ax.transAxes, wrap=True)
    
    # Kart çerçevesi
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color(colors['card_border'])
        spine.set_linewidth(2)


def create_infographic(df):
    """
    Ana infografik oluşturma fonksiyonu.
    Tüm grafikleri hiyerarşik bir düzende birleştirir.
    """
    colors = create_color_palette()
    
    # Büyük figür oluştur
    fig = plt.figure(figsize=(20, 28), facecolor=colors['background'])
    
    # GridSpec ile düzen - yükseklik oranları iyileştirildi
    gs = GridSpec(8, 4, figure=fig, 
                  height_ratios=[0.6, 0.8, 1.4, 1.0, 1.2, 1.2, 1.4, 0.25],
                  hspace=0.4, wspace=0.3,
                  left=0.06, right=0.94, top=0.96, bottom=0.02)
    
    # ========== BAŞLIK ALANI ==========
    ax_header = fig.add_subplot(gs[0, :])
    ax_header.set_facecolor(colors['background'])
    ax_header.axis('off')
    
    # Ana başlık
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    
    ax_header.text(0.5, 0.85, 'AYLIK DEPREM RAPORU', 
                   fontsize=32, color=colors['primary'], fontweight='bold',
                   ha='center', va='top', transform=ax_header.transAxes)
    ax_header.text(0.5, 0.55, f'Son 30 Günde Gerçekleşen M4.5+ Depremler',
                   fontsize=16, color=colors['text_secondary'],
                   ha='center', va='top', transform=ax_header.transAxes)
    ax_header.text(0.5, 0.3, f'{start_date.strftime("%d.%m.%Y")} - {end_date.strftime("%d.%m.%Y")} | Kaynak: USGS',
                   fontsize=12, color=colors['text_secondary'],
                   ha='center', va='top', transform=ax_header.transAxes)
    
    # ========== İSTATİSTİK KARTLARI ==========
    # Kartların verileri
    total_eq = len(df)
    max_mag = df['magnitude'].max()
    avg_depth = df['depth'].mean()
    tsunami_count = df['tsunami'].sum()
    
    # Büyüklük kategorileri
    df['mag_cat'] = df['magnitude'].apply(get_magnitude_category)
    major_count = len(df[df['magnitude'] >= 6.0])
    
    cards_data = [
        (f'{total_eq}', 'Toplam Deprem', '#', colors['primary']),
        (f'M{max_mag:.1f}', 'En Buyuk', '!', colors['secondary']),
        (f'{major_count}', 'Güçlü Deprem (M6.0+)', '*', colors['accent']),
        (f'{avg_depth:.0f}km', 'Ortalama Derinlik', 'v', colors['success']),
    ]
    
    for i, (value, label, icon, val_color) in enumerate(cards_data):
        ax_card = fig.add_subplot(gs[1, i])
        create_stat_card(ax_card, value, label, icon, colors, val_color)
    
    # ========== DÜNYA HARİTASI ==========
    ax_map = fig.add_subplot(gs[2, :])
    plot_world_map(ax_map, df, colors)
    
    # ========== BÜYÜKLÜK VE DERİNLİK ==========
    ax_mag = fig.add_subplot(gs[3, :2])
    plot_magnitude_distribution(ax_mag, df, colors)
    
    ax_depth = fig.add_subplot(gs[3, 2:])
    plot_depth_distribution(ax_depth, df, colors)
    
    # ========== ZAMAN SERİSİ ==========
    ax_timeline = fig.add_subplot(gs[4, :])
    plot_daily_timeline(ax_timeline, df, colors)
    
    # ========== BÜYÜKLÜK VS DERİNLİK ==========
    ax_scatter = fig.add_subplot(gs[5, :2])
    plot_magnitude_vs_depth(ax_scatter, df, colors)
    
    # ========== SAATLİK DAĞILIM (Polar) ==========
    ax_hourly = fig.add_subplot(gs[5, 2:], projection='polar', facecolor=colors['card_bg'])
    
    hourly = df.groupby('hour').size()
    hours = list(range(24))
    values = [hourly.get(h, 0) for h in hours]
    angles = np.linspace(0, 2*np.pi, 24, endpoint=False).tolist()
    values_closed = values + [values[0]]
    angles_closed = angles + [angles[0]]
    
    ax_hourly.set_facecolor(colors['card_bg'])
    ax_hourly.fill(angles_closed, values_closed, alpha=0.3, color=colors['primary'])
    ax_hourly.plot(angles_closed, values_closed, color=colors['primary'], linewidth=2)
    ax_hourly.scatter(angles, values, color=colors['accent'], s=40, zorder=5, edgecolors='white')
    ax_hourly.set_xticks(angles)
    ax_hourly.set_xticklabels([f'{h:02d}' for h in hours], fontsize=8, 
                              color=colors['text_secondary'])
    ax_hourly.set_title('Saatlik Dagilim (UTC)', fontsize=14, color=colors['primary'], 
                        fontweight='bold', pad=20, y=1.08)
    ax_hourly.tick_params(colors=colors['text_secondary'])
    ax_hourly.grid(True, alpha=0.3, color=colors['grid'])
    
    # ========== EN BÜYÜK DEPREMLER TABLOSU ==========
    ax_table = fig.add_subplot(gs[6, :])
    plot_top_earthquakes(ax_table, df, colors)
    
    # ========== ALT BİLGİ ==========
    ax_footer = fig.add_subplot(gs[7, :])
    ax_footer.set_facecolor(colors['background'])
    ax_footer.axis('off')
    
    ax_footer.text(0.5, 0.6, 
                   'Not: Buyukluk olcegi Richter skalasina goredir. M4.5+ depremler genellikle hissedilebilir niteliktedir.',
                   fontsize=10, color=colors['text_secondary'],
                   ha='center', va='center', transform=ax_footer.transAxes)
    ax_footer.text(0.5, 0.2, 
                   f'Oluşturulma: {datetime.now().strftime("%d.%m.%Y %H:%M")} | Python ile Veri Görselleştirme',
                   fontsize=9, color=colors['grid'],
                   ha='center', va='center', transform=ax_footer.transAxes)
    
    # Kaydet
    output_path = 'earthquake_infographic.png'
    plt.savefig(output_path, dpi=150, facecolor=colors['background'], 
                edgecolor='none', bbox_inches='tight')
    print(f"\n[OK] Infografik kaydedildi: {output_path}")
    
    plt.show()
    return fig


def create_individual_charts(df):
    """
    Bireysel grafikleri ayrı ayrı oluşturur.
    Hiyerarşik yaklaşım: Önce basit grafikler, sonra karmaşık olanlar.
    """
    colors = create_color_palette()
    
    print("\n" + "=" * 60)
    print("[*] Bireysel Grafikler Olusturuluyor...")
    print("=" * 60)
    
    # 1. Büyüklük Histogramı
    fig1, ax1 = plt.subplots(figsize=(10, 6), facecolor=colors['background'])
    plot_magnitude_distribution(ax1, df, colors)
    plt.tight_layout()
    plt.savefig('chart_01_magnitude_distribution.png', dpi=120, 
                facecolor=colors['background'], bbox_inches='tight')
    print("[+] Buyukluk dagilimi kaydedildi")
    plt.close()
    
    # 2. Derinlik Dağılımı
    fig2, ax2 = plt.subplots(figsize=(10, 6), facecolor=colors['background'])
    plot_depth_distribution(ax2, df, colors)
    plt.tight_layout()
    plt.savefig('chart_02_depth_distribution.png', dpi=120, 
                facecolor=colors['background'], bbox_inches='tight')
    print("[+] Derinlik dagilimi kaydedildi")
    plt.close()
    
    # 3. Günlük Zaman Çizelgesi
    fig3, ax3 = plt.subplots(figsize=(14, 6), facecolor=colors['background'])
    plot_daily_timeline(ax3, df, colors)
    plt.tight_layout()
    plt.savefig('chart_03_daily_timeline.png', dpi=120, 
                facecolor=colors['background'], bbox_inches='tight')
    print("[+] Günlük zaman cizelgesi kaydedildi")
    plt.close()
    
    # 4. Dünya Haritası
    fig4, ax4 = plt.subplots(figsize=(16, 8), facecolor=colors['background'])
    plot_world_map(ax4, df, colors)
    plt.tight_layout()
    plt.savefig('chart_04_world_map.png', dpi=120, 
                facecolor=colors['background'], bbox_inches='tight')
    print("[+] Dünya haritasi kaydedildi")
    plt.close()
    
    # 5. Büyüklük vs Derinlik
    fig5, ax5 = plt.subplots(figsize=(10, 8), facecolor=colors['background'])
    plot_magnitude_vs_depth(ax5, df, colors)
    plt.tight_layout()
    plt.savefig('chart_05_magnitude_vs_depth.png', dpi=120, 
                facecolor=colors['background'], bbox_inches='tight')
    print("[+] Buyukluk-Derinlik iliskisi kaydedildi")
    plt.close()
    
    # 6. Saatlik Polar Grafik
    fig6, ax6 = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'),
                              facecolor=colors['background'])
    
    hourly = df.groupby('hour').size()
    hours = list(range(24))
    values = [hourly.get(h, 0) for h in hours]
    angles = np.linspace(0, 2*np.pi, 24, endpoint=False).tolist()
    values_closed = values + [values[0]]
    angles_closed = angles + [angles[0]]
    
    ax6.set_facecolor(colors['card_bg'])
    ax6.fill(angles_closed, values_closed, alpha=0.3, color=colors['primary'])
    ax6.plot(angles_closed, values_closed, color=colors['primary'], linewidth=2)
    ax6.scatter(angles, values, color=colors['accent'], s=60, zorder=5, edgecolors='white')
    ax6.set_xticks(angles)
    ax6.set_xticklabels([f'{h:02d}:00' for h in hours], fontsize=10, 
                         color=colors['text_secondary'])
    ax6.set_title('Saatlik Deprem Dagilimi (UTC)', fontsize=16, color=colors['primary'], 
                  fontweight='bold', pad=20)
    ax6.tick_params(colors=colors['text_secondary'])
    ax6.grid(True, alpha=0.3, color=colors['grid'])
    
    plt.tight_layout()
    plt.savefig('chart_06_hourly_polar.png', dpi=120, 
                facecolor=colors['background'], bbox_inches='tight')
    print("[+] Saatlik polar grafik kaydedildi")
    plt.close()
    
    print("\n[OK] Tum bireysel grafikler olusturuldu!")


def main():
    """Ana program fonksiyonu."""
    print("\n" + "=" * 60)
    print("   DEPREM VERI GORSELLESTIRME UYGULAMASI")
    print("=" * 60 + "\n")
    
    # Veri çekme
    df = fetch_earthquake_data()
    
    if df is None or len(df) == 0:
        print("[HATA] Veri cekilemedi. Program sonlandiriliyor.")
        return
    
    # Veri özeti
    print("\n[*] VERI OZETI")
    print("-" * 40)
    print(f"  • Toplam Deprem: {len(df)}")
    print(f"  • Büyüklük Aralığı: M{df['magnitude'].min():.1f} - M{df['magnitude'].max():.1f}")
    print(f"  • Ortalama Büyüklük: M{df['magnitude'].mean():.2f}")
    print(f"  • Derinlik Aralığı: {df['depth'].min():.1f}km - {df['depth'].max():.1f}km")
    print(f"  • Ortalama Derinlik: {df['depth'].mean():.1f}km")
    print("-" * 40)
    
    # Bireysel grafikler (hiyerarşi - 1. seviye)
    create_individual_charts(df)
    
    # İnfografik oluştur (hiyerarşi - 2. seviye: tüm grafikleri birleştir)
    print("\n" + "=" * 60)
    print("[*] INFOGRAFIK OLUSTURULUYOR...")
    print("=" * 60)
    
    create_infographic(df)
    
    print("\n" + "=" * 60)
    print("   PROGRAM BASARIYLA TAMAMLANDI!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()