LAST_POSSIBLE_DAY = "http://service.tsetmc.com/tsev2/data/TseClient2.aspx?t=LastPossibleDeven"
"""Response would be like:
20231022;20231022
"""

TICKER_HISTORY = "http://old.tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i={insCode}"
TICKER_OLD_PAGE = "http://old.tsetmc.com/Loader.aspx?ParTree=151311&i={insCode}"
TICKER_NEW_PAGE = "http://www.tsetmc.com/instInfo/{insCode}"
TICKER_INSTRUMENT_INFO_FAST = "http://old.tsetmc.com/tsev2/data/instinfofast.aspx?i={insCode}&c=1"
GROUP_TICKER = "http://old.tsetmc.com/tsev2/data/InstValue.aspx?g={}&t=g&s={insCode}"
INDEX_COMPANY = "http://cdn.tsetmc.com/api/ClosingPrice/GetIndexCompany/{insCode}"
GET_STATIC_DATA = "http://cdn.tsetmc.com/api/StaticData/GetStaticData"

ALL_TICKERS = "http://old.tsetmc.com/Loader.aspx?ParTree=111C1417"
#Response in an HTML

SEARCH = "http://old.tsetmc.com/tsev2/data/search.aspx?skey={key}"
#response may contains several results but the best one is the first one

TICKER_INSTRUMENT_INFO = "http://cdn.tsetmc.com/api/Instrument/GetInstrumentInfo/{insCode}"
"""Response would be like:
{
    "instrumentInfo": {
        "eps": {
            "epsValue": null,
            "estimatedEPS": "310",
            "sectorPE": 11.69,
            "psr": 0.0
        },
        "sector": {
            "dEven": 0,
            "cSecVal": "70 ",
            "lSecVal": "انبوه سازي، املاك و مستغلات"
        },
        "staticThreshold": {
            "insCode": null,
            "dEven": 0,
            "hEven": 0,
            "psGelStaMax": 16390.00,
            "psGelStaMin": 14250.00
        },
        "minWeek": 14000.00,
        "maxWeek": 15460.00,
        "minYear": 5290.00,
        "maxYear": 37040.00,
        "qTotTran5JAvg": 41414302.0,
        "kAjCapValCpsIdx": "33",
        "dEven": 20231023,
        "topInst": 1,
        "faraDesc": "",
        "contractSize": 0,
        "nav": 0.0000,
        "underSupervision": 0,
        "cValMne": null,
        "lVal18": "Shahed Inv.",
        "cSocCSAC": null,
        "lSoc30": null,
        "yMarNSC": null,
        "yVal": "300",
        "insCode": "63481599728522324",
        "lVal30": "سرمايه‌ گذاري‌ شاهد",
        "lVal18AFC": "ثشاهد",
        "flow": 1,
        "cIsin": "IRO1SAHD0006",
        "zTitad": 6290412000.0,
        "baseVol": 2516165,
        "instrumentID": "IRO1SAHD0001",
        "cgrValCot": "N1",
        "cComVal": "1",
        "lastDate": 0,
        "sourceID": 0,
        "flowTitle": "بازار بورس",
        "cgrValCotTitle": "بازار اول (تابلوی اصلی) بورس"
    }
}
"""

# ---------- اطلاعیه -----------
GET_PREPARED_DATA = "http://cdn.tsetmc.com/api/Codal/GetPreparedData/{n}"
"""Response would be like:
{
    "preparedData": [
        {
            "id": 548178,
            "symbol": "ثشاهد",
            "name": "شاهد",
            "title": "اطلاعات و صورت‌های مالی میاندوره‌ای  دوره 3 ماهه منتهی به  1402/06/31 (حسابرسی نشده)",
            "sentDateTime_Gregorian": "2023-10-22T21:43:39",
            "publishDateTime_Gregorian": "2023-10-22T21:43:39",
            "publishDateTime_DEven": 20231022,
            "mainTableRowID": 554872,
            "hasHtmlReport": 1,
            "hasExcelReport": 1,
            "hasPDFReport": 2,
            "hasXMLReport": 0,
            "attachmentID": 476817,
            "contentType": 10,
            "fileName": "\"گزارش تفسیری مدیریت 31  شهریور 1402.pdf\"",
            "fileExtension": "pdf",
            "tracingNo": "1095625"
        },
        ...
    ]
}
"""

