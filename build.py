from pathlib import Path

repo = 'soundbar-box-contents-comparison'
base = f'https://elechid.github.io/{repo}/'
samsung = 'https://www.samsung.com/th/support/model/HW-Q990H/XT/'
jbl800 = 'https://jp.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw5bbb8082/pdfs/HA_JBL_Bar%20800MK2_OM_Global_EN_V6.pdf'
jbl1300 = 'https://dk.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw1138a118/pdfs/HA_JBL_Bar%201300MK2_OM_Global_EN_V4.pdf'
spec1300 = 'https://uk.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dwfa645752/pdfs/JBL_BAR_1300MK2_Specsheet_EN.pdf'
models = [
    ('Samsung HW-Q990H', ('國際版 HW-Q990H/XT，店內商品 SKU 已核對。','International HW-Q990H/XT, matched to the store SKU.'), 'samsung-q-series-hw-q990h-11-1-4ch-soundbar-with-subwoofer-black-2026', [samsung,'https://www.samsung.com/th/audio-devices/soundbar/q990h-black-hw-q990h-xt/','https://www.samsung.com/au/support/tv-audio-video/connecting-the-power-and-devices-for-the-q-series-soundbar/']),
    ('JBL Bar 800MK2', ('店內列為國際版，區域 SKU 及插頭待核實。','Listed as international stock. Regional SKU and plug type are unverified.'), 'jbl-bar-800mk2-7-1-dolby-atmos-sound-bar-2025international-version', [jbl800,'https://vn.jbl.com/on/demandware.static/-/Sites-masterCatalog_Harman/default/dwc4331d32/pdfs/JBL_BAR_800MK2_Specsheet_EN%20%28BR%29.pdf']),
    ('JBL Bar 1300MK2', ('店內列為國際版，區域 SKU 及插頭待核實。','Listed as international stock. Regional SKU and plug type are unverified.'), 'jbl-bar-1300mk2-11-1-4-dolby-atmos-sound-bar-2025international-version', [jbl1300,spec1300]),
]
rear_jbl = ('附送兩隻可拆式充電後置。','Two detachable rechargeable rear speakers included.')
hdmi_jbl = ('原廠列附送一條 1.2 米 HDMI 線。','JBL lists one 1.2 m HDMI cable.')
mount_jbl = ('原廠列附送主機及後置掛架、螺絲和定位紙。','JBL lists main-bar and rear-speaker brackets, screws and a mounting template.')
power_jbl = ('主機和低音炮各需一個交流電源。後置以電池運作，可接回主機充電。原廠標示 100–240V AC、50/60Hz。','The main bar and sub each need AC power. The rears run on rechargeable batteries and dock on the bar to charge. JBL specifies 100–240 V AC, 50/60 Hz.')
extra_jbl = ('如想分開充電，USB-C 充電線及合適電源另備。','For separate charging, supply a USB-C cable and compatible power source.')
verify_jbl = ('待核實：店內批次的區域 SKU、電源線數量和插頭。JBL 說明這些會因地區而異。','Unverified: the regional SKU, power-cord count and plug type for the store batch. JBL says these vary by region.')
rows = [
    (('後置喇叭','Rear speakers'), [('附送兩隻獨立無線後置，各需接電。','Two wireless rear speakers included. Each requires AC power.'),rear_jbl,rear_jbl]),
    (('低音炮','Subwoofer'), [('附送一個無線低音炮。','One wireless subwoofer included.'),('附送一個 10 吋無線低音炮。','One 10-inch wireless subwoofer included.'),('附送一個裝有兩個 8 吋單元的無線低音炮箱。','One wireless subwoofer cabinet with two 8-inch drivers included.')]),
    (('HDMI 線','HDMI cable'), [('原廠手冊列有 HDMI 線，實際批次是否附送待核實。','Samsung lists an HDMI cable in the manual. Inclusion in the supplied batch remains unverified.'),hdmi_jbl,hdmi_jbl]),
    (('掛牆配件','Wall mounting'), [('附送主機掛牆套件。後置掛架未列於盒內清單。','Main-bar mounting kit included. Rear brackets are absent from the box list.'),mount_jbl,mount_jbl]),
    (('供電要求','Power requirements'), [('主機、低音炮和兩隻後置各需一個交流電源，共四個插位。XT 原廠手冊列四條電源線。','One AC outlet each for the main bar, subwoofer and both rear speakers, four in total. The XT manual lists four power cords.'),power_jbl,power_jbl]),
    (('另購／自備','Buy separately / supply'), [('需要掛後置時，另備合適掛架或腳架。入牆固定件按牆身選配。如果盒內沒有 HDMI 線，需自備。','Supply suitable rear mounts or stands if needed, choose wall fixings for your wall type, and supply an HDMI cable if the box lacks one.'),extra_jbl,extra_jbl]),
    (('待核實','Unverified'), [('待核實：店內批次的 HDMI 線、電源插頭及各部件電壓標籤。','Unverified: HDMI cable inclusion, plug type and each component’s voltage label for the store batch.'),verify_jbl,verify_jbl]),
]
for zh in (True,False):
    def t(a,b):
        return a if zh else b
    def loc(pair):
        return pair[0 if zh else 1]
    title = t('Soundbar 盒內配件對照表','Soundbar box contents comparison')
    intro = t('比較 Samsung HW-Q990H、JBL Bar 800MK2 和 Bar 1300MK2 的盒內配件及供電。','Compare box contents and power requirements for the Samsung HW-Q990H, JBL Bar 800MK2 and Bar 1300MK2.')
    store = 'https://elechid.com'+t('','/en')
    cards = []
    for i,(model,version,handle,sources) in enumerate(models):
        details = ''.join(f'<dt>{loc(label)}</dt><dd>{loc(values[i])}</dd>' for label,values in rows)
        refs = ' · '.join(f'<a href="{source}">{t("原廠資料","Manufacturer source")} {n}</a>' for n,source in enumerate(sources,1))
        cards.append(f'<article><h2>{model}</h2><p class="version">{loc(version)}</p><dl>{details}</dl><p class="links"><a href="{store}/products/{handle}">{t("Elechid 商品頁","Elechid product page")}</a> · {refs}</p></article>')
    file = t('zh.html','index.html')
    (Path(__file__).parent/file).write_text(f'''<!doctype html>
<html lang="{t('zh-Hant-HK','en-HK')}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Elechid 音立</title><meta name="description" content="{intro}">
<link rel="canonical" href="{base+t('zh.html','')}"><link rel="alternate" hreflang="en-HK" href="{base}"><link rel="alternate" hreflang="zh-Hant-HK" href="{base}zh.html"><link rel="stylesheet" href="style.css"></head>
<body><header><nav><a href="{store}/">Elechid 音立</a><a href="{t('./','zh.html')}" lang="{t('en','zh-Hant')}">{t('English','繁體中文')}</a></nav></header>
<main><h1>{title}</h1><p>{intro}</p>
<p>{t('擺位前先數插位：Q990H 共需四個交流電源。兩款 JBL 各需兩個，後置可拆下用電池。','Plan for four AC outlets with the Q990H. Both JBL models need two, with battery-powered detachable rears.')}</p>
<div class="cards">{''.join(cards)}</div></main>
<footer><a href="https://github.com/Elechid/{repo}">{t('原始碼','Source code')}</a> · <a href="https://github.com/Elechid">{t('Elechid 工具索引','Elechid tool index')}</a></footer></body></html>
''',encoding='utf-8')
