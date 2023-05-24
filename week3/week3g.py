import re
import random
from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse

app = FastAPI()

# API = Application Programming Interface

@app.get("/topla")
async def topla( birinci: int, ikinci: int ) -> int:

    # ....................
    return {"result": birinci + ikinci, "fark": birinci - ikinci}


@app.get("/complexFunction")
async def complexFunction( productName: str ) -> int:
    return random.randint(100, 500)



def cleanup( text: str ) -> str:
    text = re.sub("[^\w]", " ", text)
    text = re.sub("\s+", " ", text)
    text = text.strip()
    text = text.lower()
    return text

@app.post("/textZip")
async def textZip( text: str ) -> dict:
    #: Cleanup text
    text = cleanup( text )
    #: Split into words
    words = text.split(" ")
    #: Get the frequency of the words
    counts = {}
    for w in words:
        if len(w) > 4:
            if w not in counts:
                counts[w] = 0
            counts[w] += 1
    #: Filter out some most freq
    counts = {k: v for k,v in counts.items() if len(k) * v > 80}
    #: Re-decorate the words
    words = [w[0] + "#" if w in counts else w for w in words]
    #: Join
    text = " ".join(words)
    #: Return 
    return {"text": text, "map": counts}



@app.get("/forecast", response_class=HTMLResponse)
async def forecast(  ) :

    tahminler = {
        'Nevresim Takimi Sarev Arno Flanel Nt Ck 2Y D Yesil': 30,
        'Nevresim Takimi Sarev Arno Flanel Nt Ck 2Y D Gri': 833,
        'Pylesos Electrolux Espc7Green': 234,
        'Tozsoran Electrolux Espc7Green': 923,
        'Pylesos Electrolux Esp754Iw': 435,
        'Tozsoran Electrolux Esp754Iw': 819,
        'Tozsoran Electrolux Eusc64': 491,
        'Pylesos Electrolux Eusc64': 198,
        'Tozsoran Electrolux Ec41 Anim': 625,
        'Pylesos Electrolux Ec41 Anim': 893,
        'Bezprovodnoj Pylesos Electrolux Eerc75Wrk': 132,
        'Naqilsiz Tozsoran Electrolux Eerc75Wrk': 667,
        'Naqilsiz Tozsoran Electrolux Eerc75Db': 755,
        'Bezprovodnoj Pylesos Electrolux Eerc75Db': 544,
        'Moyu%D1%89Ij Pylesos Bosch Bwd421Pet': 396,
        'Yuyucu Tozsoran Bosch Bwd421Pet': 768,
        'Yuyucu Tozsoran Bosch Bwd420Hyg': 706,
        'Moyu%D1%89Ij Pylesos Bosch Bwd420Hyg': 600,
        'Buxarli Generator Tefal Pro Express Ultimate Care Gv9570': 691,
        'Parogenerator Tefal Pro Express Ultimate Care Gv9570': 72,
        'Buxarli Generator Tefal Pro Express Ultimate Gv9566': 666,
        'Parogenerator Tefal Pro Express Ultimate Gv9566': 571,
        'Buxarli Generator Tefal Express Anti Calc Sv8054': 633,
        'Parogenerator Tefal Express Anti Calc Sv8054': 527,
        'Oppo Reno 7 4 128 Gb Cosmic Black': 199,
        'Oppo A57S 4 128 Gb Sky Blue': 975,
        'Oppo A57S 4 64 Gb Starry Black': 597,
        'Oppo A57S 4 64 Gb Sky Blue': 81,
        'Oppo A17 4 64 Gb Blue': 418,
        'Noutbuk Hp Envy 15 6 Fhd Ips 50H40Ea': 788,
        'Notbuk Hp Envy 15 6 Fhd Ips 50H40Ea': 486,
        'Plite Zanussi Gpz263Sb': 6,
     
    }


    textarea = ""
    for tahmin in tahminler:
        textarea += "<b>" + tahmin + "</b>: <span style='color:red;'>" + str(tahminler[tahmin]) + "</span><br>\n"


    return f"""
    <html>
        <body>
            <h1>API ile ilgili genel bilgi</h1>
            <p>
                Bu API, ......... .asadsfafadsf sdf ddescription. .....
            </p>
            <div style='border-style:solid; border-width:1px;'>
            {textarea}
            </div>
        </body>
    </html>
    """

# HTML TAGS <x>




# Forecast the next 5 days prediciton of each product

# CALLING A FUNCTION FROM OUTSIDE
# WEB SERVICE
# FastApi


uvicorn.run(
    app,
    host="127.0.01",
    port=5800,
    log_level="debug",
)