CLOSING_PRICE_DAILY_LIST = "http://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceDailyList/{insCode}/{n}"
"""Response would be like:
{
    "closingPriceDaily": [
        {
            "priceChange": 1010.00,
            "priceMin": 14130.00,
            "priceMax": 15460.00,
            "priceYesterday": 14450.00,
            "priceFirst": 14210.00,
            "last": false,
            "id": 0,
            "insCode": "63481599728522324",
            "dEven": 20231022,
            "hEven": 122956,
            "pClosing": 15320.00,
            "iClose": false,
            "yClose": true,
            "pDrCotVal": 15460.00,
            "zTotTran": 9879.0,
            "qTotTran5J": 104896419.0,
            "qTotCap": 1607174440180.00
        },
        ...
    ]
}
"""
GET_MESSAGE_BY_INSCODE = "http://cdn.tsetmc.com/api/Msg/GetMsgByInsCode/{insCode}"
GET_MESSAGE_BY_FLOW = "http://cdn.tsetmc.com/api/Msg/GetMsgByFlow/{flow}/{n}"
"""Response would be like:
{
    "msg":[
        {
            "tseMsgIdn":172395,
            "dEven":20231023,
            "hEven":154736,
            "tseTitle":"اطلاعيه مهم درخصوص صندوق سرمايه گذاري پاداش سهامداري توسعه يكم(سپاس)",
            "tseDesc":"به اطلاع سرمايه گذاران محترم مي رساند، پيرو تصميمات مورخ 1402/05/07 مجمع صندوق  سرمايه گذاري پاداش سهامداري توسعه يکم(سپاس) مبني بر تغيير نام صندوق مذکور و  مجوز سازمان بورس و اوراق بهادار در اين خصوص، نماد معاملاتي صندوق سرمايه گذاري  پاداش سهامداري توسعه يکم(سپاس) پس از پايان جلسه معاملاتي روز سه شنبه مورخ  1402/08/02، به منظور انجام فرايند تغيير نام و نماد صندوق مذكور در سامانه  معاملات و پس از معاملات، متوقف مي گردد. شايان ذکر است نماد معاملاتي صندوق  مذکور از (سپاس) به (تداوم) و همچنين نام فارسي نماد صندوق نيز از (صندوق س.  پاداش سهامداري-ثابت) به (صندوق تداوم اطمينان تمدن-ثابت) تغيير مي يابد. مديريت  ابزارهاي نوين مالي شركت بورس اوراق بهادار تهران",
            "flow":0
        },
        ...
    ]
}"""

ALL_INSTRUMENT_STATE_CHANGES = "http://cdn.tsetmc.com/api/MarketData/GetInstrumentStateAll/{insCode}"
TOP_INSTRUMENT_STATE_CHANGES = "http://cdn.tsetmc.com/api/MarketData/GetInstrumentStateTop/{n}"
"""Response would be like:
{
    "instrumentState": [
        {
            "idn": 1164910,
            "dEven": 20231023,
            "hEven": 154258,
            "insCode": "28893762709504404",
            "lVal18AFC": "سپيد مطهر06",
            "lVal30": "مرابحه سپيد مطهرانتخاب 060719",
            "cEtaval": "AS",
            "realHeven": 0,
            "underSupervision": 0,
            "cEtavalTitle": "مجاز-متوقف"
        },
        ...
    ]
}
"""

GET_CLOSING_PRICE_INFO = "http://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceInfo/{insCode}"
"""Response would be like:
{
    "closingPriceInfo": {
        "instrumentState": {
            "idn": 0,
            "dEven": 0,
            "hEven": 0,
            "insCode": null,
            "cEtaval": "A ",
            "realHeven": 0,
            "underSupervision": 0,
            "cEtavalTitle": "مجاز"
        },
        "instrument": null,
        "lastHEven": 122958,
        "finalLastDate": 20231023,
        "nvt": 0.0,
        "mop": 0,
        "thirtyDayClosingHistory": null,
        "priceChange": 0.0,
        "priceMin": 14900.00,
        "priceMax": 15950.00,
        "priceYesterday": 15320.00,
        "priceFirst": 15580.00,
        "last": false,
        "id": 0,
        "insCode": "0",
        "dEven": 20231023,
        "hEven": 122958,
        "pClosing": 15410.00,
        "iClose": false,
        "yClose": false,
        "pDrCotVal": 15320.00,
        "zTotTran": 7912.0,
        "qTotTran5J": 56250210.0,
        "qTotCap": 867055662590.00
    }
}
"""

