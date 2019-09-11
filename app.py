from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

frettir = [["„Upp­lýs­um ekki um smá­atriði“", "Ekk­ert flugrekstr­ar­leyfi hef­ur verið veitt af hálfu banda­rískra yf­ir­valda fyr­ir arf­taka WOW air ef marka má gagna­grunn banda­rískra yf­ir­valda. Jafn­framt hef­ur flug­mála­deild banda­ríska sam­gönguráðuneyt­is­ins ekki fengið neina um­sókn um slíkt leyfi, en þeim ber að birta það í gagna­grunn­in­um sem aðgengi­leg­ur er al­menn­ingi.", "https://cdn.mbl.is/frimg/1/15/63/1156303.jpg", "sigmundurad@frettir.is"], ["Lést eft­ir björg­un úr brenn­andi húsi", "Karl­maður, sem bjargað var úr brenn­andi húsi við Hlíðar­veg í Reykja­nes­bæ síðdeg­is á föstu­dag, lést á Land­spít­al­an­um síðar sama dag. \nÞetta staðfest­ir Svein­björn Hall­dórs­son, lög­reglu­full­trúi hjá lög­regl­unni á Suður­nesj­um, í sam­tali við mbl.is, en Vís­ir greindi fyrst frá.", "https://m2.mbl.is/xfWbVL2zBwleYKMCTgkAKRyc3-M=/970x606/smart/frimg/1/7/5/1070579.jpg", "sigmundurbc@frettir.is"], ["Vaxta­lækk­an­ir skili sér í hús­næðis­verð", "Gera má ráð fyr­ir að vaxta­lækk­an­ir Seðlabanka hafi áhrif á hús­næðis­vexti al­mennt. Slík­ar vaxta­lækk­an­ir gætu þrýst hús­næðis­verði upp á við. Þetta er mat Gunn­ars Bjarna Viðars­son­ar, sér­fræðings í grein­ing­ar­deild Ari­on banka.", "https://m2.mbl.is/XTmUsxDfkf3x0OmHO6SL3kKKN7Q=/970x606/smart/frimg/1/15/72/1157266.jpg", "gurragris@frettir.is"], ["Heit­asta græn­metið hér­lend­is í dag", "Græn­meti er ekki bara græn­meti eins og þið vitið öll og nú ber svo við að sam­fé­lags­miðlar nán­ast loga vegna umræðna um það sem við get­um ein­ung­is full­yrt að sé vin­sæl­asta og eft­ir­sótt­asta græn­metið í dag: Blóm­kál!", "https://cdn.mbl.is/frimg/1/15/17/1151766.jpg", "sapukula@frettir.is"]]

@app.route("/")
def home():
    return render_template('default.html')

@app.route("/kt/<kt>")
def kennitala(kt):
    summa = 0
    for i in str(kt):
        summa += int(i)

    return render_template('ktsumma.html', summa=summa, kt=kt )

'''@app.route("/tezts")
def thistest():
    return render_template("default.html", stuff=)'''

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    #app.run()