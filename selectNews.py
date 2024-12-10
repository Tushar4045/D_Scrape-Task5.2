import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

newsUrl = 'https://www.ft.com/stream/7e37c19e-8fa3-439f-a870-b33f0520bcc0'

newsHeader = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "if-none-match": "W/\"363c8-PgVNHne7gbsYgyzVja+QMN6S+aM\"",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "FTAllocation=1a93dae2-0255-4a87-8d67-c2a6912221c1; FTClientSessionId=dd44fefc-572c-441b-bcda-d24aa89219b8; spoor-id=cm151vpvt0000356mu7ce8ies; zit.data.toexclude=0; consentUUID=5082e795-9cf9-4f7a-bbef-9b58bee8200c_36; consentDate=2024-09-16T13:38:19.492Z; FTConsent=marketingBypost%3Aoff%2CmarketingByemail%3Aoff%2CmarketingByphonecall%3Aoff%2CmarketingByfax%3Aoff%2CmarketingBysms%3Aoff%2CenhancementBypost%3Aoff%2CenhancementByemail%3Aoff%2CenhancementByphonecall%3Aoff%2CenhancementByfax%3Aoff%2CenhancementBysms%3Aoff%2CbehaviouraladsOnsite%3Aon%2CdemographicadsOnsite%3Aon%2CrecommendedcontentOnsite%3Aon%2CprogrammaticadsOnsite%3Aon%2CcookiesUseraccept%3Aoff%2CcookiesOnsite%3Aoff%2CmembergetmemberByemail%3Aoff%2CpermutiveadsOnsite%3Aon%2CpersonalisedmarketingOnsite%3Aon; FTCookieConsentGDPR=true; _gcl_au=1.1.491005694.1726493934; permutive-id=9a1bfb20-ac89-43a4-8c2f-8b8bce90d72b; __exponea_etc__=da414796-50f7-4a9e-b7dd-edd29210f190; __exponea_time2__=-0.43251490592956543; _cb=DfLirQDmg318C74KlJ; usnatUUID=00af4c63-3644-43e1-92b0-152972daba44; o-typography-fonts-loaded=1; _sxh=1499,; _sxo={\"R\":1,\"tP\":3,\"tM\":0,\"sP\":1,\"sM\":0,\"dP\":3,\"dM\":0,\"dS\":1,\"tS\":2,\"cPs\":1,\"lPs\":[0,60,1],\"sSr\":1,\"sWids\":[],\"wN\":0,\"cdT\":0,\"F\":1,\"RF\":1,\"w\":0,\"SFreq\":3,\"last_wid\":0,\"bid\":1036,\"accNo\":\"\",\"clientId\":\"\",\"isEmailAud\":0,\"isPanelAud\":0,\"hDW\":0,\"isRegAud\":0,\"isExAud\":0,\"isDropoff\":0,\"devT\":0,\"exPW\":0,\"Nba\":-1,\"userName\":\"\",\"dataLayer\":\"\",\"localSt\":\"\",\"emailId\":\"\",\"emailTag\":\"\",\"subTag\":\"\",\"lVd\":\"2024-10-29\",\"oS\":\"dd44fefc-572c-441b-bcda-d24aa89219b8\",\"cPu\":\"https://www.ft.com/content/5004fbc6-23e2-4b9f-9885-14e1ea724ce2\",\"pspv\":1,\"pslv\":49472,\"pssSr\":60,\"pswN\":0,\"psdS\":0,\"pscdT\":0,\"RP\":0,\"TPrice\":0,\"ML\":\"\",\"isReCaptchaOn\":false,\"reCaptchaSiteKey\":\"\",\"reCaptchaSecretKey\":\"\",\"extRefer\":\"\",\"dM2\":0,\"tM2\":0,\"sM2\":0,\"RA\":0,\"ToBlock\":-1,\"CC\":null,\"groupName\":null}; _chartbeat2=.1726495248165.1733802655452.0000000000000011.CX6I6sCRQWfsC3KUsNBfrqgxuZ2ih.1; _cb_svref=external; _clck=16pt4au%7C2%7Cfrl%7C0%7C1720; __gads=ID=67c1ab88478605c4:T=1726495243:RT=1733802665:S=ALNI_MYKhRCYQfmoRouNeU50K4_u9v_-Vw; __eoi=ID=8afff4b27e19e421:T=1726495243:RT=1733802665:S=AA-Afjb_5rzJNyXskTan_qzK0P__; _rdt_uuid=1726493933923.dcd51af0-acbf-439e-ad7c-30ed7ec30461; _uetsid=670ea6e0b5e411efb25fa515900fbcf8; _uetvid=0420f0e0743111efa6230329bc33971c; _clsk=1qcuf3c%7C1733802674554%7C3%7C0%7Ch.clarity.ms%2Fcollect"
  }

newsResp = rq.get(url=newsUrl, headers=newsHeader)

newsSoup = BeautifulSoup(newsResp.content, 'html.parser')
allNews = newsSoup.select('div[class="o-teaser-collection o-teaser-collection--stream"] > ul > li')
selectNews = []

for n in allNews:
    date = n.select_one('div[class="stream-card__date"] > time')
    heading = n.select_one('div[class="o-teaser__heading"] > a')
    content = n.select_one('p[class="o-teaser__standfirst"] > a')
    img = n.select_one('div[class="o-teaser__image-placeholder"] > img ')
    newsData = {
        'Date' : date.attrs['datetime'] if date else None,
        'Heading' : heading.text.strip() if heading else None,
        'Content' : content.text.strip() if content else None,
        'imgAlt' :img.attrs['alt'] if img else None,
        'imgUrl' : img.attrs['data-src'] if img else None
    }
    selectNews.append(newsData)
df = pd.DataFrame(selectNews)
selectNewsDf = df.replace({r'[“”‘’]': '"'}, regex=True)
selectNewsDf.to_csv('selectNews.csv')