BEST_LIMITS = "http://cdn.tsetmc.com/api/BestLimits/{insCode}"
"""Response would be like:
{
    "bestLimits": [
        {
            "number": 1,
            "qTitMeDem": 13595,
            "zOrdMeDem": 1,
            "pMeDem": 15320.000,
            "pMeOf": 15320.000,
            "zOrdMeOf": 1,
            "qTitMeOf": 500,
            "insCode": null
        },
        {
            "number": 2,
            "qTitMeDem": 2125,
            "zOrdMeDem": 1,
            "pMeDem": 15250.000,
            "pMeOf": 15330.000,
            "zOrdMeOf": 4,
            "qTitMeOf": 82355,
            "insCode": null
        },
        {
            "number": 3,
            "qTitMeDem": 16750,
            "zOrdMeDem": 1,
            "pMeDem": 15240.000,
            "pMeOf": 15340.000,
            "zOrdMeOf": 6,
            "qTitMeOf": 15277,
            "insCode": null
        },
        {
            "number": 4,
            "qTitMeDem": 19054,
            "zOrdMeDem": 1,
            "pMeDem": 15230.000,
            "pMeOf": 15350.000,
            "zOrdMeOf": 1,
            "qTitMeOf": 1939,
            "insCode": null
        },
        {
            "number": 5,
            "qTitMeDem": 1194,
            "zOrdMeDem": 1,
            "pMeDem": 15220.000,
            "pMeOf": 15380.000,
            "zOrdMeOf": 2,
            "qTitMeOf": 7500,
            "insCode": null
        }
    ]
}
"""

GET_CLIENT_TYPE_HISTORY = "http://cdn.tsetmc.com/api/ClientType/GetClientTypeHistory/{insCode}"
"""
{
    "clientType": [
        {
            "recDate": 20231022,
            "insCode": "48990026850202503",
            "buy_I_Volume": 89858573.0,
            "buy_N_Volume": 8871458.0,
            "buy_I_Value": 392621223597.0,
            "buy_N_Value": 38614130808.0,
            "buy_N_Count": 8,
            "sell_I_Volume": 78417700.0,
            "buy_I_Count": 1538.0,
            "sell_N_Volume": 20312331.0,
            "sell_I_Value": 342407921268.0,
            "sell_N_Value": 88827433137.0,
            "sell_N_Count": 8,
            "sell_I_Count": 1184
        },
        ...
    ]
}
"""
CLIENT_TYPE = "http://cdn.tsetmc.com/api/ClientType/GetClientType/{insCode}/1/0"
"""Response would be like:
{
    "clientType": {
        "buy_I_Volume": 55801819.0,
        "buy_N_Volume": 448391.0,
        "buy_DDD_Volume": 0.0,
        "buy_CountI": 2254,
        "buy_CountN": 3,
        "buy_CountDDD": 0,
        "sell_I_Volume": 54878300.0,
        "sell_N_Volume": 1371910.0,
        "sell_CountI": 2125,
        "sell_CountN": 7
    }
}
"""

GET_TRADE = "http://cdn.tsetmc.com/api/Trade/GetTrade/{insCode}"
"""Response would be like:
{
    "trade": [
        {
            "insCode": null,
            "dEven": 0,
            "nTran": 1,
            "hEven": 90016,
            "qTitTran": 100000,
            "pTran": 15580.00,
            "qTitNgJ": 0,
            "iSensVarP": "\u0000",
            "pPhSeaCotJ": 0.0,
            "pPbSeaCotJ": 0.0,
            "iAnuTran": 0,
            "xqVarPJDrPRf": 0.0,
            "canceled": 0
        },
        ...
    ]
}
"""

GET_RELATED_COMPANY = "http://cdn.tsetmc.com/api/ClosingPrice/GetRelatedCompany/{group_code}"
"""Response would be like:
{
    "relatedCompany": [
        {
            "instrumentState": null,
            "instrument": {
                "cValMne": null,
                "lVal18": null,
                "cSocCSAC": null,
                "lSoc30": null,
                "yMarNSC": null,
                "yVal": null,
                "insCode": "14744445176220774",
                "lVal30": "بهساز كاشانه تهران",
                "lVal18AFC": "ثبهساز",
                "flow": 0,
                "cIsin": null,
                "zTitad": 0.0,
                "baseVol": 0,
                "instrumentID": null,
                "cgrValCot": null,
                "cComVal": null,
                "lastDate": 0,
                "sourceID": 0,
                "flowTitle": null,
                "cgrValCotTitle": null
            },
            "lastHEven": 0,
            "finalLastDate": 0,
            "nvt": 0.0,
            "mop": 0,
            "thirtyDayClosingHistory": null,
            "priceChange": 50.00,
            "priceMin": 2750.00,
            "priceMax": 2898.00,
            "priceYesterday": 2749.00,
            "priceFirst": 0.0,
            "last": false,
            "id": 0,
            "insCode": "14744445176220774",
            "dEven": 0,
            "hEven": 0,
            "pClosing": 2827.00,
            "iClose": false,
            "yClose": false,
            "pDrCotVal": 2799.00,
            "zTotTran": 5146.0,
            "qTotTran5J": 134249231.0,
            "qTotCap": 379558714687.00
        },
        ...
    ]
}       
"""
################################################### TO DO ##################################################################
#                        "http://cdn.tsetmc.com/api/Codal/GetStatementContentByInsCode/14/0/-1/{insCode}" #تصمیمات مجمع
#                        "http://cdn.tsetmc.com/api/Codal/GetStatementContentByInsCode/6/6/2/{insCode}" #تولید و فروش
#                        "http://cdn.tsetmc.com/api/Codal/GetStatementContentByInsCode/6/6/1/{insCode}" #سود و زیان
#                        "http://cdn.tsetmc.com/api/Codal/GetStatementContentByInsCode/6/6/0/{insCode}" #ترازنامه
#                        "http://cdn.tsetmc.com/api/Codal/GetStatementContentByInsCode/12/0/-1/{insCode} #هیات مدیره
#                        "http://cdn.tsetmc.com/api/Codal/GetStatementContentByInsCode/13/0/-1/{insCode}" #آکهی مجمع
# پورتفوی
GET_STATEMENT_BY_INSCODE = "http://cdn.tsetmc.com/api/Codal/GetStatementContentByInsCode/6/8/-1/{insCode}"
"""Response would be like:
{
    "statemetnContent": [
        {
            "title": "صورت‌های مالی  سال مالی منتهی به 1402/03/31 (حسابرسی شده)",
            "sentDateTime_Gregorian": "2023-10-14T16:23:22",
            "publishDateTime_Gregorian": "2023-10-14T16:23:22",
            "publishDateTime_DEven": 20231014,
            "reportSubType": 8,
            "pageID": 0,
            "content": "<Root><Type Code=\"8\" ReportName=\"صورت وضعیت پورتفوی\" /><YearEndToDate>1402/03/31</YearEndToDate><Period>12 ماهه</Period><IsAudited>(حسابرسی شده)</IsAudited><PeriodEndToDate>1402/03/31</PeriodEndToDate></Root>"
        },
        ...
    ]
}
"""


GET_INSTRUMENT_STATISTICS = "http://cdn.tsetmc.com/api/MarketData/GetInstrumentStatistic/{insCode}"
"""Response would be like:
{
    "instrumentStatistic": [
        {
            "insCode": 0,
            "dataType": 1,
            "dEven": 0,
            "dataValue": "822476717792",
            "dataTypeDesc": "میانگین ارزش معاملات در 3 ماه گذشته ",
            "partitionCode": 5
        },
        ...
    ]
}
"""


GET_INSTRUMENT_IDENTITY = "http://cdn.tsetmc.com/api/Instrument/GetInstrumentIdentity/{insCode}"
"""Response would be like:
{
    "instrumentIdentity": {
        "sector": {
            "dEven": 0,
            "cSecVal": "34 ",
            "lSecVal": "خودرو و ساخت قطعات"
        },
        "subSector": {
            "dEven": 0,
            "cSecVal": null,
            "cSoSecVal": 3430,
            "lSoSecVal": "قطعات يدكي و جانبي وسايل نقليه موتوري"
        },
        "cValMne": "GOST1",
        "lVal18": "Iran Kh. Inv.",
        "cSocCSAC": "GOST",
        "lSoc30": "گسترش‌سرمايه‌گذاري‌ايران‌خودرو",
        "yMarNSC": "NO",
        "yVal": "300",
        "insCode": "0",
        "lVal30": "گسترش‌سرمايه‌گذاري‌ايران‌خودرو",
        "lVal18AFC": "خگستر",
        "flow": 0,
        "cIsin": "IRO1GOST0003",
        "zTitad": 0.0,
        "baseVol": 0,
        "instrumentID": "IRO1GOST0001",
        "cgrValCot": "N1",
        "cComVal": "1",
        "lastDate": 0,
        "sourceID": 0,
        "flowTitle": "",
        "cgrValCotTitle": "بازار اول (تابلوی اصلی) بورس"
    }
}
"""

GET_INSTRUMENT_SHARE_HOLDERS = "http://cdn.tsetmc.com/api/Shareholder/GetInstrumentShareHolderLast/{insCode}"
"""Response would be like:
{
    "shareHolder": [
        {
            "shareHolderID": 0,
            "shareHolderName": "شركت ايران خودرو",
            "cIsin": "IRO1GOST0003",
            "dEven": 0,
            "numberOfShares": 17883298946.0,
            "perOfShares": 45.150,
            "change": 1,
            "changeAmount": 0.0,
            "shareHolderShareID": 19051212
        },
        ...
    ]
}
"""
# ---------- معرفی ----------
GET_CODAL_PUBLISHER_BY_SYMBOL = "http://cdn.tsetmc.com/api/Codal/GetCodalPublisherBySymbol/{symbol}"
"""Response would be like:
{
    "codalPublisher": {
        "id": 5147,
        "symbol": "خگستر",
        "displaySymbol": "خگستر",
        "name": "گسترش سرمایه گذاری ایران خودرو",
        "isic": "343022",
        "reportingType": "1000002",
        "executiveManager": "احمد رؤيائي",
        "address": "ندارد",
        "telNo": "22059548-021",
        "faxNo": "22059575-021",
        "activitySubject": "1-سرمایه گذاری در سهام، سهم الشرکه واحد های سرمایه گذاری صندوق ها یا سایر اوراق بهادار دارای حق رای با هدف کسب انتفاع به طوری که به تنهایی یا به همراه اشخاص تحت کنترل یا اشخاص تحت کنترل واحد،کنترل شرکت، موسسه یا صندوق سرمایه پذیر را در اختیار گرفته یا در آن نفوذ قابل ملاحضه یابد",
        "officeAddress": "تهران -بلوار نلسون ماندلا ( آفریقا) بلوار گلشهر پلاک34",
        "shareOfficeAddress": "تهران -بلوار نلسون ماندلا ( آفریقا) بلوار گلشهر پلاک34",
        "website": "www.ikido.org",
        "email": "info@ikido.org",
        "state": "0",
        "companyType": "0",
        "stateName": null,
        "inspector": "بهراد مشار",
        "auditorName": "حسابرسی وخدمات مالی ومدیریت ایران مشهود",
        "inspListedCapitalector": null,
        "listedCapital": "39605137",
        "financialYear": "12/29",
        "companyId": null,
        "financialManager": "رضا کمرئی",
        "enActivitySubject": null,
        "enAddress": null,
        "enDisplayedSymbol": null,
        "enExecutiveManager": null,
        "enFinancialManager": null,
        "enInspector": null,
        "enName": null,
        "enOfficeAddress": null,
        "enShareOfficeAddress": null,
        "managementGroup": null,
        "enManagementGroup": null,
        "nationalCode": "10101800682",
        "companyType1": null
    }
}
"""
